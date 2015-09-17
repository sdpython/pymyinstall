#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""
import sys
from ..installhelper.module_install import ModuleInstall


def pyquickhelper_set():
    """
    returns a list of modules needed to use
    `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_ and its extensions for notebooks,
    documentation. It is a subset of @see fn small_set.

    @return             a list of modules to install

    """
    mod = [
        # ModuleInstall("setuptools",     "wheel"),        # removed with 3.4
        # ModuleInstall("pip",            "wheel"),            # removed with 3.4
        #
        # issue with 3.0.3 because of line: raise type(self._exception),
        # self._exception, self._traceback, weird because the same exists in
        # folder lib
        ModuleInstall(
            "pyprind", "pip", purpose="Python Progress Indicator Utility"),
        ModuleInstall("futures", "pip", version="2.2.0"),
        ModuleInstall(
            "virtualenv", "pip", purpose="creatre virtual environments"),
        ModuleInstall(
            "six", "pip", purpose="helpers for python 2/3 conversion"),
        ModuleInstall("lxml", "wheel", purpose="xml parsers (C++)"),
        ModuleInstall("jinja2", "pip", purpose="templating"),
        ModuleInstall(
            "pygments", "pip", purpose="syntax highlighting package written in Python"),
        ModuleInstall(
            "pyparsing", "pip", purpose="alternative approach to creating and executing simple grammars"),
        ModuleInstall(
            "python-dateutil", "pip", "dateutil", purpose="helpers to manipulate dates"),
        ModuleInstall(
            "coverage", "pip", purpose="measure the coverage of unit tests"),
        ModuleInstall("nose", "pip", purpose="run unit tests"),
        ModuleInstall(
            "pytz", "pip", purpose="World timezone definitions, modern and historical"),
        ModuleInstall("husl", "pip", purpose="Python implementation of HUSL"),
        ModuleInstall(
            "decorator", "pip", purpose="Better living through Python with decorators"),
        ModuleInstall(
            "pipdeptree", "pip", purpose="displays module dependencies as a tree"),
        #
        ModuleInstall("openpyxl", "pip", version="1.8.6",
                      purpose="reads/writes Excel files, version is 1.8.6 due to pandas which does not work with more recent verrsions yet"),
        ModuleInstall("pywin32", "wheel" if sys.version_info[:2] <= (3, 4) else "exe_xd",
                      mname="win32com", purpose="call Windows DLL",
                      usage="WINDOWS") if sys.platform.startswith("win") else None,
        ModuleInstall("winshell", "pip", purpose="Windows shell functions",
                      usage="WINDOWS") if sys.platform.startswith("win") else None,
        #
        ModuleInstall(
            "certifi", "pip", purpose="Certifi is a carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts."),
        ModuleInstall(
            "tornado", "wheel", purpose="python server, IPython relies on it", usage="NETWORK"),
        ModuleInstall(
            "pyzmq", "wheel", mname="zmq", purpose="python librairies for Omz", usage="NETWORK"),
        #
        ModuleInstall(
            "pycparser", "wheel", purpose="pycparser is a complete parser of the C language, written in pure Python using the PLY parsing library. It parses C code into an AST and can serve as a front-end for C compilers or analysis tools."),
        ModuleInstall("Cython", "wheel", mname="cython",
                      purpose="pseudo C++ in python"),
        ModuleInstall("numpy", "wheel",
                      purpose="matrix computation", usage="DATA/ML"),
        ModuleInstall("cycler", "pip",
                      purpose="dependency for matplotlib", usage="VIZ"),
        ModuleInstall("matplotlib", "wheel",
                      purpose="most used plotting library", usage="VIZ"),

        ModuleInstall(
            "jsonschema", "pip", purpose="An implementation of JSON Schema validation for Python"),
        ModuleInstall(
            "mistune", "pip", purpose="The fastest markdown parser in pure Python with renderer features, inspired by marked."),
        ModuleInstall("wheel", "pip", purpose="handle wheels"),

        ModuleInstall(
            "alabaster", "wheel", purpose="A configurable sidebar-enabled Sphinx theme", usage="SPHINX"),
        ModuleInstall(
            "babel", "pip", version="1.3", mname="babel", purpose="Internationalization utilities, version 2.0 has bugs", usage="SPHINX"),
        ModuleInstall(
            "colorama", "pip", purpose="Cross-platform colored terminal text.", usage="SPHINX"),
        ModuleInstall("docutils", "pip",
                      purpose="interpret RST format", usage="SPHINX"),
        ModuleInstall(
            "sphinx", "pip", purpose="documentation generation based on RST", usage="SPHINX"),
        ModuleInstall(
            'sphinxcontrib-images', 'pip', mname='sphinxcontrib.images', usage="SPHINX", purpose="include images in Sphinx documentation"),
        ModuleInstall('pypiserver', 'pip',
                      purpose="run a local pypi server"),

        ModuleInstall(
            "pep8", "pip", version="1.5.7", purpose="official guidelines on Python style"),
        ModuleInstall("autopep8", "pip", purpose="apply pep8 on a script") if sys.version_info[
            :2] <= (3, 4) else None,
        ModuleInstall("autopep8", "github", "hhatto",
                      purpose="apply pep8 on a script") if sys.version_info[:2] > (3, 4) else None,
        ModuleInstall(
            "mccabe", "pip", purpose="This module provides a plugin for flake8, the Python code checker."),
        ModuleInstall("pyflakes", "pip", purpose="verify pep8 on a script"),
        ModuleInstall("flake8", "pip", purpose="verify pep8 on a script"),
        ModuleInstall('markupsafe', 'pip', purpose="parses mardown"),
        ModuleInstall(
            "pandas", "wheel", purpose="manipulate table as SQL in memory", usage="DATA/ML"),
        ModuleInstall(
            "ipython", "pip", mname="IPython", purpose="IPython, Jupyter", usage="JUPYTER"),
        ModuleInstall(
            "jupyter", "pip", purpose="Jupyter", usage="JUPYTER"),
        ModuleInstall(
            "jupyter_core", "pip", purpose="Jupyter Core", usage="JUPYTER"),
        ModuleInstall(
            "jupyter_client", "pip", purpose="Jupyter client", usage="JUPYTER"),
        ModuleInstall(
            "nbformat", "pip", purpose="IPython, notebooks conversion, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "nbconvert", "pip", purpose="IPython, notebooks conversion, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "ipython_genutils", "pip", purpose="IPython utils (nbformat)", usage="JUPYTER"),
        ModuleInstall(
            "pexpect", "pip", purpose="needed by ipykernel on Linux, Pexpect makes Python a better tool for controlling other applications.", usage="JUPYTER") if not sys.platform.startswith("win") else None,
        ModuleInstall(
            "ipykernel", "pip", purpose="IPython, Jupyter, kernels", usage="JUPYTER"),
        ModuleInstall(
            "ipywidgets", "pip", purpose="IPython, Jupyter, widgets", usage="JUPYTER"),
        ModuleInstall(
            "qtconsole", "pip", purpose="IPython, notebooks, qtconsole", usage="JUPYTER"),
        ModuleInstall(
            "traitlets", "pip", purpose="IPython, dependency", usage="JUPYTER"),
        ModuleInstall(
            "pickleshare", "pip", purpose="IPython, dependency", usage="JUPYTER"),
        ModuleInstall(
            "path.py", "pip", mname="path", purpose="IPython, dependency", usage="JUPYTER"),
        ModuleInstall(
            "simplegeneric", "pip", purpose="IPython, dependency", usage="JUPYTER"),
        ModuleInstall(
            "micropython-libc", "pip", mname="libc", purpose="dependency for ptyprocess, MicroPython FFI helper module",
            usage="JUPYTER/LINUX") if not sys.platform.startswith("win") else None,
        ModuleInstall(
            "micropython-ffilib", "pip", mname="ffi", purpose="dependency for ptyprocess, MicroPython FFI helper module",
            usage="JUPYTER/LINUX") if not sys.platform.startswith("win") else None,
        ModuleInstall(
            "micropython-fcntl", "pip", mname="fcntl", purpose="dependency for ptyprocess, Functions to compute fnctl.ioctl's opt argument",
            usage="JUPYTER/LINUX") if not sys.platform.startswith("win") else None,
        ModuleInstall(
            "ptyprocess", "pip", purpose="dependency for the terminado, Run a subprocess in a pseudo terminal",
            usage="JUPYTER/LINUX") if not sys.platform.startswith("win") else None,
        ModuleInstall(
            "terminado", "pip", purpose="dependency for the notebooks, Terminals served to term.js using Tornado websockets",
            usage="JUPYTER/LINUX") if not sys.platform.startswith("win") else None,
        ModuleInstall(
            "notebook", "pip", purpose="Jupyter notebooks, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "jupyter-console", "pip", mname="jupyter_console", purpose="Jupyter console, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "metakernel", "pip", purpose="more magic commands for Jupyter", usage="JUPYTER"),
        ModuleInstall(
            "ipystata", "pip", purpose="Jupyter kernel for Stata",
            usage="JUPYTER/PY2") if sys.version_info[0] == 2 else None,
        ModuleInstall(
            "jupyter-pip", "pip", mname="jupyterpip", purpose="Allows Jupyter notebook extension writers to make their extension pip installable!", usage="JUPYTER"),
        ModuleInstall("requests", "pip", purpose="human interface for http"),
        ModuleInstall(
            "psutil", "wheel", purpose="cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python."),  #
        ModuleInstall("sphinxjp.themes.revealjs", "pip",
                      purpose="slides based on revealjs, needed to convert notebook into slides"),
        ModuleInstall(
            "python-jenkins", "pip", mname="jenkins", purpose="interact with Jenkins"),
        ModuleInstall("wild_sphinx_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
    ]

    return [_ for _ in mod if _ is not None]
