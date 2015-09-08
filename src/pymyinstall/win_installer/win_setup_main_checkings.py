#-*- coding: utf-8 -*-
"""
@file
@brief Run some checkings about the distribution

.. versionadded:: 1.3
"""
from __future__ import print_function

import os
import sys

from .win_exception import WinInstallDistributionError
from ..packaged.automate_install import find_module_install
from ..installhelper.install_venv_helper import run_cmd_path
from ..packaged import all_fullset
from ..installhelper.module_install import ModuleInstall

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def distribution_checkings(python_path, tools_path, fLOG=print, skip_import=False):
    """
    checks a distribution was properly executed

    @param      python_path     path for python
    @param      tools_path      path for tools
    @param      fLOG            logging function
    @param      skip_import     skip the validation of every installed module (for unit test purposes)

    The function raises @see cl WinInstallDistributionError if an issue is detected.

    If *python_path* is None, it is replace by ``os.path.dirname(sys.executable)``.

    .. versionadded:: 1.3
    """
    exceptions = []
    files_to_check = ["jupyter-console.exe", "jupyter-qtconsole.exe",
                      "jupyter-notebook.exe", "jupyter.exe"]

    if python_path is None:
        python_path = os.path.dirname(sys.executable)
    pip = os.path.join(python_path, "pip.exe")
    if not os.path.exists(pip):
        scripts = os.path.join(python_path, "Scripts")
        files_to_check.extend(
            ["rodeo.exe", "spyder.exe", "pip.exe", "autopep8.exe"])
    else:
        scripts = python_path

    #############################################
    # check Jupyter, Rodeo, numpy works properly
    #############################################
    if sys.platform.startswith("win"):
        for file in files_to_check:
            f = os.path.join(scripts, file)
            if not os.path.exists(f):
                try:
                    raise FileNotFoundError(f)
                except Exception as e:
                    exceptions.append(e)

    ################################
    # check that module can be imported
    ################################
    if not skip_import:
        res = import_every_module(
            python_path, None, only_installed=True, fLOG=fLOG)
        mes = []
        for r in res:
            if not r[0]:
                m = "FAILED {0}\nOUT\n{1}\nERR\n{2}".format(
                    r[1].name, r[2], r[3])
                mes.append(m)
        if len(mes) > 0:
            raise WinInstallDistributionError(
                "cannot import modules\n" + "\n".join(mes))

    ########
    # final
    ########
    if len(exceptions) > 0:
        typstr = str  # unicode#
        errors = "\n----\n".join("{0}\n{1}".format(type(_), typstr(_))
                                 for _ in exceptions)
        raise WinInstallDistributionError("\n" + errors)


def import_every_module(python_path, module_list, only_installed=True, fLOG=print, start=0, end=-1):
    """
    import every module in *module_list* assuming they are defined
    by @see cl ModuleInstall or a string

    @param      python_path     python path
    @param      module_list     module list, if None, consider the largest list
    @param      only_installed  True to check only installed module in the list, False to test them without checking they were installed
    @param      start           start the list at *start*
    @param      end             end the list at *end* or -1 for all
    @return                     list of tuple (success, failing modules, output, error)
    """
    if os.path.isfile(python_path):
        python_path = os.path.dirname(python_path)

    if module_list is None:
        module_list = all_fullset()

    def tomod(m):
        if isinstance(m, ModuleInstall):
            return m
        else:
            return find_module_install(m)
    module_list = [tomod(m) for m in module_list]

    def noLOG(*l, **p):
        pass

    def analyze_error_success(mod, err):
        if err is None or len(err) == 0:
            return True
        if "ImportError" in err:
            return False
        if "ShimWarning" in err:
            return True
        if "kivy" in mod.name.lower():
            if "error" not in err.lower():
                return True
        return False

    res = []
    for i, m in enumerate(module_list):
        if i < start:
            continue
        if end != -1 and i >= end:
            break
        if m.is_installed():

            if m.name in ["libpython", "tutormagic", "pymyinstall"]:
                # nothing to import or failure
                continue
            sc = "import " + m.ImportName
            out, err = run_cmd_path(python_path, sc, fLOG=noLOG)
            suc = analyze_error_success(m, err)
            if suc:
                fLOG("{0}/{1}: success".format(i, len(module_list)), m)
            else:
                fLOG("{0}/{1}: failed ".format(i, len(module_list)), m)
            res.append((suc, m, out, err))
    return res
