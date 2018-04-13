# -*- coding: utf-8 -*-
"""
@file
@brief Defines a very small set of modules.
"""
import sys


def minimal_set():
    """
    list of modules to add to python to get a minimal python
    """
    names = [
        "autopep8",
        "flake8",
        'markupsafe',
        "mccabe",
        "pep8",
        "pipdeptree",
        "psutil",
        "pyflakes",
        "pycodestyle",
        "pythonnet" if sys.platform.startswith("win") else None,
        "pywin32" if sys.platform.startswith("win") else None,
        "pywin32-ctypes" if sys.platform.startswith("win") else None,
        "six",
        "virtualenv",
        "wheel",
        "winshell" if sys.platform.startswith("win") else None,
    ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]


def pywin32_set():
    """
    list of modules to add to python to get python with pywin32
    """
    names = ["pywin32" if sys.platform.startswith("win") else None,
             "pywin32-ctypes" if sys.platform.startswith("win") else None,
             "winshell" if sys.platform.startswith("win") else None,
             ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
