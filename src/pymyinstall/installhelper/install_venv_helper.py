"""
@file
@brief Helpers for virtualenv
"""
from __future__ import print_function

import os
import sys
from .install_cmd_helper import run_cmd

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


class VirtualEnvError(RuntimeError):
    """
    exception raised by the function implemented in this file
    """
    pass


def build_venv_cmd(params, posparams):
    """
    builds the command line for virtual env

    @param      params      dictionary of parameters
    @param      posparams   positional arguments
    @return                 string
    """
    import venv
    dir(venv)
    exe = sys.executable.replace("w.exe", "").replace(".exe", "")
    cmd = [exe, "-m", "venv"]
    for k, v in params.items():
        if v is None:
            cmd.append("--" + k)
        else:
            cmd.append("--" + k + "=" + v)
    cmd.extend(posparams)
    return " ".join(cmd)


def create_virtual_env(where, symlinks=False, system_site_packages=False,
                       clear=True, packages=None, fLOG=print,
                       temp_folder=None):
    """
    .. index:: virtual environment

    create a virtual environment

    @param      where                   location of this virtual environment
    @param      symlinks                attempt to symlink rather than copy
    @param      system_site_packages    Give the virtual environment access to the system site-packages dir
    @param      clear                   Delete the environment directory if it already exists.
                                        If not specified and the directory exists, an error is raised.
    @param      packages                list of packages to install (it will install module
                                        :epkg:`pymyinstall`).
    @param      fLOG                    logging function
    @param      temp_folder             temporary folder (to download module if needed), by default ``<where>/download``
    @return                             stand output

    .. exref::
        :title: Create a virtual environment

        The following example creates a virtual environment.
        Packages can be added by specifying the parameter *package*.

        ::

            from pyquickhelper.pycode import create_virtual_env
            fold = "my_env"
            if not os.path.exists(fold):
                os.mkdir(fold)
            create_virtual_env(fold)
    """
    fLOG("[pymy] create virtual environment at:", where)
    params = {}
    if symlinks:
        params["symlinks"] = None
    if system_site_packages:
        params["system-site-packages"] = None
    if clear:
        params["clear"] = None
    cmd = build_venv_cmd(params, [where])
    out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
    if len(err) > 0:
        raise VirtualEnvError(
            "unable to create virtual environement at {2}\nCMD:\n{3}\nOUT:\n{0}\nERR-G:\n{1}".format(out, err, where, cmd))

    if sys.platform.startswith("win"):
        scripts = os.path.join(where, "Scripts")
    else:
        scripts = os.path.join(where, "bin")

    if not os.path.exists(scripts):
        files = "\n  ".join(os.listdir(where))
        raise FileNotFoundError(
            "unable to find {0}, content:\n  {1}".format(scripts, files))

    in_scripts = os.listdir(scripts)
    pips = [_ for _ in in_scripts if _.startswith("pip")]
    if len(pips) == 0:
        out += venv_install(where, "pip", fLOG=fLOG,
                            temp_folder=temp_folder)
    in_scripts = os.listdir(scripts)
    pips = [_ for _ in in_scripts if _.startswith("pip")]
    if len(pips) == 0:
        raise FileNotFoundError(
            "unable to find pip in {0}, content:\n  {1}".format(scripts, in_scripts))

    if packages is not None and len(packages) > 0:
        fLOG("[pymy] install packages in:", where)
        packages = [_ for _ in packages if _ != "pymyinstall" and _ != "pip"]
        if len(packages) > 0:
            out += venv_install(where, packages, fLOG=fLOG,
                                temp_folder=temp_folder)
    return out


def venv_install(venv, packages, fLOG=print, temp_folder=None):
    """
    install a package or a list of packages in a virtual environment

    @param      venv            location of the virtual environment
    @param      packages        a package (str) or a list of packages(list[str])
    @param      fLOG            logging function
    @param      temp_folder     temporary folder (to download module if needed), by default ``<where>/download``
    @return                     standard output
    """
    if temp_folder is None:
        temp_folder = os.path.join(venv, "download")

    if isinstance(packages, str):
        packages = [packages]

    if packages == "pip" or packages == ["pip"]:
        from .get_pip import __file__ as pip_loc
        ppath = os.path.abspath(pip_loc.replace(".pyc", ".py"))
        script = ["-u", ppath]
        out = run_venv_script(venv, script, fLOG=fLOG, is_cmd=True)

        if sys.platform.startswith("win"):
            scripts = os.path.join(venv, "Scripts")
        else:
            scripts = os.path.join(venv, "bin")
        in_scripts = os.listdir(scripts)
        pips = [_ for _ in in_scripts if _.startswith("pip")]
        if len(pips) == 0:
            raise FileNotFoundError(
                "unable to find pip in {0},\nvenv:\n{2}\nppath:\n{3}\ncontent:\n  {1}".format(scripts, in_scripts, venv, ppath))
        return out
    else:
        p = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", ".."))
        ls = ','.join("'{0}'".format(_) for _ in packages)
        script = ["import sys",
                  "sys.path.append('{0}')".format(p.replace("\\", "\\\\")),
                  "import pymyinstall",
                  "ps=[{0}]".format(ls),
                  "t='{0}'".format(temp_folder.replace("\\", "\\\\")),
                  "pymyinstall.packaged.install_all(temp_folder=t,list_module=ps,up_pip=False)"]
        return run_venv_script(venv, "\n".join(script), fLOG=fLOG)


def run_venv_script(venv, script, fLOG=print, file=False, is_cmd=False):
    """
    run a script on a virtual environment (the script should be simple

    @param      venv        virtual environment
    @param      script      script as a string (not a file)
    @param      fLOG        logging function
    @param      file        is script a file or a string to execute
    @param      is_cmd      if True, script is a command line to run (as a list) for python executable
    @return                 output
    """
    if sys.platform.startswith("win"):
        exe = os.path.join(venv, "Scripts", "python")
    else:
        exe = os.path.join(venv, "bin", "python")
    if is_cmd:
        cmd = " ".join([exe, script])
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        if len(err) > 0:
            raise VirtualEnvError(
                "unable to run cmd at {2}\nCMD:\n{3}\nOUT:\n{0}\nERR-H:\n{1}".format(out, err, venv, cmd))
        return out
    else:
        script = ";".join(script.split("\n"))
        if file:
            if not os.path.exists(script):
                raise FileNotFoundError(script)
            cmd = " ".join([exe, "-u", '"{0}"'.format(script)])
        else:
            cmd = " ".join([exe, "-u", "-c", '"{0}"'.format(script)])
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        if len(err) > 0:
            raise VirtualEnvError(
                "unable to run script at {2}\nCMD:\n{3}\nOUT:\n{0}\nERR-I:\n{1}".format(out, err, venv, cmd))
        return out


def run_cmd_path(python_path, script, fLOG=print, file=False, is_cmd=False, **kwargs):
    """
    run a script knowing python path, it does not raise an exception.

    @param      python_path     python path
    @param      script          script as a string (not a file) or command line if *is_cmd* is True
    @param      fLOG            logging function
    @param      file            is script a file or a string to execute
    @param      is_cmd          if True, script is a command line to run (as a list) for python executable
    @param      kwargs          extra parameters
    @return                     output, error
    """
    if sys.platform.startswith("win"):
        exe = os.path.join(python_path, "python")
    else:
        python_name = "python" if sys.version_info[
            0] == 2 else "python%d" % sys.version_info[0]
        exe = os.path.join(python_path, python_name)
        if not os.path.exists(exe):
            exe = os.path.join(python_path, "bin", python_name)
    if is_cmd:
        cmd = " ".join([exe] + script)
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG, **kwargs)
        return out, err
    else:
        script = ";".join(script.split("\n"))
        if file:
            if not os.path.exists(script):
                raise FileNotFoundError(script)
            cmd = " ".join([exe, "-u", '"{0}"'.format(script)])
        else:
            cmd = " ".join([exe, "-u", "-c", '"{0}"'.format(script)])
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG, **kwargs)
        return out, err
