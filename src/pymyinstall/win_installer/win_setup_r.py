"""
@file
@brief Functions to prepare a setup on Windows, R functions
"""
import os
from ..installhelper import run_cmd

_script = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "R_install.r")


class RBatchException(Exception):

    """
    raised when running R in batch mode
    """
    pass


def r_run_script(r_path, script, output=None):
    """
    run a script on R

    @param      r_path      r location
    @param      script      script to run
    @param      output      where to store the output (can be None)
    @return                 output
    """
    exe = os.path.join(r_path, "bin", "x64", "R.exe")
    if not os.path.exists(exe):
        raise FileNotFoundError(exe)

    cmd = [exe, "CMD", "BATCH", script]
    if output is not None:
        cmd.append(output)
    cmd = " ".join(cmd)
    out, err = run_cmd(cmd, wait=True)
    if err is not None and len(err) > 0:
        raise RBatchException(
            "CMD:\n{0}\nOUT:\n{1}\nERR:\{2}".format(cmd, out, err))
    return out
