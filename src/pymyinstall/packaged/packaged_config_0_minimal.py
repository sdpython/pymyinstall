#-*- coding: utf-8 -*-
"""
@file
@brief Defines a very small set of modules.
"""
import sys


def minimal_set():
    """
    list of modules to add to python to get a minimal python
    """
    names = ["pipdeptree"
             "virtualenv",
             "six",
             "wheel",
             "pep8",
             "autopep8",
             "mccabe",
             "pyflakes",
             "flake8",
             'markupsafe',
             "psutil",
             ]

    if sys.platform.startswith("win"):
        names.append("pypiwin32")
        names.append("winshell")
        names.append("pythonnet")

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
