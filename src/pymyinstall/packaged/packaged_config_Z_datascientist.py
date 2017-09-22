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
    from .packaged_config_0_pyquickhelper import pyquickhelper_set
    from ..installhelper import ModuleInstall
    names = pyquickhelper_set()
    names += [
        "appdir",
        "autopep8",
        "boto",
        "botocore",
        "boto3",
        "certifi",
        "chardet",
        "cchardet"
        "cycler",
        "cython",
        "cytoolz",
        "dask",
        "flake8",
        "gensim",
        "idna",
        "jmespath",
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
        "s3transfer",
        "scikit-learn",
        "scipy",
        "smart_open",
        "six",
        "statsmodels",
        "toolz",
        "urllib3",
        "virtualenv",
        "wheel",
        "winshell" if sys.platform.startswith("win") else None,
    ]

    check_is = ["smart_open", "cycler", "olefile",
                "toolz", "s3transfer", "jmespath", "botocore"]
    names_ = set(_.name if isinstance(_, ModuleInstall) else _ for _ in names)
    for check in check_is:
        if check not in names_:
            raise ImportError("Unable to find module '{0}' in\n{1}".format(
                check, "\n".join(sorted(names_))))

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
