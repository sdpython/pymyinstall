#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""
import sys
from ..installhelper.module_install import ModuleInstall


def small_set():
    """
    returns a list of modules to work with pandas, numpy, ipython, ...

    @return             a list of modules to install

    To install them:
    @code
    for _ in small_set() :
        _.install(temp_folder="install")
    @endcode
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
        ModuleInstall(
            "pipwin", "pip", purpose="pip on Windows") if sys.platform.startswith("win") else None,
        ModuleInstall("futures", "pip", version="2.2.0"),
        ModuleInstall(
            "virtualenv", "pip", purpose="creatre virtual environments"),
        ModuleInstall(
            "six", "pip", purpose="helpers for python 2/3 conversion"),
        ModuleInstall("lxml", "wheel", purpose="xml parsers (C++)"),
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
        ModuleInstall("beautifulsoup4", "pip", mname="bs4",
                      purpose="Beautiful Soup sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree."),
        ModuleInstall(
            "coverage", "pip", purpose="measure the coverage of unit tests"),
        ModuleInstall("nose", "pip", purpose="run unit tests"),
        ModuleInstall(
            "pytz", "pip", purpose="World timezone definitions, modern and historical"),
        ModuleInstall("pyreadline", "pip", mname="pyreadline",
                      purpose="python implementation of GNU readline functionality"),
        ModuleInstall("husl", "pip", purpose="Python implementation of HUSL"),
        ModuleInstall(
            "pipdeptree", "pip", purpose="displays module dependencies as a tree"),
        #
        ModuleInstall("openpyxl", "pip", version="1.8.6",
                      purpose="reads/writes Excel files, version is 1.8.6 due to pandas which does not work with more recent verrsions yet"),
        ModuleInstall("xlrd", "pip", purpose="reads Excel files"),
        ModuleInstall("xlwt", "pip", purpose="writes Excel files"),
        ModuleInstall("pywin32", "wheel", mname="win32com", purpose="call Windows DLL",
                      usage="WINDOWS") if sys.platform.startswith("win") else None,
        ModuleInstall("winshell", "pip", purpose="Windows shell functions",
                      usage="WINDOWS") if sys.platform.startswith("win") else None,
        ModuleInstall(
            "xlwings", "pip", purpose="reads/writes Excel files", usage="WINDOWS") if sys.platform.startswith("win") else None,
        ModuleInstall(
            'XlsxWriter', 'pip', mname='xlsxwriter', purpose="writes Excel files"),
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
        ModuleInstall("matplotlib", "wheel", purpose="plots", usage="VIZ"),
        ModuleInstall(
            "gr", "wheel",
            purpose="GR is a universal framework for cross-platform visualization applications (issues on Linux and Anaconda)",
            usage="VIZ"),
        # ModuleInstall("seaborn", "pip"),   # it seems problematic for this
        # small config
        ModuleInstall(
            "scipy", "wheel", purpose="scientific computation, eigen values, linear algebra", usage="DATA/ML"),
        ModuleInstall(
            "statsmodels", "wheel", purpose="statistical modelling, depends on scipy", usage="DATA/ML"),
        ModuleInstall(
            "networkx", "pip", purpose="graph libraries, basic drawing", usage="VIZ"),
        # small config
        ModuleInstall(
            "graphviz", "pip", purpose="wrapper for graphviz (most famous tool to draw graphs", usage="VIZ"),
        ModuleInstall(
            "jsonschema", "pip", purpose="An implementation of JSON Schema validation for Python"),
        ModuleInstall(
            "mistune", "pip", purpose="The fastest markdown parser in pure Python with renderer features, inspired by marked."),
        ModuleInstall("wheel", "pip", purpose="handle wheels"),
        # sphinx
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

        ModuleInstall('Versio', 'pip', mname="versio",
                      purpose="localshop dependency, manages versions"),
        ModuleInstall('django-celery', 'pip', mname="djcelery",
                      purpose="localshop dependency, Old django celery integration project."),
        ModuleInstall('django-configurations', 'pip', mname="configurations",
                      purpose="localshop dependency, A helper for organizing Django settings."),
        ModuleInstall('django-environ', 'pip', mname="environ",
                      purpose="localshop dependency, Django-environ allows you to utilize 12factor inspired environment variables to configure your Django application."),
        ModuleInstall('django-model-utils', 'pip', mname="model_utils",
                      purpose="localshop dependency, Django model mixins and utilities."),
        ModuleInstall('django-storages', 'pip', mname="storages",
                      purpose="localshop dependency, django-storages is a collection of custom storage backends for Django."),
        ModuleInstall('django-userena', 'pip', mname="userena",
                      purpose="localshop dependency, Accounts for Django made beautifully simple"),
        ModuleInstall('django-uuidfield', 'pip', mname="uuidfield",
                      purpose="localshop dependency, UUIDField in Django"),
        ModuleInstall('django-guardian', 'pip', mname="guardian",
                      purpose="localshop dependency, Implementation of per object permissions for Django 1.2 or later."),
        ModuleInstall(
            'gunicorn', 'pip', purpose="localshop dependency, WSGI HTTP Server for UNIX"),
        ModuleInstall(
            'netaddr', 'pip', purpose="Pythonic manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses"),
        ModuleInstall('easy_thumbnails', 'pip',
                      purpose="Easy thumbnails for Django"),
        ModuleInstall('html2text', 'pip',
                      purpose="Turn HTML into equivalent Markdown-structured text."),

        ModuleInstall('localshop', 'pip',
                      purpose="run a local pypi server"),
        # flake8, pep8
        ModuleInstall(
            "pep8", "pip", version="1.5.7", purpose="official guidelines on Python style"),
        ModuleInstall("autopep8", "pip", purpose="apply pep8 on a script"),
        ModuleInstall(
            "mccabe", "pip", purpose="This module provides a plugin for flake8, the Python code checker."),
        ModuleInstall("pyflakes", "pip", purpose="verify pep8 on a script"),
        ModuleInstall("flake8", "pip", purpose="verify pep8 on a script"),
        ModuleInstall('markupsafe', 'pip', purpose="parses mardown"),
        #
        #
        ModuleInstall(
            "pandas", "wheel", purpose="manipulate table as SQL in memory", usage="DATA/ML"),
        ModuleInstall(
            "netCDF4", "wheel", mname="netCDF4", purpose="xray uses this module to save and read data (netCDF=Unidata network Common Data Form)"),
        ModuleInstall(
            "xray", "wheel", purpose="pandas like library for cubes (N-dimensional data)", usage="DATA/ML"),
        ModuleInstall(
            "bcolz", "wheel", purpose="compressed dataframe, in memory or on disk", usage="DATA/ML"),
        ModuleInstall(
            "scikit-learn", "wheel", mname="sklearn", purpose="machine learning", usage="DATA/ML"),
        # ipython
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
            "simplepam", "pip", purpose="required by jupyterhub, An interface to the Pluggable Authentication Modules (PAM) library on linux, written in pure python (using ctypes)",
            usage="JUPYTER/LINUX") if not sys.platform.startswith("win") else None,
        ModuleInstall(
            "jupyterhub", "pip", purpose="JupyterHub: A multi-user server for Jupyter notebooks", usage="JUPYTER"),
        ModuleInstall(
            "ipystata", "pip", purpose="Jupyter kernel for Stata",
            usage="JUPYTER/PY2") if sys.version_info[0] == 2 else None,
        ModuleInstall(
            "jupyter-pip", "pip", mname="jupyterpip", purpose="Allows Jupyter notebook extension writers to make their extension pip installable!", usage="JUPYTER"),
        # end of ipython
        #
        ModuleInstall(
            "mpld3", "pip", purpose="mpld3 project brings together Matplotlib and D3js."),
        #
        ModuleInstall("typecheck-decorator", "pip", mname="typecheck",
                      purpose="verifies decorators at running time"),
        ModuleInstall(
            "decorator", "pip", purpose="Better living through Python with decorators"),
        #
        ModuleInstall("requests", "pip", purpose="human interface for http"),
        #ModuleInstall("PyQt",           "wheel", mname="PyQt4", usage="GUI"),
        ModuleInstall(
            "PySide", "wheel", purpose="open source version of PyQt (issue on Linux and Anaconda)", usage="GUI"),
        ModuleInstall(
            "psutil", "wheel", purpose="cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python."),  #
        ModuleInstall(
            "rope_py3k", "pip", mname="rope", purpose="refactoring library") if sys.version_info[0] >= 3 else None,  #
        ModuleInstall(
            "pylint", "pip", purpose="statistics on Python script style"),  #
        ModuleInstall(
            "spyder", "wheel", mname="spyderlib", purpose="scientific IDE"),
        #
        ModuleInstall(
            "brewer2mpl", "pip", purpose="Connect colorbrewer2.org color maps to Python and matplotlib"),
        ModuleInstall("ggplot", "pip", purpose="ggplot graphics style"),
        ModuleInstall("goslate", "pip", version="1.4",
                      purpose="calls google translate"),
        ModuleInstall("dbfread", "pip", purpose="access DBase format"),
        # XML to JSON
        ModuleInstall(
            "xmltodict", "pip", purpose="Makes working with XML feel like you are working with JSON"),
        # shell to plain
        ModuleInstall(
            "ansiconv", "pip", purpose="A Python module for converting ANSI coded text and converts it to either plain text or HTML."),
        # shell to HTML
        ModuleInstall(
            "ansi2html", "pip", purpose="Convert text with ANSI color codes to HTML"),
        #
        # node.js
        ModuleInstall(
            "nodeenv", "pip", purpose="Node.js virtual environment builder"),
        #
        # 2015-06-05
        #
        ModuleInstall('PyYAML', 'wheel', mname='yaml',
                      purpose=" YAML parser and emitter for Python"),
        ModuleInstall(
            'markdown', 'pip', purpose="markdown parser (for bokeh)"),
        ModuleInstall(
            'pystache', 'pip', purpose="Mustache for Python (for bokeh)"),
        ModuleInstall(
            'bokeh', 'pip', purpose="interactive graphs, zoomable, javascript", usage="VIZ"),
        ModuleInstall('rpy2', 'wheel', purpose="interact with R (R_HOME needs to be set up on Linux)",
                      usage="DATA/ML"),
        ModuleInstall(
            'seaborn', 'pip', purpose="nicer graphs than matplotlib for statistical purposes", usage="VIZ"),
        ModuleInstall("sphinxjp.themes.revealjs", "pip",
                      purpose="slides based on revealjs, needed to convert notebook into slides"),
        ModuleInstall("feedparser", "wheel", purpose="parse RSS streams"),
        ModuleInstall(
            "python-jenkins", "pip", mname="jenkins", purpose="interact with Jenkins"),
        #
        # 2015-06-15
        #
        ModuleInstall(
            'envoy', 'pip', purpose="Simple API for running external processes."),
        ModuleInstall('Logbook', 'wheel', mname='logbook',
                      purpose="A logging replacement for Python"),
        ModuleInstall(
            'pkginfo', 'pip', purpose="Query metadatdata from sdists / bdists / installed packages."),
        ModuleInstall("multipledispatch", "pip",
                      purpose="A relatively sane approach to multiple dispatch in Python."),
        #
        # 2015-07
        #
        ModuleInstall("future", "pip",
                      purpose="Clean single-source support for Python 3 and 2"),
        ModuleInstall("pyprofiler", "pip",
                      purpose="profiler", usage="PROFILING"),
        ModuleInstall("mock", "pip",
                      purpose="mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used."),
        ModuleInstall("multimethods", "pip",
                      purpose="A multimethod implementation, loosely based on Guido’s initial ‘Five-minute Multimethods in Python."),
    ]

    return [_ for _ in mod if _ is not None]
