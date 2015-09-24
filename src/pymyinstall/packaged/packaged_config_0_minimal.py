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
        mod.append("pywin32")
        mod.append("winshell"
        mod.append("pythonnet")

    from . import find_module_install

    return [find_module_install(_) for _ in mod if _ is not None]
