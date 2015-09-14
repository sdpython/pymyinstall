#-*- coding: utf-8 -*-
"""
@file
@brief Defines a very small set of modules.
"""
import sys
from ..installhelper.module_install import ModuleInstall


def minimal_set():
    """
    list of modules to add to python to get a minimal python

    @return             a list of modules to install
    """
    mod = [
        ModuleInstall(
            "pyprind", "pip", purpose="Python Progress Indicator Utility"),
        ModuleInstall(
            "pipwin", "pip", purpose="pip on Windows") if sys.platform.startswith("win") else None,
        ModuleInstall(
            "pipdeptree", "pip", purpose="get packages dependencies"),
        ModuleInstall(
            "virtualenv", "pip", purpose="create virtual environments"),
        ModuleInstall(
            "six", "pip", purpose="helpers for python 2/3 conversion"),
        ModuleInstall("wheel", "pip", purpose="to play with wheel"),
        ModuleInstall("pep8", "pip", version="1.5.7",
                      purpose="official guidelines for Python syntax"),
        ModuleInstall(
            "autopep8", "pip", purpose="to make a script follow pep8"),
        ModuleInstall(
            "mccabe", "pip", purpose="This module provides a plugin for flake8, the Python code checker."),
        ModuleInstall(
            "pyflakes", "pip", purpose="to make a script follow pep8"),
        ModuleInstall("flake8", "pip", purpose="to make a script follow pep8"),
        ModuleInstall('markupsafe', 'pip', purpose="interpret markdown"),
        ModuleInstall(
            "psutil", "wheel", purpose="cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python."),
        ModuleInstall("astroid", "pip",
                      purpose="script syntax analysis (for pylint)"),
        ModuleInstall("logilab-common", "pip",
                      purpose="collection of low-level Python packages and modules used by Logilab projects (for pylint)"),
        ModuleInstall(
            "pylint", "pip", purpose="A abstract syntax tree for Python with inference support."),
    ]

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall(
            "pywin32", "wheel", mname="win32com", purpose="Python extensions for Windows"))
        mod.append(ModuleInstall(
            "winshell", "pip", purpose="light wrapper around the Windows shell functionality"))
        mod.append(
            ModuleInstall("pythonnet", "wheel", purpose="call .net DLL from python"))

    return [_ for _ in mod if _ is not None]
