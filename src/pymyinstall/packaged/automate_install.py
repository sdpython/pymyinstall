"""
@file
@brief Install or update all packages.
"""
from __future__ import print_function
import os
import warnings
from ..installhelper import ModuleInstall, has_pip, update_pip, is_installed, get_module_dependencies
from ..installhelper.module_install_exceptions import MissingVersionOnPyPiException, MissingPackageOnPyPiException
from ..installhelper.module_dependencies import missing_dependencies
from .packaged_config import all_fullset


def _build_reverse_index():
    """
    builds a reverse index of the module,
    """
    res = {}
    mods = all_fullset()
    for m in mods:
        res[m.name] = m
        if m.mname is not None:
            res[m.mname] = m
    return res


_reverse_module_index = _build_reverse_index()


def find_module_install(name):
    """
    checks if there are specific instructions to run before installing module *name*,
    on Windows, some modules requires compilation, if not uses default option with *pip*

    @param      name        module name, the name can include a specific version number with '=='
    @return                 @see cl ModuleInstall
    """
    if '=' in name:
        spl = name.split('==')
        if len(spl) != 2:
            raise ValueError("unable to interpret " + name)
        name = spl[0]
        version = spl[1]
    else:
        version = None

    if name in _reverse_module_index:
        mod = _reverse_module_index[name]
    else:
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
    for mod in all_fullset():
        if mod.name in inset and inset[mod.name] is not None:
            res.append(mod.copy(version=inset[mod.name].version))
            inset[mod.name] = None
    for mod in list_module:
        if inset[mod.name] is not None:
            res.append(mod)
    return res


def update_all(temp_folder=".", fLOG=print, verbose=True,
               list_module=None, reorder=True,
               skip_module=None):
    """
    update modules in *list_module*
    if None, this list will be returned by @see fn ensae_fullset,
    the function starts by updating pip.

    @param  temp_folder     temporary folder
    @param  verbose         more display
    @param  list_module     None or of list of str or @see cl ModuleInstall or a name set
    @param  fLOG            logging function
    @param  reorder         reorder the modules to update first modules with less dependencies (as much as as possible)
    @param  skip_module     module to skip (list of str)

    *list_module* can be a set of modules of a name set.
    Name sets can be accesses by function @see fn get_package_set.
    See the function to get the list of possible name sets.

    .. versionchanged:: 1.3
        Catch an exception while updating modules and walk through the end of the list.
        The function should be run a second time to make sure an exception remains.
        It can be due to python keeping in memory an updated module.
    """
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    if not has_pip():
        fLOG("install pip")
        from .get_pip import main
        main()

    if skip_module is None:
        skip_module = []

    if list_module is None:
        from ..packaged import ensae_fullset
        list_module = ensae_fullset()
    elif isinstance(list_module, str  # unicode#
                    ):
        from .packaged_config import get_name_set
        f = get_name_set(list_module)
        list_module = f()
    else:
        list_module = [find_module_install(mod) if isinstance(
            mod, str) else mod for mod in list_module]

    list_module = [_ for _ in list_module if _.name not in skip_module]

    if reorder:
        list_module = reorder_module_list(list_module)

    if verbose:
        fLOG("update pip if needed")

    if "pip" not in skip_module:
        update_pip()

    modules = list_module
    again = []
    errors = []
    for mod in modules:
        if verbose:
            fLOG("check module: ", mod.name)

        is_installed = mod.is_installed()
        if not is_installed:
            continue

        try:
            has_update = mod.has_update()
        except (MissingVersionOnPyPiException, MissingPackageOnPyPiException) as e:
            # this happens for custom made version such as xgboost
            fLOG("    - unable to check updates", e)
            has_update = False
        if not has_update:
            continue

        ver = mod.get_pypi_version()
        inst = mod.get_installed_version()
        m = "    - updating module  {0} --- {1} --> {2} (kind={3})" \
            .format(mod.name, inst, ver, mod.kind)
        fLOG(m)
        try:
            b = mod.update(temp_folder=temp_folder, log=verbose)
        except Exception as e:
            b = False
            m = "    - failed to update module  {0} --- {1} --> {2} (kind={3}) due to {4}" \
                .format(mod.name, inst, ver, mod.kind, str(e))
            fLOG(m)
            errors.append((mod, e))
        if b:
            again.append(m)

    if verbose:
        fLOG("")
        fLOG("updated modules")
        for m in again:
            fLOG("  ", m)
        if len(errors) > 0:
            fLOG("failed modules")
            for m in errors:
                fLOG("  ", m)


def install_all(temp_folder=".", fLOG=print, verbose=True,
                list_module=None, reorder=True, skip_module=None,
                up_pip=True, skip_missing=False, deps=False):
    """
    install modules in *list_module*
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

    *list_module* can be a set of modules of a name set.
    Name sets can be accesses by function @see fn get_package_set.
    See the function to get the list of possible name sets.
    """
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    if not has_pip():
        fLOG("install pip")
        from ..installhelper.get_pip import main
        main()

    if skip_module is None:
        skip_module = []

    if list_module is None:
        from ..packaged import ensae_fullset
        list_module = ensae_fullset()
    elif isinstance(list_module, str  # unicode#
                    ):
        from .packaged_config import get_name_set
        f = get_name_set(list_module)
        list_module = f()
    else:
        list_module = [find_module_install(mod) if isinstance(
            mod, str) else mod for mod in list_module]

    list_module = [_ for _ in list_module if _.name not in skip_module]

    if reorder:
        list_module = reorder_module_list(list_module)

    if up_pip and "pip" not in skip_module:
        if verbose:
            fLOG("update pip if needed")
        update_pip()

    modules = list_module
    again = []
    errors = []
    installed = []
    for mod in modules:
        if verbose:
            fLOG("check module: ", mod.name)
        if not mod.is_installed():
            ver = mod.version
            m = "    - installing module  {0} --- --> {1} (kind={2})" \
                .format(mod.name, ver, mod.kind)
            fLOG(m)
            try:
                b = mod.install(temp_folder=temp_folder, log=verbose)
            except Exception as e:
                b = False
                m = "    - failed to update module  {0} --- {1} --> {2} (kind={3}) due to {4}" \
                    .format(mod.name, '', ver, mod.kind, str(e))
                fLOG(m)
                errors.append((mod, e))
            if b:
                again.append(m)
                installed.append(mod)

    if deps:
        fLOG("dependencies")
        for mod in installed:
            install_module_deps(mod.name, temp_folder=temp_folder, fLOG=fLOG, verbose=verbose, deps=deps):

    if verbose:
        fLOG("")
        fLOG("installed modules")
        for m in again:
            fLOG("  ", m)
        if len(errors) > 0:
            fLOG("failed modules")
            for m in errors:
                fLOG("  ", m)

    if not skip_missing:
        miss = missing_dependencies()
        if len(miss) > 0:
            mes = "\n".join("{0} misses {1}".format(k, ", ".join(v))
                            for k, v in sorted(miss.items()))
            warnings.warn(mes)


def install_module_deps(name, temp_folder=".", fLOG=print, verbose=True, deps=True):
    """
    install a module with its dependencies,
    if a module is already installed, it installs the missing dependencies

    @param      module          module name
    @param      temp_folder     where to download
    @param      fLOG            logging function
    @param      verbose         more display
    @param      deps            add dependencies
    @return                     list of installed modules

    The function does not handle properly contraints on versions.
    It checks in the registered list of modules if *name* is present.
    If it is the case, it uses it, otherwise, it uses *pip*.
    """
    installed = []
    if not is_installed(name):
        install_all(temp_folder=temp_folder, fLOG=fLOG, verbose=verbose,
                    list_module=[name], reorder=True, up_pip=False,
                    skip_missing=True)

    installed.append(name)
    stack = [name]
    while len(stack) > 0:
        name = stack[-1]
        del stack[-1]
        res = get_module_dependencies(name, refresh_cache=True, use_pip=True)
        if res is None:
            raise ImportError("unable to check dependencies of module {0}\ninstalled:\n{1}".format(
                name, "\n".join(installed)))
        list_m = [k for k, v in res.items()]
        inst = [k for k in list_m if not is_installed(k)]
        install_all(temp_folder=temp_folder, fLOG=fLOG, verbose=verbose,
                    list_module=inst, reorder=True, up_pip=False,
                    skip_missing=True)
        stack.extend(inst)
        installed.extend(inst)

    return list(sorted(set(installed)))
