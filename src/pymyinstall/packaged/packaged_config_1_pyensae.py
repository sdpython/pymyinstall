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
    from .packaged_config_4_ml import ensae_set
    names = pyquickhelper_set()
    names += [
        "ansi2html",  # ssh
        "ansiconv",  # ssh
        "antlr4-python3-runtime",
        "azureml",
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
        "pycrypto",  # paramiko, cannot be replaced by pycryptodome
        "pyquickhelper",
        "qgrid",  # magic command
        "scipy",
        "scikit-learn",
        "urllib3",
    ]

    for m in ensae_set():
        if m.name.startswith("azure"):
            names.append(m)

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
