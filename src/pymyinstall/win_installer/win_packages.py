"""
@file
@brief To install packages for a specific distribution.
"""
from __future__ import print_function

import os
import sys
from .win_exception import WinInstallPackageException
from ..installhelper.install_cmd_helper import run_cmd
from ..installhelper.module_install import get_module_version
from ..packaged.packaged_config import installation_ensae, installation_teachings


def get_modules_version():
    """
    calls @see fn get_module_version
    """
    return get_module_version(None)


def win_install_package_other_python(python_path, package, verbose=False, fLOG=print):
    """
    Install a package for another Python distribution than the current one.

    @param      python_path     location of python
    @param      package         location of the package (.tar.gz or .whl)
    @param      verbose         display more information
    @param      fLOG            logging function
    @return                     operations ("pip", module) if installed, empty if already installed
    """
    if verbose:
        fLOG("*** INSTALL", package)
    operations = []

    if sys.version_info[0] == 2:
        pip = os.path.join(python_path, "Scripts", "pip.exe")
    else:
        pip = os.path.join(python_path, "Scripts", "pip3.exe")

    if not os.path.exists(pip):
        raise FileNotFoundError(pip)

    cmd = "{0} install {1}".format(pip, package)
    if verbose:
        fLOG(cmd)

    cur = os.getcwd()
    if cur != python_path:
        os.chdir(python_path)

    out, err = run_cmd(cmd, wait=True, fLOG=fLOG, do_not_log=True)

    if cur != python_path:
        os.chdir(cur)

    if verbose:
        fLOG(out)

    if err is not None and len(err) > 0:
        raise WinInstallPackageException(
            "unable to install {0}, due to:\nOUT:\n{0}\nERR:\n{1}".format(package, out, err))

    if "No distributions matching the version" in out:
        raise WinInstallPackageException(
            "unable to install " +
            package +
            "\nOUT:\n" +
            out +
            "\nERR:\n" +
            err)
    elif "Testing of typecheck-decorator passed without failure." in out:
        operations.append(("pip", package))
    elif "Successfully installed" not in out:
        if "error: Unable to find vcvarsall.bat" in out:
            url = "http://www.xavierdupre.fr/blog/2013-07-07_nojs.html"
            raise WinInstallPackageException(
                "unable to install " +
                package +
                "\nread:\n" +
                url +
                "OUT:\n" +
                out +
                "\nERR:\n" +
                err)
        if "Requirement already satisfied" not in out:
            raise WinInstallPackageException(
                "unable to install " +
                package +
                "\nOUT:\n" +
                out +
                "\nERR:\n" +
                err)
    else:
        operations.append(("pip", package))

    return operations


def _is_package_in_list(module_name, list_packages):
    """
    determines of this package is the one for the given module_name

    @param      list_packages       list of packages names (list of wheel)
    @param      module_name         module name
    @return                         package name
    """
    module_name = module_name.lower()
    p = "." in module_name
    if p:
        pp = module_name.replace(".", "_")

    d = "-" in module_name
    if d:
        pd = module_name.split("-")
        if len(pd[-1]) == 0:
            pd = "_".join(pd[:-1]) + "-"
        else:
            pd = "_".join(pd)

    for a in list_packages:
        al = a.lower()
        if "theme-" in al:
            al = al.split("theme-")
            al = al[0].replace("-", "_") + "theme-" + al[1]

        if al.startswith(module_name):
            return a
        if p and al.startswith(pp):
            return a
        if d and al.startswith(pd):
            return a
    return None


def is_package_installed(python_path, module_name):
    """
    not very accurate but it should speed up the process

    @param      python_path     python path
    @param      module_name     module name (import name)
    @return                     boolean
    """
    if isinstance(module_name, str  # unicode#
                  ):
        module_name = [module_name]
    modules = get_modules_version()
    for name in module_name:
        if name in modules:
            return True
        pymy = os.path.join(python_path, "lib", "site-packages", name)
        r = os.path.exists(pymy)
        if r:
            return True
    return False


def win_install_packages_other_python(python_path, package_folder, verbose=False, fLOG=print):
    """
    Install all packages for another Python distribution
    where package could be found in a folder

    @param      python_path     location of python
    @param      package_folder  location of the package (.tar.gz or .whl)
    @param      verbose         display more information
    @param      fLOG            logging function
    @return                     operations ("pip", module) if installed, empty if already installed
    """
    files = os.listdir(package_folder)
    files = [_ for _ in files if os.path.splitext(_)[-1] in {".gz", ".zip", ".whl"}
             and _ not in {"Scite.zip", "scite.zip"}
             and not _.startswith("SQLiteSpy_")]

    # we need to order the package to install them in the right order
    # it speeds up the process and avoid using C++ compiler
    operations = []
    done = set()
    full_list = installation_ensae() + installation_teachings()
    for mod in full_list:
        a = _is_package_in_list(mod.name + "-", files)
        if a is None:
            continue
        if a not in done:
            mname = mod.mname if mod.mname is not None else mod.name
            if not is_package_installed(python_path, [mod.name, mname]):
                full = os.path.join(package_folder, a)
                try:
                    op = win_install_package_other_python(
                        python_path, full, verbose=verbose, fLOG=fLOG)
                except Exception as e:
                    mes = "failed to install {0}: {1}".format(mod.name, full)
                    raise Exception(mes) from e
                if len(op) > 0:
                    fLOG("installed", mod.name, " with ", a)
                operations.extend(op)
            done.add(a)

    if verbose:
        fLOG("*** install packages with unknown dependencies")
    for pack in files:
        if pack not in done:
            full = os.path.join(package_folder, pack)
            op = win_install_package_other_python(
                python_path, full, verbose=verbose, fLOG=fLOG)
            if len(op) > 0:
                fLOG("installed", pack, " with ", full)
            else:
                fLOG("skipped package", pack, " from ", full)
            operations.extend(op)

    return operations
