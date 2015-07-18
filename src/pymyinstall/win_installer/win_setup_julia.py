"""
@file
@brief Functions to prepare a setup on Windows, R functions
"""
from __future__ import print_function

import os
from ..installhelper.install_cmd_helper import run_cmd

if sys.version_info[0] == 2:
    from codecs import open


_script_install = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "Julia_install.jl")

_script_build = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "Julia_build.jl")

_script_init = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "Julia_init.jl")


class JuliaBatchException(Exception):

    """
    raised when running R in batch mode
    """
    pass


def julia_run_script(julia_path, python_path, script, verbose=False, fLOG=print):
    """
    run a script on Julia

    @param      julia_path      julia location
    @param      script          script to run
    @param      python_path     path to python
    @param      verbose         more information
    @param      fLOG            logging function
    @return                     output
    """
    memo_path = os.environ["PATH"]
    epath = memo_path + ";" + \
        ";".join([python_path, os.path.join(python_path, "Scripts")])
    os.environ["PATH"] = epath

    exe = os.path.join(julia_path, "bin", "julia.exe")
    if not os.path.exists(exe):
        raise FileNotFoundError(exe)
    pkg = os.path.join(julia_path, "pkg")
    if not os.path.exists(pkg):
        os.mkdir(pkg)

    os.environ["JULIA_PKGDIR"] = pkg
    cmd = [exe, script, "--no_history-file"]
    cmd = " ".join(cmd)
    if verbose:
        fLOG("set JULIA_PKGDIR=" + pkg)
    out, err = run_cmd(cmd, wait=True)
    if err is not None and len(err) > 0 and \
            "err" in err.lower() or "warn" in err.lower():
        raise JuliaBatchException(
            "CMD:\n{0}\nOUT:\n{1}\nERR:\n{2}".format(cmd, out, err))

    os.environ["PATH"] = memo_path
    patch_julia03(julia_path, verbose=verbose, fLOG=fLOG)
    return out


def patch_julia03(julia_path, verbose=False, fLOG=print):
    """
    patch absolute path in packages such as Julia/ZMQ or Julia/Nettle.

    @param      julia_path      julia_path
    @param      verbose         more information
    @param      fLOG            logging function
    """
    pkg = os.path.join(julia_path, "pkg")
    pkg_d = pkg.replace("\\", "\\\\")
    if verbose:
        fLOG("  string to replace", pkg_d)
    for root, dirs, files in os.walk(pkg):
        for name in files:
            if name.endswith("deps.jl"):
                full = os.path.join(root, name)
                with open(full, "r", encoding="utf8") as f:
                    content = f.read()
                if pkg_d in content:
                    content = content.replace(pkg_d, "%JULIA_PKGDIR%")
                    if verbose:
                        fLOG("  patch ", full)
                    with open(full, "w", encoding="utf8") as f:
                        f.write(content)
