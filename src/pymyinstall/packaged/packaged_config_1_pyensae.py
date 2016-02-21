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
        "azure-nspkg",
        "azure-mgmt-nspkg",
        "azure-common",
        "azure-mgmt-common",
        "azure-mgmt-compute",
        "azure-mgmt-network",
        "azure-mgmt-resource",
        "azure-mgmt-storage",
        "azure-mgmt",
        "azure-servicebus",
        "azure-storage",
        "azure-servicemanagement-legacy",
        "colormap",
        "dbfread",
        "easydev",
        "ecdsa",  # paramiko
        "folium",  # maps
        "osmapi",  # maps
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
