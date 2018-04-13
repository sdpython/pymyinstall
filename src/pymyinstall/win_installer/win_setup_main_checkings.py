# -*- coding: utf-8 -*-
"""
@file
@brief Run some checkings about the distribution

.. versionadded:: 1.1
"""
from __future__ import print_function

import os
import sys

from .win_exception import WinInstallDistributionError
from ..packaged.automate_install import find_module_install
from ..installhelper.install_venv_helper import run_cmd_path
from ..packaged import all_set
from ..installhelper.module_install import ModuleInstall, run_cmd

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def distribution_checkings(python_path, tools_path, fLOG=print, skip_import=False, module_list=None):
    """
    checks a distribution was properly executed

    @param      python_path     path for python
    @param      tools_path      path for tools
    @param      fLOG            logging function
    @param      skip_import     skip the validation of every installed module (for unit test purposes)
    @param      module_list     module list to check

    The function raises @see cl WinInstallDistributionError if an issue is detected.

    If *python_path* is None, it is replace by ``os.path.dirname(sys.executable)``.

    .. versionadded:: 1.1
    """
    exceptions = []
    files_to_check = ["jupyter-console.exe", "jupyter-qtconsole.exe",
                      "jupyter-notebook.exe", "jupyter.exe"]

    if python_path is None:
        python_path = os.path.dirname(sys.executable)

    # on Python 3.5, pip does not always exist
    # in a virtual environment (probable bug)
    pip = os.path.join(python_path, "pip.exe")
    pep8 = os.path.join(python_path, "pep8.exe")
    if not os.path.exists(pip) and not os.path.exists(pep8):
        scripts = os.path.join(python_path, "Scripts")
        files_to_check.extend(
            [("spyder.bat", 'spyder.exe'), "autopep8.exe"])
        if sys.version_info[:2] != (3, 5):
            files_to_check.append("pip.exe")
    else:
        scripts = python_path

    ######################################
    # check Jupyter, numpy, works properly
    ######################################
    if sys.platform.startswith("win"):
        new_files_to_check = []
        for file in files_to_check:
            if isinstance(file, tuple):
                fs = [os.path.join(scripts, f) for f in file]
                ft = [f for f in fs if os.path.exists(f)]
                if len(ft) > 0:
                    new_files_to_check.append(os.path.split(ft[0])[-1])
                else:
                    try:
                        raise FileNotFoundError(fs)
                    except Exception as e:
                        exceptions.append(e)
            else:
                f = os.path.join(scripts, file)
                if not os.path.exists(f):
                    try:
                        raise FileNotFoundError(f)
                    except Exception as e:
                        exceptions.append(e)
                else:
                    new_files_to_check.append(file)
        files_to_check = new_files_to_check

    ################################
    # check that module can be imported
    ################################
    if not skip_import:
        res = import_every_module(
            python_path, module_list, only_installed=True, fLOG=fLOG)
        mes = []
        for r in res:
            if not r[0]:
                m = "------\nFAILED {0}\nOUT\n{1}\nERR--E\n{2}".format(
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
    if python_path is None:
        python_path = os.path.dirname(sys.executable)
    if os.path.isfile(python_path):
        python_path = os.path.dirname(python_path)

    if module_list is None:
        module_list = all_set()

    def tomod(m):
        if isinstance(m, ModuleInstall):
            return m
        else:
            return find_module_install(m)
    module_list = [tomod(m) for m in module_list]

    def noLOG(*l, **p):
        pass

    def is_errored_line(line):
        if ".py" in line:
            if "UserWarning:" in line:
                return False
            if "FutureWarning:" in line:
                return False
            return True
        return False

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

        if err is not None:
            lines = err.split("\n")
            for line in lines:
                if ".py" in line:
                    res = is_errored_line(lines)
                    if res:
                        return False
                else:
                    continue
            return True
        return False

    res = []
    for i, m in enumerate(module_list):
        if i < start:
            continue
        if end != -1 and i >= end:
            fLOG("[pymy] {0}/{1}: end".format(i, len(module_list) - start))
            break
        if m.is_installed_version():

            if m.name in ["libpython", "tutormagic", "pymyinstall", "distribute"]:
                # nothing to import or failure
                fLOG("[pymy] {0}/{1}: skipped".format(i,
                                                      len(module_list) - start), m)
                continue
            elif m.mname == "theano":
                # we need to check that TDM-GCC is installed
                cmd = "g++ --help"
                out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
                if err is not None and len(err) > 0:
                    fLOG("[pymy] {0}/{1}: failed (g++)".format(i,
                                                               len(module_list) - start), m)
                    res.append((False, m, out, err))
                    continue
                if "Usage: g++ [options] file..." not in out:
                    fLOG("[pymy] {0}/{1}: failed (g++)".format(i,
                                                               len(module_list) - start), m)
                    res.append((False, m, out, err))
                    continue

            sc = "import " + m.ImportName
            if m.name == "cvxopt":
                # see
                # http://stackoverflow.com/questions/14778178/import-cvxopt-base-the-specified-module-could-not-be-found
                sc += "import numpy;" + sc
            if m.name == "scipy":
                # see
                # http://stackoverflow.com/questions/14778178/import-cvxopt-base-the-specified-module-could-not-be-found
                sc += sc + ";import scipy.stats"
            out, err = run_cmd_path(
                python_path, sc, fLOG=fLOG, communicate=True, timeout=40)
            suc = analyze_error_success(m, err)
            nextm = module_list[i + 1] if i + 1 < len(module_list) else ""
            if suc:
                fLOG("[pymy] {0}/{1}: success".format(i,
                                                      len(module_list) - start), m, "-->", nextm)
            else:
                fLOG("[pymy] {0}/{1}: failed ".format(i,
                                                      len(module_list) - start), m, "-->", nextm)
                if m.name == "paramiko":
                    err = "You might have to install manually pycrypto.\n" + \
                          "Please read http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/2016/2016-02-27_pycrypto_paramiko.html" + \
                          err
                err = [(" - ERR--F: " if is_errored_line(line)
                        else " - OK:  ") + line.rstrip("\n\r") for line in err.split("\n")]
                err = "\n".join(err)
            res.append((suc, m, out, err))
    return res
