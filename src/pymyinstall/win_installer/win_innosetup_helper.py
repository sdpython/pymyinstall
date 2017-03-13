"""
@file
@brief Functions to prepare a setup on Windows, use InnoSetup
"""
from __future__ import print_function

import os
import sys
from ..installhelper.install_cmd_helper import run_cmd
from .win_ipy_kernels import install_kernels

if sys.version_info[0] == 2:
    from codecs import open
    FileNotFoundError = Exception


class InnoSetupException(Exception):

    """
    Exception happening with InnoSetup
    """
    pass


def find_innosetup():
    """
    find InnoSetup executable

    @return     executable
    """
    exe = r"C:\Program Files (x86)\Inno Setup 5\compil32.exe"
    if not os.path.exists(exe):
        raise FileNotFoundError(exe)
    return exe


def run_innosetup(new_script, innosetup=None, log_script=None, temp_folder=".", fLOG=print):
    """
    run InnotSetup for a script

    @param  new_script      script to run
    @param  innosetup       location of InnoSetup (if None, use default location)
    @param  log_script      output logs to this file
    @param  temp_folder     where to copy the modified script
    @param  fLOG            logging function
    @return                 output
    """
    if innosetup is None:
        innosetup = find_innosetup()

    cmd = [innosetup, "/cc", new_script]
    if log_script is not None:
        raise NotImplementedError()
        # cmd.append('/LOG="{0}"'.format(log_script))

    fLOG("ISS script", new_script)
    fLOG("CMD", cmd)
    out, err = run_cmd(" ".join(cmd), wait=True, fLOG=fLOG)
    if err is not None and len(err) > 0:
        raise InnoSetupException(
            "CMD:\n{0}\nOUT:\n{1}\nERR-5:\n{2}".format(cmd, out, err))
    return out


def innosetup_replacements(script=None, innosetup=None, replacements=None, log_script=None, temp_folder=".", fLOG=print):
    """
    run InnotSetup for a script

    @param  script          script to run, if None, use the default script assuming you want to build a Python Distribution
    @param  innosetup       location of InnoSetup (if None, use default location)
    @param  replacements    replace to make in the script (dictionary)
    @param  log_script      output logs to this file
    @param  temp_folder     where to copy the modified script
    @param  fLOG            logging function
    @return                 new script
    """
    if script is None:
        script = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "innosetup_script.iss"))

    if replacements is None:
        replacements = dict()

    with open(script, "r", encoding="utf8") as f:
        content = f.read()

    for k, v in replacements.items():
        content = content.replace(k, v)

    new_script = os.path.join(os.path.abspath(temp_folder),
                              os.path.split(script)[-1].replace(".iss", ".temp.iss"))
    with open(new_script, "w", encoding="utf8") as f:
        f.write(content)

    return new_script


def inno_install_kernels(root, suffix):
    """
    install kernels for Jupyter notebooks

    @param      root        root folder
    @param      suffix      suffix
    """
    if root in os.environ:
        path = os.environ[root]
        tools = os.path.join(path, "tools")
        if not os.path.exists(tools):
            tools = os.path.normpath(os.path.join(path, "..", "tools"))
            python = os.path.normpath(os.path.join(path, "..", "python"))
        else:
            python = os.path.join(path, "python")

    else:
        tools = os.path.join(root, "tools")
        python = os.path.join(root, "python")

    if not os.path.exists(tools):
        raise FileNotFoundError(tools)
    if not os.path.exists(python):
        raise FileNotFoundError(python)

    install_kernels(tools, python, suffix)
