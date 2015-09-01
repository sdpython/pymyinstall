"""
@file
@brief Functions to get module version, license
"""
import sys

if sys.version_info[0] == 2:
    import urllib2 as urllib_request
    import xmlrpclib as xmlrpc_client
else:
    import urllib.request as urllib_request
    import xmlrpc.client as xmlrpc_client

from .install_cmd_helper import run_cmd, get_pip_program
from .install_memoize import install_memoize
from .module_install_exceptions import MissingPackageOnPyPiException, AnnoyingPackageException, ConfigurationError, MissingVersionOnPyPiException


annoying_modules = {"pygame", "liblinear", "mlpy", "VideoCapture",
                    "libsvm", "opencv_python", "scikits.cuda",
                    "NLopt"}


@install_memoize
def get_page_wheel(page):
    """
    get the page

    @param      page        location
    @return                 page content
    """
    req = urllib_request.Request(
        page,
        headers={
            'User-agent': 'Mozilla/5.0'})
    u = urllib_request.urlopen(req)
    text = u.read()
    u.close()
    text = text.decode("utf8")
    text = text.replace("&quot;", "'")
    text = text.replace("&#8209;", "-")
    return text


def call_get_installed_distributions(local_only=True,
                                     skip=None,
                                     include_editables=True,
                                     editables_only=False,
                                     user_only=False):
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
    @return                 list of installed Distribution objects.
    """
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
            v = mod.version
            res[a] = v
            if a != al:
                res[al] = v

    _get_module_version_manual_memoize.update(res)
    return res


_get_module_metadata_manual_memoize = {}


def get_module_metadata(module, use_cmd=False):
    """
    return a dictionary { module:metadata }

    @param      module      unused, None
    @return                 dictionary
    """
    if module is not None:
        modl = module.lower()
        res = get_module_metadata(None, use_cmd=use_cmd)
        return res.get(modl, None)

    global _get_module_metadata_manual_memoize
    if len(_get_module_metadata_manual_memoize) > 0:
        return _get_module_metadata_manual_memoize

    res = {}
    # local_only must be False to get all modules
    # not only the ones installed in the virtual environment
    dist = call_get_installed_distributions(local_only=False)
    if len(dist) == 0:
        raise ConfigurationError("no installed module, unexpected (pip should be there): sys.executable={0}, sys.prefix={1}, sys.base_prefix={2}".format(
            sys.executable, sys.prefix, sys.base_prefix))
    for mod in dist:
        d = {}
        lines = mod._get_metadata(mod.PKG_INFO)
        for line in lines:
            spl = line.split(":")
            d[spl[0].strip()] = ":".join(spl[1:]).strip()
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
    """
    global _get_pypi_version_memoize
    key = module_name, full_list, url
    if key in _get_pypi_version_memoize:
        available = _get_pypi_version_memoize[key]
    else:

        pypi = xmlrpc_client.ServerProxy(url)
        tried = [module_name]
        available = pypi.package_releases(module_name, True)

        if available is None or len(available) == 0:
            tried.append(module_name.capitalize())
            available = pypi.package_releases(tried[-1], True)

        if available is None or len(available) == 0:
            tried.append(module_name.replace("-", "_"))
            available = pypi.package_releases(tried[-1], True)

        if available is None or len(available) == 0:
            tried.append(module_name.replace("_", "-"))
            available = pypi.package_releases(tried[-1], True)

        if available is None or len(available) == 0:
            tried.append(module_name.lower())
            available = pypi.package_releases(tried[-1], True)

        if available is None or len(available) == 0:
            ml = module_name.lower()
            if ml == "markupsafe":
                tried.append("MarkupSafe")
                available = pypi.package_releases(tried[-1], True)
            elif ml == "flask-sqlalchemy":
                tried.append("Flask-SQLAlchemy")
                available = pypi.package_releases(tried[-1], True)
            elif ml == "apscheduler":
                tried.append("APScheduler")
                available = pypi.package_releases(tried[-1], True)
            elif ml == "datashape":
                tried.append("DataShape")
                available = pypi.package_releases(tried[-1], True)
            elif ml == "pycontracts":
                tried.append("PyContracts")
                available = pypi.package_releases(tried[-1], True)
            elif ml == "pybrain":
                tried.append("PyBrain")
                available = pypi.package_releases(tried[-1], True)
            elif ml == "jsanimation":  # github
                tried.append("JSAnimation")
                available = ["-"]
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
