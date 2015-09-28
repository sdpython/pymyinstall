#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""
import sys


def pyquickhelper_set():
    """
    list of modules needed to run unit test of module *pyquickhelper*
    """
    names = [
        "futures",
        "virtualenv",
        "six",
        "lxml",
        "jinja2",
        "pygments",
        "pyparsing",
        "python-dateutil",
        "coverage",
        "nose",
        "pytz",
        "husl",
        "decorator",
        "pipdeptree",
        "openpyxl",
        "pywin32" if sys.platform.startswith("win") else None,
        "winshell" if sys.platform.startswith("win") else None,
        "certifi",
        "tornado",
        "pyzmq",
        "pycparser",
        "Cython",
        "numpy",
        "cycler",
        "matplotlib",
        "jsonschema",
        "mistune",
        "wheel",
        "alabaster",
        "babel",
        "colorama",
        "docutils",
        "sphinx",
        'sphinxcontrib-images',
        'pypiserver',
        "pep8",
        "autopep8",
        "mccabe",
        "pyflakes",
        "flake8",
        'markupsafe',
        "pandas",
        "ipython",
        "jupyter",
        "jupyter_core",
        "jupyter_client",
        "nbformat",
        "nbconvert",
        "notedown",
        "ipython_genutils",
        "pexpect" if not sys.platform.startswith("win") else None,
        "ipykernel",
        "ipywidgets",
        "qtconsole",
        "traitlets",
        "pickleshare",
        "path.py",
        "simplegeneric",
        "micropython-libc" if not sys.platform.startswith("win") else None,
        "micropython-ffilib" if not sys.platform.startswith(
            "win") else None,
        "micropython-fcntl" if not sys.platform.startswith(
            "win") else None,
        "ptyprocess" if not sys.platform.startswith("win") else None,
        "terminado" if not sys.platform.startswith("win") else None,
        "notebook",
        "jupyter-console",
        "metakernel",
        "ipystata" if sys.version_info[0] == 2 else None,
        "jupyter-pip",
        "requests",
        "psutil",
        'snowballstemmer',
        'sphinx-rtd-theme',
        "sphinxjp.themes.revealjs",
        "pbr",
        "python-jenkins",
        "wild_sphinx_theme",
    ]

    from . import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
