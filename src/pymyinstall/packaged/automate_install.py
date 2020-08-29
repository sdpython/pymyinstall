"""
@file
@brief Install or update all packages.

.. faqref::
    :title: Skipped modules

    Some modules are still marked as a dependency by others
    even if they are not needed or cannot be installed.

    * `enum-compat <https://pypi.python.org/pypi/enum-compat>`_:
      not needed after Python 3.5
    * `prettytable <https://pypi.python.org/pypi/PrettyTable>`_:
      should be repladed by `PTable <https://pypi.python.org/pypi/PTable>`_.
"""
from __future__ import print_function
import sys
import os
import warnings
import time
from textwrap import wrap
from ..installhelper import ModuleInstall, has_pip, update_pip, is_installed, get_module_dependencies
from ..installhelper.module_install_exceptions import MissingVersionOnPyPiException, MissingPackageOnPyPiException, MissingReferenceException
from ..installhelper.module_dependencies import missing_dependencies
from .packaged_exception import ModuleNotFoundError
from .packaged_config import all_set


def _build_reverse_index():
    """
    builds a reverse index of the module,
    """
    res = {}
    mods = all_set()
    for m in mods:
        res[m.name] = m
        if m.mname is not None and m.mname != m.name:
            res[m.mname] = m
        if m.name.lower() not in (m.name, m.mname):
            res[m.name.lower()] = m
    return res


_reverse_module_index = _build_reverse_index()


def find_module_install(name, must_exist=False):
    """
    Checks if there are specific instructions
    to run before installing module *name*,
    on Windows, some modules requires compilation,
    if not uses default option with *pip*.

    @param      name        module name, the name can include a specific version number with '=='
    @param      must_exist  if True, raise an exception if not found
    @return                 @see cl ModuleInstall
    """
    if isinstance(name, ModuleInstall):
        return name

    if name in {"pip", "python"}:
        return None

    if '=' in name:
        spl = name.split('==')
        if len(spl) != 2:
            raise ValueError(
                "[find_module_install] unable to interpret " + name)
        name = spl[0]
        version = spl[1]
    else:
        version = None

    if name in _reverse_module_index:
        mod = _reverse_module_index[name]
    else:
        names = [name[0].upper() + name[1:],
                 name.replace("-python", ""),
                 name + "-python"]
        if name == "pytables":
            names.append("tables")
        elif name == "pyopengl-accelerate":
            names.append("PyOpenGL_accelerate")
        elif name == "pywin32":
            names.append("pywin32")  # pypiwin32
        for n in names:
            if n in _reverse_module_index:
                return _reverse_module_index[n]
        if must_exist:
            raise MissingReferenceException(
                "Unable to find reference for module '{0}'\nCheck '{0}'".format(name))
        mod = ModuleInstall(name, "pip")

    if version is not None:
        mod.version = version
    return mod


def reorder_module_list(list_module):
    """
    reorder a list of modules to install, a module at position *p*
    should not depend not module at position *p+1*

    @param      list_module     list of module (@see cl ModuleInstall)
    @return                     list of modules

    The function uses modules stored in :mod:`pyminstall.packaged.packaged_config`,
    it does not go to pypi. If a module was not registered, it will be placed
    at the end in the order it was given to this function.
    """
    inset = {m.name: m for m in list_module}
    res = []
    for mod in all_set():
        if mod.name in inset and inset[mod.name] is not None:
            res.append(mod.copy(version=inset[mod.name].version))
            inset[mod.name] = None
    for mod in list_module:
        if inset[mod.name] is not None:
            res.append(mod)
    return res


class FileShouldNotBeFound(Exception):
    """
    Raised by function @see fn check_sys_path.
    """
    pass


def check_sys_path():
    """
    An issue is happening during unit test as pymyinstall
    could be imported from two locations. We check this is
    not the case.
    """
    exp = "pymyinstall_ut_skip_pyquickhelper_%d%d_std" % sys.version_info[:2]
    exp = os.path.join(exp, "src")
    for path in sys.path:
        if exp in path:
            raise FileShouldNotBeFound(
                "'{0}' was found in sys.path:\n{1}\n----\ncwd='{2}'\nexe='{3}'".format(path, "\n".join(sys.path), os.getcwd(), sys.executable))


def update_all(temp_folder=".", fLOG=print, verbose=True,
               list_module=None, reorder=True,
               skip_module=None, schedule_only=False,
               source=None, download_only=False):
    """
    Updates modules in *list_module*
    if None, this list will be returned by @see fn ensae_fullset,
    the function starts by updating :epkg:`pip`.

    @param      temp_folder     temporary folder
    @param      verbose         more display
    @param      list_module     None or of list of str or @see cl ModuleInstall or a name set
    @param      fLOG            logging function
    @param      reorder         reorder the modules to update first modules with less dependencies (as much as as possible)
    @param      skip_module     module to skip (list of str)
    @param      schedule_only   if True, the function returns the list of modules scheduled to be installed
    @param      source          overwrite the wheels location, see @see me get_exewheel_url_link2
    @param      download_only   only downloads the module, no installation

    *list_module* can be a set of modules of a name set.
    Name sets can be accesses by function @see fn get_package_set.
    See the function to get the list of possible name sets.

    .. versionchanged:: 1.1
        Catch an exception while updating modules and walk through the end of the list.
        The function should be run a second time to make sure an exception remains.
        It can be due to python keeping in memory an updated module.
        Parameters *source*, *download_only* were added.
    """
    check_sys_path()
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    if not has_pip():
        fLOG("install pip")
        from .get_pip import main  # pylint: disable=E0401
        main()

    if skip_module is None:
        skip_module = []

    if list_module is None:
        from ..packaged import ensae_fullset
        list_module = ensae_fullset()
    elif isinstance(list_module, str  # unicode#
                    ):
        from .packaged_config import get_package_set
        f = get_package_set(list_module)
        list_module = f()
    else:
        list_module = [find_module_install(mod) if isinstance(
            mod, str) else mod for mod in list_module]

    list_module = [_ for _ in list_module if _.name not in skip_module]
    check_sys_path()

    if reorder:
        list_module = reorder_module_list(list_module)

    if verbose:
        fLOG("update pip if needed")

    if "pip" not in skip_module:
        update_pip()

    modules = list_module
    again = []
    errors = []
    schedule = []
    for mod in modules:
        check_sys_path()
        is_installed = mod.is_installed_version()
        if not is_installed:
            continue
        if verbose:
            fLOG("[wait] 0.5 seconds")
        time.sleep(0.5)
        if verbose:
            fLOG("[update-check] ##", mod.name, "## [begin]")

        try:
            has_update = mod.has_update()
        except (MissingVersionOnPyPiException, MissingPackageOnPyPiException) as e:
            # this happens for custom made version such as xgboost
            fLOG("    - unable to check updates", e)
            has_update = False
        if not has_update:
            if verbose:
                fLOG("[update-check] ##", mod.name, "## [end no update]")
            continue

        ver = mod.get_pypi_version()
        inst = mod.get_installed_version()

        schedule.append(mod)
        if not schedule_only:
            m = "    - updating module  {0} --- {1} --> {2} (kind={3})" \
                .format(mod.name, inst, ver, mod.kind)
            fLOG(m)
            try:
                if download_only:
                    b = mod.download(temp_folder=temp_folder, source=source)
                else:
                    b = mod.update(temp_folder=temp_folder,
                                   log=verbose, source=source)
            except (SystemExit, Exception) as e:
                b = False
                m = "    - failed to update module  {0} --- {1} --> {2} (kind={3}) due to {4} ({5})" \
                    .format(mod.name, inst, ver, mod.kind, str(e), type(e))
                fLOG(m)
                errors.append((mod, e))
            if b:
                again.append(m)

        if verbose:
            fLOG("[update-check] ##", mod.name, "## [end]")

    if schedule_only:
        return schedule

    if verbose:
        fLOG("")
        fLOG("updated modules")
        for m in again:
            fLOG("  ", m)
        if len(errors) > 0:
            fLOG("failed modules")
            for m in errors:
                fLOG("  ", m[0], m[1])
    return None


def install_all(temp_folder=".", fLOG=print, verbose=True,
                list_module=None, reorder=True, skip_module=None,
                up_pip=True, skip_missing=False, deps=False,
                schedule_only=False, deep_deps=False,
                _memory=None, source=None, download_only=False,
                force=False):
    """
    Installs modules in *list_module*
    if None, this list will be returned by @see fn ensae_fullset,
    the function starts by updating pip.

    @param      temp_folder     temporary folder
    @param      verbose         more display
    @param      list_module     None or of list of str or @see cl ModuleInstall or a name set
    @param      fLOG            logging function
    @param      reorder         reorder the modules to update first modules with less dependencies (as much as as possible)
    @param      skip_module     module to skip (list of str)
    @param      up_pip          upgrade pip (pip must not be in *skip_module*)
    @param      skip_missing    skip the checking of the missing dependencies
    @param      deps            install the dependencies of the installed modules
    @param      schedule_only   if True, the function returns the list of modules scheduled to be installed
    @param      deep_deps       check dependencies for dependencies
    @param      _memory         stores installed packages, avoid going into an infinite loop
    @param      source          overwrite the location of the wheels, see @see me get_exewheel_url_link2
    @param      download_only   only downloads the module, no installation
    @param      force           force the installation or the download
    @return                     output streams

    *list_module* can be a set of modules of a name set.
    Name sets can be accesses by function @see fn get_package_set.
    See the function to get the list of possible name sets.

    About *name set*, the function can install a set of modules but these set of modules have dependencies:

    * @see fn extended_set, @see fn sphinx_theme_set requires @see fn small_set
    * @see fn ml_set, @see fn ensae_set, @see fn teachings_set, @see fn iot_set, @see fn scraping_set
      requires @see fn small_set and @see fn extended_set

    If you want to install a specific module with its dependencies, I suggest
    to use option *deep_deps*.

    .. versionadded:: 1.1
    """
    check_sys_path()
    fLOG("[install_all] begin, exe:", sys.executable)
    if _memory is None:
        _memory = {}
    deps = deps or deep_deps
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    if not has_pip():
        fLOG("install pip")
        from ..installhelper.get_pip import main
        main()

    if skip_module is None:
        skip_module = []

    if list_module is None:
        list_module = all_set()
    elif isinstance(list_module, str  # unicode#
                    ):
        from .packaged_config import get_package_set
        f = get_package_set(list_module)
        list_module = f()
    else:
        list_module = [find_module_install(mod) if isinstance(
            mod, str) else mod for mod in list_module]

    list_module = [_ for _ in list_module if _.name not in skip_module]
    check_sys_path()

    if reorder:
        list_module = reorder_module_list(list_module)

    if up_pip and "pip" not in skip_module:
        if verbose:
            fLOG("update pip if needed")
        update_pip()

    # More information.
    sorted_names = ", ".join(sorted(_.name.lower() for _ in list_module))
    ordered_names = ", ".join(_.name for _ in list_module)
    fLOG('[install_all] sorted modules ----------------------------')
    fLOG("\n".join(wrap(sorted_names, width=100,
                        initial_indent='    ', subsequent_indent='    ')))
    fLOG('[install_all] modules installation order ----------------')
    fLOG("\n".join(wrap(ordered_names, width=100,
                        initial_indent='    ', subsequent_indent='    ')))
    fLOG('[install_all] begin ----------------------')

    modules = list_module
    again = []
    errors = []
    installed = []
    schedule = []
    out_streams_module = {}
    for mod in modules:
        check_sys_path()
        if mod.name in _memory:
            # already done
            continue
        if verbose:
            fLOG("[install-check] ##", mod.name, "## [begin]")
        if force or not mod.is_installed_version():
            schedule.append(mod)
            if not schedule_only:
                ver = mod.version
                m = "    - installing module '{0}' --- --> '{1}' (kind='{2}')" \
                    .format(mod.name, ver, mod.kind)
                fLOG(m)
                if deps:
                    fLOG("[install-check-dep] ##", mod.name, "## [begin]")
                    install_module_deps(mod.name, temp_folder=temp_folder,
                                        fLOG=fLOG, verbose=verbose, deps=deps, deep_deps=deep_deps,
                                        _memory=_memory, source=source, download_only=download_only,
                                        force=force)
                    fLOG("[install-check-dep] ##", mod.name, "## [end]")
                else:
                    out_streams = []
                    try:
                        if download_only:
                            b = mod.download(
                                temp_folder=temp_folder, source=source)
                        else:
                            b = mod.install(temp_folder=temp_folder,
                                            log=verbose, source=source,
                                            out_streams=out_streams)
                    except (SystemExit, Exception) as e:
                        b = False
                        m = "    - failed to update module '{0}' --- '{1}' --> '{2}' (kind='{3}') due to '{4}' ('{5}')" \
                            .format(mod.name, '', ver, mod.kind, str(e), type(e))
                        fLOG(m)
                        errors.append((mod, e))
                    if b:
                        again.append(m)
                        installed.append(mod)
                    if verbose:
                        ne = 0
                        for lll in out_streams:
                            if lll[-1]:
                                ne += 1
                        if ne > 0:
                            fLOG("###################")
                            fLOG("##", mod.name, "##")
                            for jj in out_streams:
                                for la, va in zip(("CMD", "OUT", "ERR-1"), jj):
                                    fLOG(la, va)
                            fLOG("###################.")
                    out_streams_module[mod.name] = out_streams
        if verbose:
            fLOG("[install-check] ##", mod.name, "## [end]")
        _memory[mod.name] = True

    if schedule_only:
        return schedule

    if verbose:
        fLOG("")
        fLOG("[install_all]" +
             (" downloaded modules" if download_only else "installed modules"))
        for m in again:
            fLOG("  ", m)
        fLOG("[install_all] end: ", len(errors), "errors")
        if len(errors) > 0:
            fLOG("[install_all] failed modules")
            for m in errors:
                fLOG("  ", m[0], m[1])
            fLOG("[install_all] end failed modules")

    if not skip_missing:
        fLOG("[install_all] check dependencies")
        miss = missing_dependencies()
        if len(miss) > 0:
            mes = "\n".join("Module '{0}' misses '{1}'".format(k, ", ".join(v))
                            for k, v in sorted(miss.items()))
            warnings.warn("[install_all] missing dependencies\n" + mes)
        fLOG("[install_all] end check dependencies")

    for k, v in sorted(out_streams_module.items()):
        fLOG("[%s] #########################" % k)
        if isinstance(v, list):
            for _ in v:
                for la, va in zip(("CMD", "OUT", "ERR-2"), _):
                    if va is not None and len(va) > 0:
                        fLOG(la, va)
        else:
            for la, va in zip(("CMD", "OUT", "ERR-3"), v):
                if va is not None and len(va) > 0:
                    fLOG(la, va)
        fLOG(".")
    return out_streams_module


def install_module_deps(name, temp_folder=".", fLOG=print, verbose=True, deps=True,
                        deep_deps=False, _memory=None, source=None,
                        download_only=False, force=False):
    """
    Installs a module with its dependencies,
    if a module is already installed, it installs
    the missing dependencies.

    @param      module              module name
    @param      temp_folder         where to download
    @param      fLOG                logging function
    @param      verbose             more display
    @param      deps                add dependencies
    @param      deep_deps           check dependencies for dependencies
    @param      _memory             stores installed packages, avoid going into an infinite loop
    @param      source              overwrite the wheels location, see @see me get_exewheel_url_link2
    @param      download_only       only downloads the module, no installation
    @param      force               force the download or the update
    @return                         list of installed modules

    The function does not handle properly contraints on versions.
    It checks in the registered list of modules if *name* is present.
    If it is the case, it uses it, otherwise, it uses *pip*.

    .. versionadded:: 1.1
    """
    check_sys_path()
    if _memory is None:
        _memory = {}
    deps = deps or deep_deps
    installed = []
    first_name = name
    memory2 = {}
    if not is_installed(name):
        install_all(temp_folder=temp_folder, fLOG=fLOG, verbose=verbose,
                    list_module=[name], reorder=True, up_pip=False,
                    skip_missing=True, _memory=memory2, deps=False,
                    deep_deps=False, source=source, download_only=download_only,
                    force=force)
        installed.append(name)

    stack = [name]
    while len(stack) > 0:
        check_sys_path()
        name = stack[-1]
        del stack[-1]
        if name in _memory:
            # already done, avoid loops on
            continue
        if name == first_name:
            _memory.update(memory2)

        res = get_module_dependencies(name, refresh_cache=True, use_pip=True)
        if res is None:
            raise ImportError("unable to check dependencies of module {0}\ninstalled:\n{1}".format(
                name, "\n".join(installed)))
        list_m = [k for k, v in res.items()]
        fLOG("[deps] [{}] requires".format(name), list_m)
        inst = [k for k in list_m if deep_deps or not is_installed(k)]
        fLOG("[deps] installation of ", inst)
        install_all(temp_folder=temp_folder, fLOG=fLOG, verbose=verbose,
                    list_module=inst, reorder=True, up_pip=False,
                    skip_missing=True, deep_deps=deep_deps,
                    _memory=_memory, source=source, download_only=download_only)
        stack.extend(inst)
        installed.extend(inst)
        for i in inst:
            _memory[i] = True

    return list(sorted(set(installed)))


def install_module(module_name, temp_folder=".", fLOG=print, verbose=True,
                   reorder=True, skip_module=None,
                   up_pip=True, skip_missing=False, deps=False,
                   schedule_only=False, deep_deps=False,
                   _memory=None, source=None, download_only=False,
                   force=False):
    """
    Installs a module.

    @param      module_name     module to install
    @param      temp_folder     temporary folder
    @param      verbose         more display
    @param      fLOG            logging function
    @param      reorder         reorder the modules to update first modules with less dependencies (as much as as possible)
    @param      skip_module     module to skip (list of str)
    @param      up_pip          upgrade pip (pip must not be in *skip_module*)
    @param      skip_missing    skip the checking of the missing dependencies
    @param      deps            install the dependencies of the installed modules
    @param      schedule_only   if True, the function returns the list of modules scheduled to be installed
    @param      deep_deps       check dependencies for dependencies
    @param      _memory         stores installed packages, avoid going into an infinite loop
    @param      source          overwrite the wheels location, see @see me get_exewheel_url_link2
    @param      download_only   only downloads the module, no installation
    @param      force           force the download or the install

    .. versionadded:: 1.1
    """
    if not isinstance(module_name, list):
        module_name = [module_name]
    install_all(list_module=module_name, temp_folder=temp_folder, fLOG=fLOG,
                verbose=verbose, reorder=reorder, skip_module=skip_module,
                up_pip=up_pip, skip_missing=skip_missing, deps=deps,
                schedule_only=schedule_only, deep_deps=deep_deps,
                _memory=_memory, source=source, download_only=download_only,
                force=force)


def update_module(module_name, temp_folder=".", fLOG=print, verbose=True,
                  reorder=True, skip_module=None, schedule_only=False,
                  source=None):
    """
    Updates modules in *list_module*
    if None, this list will be returned by @see fn ensae_fullset,
    the function starts by updating pip.

    @param      module_name     module to update
    @param      temp_folder     temporary folder
    @param      verbose         more display
    @param      fLOG            logging function
    @param      reorder         reorder the modules to update first modules with less dependencies (as much as as possible)
    @param      skip_module     module to skip (list of str)
    @param      schedule_only   if True, the function returns the list of modules scheduled to be installed
    @param      source          overwrite the wheels location, see @see me get_exewheel_url_link2
    """
    if not isinstance(module_name, list):
        module_name = [module_name]
    update_all(list_module=module_name, temp_folder=temp_folder, fLOG=fLOG, verbose=verbose,
               reorder=reorder, skip_module=skip_module, schedule_only=schedule_only,
               source=source)


def download_module(module_name,
                    temp_folder=".", force=False,
                    unzipFile=True, file_save=None, deps=False,
                    source=None, fLOG=print):
    """
    Downloads the module without installation.

    @param      temp_folder     destination
    @param      force           force the installation even if already installed
    @param      unzipFile       if it can be unzipped, it will be (for github, mostly)
    @param      file_save       for debug purposes, do not change it unless you know what you are doing
    @param      deps            download the dependencies too (only available for pip)
    @param      source          overwrite the wheels location, see @see me get_exewheel_url_link2
    @return                     downloaded files
    """
    if not isinstance(module_name, list):
        module_name = [module_name]

    res = []
    for mod in module_name:
        if not isinstance(mod, ModuleInstall):
            mod = find_module_install(mod, True)
            if mod is None:
                raise ModuleNotFoundError(
                    "unable to find an objec for module: " + ", ".join(module_name))
        k = mod.fLOG
        mod.fLOG = fLOG
        f = mod.download(temp_folder=temp_folder, force=force,
                         unzipFile=unzipFile, file_save=file_save, deps=deps, source=source)
        mod.fLOG = k
        res.append(f)
    return res
