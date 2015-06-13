"""
@file
@brief Functions to prepare a setup on Windows, use InnoSetup
"""
import os
from ..installhelper import run_cmd


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


def run_innosetup(script=None, innosetup=None, replacements=None, log_script=None, temp_folder=".",
                  fLOG=print):
    """
    run InnotSetup for a script

    @param  script          script to run, if None, use the default script assuming you want to build a Python Distribution
    @param  innosetup       location of InnoSetup (if None, use default location)
    @param  replacements    replace to make in the script (dictionary)
    @param  log_script      output logs to this file
    @param  temp_folder     where to copy the modified script
    @param  fLOG            logging function
    @return                 output
    """
    if script is None:
        script = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "PythonENSAE.iss"))

    if innosetup is None:
        innosetup = find_innosetup()

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

    cmd = [innosetup, "/cc", new_script]
    if log_script is not None:
        raise NotImplementedError()
        # cmd.append('/LOG="{0}"'.format(log_script))

    fLOG("ISS script", script)
    fLOG("CMD", cmd)
    out, err = run_cmd(" ".join(cmd), wait=True, fLOG=fLOG)
    if err is not None and len(err) > 0:
        raise InnoSetupException(
            "CMD:\n{0}\nOUT:\n{1}\nERR:\{2}".format(cmd, out, err))
    return out
