"""
@file
@brief Functions to prepare a setup on Windows, R functions
"""
import os
from ..installhelper.install_cmd_helper import run_cmd

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

    os.environ["R_LIBS"] = os.path.join(r_path, "library")
    cmd = [exe, "CMD", "BATCH", script]
    if output is not None:
        cmd.append(output)
    cmd = " ".join(cmd)
    out, err = run_cmd(cmd, wait=True)
    if err is not None and len(err) > 0:
        raise RBatchException(
            "CMD:\n{0}\nOUT:\n{1}\nERR:\{2}".format(cmd, out, err))
    return out


def get_package_description(r_path, pack):
    """
    returns the description of an R package as a dictionary

    @param      r_path      path to R
    @param      pack        package name
    @return                 dictionary
    """
    path = os.path.join(r_path, "library", pack)
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    version = os.path.join(path, "DESCRIPTION")
    if not os.path.exists(version):
        raise FileNotFoundError(version)
    with open(version, "r") as f:
        lines = f.readlines()
    res = {}
    for line in lines:
        spl = line.split(":")
        if len(spl) > 1:
            key = spl[0]
            val = ":".join(spl[1:])
            res[key] = val
    return res
