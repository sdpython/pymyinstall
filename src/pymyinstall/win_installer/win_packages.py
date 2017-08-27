"""
@file
@brief To install packages for a specific distribution.
"""
from __future__ import print_function

import os
import sys
from .win_exception import WinInstallPackageException
from ..installhelper.install_cmd_helper import run_cmd, get_pip_program
from ..packaged import ensae_fullset, find_module_install

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def get_modules_version(python_path):
    """
    return a dictionary { module:version }

    @param      python_path     path to python
    @return                     dictionary
    """
    if sys.platform.startswith("win"):
        prog = os.path.join(python_path, "Scripts", "pip.exe")
        if not os.path.exists(prog):
            prog = get_pip_program(exe=python_path)
    else:
        prog = get_pip_program(exe=python_path)

    cmd = prog + " list"
    from pip import __version__
    if int(__version__.split(".")[0]) >= 9:
        cmd += " --format=legacy"

    try:
        out, err = run_cmd(cmd, wait=True, fLOG=None, change_path=python_path)
    except Exception as e:
        raise Exception("unable to run: {0}".format(cmd)) from e

    if err is not None and len(err) > 0:
        if len(err.split("\n")) > 3 or \
           "You should consider upgrading via the 'pip install --upgrade pip' command." not in err:
            raise Exception("unable to run, #lines {0}\nERR-8:\n{1}\nOUT:\n{2}".format(
                len(err.split("\n")), err, out))

    lines = out.split("\n")
    res = {}
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
    return res


def win_install_package_other_python(python_path, package, verbose=False, deps=True, fLOG=print):
    """
    Install a package for another Python distribution than the current one.

    @param      python_path     location of python
    @param      package         location of the package (.tar.gz, .whl, .tgz, .bz2)
    @param      verbose         display more information
    @param      deps            take dependencies into account or not
    @param      fLOG            logging function
    @return                     operations ("pip", module) if installed, empty if already installed

    .. versionchanged:: 1.1
        ``deps=False`` is the default for module zipline
    """
    thename = os.path.split(package)[-1]
    if thename == "jenkins.zip":
        # jenkins.zip is not a python package
        return []
    if verbose:
        fLOG("[pymy] *** INSTALL", package)
    operations = []

    if sys.version_info[0] == 2:
        pip = os.path.join(python_path, "Scripts", "pip.exe")
    else:
        pip = os.path.join(python_path, "Scripts",
                           "pip%d.exe" % sys.version_info[0])

    if not os.path.exists(pip):
        raise FileNotFoundError(pip)

    cmd = "{0} install {1}".format(pip, package)
    if verbose:
        fLOG(cmd)

    cur = os.getcwd()
    if cur != python_path:
        os.chdir(python_path)
    name = os.path.split(package)[-1]
    if (deps is not None and not deps) or name.startswith("zipline"):
        cmd += " --no-deps"

    out, err = run_cmd(cmd, wait=True, fLOG=fLOG)

    if cur != python_path:
        os.chdir(cur)

    if verbose:
        fLOG(out)

    if err is not None and len(err) > 0:
        name = "-".join(package.split("-")[:-1])
        look = "Successfully installed " + name
        if look not in err:
            raise WinInstallPackageException(
                "unable to install {0}, due to:\nCMD\n{3}\nOUT:\n{1}\nERR-9:\n{2}\nNOT FOUND\n{4}".format(package, out, err, cmd, look))

    if "No distributions matching the version" in out:
        raise WinInstallPackageException(
            "unable to install " +
            package +
            "\nCMD\n" +
            cmd +
            "\nOUT:\n" +
            out +
            "\nERR--A:\n" +
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
                "\nCMD\n" +
                cmd +
                "OUT:\n" +
                out +
                "\nERR--B:\n" +
                err)
        if "Requirement already satisfied" not in out:
            raise WinInstallPackageException(
                "unable to install " +
                package +
                "\nCMD\n" +
                cmd +
                "\nOUT:\n" +
                out +
                "\nERR--C:\n" +
                err)
    else:
        operations.append(("pip", package))

    return operations


def _is_package_in_list(module_name, list_packages, no_wheel=False):
    """
    determines of this package is the one for the given module_name

    @param      list_packages       list of packages names (list of wheel)
    @param      module_name         module name
    @param      no_wheel            skip wheels
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
        if no_wheel and al.endswith(".whl"):
            continue
        if module_name == "python" and ".msi" not in a:
            continue
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


def is_package_installed(python_path, module_name, installed_packages=None):
    """
    not very accurate but it should speed up the process

    @param      python_path         python path
    @param      module_name         module name (import name)
    @param      installed_packages  list of installed packages (can be None)
    @return                         boolean
    """
    if isinstance(module_name, str  # unicode#
                  ):
        module_name = [module_name]
    modules = get_modules_version(python_path)
    for name in module_name:
        if name in modules:
            return True
        if installed_packages is not None and name in installed_packages:
            return True
        pymy = os.path.join(python_path, "lib", "site-packages", name)
        if os.path.exists(pymy):
            return True
        pymy += ".py"
        if os.path.exists(pymy):
            return True
        pymy = pymy.replace(".py", ".cp%d%d-win_amd64.pyd" %
                            (sys.version_info[0], sys.version_info[1]))
        if os.path.exists(pymy):
            return True
        mod = find_module_install(name)
        if mod:
            pymy = os.path.join(python_path, "lib", "site-packages", mod.mname)
            if os.path.exists(pymy):
                return True
    return False


def win_install_packages_other_python(python_path, package_folder, verbose=False, module_list=None, fLOG=print):
    """
    Install all packages for another Python distribution
    where package could be found in a folder

    @param      python_path     location of python
    @param      package_folder  location of the package (.tar.gz, .whl, .bz2, .tgz)
    @param      verbose         display more information
    @param      module_list     list of modules to install, if None, it tries to guess a good
                                order to install downloaded packages
    @param      fLOG            logging function
    @return                     operations ("pip", module) if installed, empty if already installed
    """
    files = os.listdir(package_folder)
    files = [_ for _ in files if os.path.splitext(_)[-1] in {".gz", ".zip", ".whl", ".bz2", ".tgz"} and
             _ not in {"Scite.zip", "scite.zip"} and
             not _.startswith("SQLiteSpy_")]

    # we need to order the package to install them in the right order
    # it speeds up the process and avoid using C++ compiler
    operations = []
    done = set()
    if module_list is None:
        full_list = ensae_fullset()
    else:
        full_list = module_list

    # existing list
    installed_packages = get_modules_version(python_path)

    for mod in full_list:
        a = _is_package_in_list(mod.name + "-", files)
        if a is None:
            continue
        if a not in done:
            mname = mod.mname if mod.mname is not None else mod.name
            if not is_package_installed(python_path, [mod.name, mname], installed_packages):
                full = os.path.join(package_folder, a)
                try:
                    op = win_install_package_other_python(
                        python_path, full, verbose=verbose, deps=mod.deps, fLOG=fLOG)
                except Exception as e:
                    mes = "failed to install {0}: {1}".format(mod.name, full)
                    raise Exception(mes) from e
                if len(op) > 0:
                    fLOG("[pymy] installed", mod.name, " with ", a)
                operations.extend(op)
            done.add(a)

    if verbose:
        fLOG("[pymy] *** install packages with unknown dependencies")
    for pack in files:
        if pack not in done:
            full = os.path.join(package_folder, pack)
            op = win_install_package_other_python(
                python_path, full, verbose=verbose, fLOG=fLOG)
            if len(op) > 0:
                fLOG("[pymy] installed", pack, " with ", full)
            else:
                fLOG("[pymy] skipped package", pack, " from ", full)
            operations.extend(op)

    return operations
