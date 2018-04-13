# -*- coding: utf-8 -*-
"""
@file
@brief Functions to prepare a setup on Windows

.. todoext::
    :title: enables js extension on jupyter
    :tag: enhancement

    Run something like::

        jupyter nbextension enable --py --sys-prefix widgetsnbextension
"""
from __future__ import print_function
import sys
import os

from ..installhelper.install_cmd_helper import run_cmd, get_pip_program
from .win_exception import WinInstallException

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def ipython_create_profile(config_path, python_path, name="win_profile", fLOG=print):
    """
    creates a ipython profile

    @param      config_path     where to create it
    @param      python_path     python path (to get ipython)
    @param      profile         name
    @param      fLOG            logging function
    @return                     profile path
    """
    if sys.platform.startswith("win"):
        ipython_path = os.path.join(python_path, "ipython.exe")
        if not os.path.exists(ipython_path):
            ipython_path = os.path.join(
                python_path, "Scripts", "ipython.exe")
            if not os.path.exists(ipython_path):
                raise FileNotFoundError(ipython_path)
    else:
        ipython_path = os.path.join(
            python_path, "ipython")

    cmd = " profile create {1} --ipython-dir={0}".format(config_path, name)
    cmd = ipython_path + cmd
    out, err = run_cmd(cmd, wait=True, fLOG=fLOG, change_path=python_path)
    profile = os.path.join(
        config_path, "profile_" + name, "ipython_config.py")
    if not os.path.exists(profile):
        raise WinInstallException(
            "missing file, unable to execute:\nFILE:\n{3}\nCMD:\n{0}\nOUT:\n{1}\nERR-6:\n{2}".format(cmd, out, err, profile))
    return os.path.dirname(profile)


def ipython_update_profile(profile_path):
    """
    update the profile with custom settings (file filters)

    @param      profile_path        path to profile
    """
    profile = os.path.join(profile_path, "ipython_kernel_config.py")
    with open(profile, "r") as f:
        content = f.read()
    add = """
                c.ContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store', '*.so', '*.dylib', '*~', ".ipynb_checkpoints",
                    ".kernel-*.json", ".kernel", ".RData", ".RHistory"]
                c.FileContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store',
                    '*.so', '*.dylib', '*~', ".ipynb_checkpoints", ".kernel-*.json", ".kernel", ".RData", ".RHistory"]
                """.split("\n")
    content += "\n".join(_.strip() for _ in add)
    with open(profile, "w") as f:
        f.write("\n" + content + "\n")


def install_jupyter_extension(python_path):
    """
    install jupyter extension

    @param  python_path     python path
    @return                 out, err
    """
    if sys.platform.startswith("win"):
        pip = os.path.join(python_path, "Scripts", "pip.exe")
        if not os.path.exists(pip):
            pip = get_pip_program(exe=python_path)
    else:
        pip = get_pip_program(exe=python_path)

    cmd = "{0} install https://github.com/ipython-contrib/IPython-notebook-extensions/archive/master.zip --user".format(
        pip)
    out, err = run_cmd(cmd)
    if err:
        raise WinInstallException(
            "unable to install jupyter extension\nOUT:{0}\nERR-7{1}".format(out, err))
    return out, err
