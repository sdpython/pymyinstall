#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""
import sys
from ..installhelper.module_install import ModuleInstall
from ..installhelper.install_cmd_helper import is_conda_distribution


def small_set():
    """
    list of modules to work with pandas, numpy, ipython, ...
    """
    mod = [
        # issues with this modules in a virtual environment raise a, b, c instead or raise (a, b, c)
        # ModuleInstall("futures", "pip", mname="concurrent.futures",
        # purpose="Backport of the concurrent.futures package from Python
        # 3.2"),
        ModuleInstall(
            "wincertstore", "pip", purpose="Python module to extract CA and CRL certs from Windows' cert store (ctypes based).") \
        if sys.platform.startswith("win") else None,
        ModuleInstall(
            "virtualenv", "pip", purpose="creatre virtual environments") if not is_conda_distribution() else None,
        ModuleInstall(
            "six", "pip", purpose="helpers for python 2/3 conversion"),
        ModuleInstall("lxml", "wheel", purpose="xml parsers (C++)"),
        ModuleInstall('markupsafe', 'pip', purpose="parses mardown"),
        ModuleInstall("jinja2", "pip", purpose="templating"),
        ModuleInstall("Mako", "pip", mname="mako", purpose="templating"),
        ModuleInstall(
            "pygments", "pip", purpose="syntax highlighting package written in Python"),
        ModuleInstall(
            "pyparsing", "pip", purpose="alternative approach to creating and executing simple grammars"),
        ModuleInstall(
            "python-dateutil", "pip", "dateutil", purpose="helpers to manipulate dates"),
        ModuleInstall(
            "html5lib", "pip", purpose="pure-python library for parsing HTML"),
        ModuleInstall(
            "webencodings", "pip", purpose="Character encoding aliases for legacy web content"),
        ModuleInstall("beautifulsoup4", "pip", mname="bs4",
                      purpose="Beautiful Soup sits atop an HTML or XML parser, providing Pythonic idioms for " +
                      "iterating, searching, and modifying the parse tree."),
        ModuleInstall(
            "coverage", "pip", purpose="measure the coverage of unit tests"),
        ModuleInstall(
            "codecov", "pip", purpose="submit coverage report to codecov"),
        ModuleInstall("nose", "pip", purpose="run unit tests"),
        ModuleInstall(
            "pytz", "pip", purpose="World timezone definitions, modern and historical"),
        ModuleInstall("pyreadline", "pip", mname="pyreadline",
                      purpose="python implementation of GNU readline functionality"),
        ModuleInstall("husl", "pip", purpose="Python implementation of HUSL"),
        ModuleInstall(
            "pipdeptree", "pip", purpose="displays module dependencies as a tree"),
        ModuleInstall("jdcal", "pip",
                      purpose="Julian dates from proleptic Gregorian and Julian calendars."),
        ModuleInstall('et_xmlfile', "pip",
                      purpose="et_xmlfile is a low memory library for creating large XML files (for openpyxl)."),
        ModuleInstall("openpyxl", "pip",
                      purpose="reads/writes Excel files, version is 1.8.6 due to pandas which does not work with more recent verrsions yet"),
        ModuleInstall("xlrd", "pip", purpose="reads Excel files"),
        ModuleInstall("xlwt", "pip", purpose="writes Excel files"),
        ModuleInstall("pypiwin32", "pip",
                      mname="win32com", purpose="call Windows DLL",
                      usage="WINDOWS") if sys.platform.startswith("win") else None,
        ModuleInstall("pywin32-ctypes", "pip", mname="win32ctypes",
                      purpose="call Windows DLL", usage="WINDOWS") if sys.platform.startswith("win") else None,
        ModuleInstall("winshell", "pip", purpose="Windows shell functions",
                      usage="WINDOWS") if sys.platform.startswith("win") else None,
        ModuleInstall(
            'XlsxWriter', 'pip', mname='xlsxwriter', purpose="writes Excel files"),
        ModuleInstall("requests", "pip", purpose="human interface for http"),
        ModuleInstall(
            "tornado", "wheel", purpose="python server, IPython relies on it", usage="NETWORK"),
        ModuleInstall(
            "sockjs-tornado", "pip", mname="sockjs.tornado", usage="NETWORK",
            purpose="SockJS-tornado is a Python server side counterpart of SockJS-client browser library running on top of Tornado framework."),
        ModuleInstall(
            "pyzmq", "wheel", mname="zmq", purpose="python librairies for Omz (pipy distributes the binaries)", usage="NETWORK"),
        ModuleInstall(
            "pycparser", "pip", purpose="pycparser is a complete parser of the C language, written in pure " +
            "Python using the PLY parsing library. It parses C code into " +
            "an AST and can serve as a front-end for C compilers or analysis tools."),
        ModuleInstall("Cython", "wheel", mname="cython",
                      purpose="pseudo C++ in python"),
        ModuleInstall("numpy", "wheel",
                      purpose="matrix computation", usage="DATA/ML"),
        ModuleInstall("cycler", "pip",
                      purpose="dependency for matplotlib", usage="VIZ"),
        ModuleInstall("matplotlib", "wheel",
                      purpose="most used plotting library", usage="VIZ"),
        ModuleInstall(
            "brewer2mpl", "pip", purpose="Connect colorbrewer2.org color maps to Python and matplotlib"),
        ModuleInstall(
            'patsy', 'pip', purpose="A Python package for describing statistical models and for building design matrices (y ~ x1 + x2)"),
        ModuleInstall(
            "scipy", "wheel", purpose="scientific computation, eigen values, linear algebra", usage="DATA/ML"),
        ModuleInstall(
            "patsy", "pip", purpose="A Python package for describing statistical models and for building design matrices.", usage="DATA/ML"),
        ModuleInstall(
            "statsmodels", "wheel", purpose="statistical modelling, depends on scipy", usage="DATA/ML"),
        ModuleInstall(
            "decorator", "pip", purpose="Better living through Python with decorators"),
        ModuleInstall(
            "networkx", "pip", purpose="graph libraries, basic drawing", usage="VIZ"),
        ModuleInstall(
            "graphviz", "pip", purpose="wrapper for graphviz (most famous tool to draw graphs", usage="VIZ"),
        ModuleInstall(
            "jsonschema", "pip", purpose="An implementation of JSON Schema validation for Python"),
        ModuleInstall(
            "mistune", "pip", purpose="The fastest markdown parser in pure Python with renderer features, inspired by marked."),
        ModuleInstall("wheel", "pip", purpose="handle wheels"),
        ModuleInstall(
            "alabaster", "pip", purpose="A configurable sidebar-enabled Sphinx theme", usage="SPHINX"),
        ModuleInstall("babel", "pip",  # version="1.3",
                      mname="babel", purpose="Internationalization utilities, version 2.0 has bugs", usage="SPHINX"),
        ModuleInstall(
            "colorama", "pip", purpose="Cross-platform colored terminal text.", usage="SPHINX"),
        ModuleInstall(
            "wcwidth", "pip", purpose="Measures number of Terminal column cells of wide-character codes", usage="JUPYTER"),
        ModuleInstall(
            "prompt_toolkit", "pip", purpose="Library for building powerful interactive command lines in Python", usage="JUPYTER"),
        ModuleInstall(
            "traitlets", "pip", purpose="IPython, dependency", usage="JUPYTER"),
        ModuleInstall("docutils", "pip",
                      purpose="interpret RST format", usage="SPHINX"),
        ModuleInstall(
            "sphinx", "pip", purpose="documentation generation based on RST", usage="SPHINX"),
        ModuleInstall(
            'imagesize', 'pip', usage="SPHINX", purpose="Getting image size from png/jpeg/jpeg2000/gif file"),
        ModuleInstall(
            'sphinxcontrib-images', 'pip', mname='sphinxcontrib.images', usage="SPHINX", purpose="include images in Sphinx documentation"),
        ModuleInstall('pypiserver', 'pip',
                      purpose="run a local pypi server"),
        ModuleInstall(
            "pycodestyle", "pip", purpose="Python style guide checker"),
        ModuleInstall(
            "pep8", "pip", purpose="official guidelines on Python style"),
        ModuleInstall("autopep8", "pip", purpose="apply pep8 on a script"),
        ModuleInstall(
            "mccabe", "pip", purpose="This module provides a plugin for flake8, the Python code checker."),
        ModuleInstall("pyflakes", "pip", purpose="verify pep8 on a script"),
        ModuleInstall("flake8", "pip", purpose="verify pep8 on a script"),
        ModuleInstall(
            "pandas", "wheel", purpose="manipulate table as SQL in memory", usage="DATA/ML"),
        ModuleInstall(
            "certifi", "pip", purpose="Certifi is a carefully curated collection of Root Certificates for validating the trustworthiness " +
            "of SSL certificates while verifying the identity of TLS hosts."),
        ModuleInstall("ggplot", "pip", purpose="ggplot graphics style"),
        ModuleInstall(
            "requests-file", "pip", mname="requests_file", purpose="File transport adapter for Requests"),
        ModuleInstall(
            "pandas-datareader", "pip", mname="pandas_datareader",
            purpose="Up to date remote data access for pandas, works for multiple versions of pandas.", usage="DATA/ML"),
        ModuleInstall(
            "netCDF4", "wheel", mname="netCDF4", purpose="xarray uses this module to save and read data (netCDF=Unidata network Common Data Form)"),
        ModuleInstall(
            "xarray", "pip", purpose="pandas like library for cubes (N-dimensional data)", usage="DATA/ML"),
        ModuleInstall(
            "bcolz", "wheel", purpose="compressed dataframe, in memory or on disk", usage="DATA/ML"),
        ModuleInstall(
            "scikit-learn", "wheel", mname="sklearn", purpose="machine learning", usage="DATA/ML"),
        # ipython
        ModuleInstall("win_unicode_console", "pip",
                      "Enable Unicode input and display when running Python from Windows console."),
        ModuleInstall(
            "ipython", "pip", mname="IPython", purpose="IPython, Jupyter", usage="JUPYTER"),
        ModuleInstall(
            "ipython_genutils", "pip", purpose="IPython utils (nbformat)", usage="JUPYTER"),
        ModuleInstall(
            "jupyter_core", "pip", purpose="Jupyter Core", usage="JUPYTER"),
        ModuleInstall(
            "jupyter", "pip", purpose="Jupyter", usage="JUPYTER"),
        ModuleInstall(
            "jupyter_client", "pip", purpose="Jupyter client", usage="JUPYTER"),
        ModuleInstall(
            "nbformat", "pip", purpose="IPython, notebooks conversion, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "entrypoints", "pip", purpose="Discover and load entry points from installed packages.", usage="JUPYTER"),
        ModuleInstall(
            "nbconvert", "pip", purpose="IPython, notebooks conversion, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall("PyPDF2", "pip", purpose="PDF toolkit"),
        ModuleInstall(
            "ghost.py", "pip", mname="ghost", purpose="ghost.py is a webkit web client written in python", usage="JUPYTER"),
        ModuleInstall("nbbrowserpdf", "pip",
                      purpose="LaTeX-free PDF generation from Jupyter Notebooks", usage="JUPYTER"),
        ModuleInstall(
            "nbpresent", "pip", purpose="Next generation slides from Jupyter Notebooks", usage="JUPYTER"),
        ModuleInstall("pandocfilters", "pip",
                      purpose="Utilities for writing pandoc filters in python"),
        ModuleInstall("pandoc-attributes", "pip", mname="pandocattributes",
                      purpose="An Attribute class to be used with pandocfilters"),
        ModuleInstall(
            "notedown", "pip", purpose="Convert markdown to IPython notebook.", usage="JUPYTER"),
        ModuleInstall("pexpect", "pip",
                      purpose="needed by ipykernel on Linux, Pexpect makes Python a better tool for controlling other applications.",
                      usage="JUPYTER"),
        ModuleInstall(
            "ipykernel", "pip", purpose="IPython, Jupyter, kernels", usage="JUPYTER"),
        ModuleInstall(
            "ipywidgets", "pip", purpose="IPython, Jupyter, widgets", usage="JUPYTER"),
        ModuleInstall(
            "qtconsole", "pip", purpose="IPython, notebooks, qtconsole", usage="JUPYTER"),
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
            "backports_abc", "pip", purpose="A backport of recent additions to the 'collections.abc' module",
            usage="JUPYTER"),
        ModuleInstall("yapf", "pip", purpose="Code formatter"),
        ModuleInstall(
            "widgetsnbextension", "pip",
            purpose="Interactive HTML widgets for Jupyter notebooks.", usage="JUPYTER"),
        ModuleInstall(
            "jupyter_contrib_nbextensions", "github", "ipython-contrib",
            purpose="This repository contains a collection of extensions that add functionality to the Jupyter notebook.", usage="JUPYTER"),
        ModuleInstall(
            "backports.shutil-get-terminal-size", "pip", mname="backports", purpose="needed for Jupyter",
            usage="JUPYTER"),
        ModuleInstall(
            "notebook", "pip", purpose="Jupyter notebooks, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "jupyter-console", "pip", mname="jupyter_console", purpose="Jupyter console, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "metakernel", "pip", purpose="more magic commands for Jupyter", usage="JUPYTER"),
        ModuleInstall('SQLAlchemy', 'wheel', mname='sqlalchemy',
                      purpose="model SQL queries as objects", usage="SQL"),
        ModuleInstall('sqlparse', 'pip', usage="SQL",
                      purpose="Non-validating SQL parser"),
        ModuleInstall(
            "ipystata", "pip", purpose="Jupyter kernel for Stata",
            usage="JUPYTER/PY2") if sys.version_info[0] == 2 else None,
        ModuleInstall("jupyter-pip", "pip", mname="jupyterpip",
                      purpose="Allows Jupyter notebook extension writers to make their extension pip installable!",
                      usage="JUPYTER"),
        ModuleInstall("ipyparallel", "pip", usage="JUPYTER",
                      purpose="Interactive Parallel Computing with IPython"),
        # end of ipython
        #
        ModuleInstall("mpld3", "pip", usage="VIZ",
                      purpose="mpld3 project brings together Matplotlib and D3js."),
        ModuleInstall("typing", "pip", purpose="Type Hints for Python") if sys.version_info[
            :2] < (3, 5) else None,
        ModuleInstall("typecheck-decorator", "pip", mname="typecheck",
                      purpose="verifies decorators at running time"),
        ModuleInstall("requests-cache", "pip", mname="requests_cache",
                      purpose="Persistent cache for requests library"),
        ModuleInstall("PyQt4", "wheel", mname="PyQt4", usage="GUI"),
        ModuleInstall("qtpy", "pip", usage="GUI",
                      purpose="single interface for QtPy4, 5, PySide"),
        ModuleInstall(
            "PySide", "wheel",
            purpose="open source version of PyQt (issue on Linux and Anaconda)",
            usage="GUI") if sys.version_info[:2] <= (3, 4) else None,
        ModuleInstall(
            "psutil", "wheel", purpose="cross-platform library for retrieving information " +
            "onrunning processes and system utilization (CPU, memory, disks, network)in Python."),  #
        ModuleInstall(
            "rope_py3k", "pip", mname="rope", purpose="refactoring library") if sys.version_info[0] >= 3 else None,  #
        ModuleInstall(
            "isort", "pip", purpose="A Python utility / library to sort Python imports."),
        ModuleInstall(
            "backports.functools_lru_cache", "pip",
            purpose="backports.functools_lru_cache"),
        ModuleInstall(
            "astroid", "pip",
            purpose="A abstract syntax tree for Python with inference support."),
        ModuleInstall(
            "pylint", "pip", purpose="statistics on Python script style"),  #
        ModuleInstall(
            "guidata", "pip", purpose="Automatic graphical user interfaces generation for easy dataset editing and display (Spyder)"),
        ModuleInstall(
            "pythonqwt", "pip", purpose="Qt plotting widgets (Spyder)"),
        ModuleInstall(
            "guiqwt", "wheel", purpose="Efficient 2D plotting Python library based on PythonQwt (Spyder)"),
        ModuleInstall(
            "QtAwesome", "pip", mname="qtawesome",
            purpose="QtAwesome enables iconic fonts such as Font Awesome and Elusive Icons in PyQt and PySide applications."),
        ModuleInstall(
            "spyder", "pip", mname="spyderlib", purpose="scientific IDE"),
        # remove goslate from the list to avoid installing futures which appears as a dependency
        # ModuleInstall("goslate", "pip",  # version="1.4",
        #               purpose="calls google translate"),
        ModuleInstall("dbfread", "pip", purpose="access DBase format"),
        ModuleInstall(
            "aenum", "pip", purpose="Advanced Enumerations (compatible with Python's stdlib Enum), NamedTuples, and NamedConstants"),
        ModuleInstall("dbf", "pip", purpose="access DBase format"),
        ModuleInstall(
            "xmltodict", "pip", purpose="Makes working with XML feel like you are working with JSON"),
        ModuleInstall(
            "ansiconv", "pip", purpose="A Python module for converting ANSI coded text and converts it to either plain text or HTML."),
        ModuleInstall(
            "ansi2html", "pip", purpose="Convert text with ANSI color codes to HTML"),
        ModuleInstall(
            "nodeenv", "pip", purpose="Node.js virtual environment builder"),
        ModuleInstall("greenlet", "wheel",
                      purpose="Greenlet allows lightweight in-process concurrent programming."),
        ModuleInstall(
            'werkzeug', 'pip', purpose="The Swiss Army knife of Python web development"),
        ModuleInstall('itsdangerous', 'pip',
                      purpose="Various helpers to pass trusted data to untrusted environments and back."),
        ModuleInstall('simplejson', 'wheel', purpose="json parser"),
        ModuleInstall('flask', 'pip', usage="NETWORK",
                      purpose="Flask is a microframework for Python based on Werkzeug, " +
                      "Jinja 2 and good intentions. And before you ask: It's BSD licensed!"),
        ModuleInstall('flask-sqlalchemy', 'pip',
                      mname='flask.ext.sqlalchemy', usage="NETWORK"),
        ModuleInstall('flask-login', 'pip',
                      mname='flask.ext.login', usage="NETWORK"),
        ModuleInstall("flask-cors", "pip", mname="flask_cors",
                      purpose="A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible."),
        ModuleInstall('PyYAML', 'wheel', mname='yaml',
                      purpose=" YAML parser and emitter for Python"),
        ModuleInstall('python-mimeparse', 'pip',
                      purpose="A module provides basic functions for parsing mime-type names and matching them against a list of media-ranges. (falcon)"),
        ModuleInstall('falcon', 'pip', usage="NETWORK",
                      purpose="Falcon is a very fast, very minimal Python web framework for building microservices, " +
                      "app backends, and higher-level frameworks."),
        ModuleInstall(
            'markdown', 'pip', purpose="markdown parser (for bokeh)"),
        ModuleInstall(
            'pystache', 'pip', purpose="Mustache for Python (for bokeh)"),
        ModuleInstall(
            'bokeh', 'pip', purpose="interactive graphs, zoomable, javascript", usage="VIZ"),
        ModuleInstall(
            'traittypes', 'pip', purpose="Custom trait types for scientific computing."),
        ModuleInstall(
            'bqplot', 'pip', purpose="interactive graphs, zoomable, d3.js for notebooks", usage="VIZ"),
        ModuleInstall(
            'seaborn', 'pip', purpose="nicer graphs than matplotlib for statistical purposes", usage="VIZ"),
        ModuleInstall(
            'toolz', 'pip', purpose="Toolz provides a set of utility functions for iterators, functions, and dictionaries.", usage="DATA/ML"),
        ModuleInstall(
            'cytoolz', 'wheel', purpose="Cython implementation of Toolz: High performance functional utilities", usage="DATA/ML"),
        ModuleInstall('snowballstemmer', 'pip',
                      purpose="This package provides 16 stemmer algorithms (15 + Porter English stemmer) generated from Snowball " +
                      "algorithms, needed by sphinx-rtd-theme."),
        ModuleInstall('sphinx-rtd-theme', 'pip', mname='sphinx_rtd_theme',
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinxjp.themes.revealjs", "pip",
                      purpose="slides based on revealjs, needed to convert notebook into slides"),
        ModuleInstall("feedparser", "pip", purpose="parse RSS streams"),
        ModuleInstall(
            "pbr", "pip", purpose="PBR is a library that injects some useful and sensible default behaviors into your setuptools run."),
        ModuleInstall(
            "multi-key-dict", "pip", mname="multi_key_dict", purpose="Multi key dictionary implementation"),
        ModuleInstall(
            "python-jenkins", "pip", mname="jenkins", purpose="interact with Jenkins"),
        ModuleInstall(
            'envoy', 'pip', purpose="Simple API for running external processes."),
        ModuleInstall('Logbook', 'wheel', mname='logbook',
                      purpose="A logging replacement for Python"),
        ModuleInstall(
            'pkginfo', 'pip', purpose="Query metadatdata from sdists / bdists / installed packages."),
        ModuleInstall("multipledispatch", "pip",
                      purpose="A relatively sane approach to multiple dispatch in Python."),
        ModuleInstall("future", "pip",
                      purpose="Clean single-source support for Python 3 and 2"),
        ModuleInstall("mock", "pip",
                      purpose="mock is a library for testing in Python. It allows you to replace parts of your system " +
                      "under test with mock objects and make assertions about how they have been used."),
        ModuleInstall("multimethods", "pip",
                      purpose="A multimethod implementation, loosely based on Guido’s initial ‘Five-minute Multimethods in Python."),
        ModuleInstall("appdirs", "pip",
                      purpose="A small Python module for determining appropriate platform-specific dirs"),
        ModuleInstall("qgrid", "pip", usage="VIZ",
                      purpose="A Pandas DataFrame viewer for IPython Notebook."),
        ModuleInstall("ujson", "wheel",
                      purpose="Ultra fast JSON encoder and decoder for Python"),
        ModuleInstall("natsort", "pip", purpose="Sort lists naturally"),
        ModuleInstall("wget", "pip", purpose="pure python download utility"),
        ModuleInstall("queuelib", "pip",
                      purpose="Collection of persistent (disk-based) queues"),
        ModuleInstall("semantic_version", "pip",
                      purpose="A library implementing the 'SemVer' scheme."),
        ModuleInstall("unidecode", "pip",
                      purpose="ASCII transliterations of Unicode text"),
        ModuleInstall("sqlite_bro", "pip",
                      purpose="GUI for SQLite"),
        ModuleInstall("uvloop", "pip", purpose="Fast implementation of asyncio event loop on top of libuv") if sys.version_info[
            :2] > (3, 5) else None,
        ModuleInstall("tabulate", "pip",
                      purpose="Pretty-print tabular data"),
        ModuleInstall("httpie", "pip",
                      purpose="HTTPie - a CLI, cURL-like tool for humans"),
        ModuleInstall("version-information", "pip", mname="version_information",
                      purpose="Version information"),
    ]

    return [_ for _ in mod if _ is not None]
