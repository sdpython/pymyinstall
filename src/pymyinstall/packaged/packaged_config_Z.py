#-*- coding: utf-8 -*-
"""
@file
@brief Defines a very small set of modules.
"""
import sys


def datascientistbase_set():
    """
    list of modules to add to python to get a minimal python
    """
    names = [
        "appdir",
        "autopep8",
        "boto",
        "boto3",
        "certifi",
        "chardet",
        "cchardet",
        "cython",
        "cytoolz",
        "dask",
        "flake8",
        "gensim",
        "idna",
        'markupsafe',
        "matplotlib",
        "mccabe",
        "numpy",
        "olefile",
        "openpyxl",
        "packaging",
        "pandas",
        "pep8",
        "pillow",
        "pipdeptree",
        "psutil",
        "pyflakes",
        "pycodestyle",
        "pyparsing",
        "pythonnet" if sys.platform.startswith("win") else None,
        "python-dateutil",
        "pytz",
        "pywin32" if sys.platform.startswith("win") else None,
        "pywin32-ctypes" if sys.platform.startswith("win") else None,
        "requests",
        "scikit-learn",
        "scipy",
        "smart_open",
        "six",
        "statsmodels",
        "urllib3",
        "virtualenv",
        "wheel",
        "winshell" if sys.platform.startswith("win") else None,
    ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
