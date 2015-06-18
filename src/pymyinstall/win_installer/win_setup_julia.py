"""
@file
@brief Functions to prepare a setup on Windows, R functions
"""
import os
from ..installhelper.install_cmd_helper import run_cmd

_script = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "Julia_install.jl")


class JuliaBatchException(Exception):

    """
    raised when running R in batch mode
    """
    pass


def julia_run_script(julia_path, script):
    """
    run a script on Julia

    @param      julia_path  julia location
    @param      script      script to run
    @return                 output
    """
    exe = os.path.join(julia_path, "bin", "julia.exe")
    if not os.path.exists(exe):
        raise FileNotFoundError(exe)
    pkg = os.path.join(julia_path, "pkg")
    if not os.path.exists(pkg):
        os.mkdir(pkg)

    os.environ["JULIA_PKGDIR"] = pkg
    cmd = [exe, script, "--no_history-file"]
    cmd = " ".join(cmd)
    out, err = run_cmd(cmd, wait=True)
    if err is not None and len(err) > 0 and \
            "err" in err.lower() or "warn" in err.lower():
        raise JuliaBatchException(
            "CMD:\n{0}\nOUT:\n{1}\nERR:\n{2}".format(cmd, out, err))
    return out
