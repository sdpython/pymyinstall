"""
@file
@brief Functions to get module version, license, dependencies
"""
from .install_cmd_helper import run_cmd, get_pip_program
from .module_install_exceptions import MissingPackageOnPyPiException, AnnoyingPackageException
from .module_install_exceptions import ConfigurationError, MissingVersionOnPyPiException, WrongVersionError, MissingVersionWheelException
from .install_cmd_regex import regex_wheel_version, regex_wheel_version2

import sys
import re
# import pip._vendor.pkg_resources
import warnings
import functools

if sys.version_info[0] == 2:
    FileNotFoundError = Exception
    import xmlrpclib as xmlrpc_client
    TimeoutError = Exception
else:
    import xmlrpc.client as xmlrpc_client
    # from importlib import reload


annoying_modules = {"pygame", "liblinear", "mlpy", "VideoCapture",
                    "libsvm", "opencv_python", "scikits.cuda",
                    "NLopt"}


def call_get_installed_distributions(local_only=True,
                                     skip=None,
                                     include_editables=True,
                                     editables_only=False,
                                     user_only=False,
                                     use_cmd=False):
    """
    Direct call to function *get_installed_distributions* from
    `pip <https://pip.pypa.io/en/stable/>`_

    Return a list of installed Distribution objects.

    @param  local_only      if True (default), only return installations
                            local to the current virtualenv, if in a virtualenv.
    @param  skip            argument is an iterable of lower-case project names to
                            ignore; defaults to ``pip.compat.stdlib_pkgs`` (if *skip* is None)
    @param  editables       if False, don't report editables.
    @param  editables_only  if True , only report editables.
    @param  user_only       if True , only report installations in the user
                            site directory.
    @param  use_cmd         if True, use a different process (updated package list)
    @return                 list of installed Distribution objects.
    """
    if use_cmd:
        raise NotImplementedError("use_cmd should be False")
    # we disable this line, it fails on travis
    # reload(pip._vendor.pkg_resources)
    if skip is None:
        from pip.compat import stdlib_pkgs
        skip = stdlib_pkgs
    from pip.utils import get_installed_distributions
    return get_installed_distributions(local_only=local_only,
                                       skip=skip,
                                       include_editables=include_editables,
                                       editables_only=editables_only,
                                       user_only=user_only)


_get_module_version_manual_memoize = {}


def get_module_version(module, use_cmd=False):
    """
    return a dictionary { module:version }

    @param      module      unused, None
    @param      use_cmd     use command line
    @return                 dictionary
    """
    if module is not None:
        modl = module.lower()
        res = get_module_version(None, use_cmd=use_cmd)
        return res.get(modl, None)

    global _get_module_version_manual_memoize
    if len(_get_module_version_manual_memoize) > 0:
        return _get_module_version_manual_memoize

    res = {}

    if use_cmd:
        prog = get_pip_program()
        cmd = prog + " list"
        out, err = run_cmd(cmd, wait=True, do_not_log=True)

        if err is not None and len(err) > 0:
            if len(err.split("\n")) > 3 or \
               "You should consider upgrading via the 'pip install --upgrade pip' command." not in err:
                raise Exception("unable to run, #lines {0}\nCMD:\n{3}\nERR:\n{1}\nOUT:\n{2}".format(
                    len(err.split("\n")), err, out, cmd))
        lines = out.split("\n")

        for line in lines:
            if "(" in line:
                spl = line.split()
                if len(spl) == 2:
                    a = spl[0]
                    b = spl[1].strip(" \n\r")
                    res[a] = b.strip("()")
                    al = a.lower()
                    if al != a:
                        res[al] = res[a]
    else:
        # local_only must be False to get all modules
        # not only the ones installed in the virtual environment
        dist = call_get_installed_distributions(local_only=False)
        if len(dist) == 0:
            raise ConfigurationError("no installed module, unexpected (pip should be there): sys.executable={0}, sys.prefix={1}, sys.base_prefix={2}".format(
                sys.executable, sys.prefix, sys.base_prefix))
        for mod in dist:
            al = mod.key.lower()
            a = mod.key
            try:
                v = mod.version
            except ValueError:
                v = "UNKNOWN"
            res[a] = v
            if a != al:
                res[al] = v

    _get_module_version_manual_memoize.update(res)
    return res


def is_installed(name):
    """
    tells if a module is installed or not

    @param      name        module name
    @return                 boolean
    """
    return get_module_version(name) is not None


_get_module_metadata_manual_memoize = {}


def get_module_metadata(module, use_cmd=False, refresh_cache=False):
    """
    return a dictionary { module:metadata }

    @param      module          unused, None
    @param      refresh_cache   refresh the cache before getting metadata
    @return                     dictionary
    """
    if module is not None:
        modl = module.lower()
        res = get_module_metadata(
            None, use_cmd=use_cmd, refresh_cache=refresh_cache)
        return res.get(modl, None)

    global _get_module_metadata_manual_memoize
    if not refresh_cache and len(_get_module_metadata_manual_memoize) > 0:
        return _get_module_metadata_manual_memoize

    # local_only must be False to get all modules
    # not only the ones installed in the virtual environment
    dist = call_get_installed_distributions(local_only=False, use_cmd=use_cmd)
    if len(dist) == 0:
        raise ConfigurationError("no installed module, unexpected (pip should be there): sys.executable={0}, sys.prefix={1}, sys.base_prefix={2}".format(
            sys.executable, sys.prefix, sys.base_prefix))
    res = {}
    for mod in dist:
        d = {}
        lines = mod._get_metadata(mod.PKG_INFO)
        for line in lines:
            if sys.version_info[0] == 2:
                typstr = str  # unicode#
                if not isinstance(line, typstr):
                    line = typstr(line, encoding="utf8", errors="ignore")
            try:
                spl = line.split(":")
            except UnicodeDecodeError:
                warnings.warn("UnicodeDecodeError with: " + line)
                continue
            key = spl[0].strip()
            value = ":".join(spl[1:]).strip()
            if key not in d:
                d[key] = value
            else:
                if not isinstance(d[key], list):
                    d[key] = [d[key]]
                d[key].append(value)

        a = mod.key
        res[a] = d
        al = mod.key.lower()
        if a != al:
            res[al] = d

    _get_module_metadata_manual_memoize.update(res)
    return res


def _get_pypi_version_memoize_op(f):
    memo = {}

    def helper(module_name, full_list=False, url="http://pypi.python.org/pypi"):
        key = module_name, full_list, url
        if key not in memo:
            memo[key] = f(module_name, full_list, url)
        return memo[key]
    return helper

_get_pypi_version_memoize = {}


def get_pypi_version(module_name, full_list=False, url="http://pypi.python.org/pypi"):
    """
    returns the version of a package on pypi,
    we skip alpha, beta or dev version

    @param      module_name     module name
    @param      url             pipy server
    @param      full_list       results as a list or return the last stable version
    @return                     version (str or list)

    See also `installing_python_packages_programatically.py <https://gist.github.com/rwilcox/755524>`_,
    `pkgtools.pypi: PyPI interface <http://pkgtools.readthedocs.org/en/latest/pypi.html>`_.

    The function leaves a connection open::

        ResourceWarning: unclosed <socket.socket fd=XXX, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('XXX.XXX.X...

    It should be fixed in Python > 3.4.
    It the function fails, check the status of
    `Python Infrastructure <https://status.python.org/>`_.
    It can return errors::

        ProtocolError: ProtocolError for pypi.python.org/pypi: 503 No healthy backends
    """

    global _get_pypi_version_memoize
    key = module_name, full_list, url
    if key in _get_pypi_version_memoize:
        available = _get_pypi_version_memoize[key]
    else:

        with xmlrpc_client.ServerProxy(url) as pypi:

            def pypi_package_releases(module_name, b):
                nbtry = 0
                while nbtry < 2:
                    try:
                        available = pypi.package_releases(module_name, True)
                        return available
                    except TimeoutError as e:
                        nbtry += 1
                        warnings.warn(e)
                return None

            tried = [module_name]
            available = pypi_package_releases(module_name, True)

            if available is None or len(available) == 0:
                ntry = module_name.capitalize()
                if ntry not in tried:
                    tried.append(ntry)
                    available = pypi_package_releases(tried[-1], True)

            if available is None or len(available) == 0:
                ntry = module_name.replace("-", "_")
                if ntry not in tried:
                    tried.append(ntry)
                    available = pypi_package_releases(tried[-1], True)

            if available is None or len(available) == 0:
                ntry = module_name.replace("_", "-")
                if ntry not in tried:
                    tried.append(ntry)
                    available = pypi_package_releases(tried[-1], True)

            if available is None or len(available) == 0:
                ntry = module_name.lower()
                if ntry not in tried:
                    tried.append(ntry)
                    available = pypi_package_releases(tried[-1], True)

            if available is None or len(available) == 0:
                ml = module_name.lower()
                if ml == "markupsafe":
                    tried.append("MarkupSafe")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "flask-sqlalchemy":
                    tried.append("Flask-SQLAlchemy")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "apscheduler":
                    tried.append("APScheduler")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "datashape":
                    tried.append("DataShape")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "pycontracts":
                    tried.append("PyContracts")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "pybrain":
                    tried.append("PyBrain")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "pyexecjs":
                    tried.append("PyExecJS")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "dataspyre":
                    tried.append("DataSpyre")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "heapdict":
                    tried.append("HeapDict")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "pyreact":
                    tried.append("PyReact")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "qtpy":
                    tried.append("QtPy")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "pythonqwt":
                    tried.append("PythonQwt")
                    available = pypi_package_releases(tried[-1], True)
                elif ml == "onedrive-sdk-python":
                    tried.append("onedrivesdk")
                    available = pypi_package_releases(tried[-1], True)
                elif ml.startswith("orange3-"):
                    s = ml.split("-")[1]
                    ntry = "Orange3-" + s[0].upper() + s[1:]
                    tried.append(ntry)
                    available = pypi_package_releases(tried[-1], True)
                elif module_name in annoying_modules:
                    raise AnnoyingPackageException(module_name)

            # this raises a warning about an opened connection
            # see documentation of the function
            # del pypi

        if available is None or len(available) == 0:
            raise MissingPackageOnPyPiException("tried:\n" + "\n".join(tried))

        if full_list:
            _get_pypi_version_memoize[key] = available
            return available

        for a in available:
            spl = a.split(".")
            if len(spl) in (2, 3):
                last = spl[-1]
                if "a" not in last and "b" not in last and "dev" not in last:
                    _get_pypi_version_memoize[key] = available
                    return a
            else:
                _get_pypi_version_memoize[key] = available
                return a

        raise MissingVersionOnPyPiException(
            "{0}\nversion:\n{1}".format(module_name, "\n".join(available)))


def numeric_version(vers):
    """
    convert a string into a tuple with numbers wherever possible

    @param      vers    string
    @return             tuple
    """
    if isinstance(vers, tuple):
        return vers
    if isinstance(vers, list):
        raise Exception("unexpected value:" + str(vers))
    spl = vers.split(".")
    r = []
    for _ in spl:
        try:
            i = int(_)
            r.append(i)
        except:
            r.append(_)
    return tuple(r)


def compare_version(num, vers):
    """
    compare two versions

    @param      num     first version
    @param      vers    second version
    @return             -1, 0, 1
    """
    if num is None:
        if vers is None:
            return 0
        else:
            return 1
    if vers is None:
        return -1

    if not isinstance(vers, tuple):
        vers = numeric_version(vers)
    if not isinstance(num, tuple):
        num = numeric_version(num)

    if len(num) == len(vers):
        for a, b in zip(num, vers):
            if isinstance(a, int) and isinstance(b, int):
                if a < b:
                    return -1
                elif a > b:
                    return 1
            else:
                a = str(a)
                b = str(b)
                if a < b:
                    return -1
                elif a > b:
                    return 1
        return 0
    else:
        if len(num) < len(vers):
            num = num + (0,) * (len(vers) - len(num))
            return compare_version(num, vers)
        else:
            vers = vers + (0,) * (len(num) - len(vers))
            return compare_version(num, vers)


def version_consensus(v1, v2):
    """
    *v1* and *v2* are two versions of the same module, which one to keep?

    @param      v1      version 1
    @param      v2      version 2
    @return             consensus

    * ``v1=None``, ``v2='(>=1.5)'`` --> ``v='>=1.5'``

    To improve:

    * ``v1='<=1.6'``, ``v2='(>=1.5)'`` --> ``v='==1.6'``
    """
    reg = re.compile("([><=]*)([^><=]+)")

    def process_version(v):
        if isinstance(v, str  # unicode#
                      ):
            v = v.strip('()')
            find = reg.search(v)
            if not find:
                raise WrongVersionError(v)
            sign = find.groups()[0]
            number = numeric_version(find.groups()[1])
        else:
            try:
                sign, number = v
            except ValueError as e:
                raise ValueError("weird format: " + str(v) +
                                 " - " + str(type(v))) from e
        return sign, number

    if v1 is None:
        return v2
    elif v2 is None:
        return v1
    else:
        s1, n1 = process_version(v1)
        s2, n2 = process_version(v2)

        if s1 not in ('<=', '==', '<', '>', '>='):
            raise ValueError("wrong sign {0} for v1={1}", s1, v1)
        if s2 not in ('<=', '==', '<', '>', '>='):
            raise ValueError("wrong sign {0} for v1={1}", s2, v2)

        if s1 == "==":
            if s2 == "==":
                if compare_version(n1, n2) != 0:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
            else:
                res = s1, n1

        elif s1 == "<=":
            if s2 == "<=":
                res = s1, min(n1, n2)
            elif s2 == "==":
                if compare_version(n1, n2) < 0:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
                res = s2, n2
            elif s2 == '<':
                if compare_version(n1, n2) == -1:
                    res = s1, n1
                else:
                    res = s2, n2
            elif s2 in ('>', '>='):
                if compare_version(n1, n2) <= 0:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
                res = s1, n1

        elif s1 == "<":
            if s2 == "<":
                res = s1, min(n1, n2)
            elif s2 == "==":
                if compare_version(n1, n2) <= 0:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
                res = s2, n2
            elif s2 == '<=':
                if compare_version(n1, n2) <= 0:
                    res = s1, n1
                else:
                    res = s2, n2
            elif s2 in ('>', '>='):
                if compare_version(n1, n2) <= 0:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
                res = s1, n1

        elif s1 == ">=":
            if s2 == ">=":
                res = s1, max(n1, n2)
            elif s2 == "==":
                if compare_version(n1, n2) == -1:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
                res = s2, n2
            elif s2 == '>':
                if compare_version(n1, n2) <= 0:
                    res = s2, n2
                else:
                    res = s1, n1
            elif s2 in ('<', '<='):
                if compare_version(n1, n2) >= 0:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
                res = s2, n2

        elif s1 == ">":
            if s2 == ">":
                res = s1, max(n1, n2)
            elif s2 == "==":
                if compare_version(n1, n2) >= 0:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
                res = s2, n2
            elif s2 == '>=':
                if compare_version(n1, n2) == -1:
                    res = s2, n2
                else:
                    res = s1, n1
            elif s2 in ('<', '<='):
                if compare_version(n1, n2) == 1:
                    raise WrongVersionError(
                        "incompatible version: {0}{1} and {2}{3}".format(s1, n1, s2, n2))
                res = s2, n2
        else:
            res = None, None

        if res[0] is None:
            raise WrongVersionError(
                "incompatible version and wrong format: {0}{1} and {2}{3}".format(s1, n1, s2, n2))

        return '{0}{1}'.format(res[0], '.'.join(str(_) for _ in res[1]))

_get_module_dependencies_deps = None


def get_module_dependencies(module, use_cmd=False, deep=False, collapse=True, use_pip=None, refresh_cache=False):
    """
    return the dependencies for a module

    @param      module          unused, None
    @param      use_cmd         use command line
    @param      deep            dig into dependencies of dependencies
    @param      collapse        only one row per module
    @param      use_pip         use pip to discover dependencies or not (parse metadata)
    @param      refresh_cache   refresh the cache (see below)
    @return                     list of tuple (module, version, required by as a str)
                                or dictionary  { module: (version, required by as a list) } if *collapse* is True

    The function which uses *use_pip=True* is not fully tested, it does not
    return contraints (== 2.4). The function caches the results to avoid doing it again
    during a second execution unless *refresh_cache* is True

    This function is not tested on Python 2.7.
    """
    if use_pip is None:
        use_pip = not sys.platform.startswith("win")

    if use_pip:
        global _get_module_dependencies_deps
        if _get_module_dependencies_deps is None or refresh_cache:
            temp = call_get_installed_distributions(
                local_only=False, skip=[], use_cmd=use_cmd)
            _get_module_dependencies_deps = dict(
                (p.key, (p, p.requires())) for p in temp)
        if module not in _get_module_dependencies_deps:
            raise ValueError("module {0} was not installed".format(module))
        res = []
        dist, req = _get_module_dependencies_deps[module]
        if isinstance(req, list):
            for r in req:
                res.append((r.key, None, module))
        else:
            res.append((req.key, None, module))
    else:
        meta = get_module_metadata(
            module, use_cmd, refresh_cache=refresh_cache)
        if meta is None:
            raise ImportError(
                "unable to get metadata for {0} - refresh_cache={1}".format(module, refresh_cache))
        deps = [v for k, v in meta.items() if "Requires" in k]
        res = []
        for d in deps:
            if not isinstance(d, list):
                dl = [d]
            else:
                dl = d
            for v in dl:
                spl = v.split()
                if len(spl) == 1:
                    key = (v, None, module)
                else:
                    key = (spl[0], spl[1], module)
                if key not in res:
                    res.append(key)

    if deep:
        done = {module: None}
        mod = 1
        while mod > 0:
            mod = 0
            for r in res:
                if r[0] not in done:
                    temp = get_module_dependencies(
                        r[0], use_cmd=use_cmd, deep=deep, collapse=False, use_pip=use_pip, refresh_cache=refresh_cache)
                    for key in temp:
                        if key not in res:
                            res.append(key)
                    mod += 1
                    done[r[0]] = None

    if collapse:
        final = {}
        for name, version, required in res:
            if name not in final:
                final[name] = (version, [required])
            else:
                ex = final[name][1]
                if required not in ex:
                    ex.append(required)
                    try:
                        v = version_consensus(final[name][0], version)
                    except WrongVersionError as e:
                        raise WrongVersionError("unable to reconcile versions:\n{0}\n{1}".format(
                            ex, str((name, version, required)))) from e
                    final[name] = (v, ex)
        final = {k: (v[0], list(sorted(v[1]))) for k, v in final.items()}
        return final
    else:
        return [(name, version.strip('()') if version is not None else version, required)
                for name, version, required in res]


def choose_most_recent(list_name):
    """
    choose the most recent version for a list of module names

    @param      list_name       list of names
    @return                     most recent version or None if the input list is empty

    In the following case, we would choose the first option::

        numpy-1.10.0+mkl-cp34-none-win_amd64.whl
        numpy-1.9.1.0+mkl-cp34-none-win_amd64.whl
    """
    if len(list_name) == 0:
        return None
    if isinstance(list_name[0], tuple):
        list_name = [(_[-1], _) for _ in list_name]
    else:
        list_name = [(_, _) for _ in list_name]

    version = re.compile(regex_wheel_version)
    version4 = re.compile(regex_wheel_version2)

    def search_regex(_):
        try:
            resv = version.search(_[0])
        except TypeError as e:
            raise TypeError("unable to parse '{0}'".format(_)) from e
        if resv is None and "pywin32" in _[0]:
            version2 = re.compile(regex_wheel_version.replace(
                "[0-9]+[.][abc0-9]+", "[0-9]{3}"))
            resv = version2.search(_[0])
        if resv is None:
            resv = version4.search(_[0])
        if resv is None:
            raise MissingVersionWheelException(
                "unable to get version number for regex {}:\n{}\n{}".format(_, regex_wheel_version, regex_wheel_version2))
        return resv

    list_name = [(search_regex(_).groups()[0], _[0], _[1])
                 for _ in list_name]

    def cmp(el1, el2):
        return compare_version(el1[0], el2[0])

    list_name = list(sorted(list_name, key=functools.cmp_to_key(cmp)))
    return list_name[-1][-1]


def get_wheel_version(whlname):
    """
    extract the version from a wheel file,
    return ``2.6.0`` for ``rpy2-2.6.0-cp34-none-win_amd64.whl``

    @param      whlname     file name
    @return                 string
    """
    exp = re.compile(regex_wheel_version)
    find = exp.findall(whlname)
    if len(find) == 0:
        exp = re.compile(regex_wheel_version2)
        find = exp.findall(whlname)
    if len(find) == 0:
        raise ValueError(
            "[get_wheel_version] unable to extract version of {0} (pattern: {1})".format(whlname, exp.pattern))
    if len(find) > 1:
        raise ValueError(
            "[get_wheel_version] unable to extract version of {0} (multiple version) (pattern: {1})".format(whlname, exp.pattern))
    return find[0][0]
