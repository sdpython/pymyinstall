#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""


def pyensae_set():
    """
    list of modules needed to run unit test of module *pyensae*
    """
    from .packaged_config_0_pyquickhelper import pyquickhelper_set
    names = pyquickhelper_set()
    names += [
        "ansi2html",  # ssh
        "ansiconv",  # ssh
        "antlr4-python3-runtime",
        "azure",  # azure
        "colormap",
        "dbfread",
        "easydev",
        "ecdsa",  # paramiko
        "folium",  # maps
        "linkedin",
        "networkx",
        "requests_file",
        "pandas_datareader",
        "paramiko",  # ssh
        "pycryptodrome",  # paramiko
        "pyquickhelper",
        "qgrid",  # magic command
        "scipy",
        "scikit-learn",
    ]

    from . import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
