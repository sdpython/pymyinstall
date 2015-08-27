#-*- coding: utf-8 -*-
"""
@file
@brief Defines different set of modules to install.
"""
import sys
from ..installhelper.module_install import ModuleInstall


def is_64bit():
    """
    tells if the python is 64 bit or not

    @return     boolean
    """
    return sys.maxsize > 2 ** 32


def minimal_set():
    """
    returns a list of modules to add to python to get a minimal python

    @return             a list of modules to install

    To install them:
    @code
    for _ in minimal_set() :
        _.install(temp_folder="install")
    @endcode
    """
    mod = [
        ModuleInstall(
            "virtualenv", "pip", purpose="creatre virtual environments"),
        ModuleInstall(
            "six", "pip", purpose="helpers for python 2/3 conversion"),
        ModuleInstall("wheel", "pip", purpose="to play with wheel"),
        ModuleInstall("pep8", "pip", version="1.5.7",
                      purpose="official guidelines for Python syntax"),
        ModuleInstall(
            "autopep8", "pip", purpose="to make a script follow pep8"),
        ModuleInstall(
            "mccabe", "pip", purpose="This module provides a plugin for flake8, the Python code checker."),
        ModuleInstall(
            "pyflakes", "pip", purpose="to make a script follow pep8"),
        ModuleInstall("flake8", "pip", purpose="to make a script follow pep8"),
        ModuleInstall('markupsafe', 'pip', purpose="interpret markdown"),
        ModuleInstall(
            "psutil", "wheel", purpose="cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python."),
        ModuleInstall("astroid", "pip",
                      purpose="script syntax analysis (for pylint)"),
        ModuleInstall("logilab-common", "pip",
                      purpose="collection of low-level Python packages and modules used by Logilab projects (for pylint)"),
        ModuleInstall(
            "pylint", "pip", purpose="A abstract syntax tree for Python with inference support."),
    ]

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall(
            "pywin32", "wheel", mname="win32com", purpose="Python extensions for Windows"))
        mod.append(ModuleInstall(
            "winshell", "pip", purpose="light wrapper around the Windows shell functionality"))
        mod.append(
            ModuleInstall("pythonnet", "wheel", purpose="call .net DLL from python"))

    return [_ for _ in mod if _ is not None]


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
        ModuleInstall(
            "xlwings", "pip", purpose="reads/writes Excel files") if sys.platform.startswith("win") else None,
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
            "networkx", "wheel", purpose="graph libraries, basic drawing", usage="VIZ"),
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
                      purpose="run a local pipy server", usage="SPHINX"),
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
            "netCDF4", "wheel", mname="netcdf4", purpose="xray uses this module to save and read data (netCDF=Unidata network Common Data Form)"),
        ModuleInstall(
            "xray", "wheel", purpose="pandas like library for cubes (N-dimensional data)", usage="DATA/ML"),
        ModuleInstall(
            "bcolz", "wheel", purpose="compressed dataframe, in memory or on disk", usage="DATA/ML"),
        ModuleInstall(
            "scikit-learn", "wheel", mname="sklearn", purpose="machine learning", usage="DATA/ML"),
        # ipython
        ModuleInstall(
            "ipython", "pip", purpose="IPython, Jupyter", usage="JUPYTER"),
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
            "notebook", "pip", purpose="Jupyter notebooks, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "jupyter-console", "pip", mname="jupyter_console", purpose="Jupyter console, new in Jupyter 4.0", usage="JUPYTER"),
        ModuleInstall(
            "metakernel", "pip", purpose="more magic commands for Jupyter", usage="JUPYTER"),
        ModuleInstall(
            "simplepam", "pip", purpose="required by jupyterhub, An interface to the Pluggable Authentication Modules (PAM) library on linux, written in pure python (using ctypes)", usage="JUPYTER"),
        ModuleInstall(
            "jupyterhub", "pip", purpose="JupyterHub: A multi-user server for Jupyter notebooks", usage="JUPYTER"),
        ModuleInstall(
            "ipystata", "pip", purpose="Jupyter kernel for Stata", usage="JUPYTER"),
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
        ModuleInstall("multipledispatch ", "pip",
                      purpose="A relatively sane approach to multiple dispatch in Python."),
        #
        # 2015-07
        #
        ModuleInstall("pyprofiler", "pip", purpose="profiler"),
        ModuleInstall("mock", "pip",
                      purpose="mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used."),
        ModuleInstall("multimethods", "pip",
                      purpose="A multimethod implementation, loosely based on Guido’s initial ‘Five-minute Multimethods in Python."),
    ]

    if sys.platform.startswith("win"):
        mod.append(
            ModuleInstall("pywin32", "wheel", mname="win32com", purpose="call Windows DLL"))
        mod.append(
            ModuleInstall("winshell", "pip", purpose="Windows shell functions"))

    return [_ for _ in mod if _ is not None]


def sphinx_theme_set():
    """
    list of sphinx themes
    """
    mod = [
        ModuleInstall('sphinx-rtd-theme', 'pip', mname='sphinx_rtd_theme',
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            'sphinxjp.themes.basicstrap', 'pip', purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall('solar_theme', 'pip',
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall('cloud_sptheme', 'pip',
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            'sphinx_readable_theme', 'pip', purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            "hachibee-sphinx-theme", "pip", mname="hachibee_sphinx_theme", purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("wild_sphinx_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinx_bootstrap_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            "sphinxjp.themes.sphinxjp", "pip", purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            "sphinx_py3doc_enhanced_theme", "pip", purpose="sphinx theme", usage="SPHINX") if sys.version_info[0] >= 3 else None,
        ModuleInstall(
            "epfl-sphinx-theme", "pip", mname="epfl_theme", purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            "sphinx-better-theme", "pip", mname="better", purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("guzzle_sphinx_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("flyingsphinx", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("itcase_sphinx_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinxtrap", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
    ]
    return [_ for _ in mod if _ is not None]


def extended_set():
    """
    returns a list of modules to install, an rich set
    to work with data and more

    @return             a list of modules to install

    To install them:
    @code
    for _ in small_set() + extended_set() :
        _.install(temp_folder="install")
    @endcode
    """
    mod = [
        ModuleInstall(
            'werkzeug', 'pip', purpose="The Swiss Army knife of Python web development"),
        ModuleInstall('itsdangerous', 'pip',
                      purpose="Various helpers to pass trusted data to untrusted environments and back."),
        ModuleInstall('SQLAlchemy', 'wheel', mname='sqlalchemy',
                      purpose="model SQL queries as objects", usage="SQL"),
        ModuleInstall('simplejson', 'wheel', purpose="json parser"),
        ModuleInstall('python-pptx', 'pip', mname="pptx",
                      purpose="read/write PowerPoint presentation"),
        ModuleInstall(
            'python-docx', 'pip', mname="docx", purpose="read/write Word document"),
        ModuleInstall('flask', 'pip', purpose="python server",
                      usage="NETWORK"),
        ModuleInstall('flask-sqlalchemy', 'pip',
                      mname='flask.ext.sqlalchemy', usage="NETWORK"),
        # ModuleInstall('flasksphinx', 'pip', purpose="serves Sphinx
        # documentation through a Flask server"), # issue with Python 3
        ModuleInstall(
            'cffi', 'wheel', purpose="Foreign Function Interface for Python calling C code."),
        ModuleInstall(
            'odo', 'wheel', purpose="usually used with blaze, handles dataframe in various type of containers", usage="DATA/ML"),
        ModuleInstall(
            'cytoolz', 'wheel', purpose="Cython implementation of Toolz: High performance functional utilities", usage="DATA/ML"),
        ModuleInstall(
            'toolz', 'wheel', purpose="Toolz provides a set of utility functions for iterators, functions, and dictionaries.", usage="DATA/ML"),
        ModuleInstall(
            'datashape', 'pip', purpose="A data description language."),
        ModuleInstall(
            'dynd', 'wheel', purpose="DyND-Python, a component of the Blaze project, is the Python exposure of the DyND dynamic multi-dimensional array library.")
        if sys.version_info[0] >= 3 else None,
        ModuleInstall(
            'blaze', 'wheel', purpose="separate expression from computation (works with iterators), used with odo, avoids doing everything in memory, handle better large datasets",
            usage="DATA/ML"),
        ModuleInstall(
            'sympy', 'pip', purpose="SymPy is a Python library for symbolic mathematics."),
        ModuleInstall('gmpy2', 'wheel',
                      purpose="big real numbers (issue on Linux and Anaconda)"),
        ModuleInstall('llvmpy', 'wheel', mname='llvm',
                      purpose="Python bindings for LLVM, C++ library which allows simple access to compiler tools."),
        ModuleInstall(
            'llvmlite', 'wheel', purpose="lightweight wrapper around basic LLVM functionality"),
        ModuleInstall(
            'numba', 'wheel', purpose="Numba is an Open Source NumPy-aware optimizing compiler for Python sponsored by Continuum Analytics, Inc."),
        ModuleInstall('snowballstemmer', 'pip',
                      purpose="This package provides 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms."),
        ModuleInstall('scikit-image', 'wheel', mname='skimage',
                      purpose="scikit-image is a collection of algorithms for image processing."),
        ModuleInstall(
            'patsy', 'pip', purpose="A Python package for describing statistical models and for building design matrices (y ~ x1 + x2)"),
        ModuleInstall(
            'cvxopt', 'wheel', purpose="linear, quadratique optimization", usage="DATA/ML"),
        ModuleInstall('pymc', 'wheel',
                      purpose="Monte Carlo computation", usage="DATA/ML"),
        ModuleInstall(
            'PyWavelets', 'wheel', mname='pywt', purpose="wavelets computation", usage="DATA/ML"),
        ModuleInstall('fastcluster', 'wheel',
                      purpose="clustering, AHC, ... (issue on Linux and Anaconda)", usage="DATA/ML"),
        ModuleInstall(
            'pycosat', 'wheel', purpose="PicoSAT is a popular SAT solver written by Armin Biere in pure C."),
        ModuleInstall('pyshp', 'pip', mname='shapefile',
                      purpose="Pure Python read/write support for ESRI Shapefile format"),
        ModuleInstall('Shapely', 'wheel', mname='shapely',
                      purpose="Manipulation and analysis of geometric objects in the Cartesian plane."),
        ModuleInstall(
            'vispy', 'pip', purpose="Vispy is a high-performance interactive 2D/3D data visualization library."),
        ModuleInstall(
            'selenium', 'pip', purpose="Python wrapper for Selenium", usage="NETWORK"),
        ModuleInstall(
            'Pillow', 'wheel', mname='PIL', purpose="read/create images"),
        ModuleInstall(
            'pygame', 'wheel', purpose="GUI, interface for games (needs to be installed from www.pygame.org on Linux)", usage="GUI"),
        ModuleInstall(
            'Kivy', 'wheel', mname='kivy', purpose="GUI, interface for games, mobile (use sudo apt-get install python3-kivy on Linux)", usage="GUI"),
        ModuleInstall('kivy-garden', 'pip', mname='kivy.garden',
                      purpose="Garden tool for kivy flowers.", usage="GUI"),
        ModuleInstall(
            'py4j', 'pip', purpose="Enables Python programs to dynamically access arbitrary Java objects"),
        ModuleInstall('python-igraph', 'wheel', mname='igraph',
                      purpose="High performance graph data structures and algorithms (issue on Linux and Anaconda)"),
        ModuleInstall(
            'lockfile', 'pip', purpose="Platform-independent file locking module"),
        ModuleInstall('python-daemon', 'pip', mname='daemon',
                      purpose="Library to implement a well-behaved Unix daemon process."),
        ModuleInstall('cached_property', 'pip',
                      purpose="A decorator for caching properties in classes (for luigi)"),
        ModuleInstall('luigi', 'pip',
                      purpose="workflows, data workflows", usage="WORKFLOW"),
        #
        ModuleInstall('setproctitle', 'wheel', mname='setproctitle',
                      purpose="A Python module to customize the process title"),
        # thrift only works only for Python 2.7
        ModuleInstall(
            'ply', 'pip', purpose="Python Lex & Yacc (for thrifty)"),
        ModuleInstall(
            'thriftpy', 'pip', purpose="pure python implemention of Apache Thrift."),
        # ModuleInstall('airflow', 'pip'),  # does not work on Python 3
        ModuleInstall(
            'smopy', 'pip', purpose="OpenStreetMap image tiles in Python", usage="VIZ"),
        ModuleInstall(
            'folium', 'pip', purpose="Make beautiful maps with Leaflet.js & Python", usage="VIZ"),
        ModuleInstall(
            'geopy', 'pip', purpose="Python Geocoding Toolbox", usage="VIZ"),
        ModuleInstall('basemap', 'wheel', mname='mpl_toolkits.basemap',
                      purpose="maps extension for matplotlib", usage="VIZ"),
        ModuleInstall('pyproj', 'wheel',
                      purpose="python interface to PROJ4 library for cartographic transformations https://jswhit.github.io/pyproj, needed by cartopy", usage="VIZ"),
        ModuleInstall('Cartopy', 'wheel', mname="cartopy",
                      purpose="Cartopy is a Python package designed to make drawing maps for data analysis and visualisation as easy as possible (issue on Linux and Anaconda)", usage="VIZ"),
        # the module cartopy requires GEOS https://trac.osgeo.org/geos/
        #
        ModuleInstall("python-linkedin", "pip", mname="linkedin",
                      purpose="python wrapper for linkedin interface"),
        # access to linkedin
        ModuleInstall(
            "oauthlib", "pip", purpose="A generic, spec-compliant, thorough implementation of the OAuth request-signing logic"),
        ModuleInstall("requests_oauthlib", "pip",
                      purpose="OAuthlib authentication support for Requests."),
        ModuleInstall("antlr4-python3-runtime", "pip",
                      mname="antlr4", purpose="antlr4 runtime, grammar parser"),
        # ModuleInstall("unqlite",                    "pip"),   #
        # key/value store (NoSQL)
        ModuleInstall("pycontracts", "pip", mname="contracts",
                      purpose="PyContracts is a Python package that allows to declare constraints on function parameters and return values"),
        #
        ModuleInstall(
            "ecdsa", "pip", purpose="ECDSA cryptographic signature library (pure python)"),
        ModuleInstall("pycrypto", "wheel_xd", mname="Crypto",
                      purpose="Cryptographic modules for Python (not available on x64 and Python 3)") if sys.version_info[0] >= 3 and is_64bit() else None,
        ModuleInstall("paramiko", "pip",
                      purpose="SSH2 protocol library", usage="NETWORK"),
        #
        # ModuleInstall("pattern", "pip", purpose="Web mining module for Python, with tools for scraping, natural language processing, machine learning, network analysis and visualization.") #only works on Python 2.7
        #
        ModuleInstall(
            "pbr", "pip", purpose="PBR is a library that injects some useful and sensible default behaviors into your setuptools run."),
        #
        # 2015-02-05
        #
        ModuleInstall("autopy3", "wheel", mname="autopy3",
                      purpose="A simple, cross-platform GUI automation toolkit for Python 3 (issue on Linux and Anaconda)") if sys.version_info[0] >= 3 else None,  # simulate events
        # large double
        ModuleInstall("bigfloat", "wheel", purpose="big float (issue with Linux and Anaconda)"),
        # convex optimization, depends on CVXOPT
        ModuleInstall(
            "scs", "wheel", purpose="Solves convex cone programs via operator splitting."),
        ModuleInstall(
            "ecos", "wheel", purpose="ECOS is a numerical software for solving convex second-order cone programs (SOCPs)"),
        ModuleInstall(
            "cvxpy", "pip", purpose="linear, quadratic optimization, depends on cvxopt"),
        # better large list
        ModuleInstall(
            "blist", "wheel", purpose="a list-like type with better asymptotic performance and similar performance on small lists"),
        # to install packages with conda
        ModuleInstall("conda", "pip", purpose="package management tool"),
        ModuleInstall("libLAS", "wheel", mname="liblas",
                      purpose="libLAS is a C/C++ library for reading and writing the very common LAS LiDAR format."),
        ModuleInstall(
            "liblinear", "wheel", purpose="A Library for Large Linear Classification"),
        ModuleInstall("marisa_trie", "wheel",
                      purpose="Static memory-efficient & fast Trie-like structures for Python (based on marisa-trie C++ library)"),
        ModuleInstall(
            "mlpy", "wheel", purpose="mlpy is a Python module for Machine Learning built on top of NumPy/SciPy, has wavelets"),
        ModuleInstall(
            "pygit2", "wheel", purpose="Pygit2 is a set of Python bindings to the libgit2 shared library, libgit2 implements the core of Git."),
        ModuleInstall(
            "pymongo", "wheel", purpose="Python wrapper for MongoDB", usage="NoSQL"),
        ModuleInstall(
            "PyOpenGL", "wheel", mname="OpenGL", purpose="use OpenGL in Python"),
        ModuleInstall(
            "Theano", "wheel", mname="theano", purpose="deep learning, GPU", usage="DATA/ML"),
        ModuleInstall("keras", "pip", purpose="deep learning",
                      usage="DATA/ML"),
        ModuleInstall("neon", "pip", purpose="deep learning", usage="DATA/ML"),
        ModuleInstall(
            "pyqtgraph", "pip", purpose="Scientific Graphics and GUI Library for Python, depends on PySide", usage="GUI"),
        ModuleInstall("deap", "pip", purpose="deep learning"),
        # for gensim
        ModuleInstall(
            "boto", "pip", purpose="A Python interface to Amazon Web Services", usage="NETWORK"),
        # for gensim
        ModuleInstall("bz2file", "pip", purpose="process bz2 files"),
        # for gensim
        ModuleInstall("smart_open", "wheel",
                      purpose="Utils for streaming large files (S3, HDFS, gzip, bz2...), provides the same API for many format"),
        ModuleInstall("gensim", "wheel", purpose="genetic algorithm"),
        # ModuleInstall("pybrain", "pip"),   # some issues with the code
        # (relative import are not well handled in version 0.3.3
        ModuleInstall(
            "h5py", "wheel", purpose="The h5py package is a Pythonic interface to the HDF5 binary data format. Trillion-Particle Simulation.", usage="DATA/ML"),
        # Bayesian
        ModuleInstall(
            "bayespy", "pip", purpose="bayesian modelling and computation", usage="DATA/ML"),
        ModuleInstall(
            "numexpr", "wheel", purpose="Fast numerical array expression evaluator for Python, NumPy, PyTables, pandas, bcolz and more."),
        #
        ModuleInstall("glueviz", "wheel", mname="glue",
                      purpose="ploting, Multidimensional data visualzation across files", usage="DATA/ML"),
        #
        # javascript graphs
        ModuleInstall("charts", "pip",
                      purpose="plotting in javascript", usage="VIZ"),
        #
        ModuleInstall(
            "dill", "pip", purpose="serialize all of python (almost), Dill extends python's \"pickle\" module for serializing and de-serializing python objects to the majority of the built-in python types."),  # for dask
        # parallel computation
        ModuleInstall(
            "dask", "pip", purpose="parallization of operations with dataframe", usage="DATA/ML"),
        #
        ModuleInstall(
            "jedi", "pip", purpose="An autocompletion tool for Python that can be used for text editors."),
        ModuleInstall(
            "docopt", "pip", purpose="Pythonic argument parser, that will make you smile"),
        ModuleInstall("markdown2", "pip", purpose="markdown parser"),
        ModuleInstall(
            "structures", "pip", purpose="User-friendly library for creating data structures."),
        ModuleInstall(
            "py2exe", "wheel", purpose="convert a python program into an exe program"),
        ModuleInstall(
            "rodeo", "pip", purpose="Scientific IDE, mixed between Spyder and IPython", usage="VIZ"),
        ModuleInstall(
            "tzlocal", "pip", purpose="tzinfo object for the local timezone"),
        ModuleInstall(
            "apscheduler", "pip", purpose="to schedule the execution of jobs, tasks"),
        #
        # ModuleInstall("pdfminer", "pip"),  # PDF extraction (no python 3 version)
        # ModuleInstall("minecart", "pip"),  # PDF extraction (no python 3 version)
        #
        # ModuleInstall("pygauss", "pip"),  # molecule, bio-informatic,
        # requires PIL which is deprecated
        #
        # July 2015
        #
        ModuleInstall("ete", "github", "jhcepas", mname="ete3",
                      web="https://github.com/jhcepas/ete/tree/3.0",
                      purpose="tree visualisation", usage="VIZ"),  # graph visualization
        # visualisation
        ModuleInstall(
            "pyexecjs", "pip", mname="execjs", purpose="Run JavaScript code from Python (for pyreact)", usage="NETWORK"),
        ModuleInstall(
            "pyreact", "pip", purpose="Python bridge to JSX & the React JavaScript library. (for pyxley)", usage="NETWORK"),
        ModuleInstall(
            "pyxley", "pip", purpose="A pure-Python SNMPv1/v2c/v3 library", usage="NETWORK"),

        #
        # 2015-08
        #
        ModuleInstall(
            "pyasn1", "pip", purpose="ASN.1 types and codecs (for pysnmp)"),
        ModuleInstall(
            "pysnmp", "pip", purpose="A pure-Python SNMPv1/v2c/v3 library", usage="NETWORK"),
        # pyinstaller does not install properly on Windows
        # ModuleInstall(
        #    "pyinstaller", "pip", purpose="Converts (packages) Python programs into stand-alone executables, under Windows, Linux, Mac OS X, AIX and Solaris."),
        ModuleInstall(
            "imageio", "pip", purpose="Library for reading and writing a wide range of image, video, scientific, and volumetric data formats (for moviepy)", usage="VIDEO"),
        ModuleInstall(
            "tqdm", "pip", purpose="A Simple Python Progress Meter (for moviepy)", usage="VIDEO"),
        ModuleInstall(
            "moviepy", "pip", purpose="Video editing with Python", usage="VIDEO"),
        ModuleInstall(
            "xgboost", "wheel_xd", purpose="Parallelized Stochastic Gradient Descent (only available on Python 3 and x64)", usage="DATA/ML") if sys.version_info[0] >= 3 and is_64bit() else None,
        ModuleInstall("pygling", "pip",
                      purpose="to build makefile with python"),
        ModuleInstall("cuda4py", "pip",
                      purpose="Python cffi CUDA bindings and helper classes"),
        ModuleInstall("whoosh", "pip", purpose="search engine in Python"),
        ModuleInstall("pymatbridge", "pip",
                      purpose="pymatbridge is a set of python and matlab functions to allow these two systems to talk to each other"),
        ModuleInstall("scilab2py", "pip",
                      purpose="Python to Scilab bridge", usage="DATA/ML"),
        ModuleInstall("scilab_kernel", "pip",
                      purpose="A Scilab kernel for IPython", usage="JUPYTER"),
        ModuleInstall("psycopg2", "wheel",
                      purpose="Psycopg is the most popular PostgreSQL adapter for the Python programming language.", usage="SQL"),
        ModuleInstall("pymssql", "wheel",
                      purpose="A simple database interface for Python that builds on top of FreeTDS to provide a Python DB-API (PEP-249) interface to Microsoft SQL Server.", usage="SQL"),
        ModuleInstall("mysqlclient", "pip",
                      purpose="MySQL driver written in Python which does not depend on MySQL C client libraries and implements the DB API v2.0 specification (PEP-249).", usage="SQL"),
        ModuleInstall("line_profiler", "wheel",
                      purpose="line_profiler is a module for doing line-by-line profiling of functions. kernprof is a convenient script for running either line_profiler or the Python standard library's cProfile or profile modules, depending on what is available."),
        ModuleInstall("mpmath", "pip",
                      purpose="mpmath is a free (BSD licensed) Python library for real and complex floating-point arithmetic with arbitrary precision."),
    ]

    return [_ for _ in mod if _ is not None]


def azure_set():
    """
    Modules to handle huge datasets on disk, hierarchical datasets.

    """
    mod = [
        ModuleInstall(
            "azure", "pip", purpose="Python wrapper for Azure API (HDInsight, Blog Storage)"),
        ModuleInstall(
            "azureml", "pip", purpose="Python wrapper for Azure ML API (Azure ML Pipeline)"),
    ]

    return [_ for _ in mod if _ is not None]


def ensae_set():
    """
    .. index:: ENSAE

    Modules introduced by students and some others added after some reading.
    """
    mod = [
        ModuleInstall(
            "billiard", "pip", purpose="Python multiprocessing fork with improvements and bugfixes (for celery)"),
        ModuleInstall(
            "kombu", "pip", purpose="Messaging library for Python (for celery)"),
        ModuleInstall(
            "anyjson", "pip", purpose="Wraps the best available JSON implementation available in a common interface (for celery)"),
        ModuleInstall(
            "amqp", "pip", purpose="Low-level AMQP client for Python (fork of amqplib) (for celery)"),
        ModuleInstall(
            "celery", "pip", purpose="Celery is an asynchronous task queue/job queue based on distributed message passing."),
        ModuleInstall(
            "tweepy", "pip", purpose="Python wrapper for the twitter API"),
        #ModuleInstall("newspaper3k", "pip", mname="newspaper"),
        ModuleInstall(
            "django", "pip", purpose="web application, most famous module about it, the only when to build a scalable website", usage="NETWORK"),
        ModuleInstall(
            "mutagenx", "pip", purpose="ead and write audio tags for many formats in Python 3"),
        ModuleInstall("django-audiotracks", "pip",
                      mname="audiotracks", purpose="read audio with django"),
        ModuleInstall("Quandl", "pip", purpose="access Quandl API"),
        #ModuleInstall("Lasagne", "pip", mname="lasagne"),
        ModuleInstall(
            "pymunk", "pip", purpose="pymunk is a easy-to-use pythonic 2d physics library that can be used whenever you need 2d rigid body physics from Python. Perfect when you need 2d physics in your game, demo or other application! It is built on top of the very nice 2d physics library Chipmunk."),
        ModuleInstall(
            "nltk", "wheel", purpose="NLP, natural language processing", usage="DATA/ML"),
        ModuleInstall(
            "textblob", "pip", purpose="TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more."),
        ModuleInstall(
            "dev", "pip", purpose="Header files, a static library and development tools for building Python modules, extending the Python interpreter or embedding Python in applications."),
        ModuleInstall(
            "opencv_python", "wheel", mname="cv", purpose="OpenVC wrapper"),
        ModuleInstall("PyAudio", "wheel", mname="pyaudio",
                      purpose="PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio streams on a variety of platforms (e.g., GNU/Linux, Microsoft Windows, and Mac OS X)."),
        ModuleInstall(
            "zope.interface", "wheel", purpose="interfaces for python"),
        ModuleInstall(
            "persistent", "wheel", purpose="Objets persistants translucides"),
        # requires zope.interface, persistents
        ModuleInstall(
            "BTrees", "wheel", purpose="This package contains a set of persistent object containers built around a modified BTree data structure.", usage="ALGO"),
        ModuleInstall(
            "datrie", "wheel", purpose="Fast, efficiently stored Trie for Python.", usage="ALGO"),
        # ModuleInstall("pysparse", "pip"), #does not work
        ModuleInstall(
            "la", "wheel", purpose="Label the rows, columns, any dimension, of your NumPy arrays."),
        ModuleInstall(
            "mahotas", "wheel", purpose="Mahotas: Computer Vision Library", usage="VIZ"),
        ModuleInstall("milk", "wheel",
                      purpose="machine learning toolkit", usage="DATA/ML"),
        ModuleInstall("minepy", "wheel", purpose="interface to MineCraft"),
        ModuleInstall(
            "NLopt", "wheel", mname="nlopt", purpose="linear, quadratic optimization",
            web="http://ab-initio.mit.edu/wiki/index.php/NLopt", usage="DATA/ML"),
        ModuleInstall("Pmw", "wheel", mname="Pmw",
                      purpose="Pmw is a toolkit for building high-level compound widgets in Python using the Tkinter module."),
        ModuleInstall(
            "pytools", "pip", purpose="A collection of tools for Python"),
        ModuleInstall(
            "pycuda", "wheel", purpose="PyCUDA lets you access Nvidia's CUDA parallel computation API from Python.",
            usage="GPU"),
        # ModuleInstall("scikits.cuda", "pip", mname="skcuda"), # no stable
        # version
        ModuleInstall(
            "pylzma", "wheel", purpose="Python bindings for the LZMA library by Igor Pavlov."),
        ModuleInstall("pymvpa2", "wheel", mname="mvpa2",
                      purpose="PyMVPA is a Python module intended to ease pattern classification analyses of large datasets."),
        ModuleInstall(
            "pyodbc", "wheel", purpose="access to protocal ODBC (SQL databases)", usage="SQL"),
        ModuleInstall(
            "pypmc", "wheel", purpose="pypmc is a python package focusing on adaptive importance sampling."),
        ModuleInstall(
            "pyserial", "wheel", mname="serial", purpose="access to serial port"),
        ModuleInstall("PyX", "wheel", mname="pyx",
                      purpose="plotting", usage="VIZ"),
        ModuleInstall(
            "scandir", "wheel", purpose="Better directory iterator and faster os.walk(), now in the Python 3.5 stdlib"),
        ModuleInstall(
            "zs", "wheel", purpose="S is a compressed, read-only file format for efficiently distributing, querying, and archiving arbitrarily large record-oriented datasets."),
        # machine learning
        ModuleInstall(
            "joblib", "pip", purpose="distribute jobs, parallelization"),
        #
        # teachings
        #
        ModuleInstall(
            "tutormagic", "pip", purpose="brings PythonTutor in a notebok", usage="TEACH"),
        # cache resuls from a long computation
        ModuleInstall(
            "ipycache", "pip", purpose="Defines a %%cache cell magic in the IPython notebook to cache results of long-lasting computations in a persistent pickle file",
            usage="JUPYTER"),
        # to upload a file in a notebook
        ModuleInstall(
            "nbupload", "pip", purpose="widget to upload a file in a notebook",
            usage="JUPYTER"),
        # see https://github.com/PetterS/numpy_display/blob/master/numpy_display.py
        # https://github.com/damiendr/callipy
        #
        ModuleInstall("libsvm", "wheel", mname="svm", purpose="SVM library"),
        # Bayesian ABC
        ModuleInstall("abcpmc", "pip", purpose="Monte Carlo and ABC methods"),
        # ModuleInstall("cosmoabc", "pip"), # Bayesian ABC, only python 2.7
        #
        # ModuleInstall("kabuki", "wheel"),    # requires pymc 2.3.3 not 2.3.4, why?
        # ModuleInstall("HDDM", "wheel", mname="hddm"),  # Bayesian, does not
        # work, it expects to have pymc with some optimization
        #
        # ModuleInstall("pyjs", "pip"), # needs manual installation
        # ModuleInstall("pyjs", "github", "pyjs"), #does not work really
        # ModuleInstall("pyjsdl", "github", "jggatc"), # no setup.py
        #
        # twisted, scrapy, not ready yet on Python 3

        #
        #
        #
        ModuleInstall(
            "zipline", "pip", purpose="Zipline is a Pythonic algorithmic trading library. The system is fundamentally event-driven and a close approximation of how live-trading systems operate."),  # finance
        ModuleInstall("vincent", "pip", purpose="plotting",
                      usage="VIZ"),  # graph
        # graph, pygal_maps_world only accepts the latest version
        #ModuleInstall("pygal", "github", "Kozea", purpose="plotting"),
        ModuleInstall(
            "pygal", "pip", "Kozea", purpose="plotting (javascript)", usage="VIZ"),
        ModuleInstall(
            "pygal_maps_world", "pip", purpose="extension to pygal (maps)", usage="VIZ"),  # graph
        #
        # 2015-06-30
        #
        ModuleInstall(
            "sas7bdat", "pip", purpose="read/write SAS format"),  # SAS
        #
        # 2015-07-15
        #
        # linear optimisation, see
        # http://blog.yhathq.com/posts/decision-making-under-uncertainty.html
        ModuleInstall("PuLP", "wheel", mname="pulp",
                      purpose="linear, quadratique optimization with constraints", usage="DATA/ML"),
        # for pyensae unit test
        ModuleInstall("JSAnimation", "wheel_xd",
                      purpose="provides javascript script to display differences between two files", usage="JUPYTER"),
        #
        # pydata
        #
        ModuleInstall("CherryPy", "wheel", mname="cherrypy",
                      purpose="create web application, needed by Spyre"),
        ModuleInstall("dataspyre", "pip", mname="spyre",
                      purpose="create simple web application to visualize data", usage="VIZ"),
        # ModuleInstall("python-recsys", "github", "ocelma", mname="recsys",
        # purpose="recommendation system", usage="DATA/ML"), #only works on
        # Python 2.7 + csc-pysparse + dividi2 (not maintained anymore)
        ModuleInstall(
            "colorspacious", "pip", purpose="A powerful, accurate, and easy-to-use Python library for doing colorspace conversions (for viscm)"),
        ModuleInstall(
            "viscm", "pip", purpose="tool for analyzing colormaps and creating new colormaps."),
        ModuleInstall("cubehelix", "github", "jradavenport",
                      purpose="a full implementation of Dave Green's cubehelix colormap for Python",
                      web="https://github.com/jradavenport/cubehelix"),
        ModuleInstall("lifelines", "pip", purpose="survival analysis"),
        # ModuleInstall("pysnptools", "pip", purpose="operation on DNA sequences"), # only available on Python 2.7
        #
        # 2015-07
        #
        ModuleInstall(
            "nuitka", "pip", purpose="C++ compilation, code optimization"),
        # ModuleInstall("tri", "pip", purpose="Delaunay triangulation"), # only
        # works on Python 2.7
        ModuleInstall(
            "blosc", "wheel", purpose="Blosc (http://blosc.org) is a high performance compressor optimized for binary data."),
        ModuleInstall(
            "tables", "wheel", purpose="PyTables is a package for managing hierarchical datasets and designed to efficiently and easily cope with extremely large amounts of data."),
        ModuleInstall(
            "heatmap", "wheel", purpose="draw heatmap", usage="VIZ"),
        ModuleInstall("planar", "wheel",
                      purpose="2D planar geometry library for Python."),
        ModuleInstall("GDAL", "wheel", mname="osgeo",
                      purpose="GDAL is a translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation."),
        ModuleInstall("cgal_bindings", "wheel", mname="CGAL",
                      purpose="The CGAL Bindings project allows to use some packages of CGAL, the Computational Algorithms Library, in languages other than C++, as for example Java and Python.",
                      web="https://github.com/cgal/cgal-swig-bindings"),
        ModuleInstall("tifffile", "pip",
                      purpose="Read and write image data from and to TIFF files. (for pims)"),
        ModuleInstall("pims", "pip",
                      purpose="Python Image Sequence (for trackpy)"),
        ModuleInstall("trackpy", "pip",
                      purpose="trackpy is a Python package for particle tracking in 2D, 3D, and higher dimensions.", usage="DATA/ML"),
        ModuleInstall("triangle", "wheel",
                      purpose="Python Triangle is a python wrapper around Jonathan Richard Shewchuk's two-dimensional quality mesh generator and delaunay triangulator library."),
        ModuleInstall("redis", "pip",
                      purpose="Python client for Redis key-value store"),
        # this module is not on pypi and the py3k version is in a separate folder
        # i don't want to write too much specific code for it
        # i compile it into a wheel
        ModuleInstall("skdata", "wheel_xd",
                      purpose="Data Sets for Machine Learning in Python", usage="DATA"),
        ModuleInstall("hebel", "pip",
                      purpose="GPU-Accelerated Deep Learning Library in Python", usage="DATA/ML"),
        # ModuleInstall("vowpal_porpoise", "pip",
        #              purpose="Lightweight python wrapper for vowpal_wabbit.", purpose="DATA/ML"),
        # it requires to build vowpal_wabbit for Windows
        # dpark
        ModuleInstall("protobuf", "pip",
                      purpose="Protocol Buffers are Google’s data interchange format (for dpark)"),
        ModuleInstall("invoke", "pip",
                      purpose="Invoke is a Python task execution tool & library, drawing inspiration from various sources to arrive at a powerful & clean feature set. (for dpark)"),
        ModuleInstall("mesos.interface", "pip",
                      purpose="Mesos interfaces (for dpark)"),
        ModuleInstall("pymesos", "pip",
                      purpose="Mesos interfaces (for dpark)"),
        ModuleInstall("fabric", "pip",
                      purpose="Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. (for streamparse)"),
        ModuleInstall("prettytable", "pip",
                      purpose="A simple Python library for easily displaying tabular data in a visually appealing ASCII table format. (for streamparse)"),
        ModuleInstall("streamparse", "pip",
                      purpose="Streamparse lets you run Python code against real-time streams of data via Apache Storm."),
        ModuleInstall("msgpack-python", "pip", mname="msgpack",
                      purpose="MessagePack (de)serializer. (for dpark)"),
        ModuleInstall("lz4", "wheel",
                      purpose="LZ4 Bindings for Python (for dpark)"),
        ModuleInstall("dpark", "github", gitrepo="douban",
                      purpose="DPark is a Python clone of Spark, MapReduce(R) alike computing framework supporting iterative computation.", usage="DATA/ML"),
        ModuleInstall("tinydb", "pip",
                      purpose="TinyDB is a tiny, document oriented database optimized for your happiness :) It's written in pure Python and has no external requirements.", usage="noSQL"),
        ModuleInstall("urllib3", "pip",
                      purpose="urllib2 extension"),
        ModuleInstall("greenlet", "wheel",
                      purpose="Greenlet allows lightweight in-process concurrent programming."),
        ModuleInstall("gevent", "pip",
                      purpose="gevent is a coroutine-based Python networking library"),
        ModuleInstall("grequests", "pip",
                      purpose="GRequests allows you to use Requests with Gevent to make asynchronous HTTP Requests easily."),
        ModuleInstall("pycurl", "wheel",
                      purpose="PycURL, a interface to the libcurl library. (for grab)"),
        ModuleInstall("pytils", "pip",
                      purpose="Russian-specific string utils (for selection, weblib)"),
        ModuleInstall("selection", "pip",
                      purpose="API to extract data from HTML and XML documents. (for grab)"),
        ModuleInstall("weblib", "pip",
                      purpose="Set of tools for web scraping projects (for grab)"),
        ModuleInstall("grab", "pip",
                      purpose="Grab is a python web scraping framework. Grab provides tons of helpful methods to scrape web sites "),
        ModuleInstall("imbox", "pip",
                      purpose="Python library for reading IMAP mailboxes and converting email content to machine readable data"),
        ModuleInstall("neural-python", "pip", mname="neuralpy",
                      purpose="NeuralPy is the Artificial Neural Network library implemented in Python.", usage="DATA/ML"),
    ]

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall("VideoCapture", "wheel",
                                 purpose="A Win32 Python Extension for Accessing Video Devices", usage="VIDEO"))
        mod.append(ModuleInstall("comtypes", "pip",
                                 purpose="Pure Python COM package"))
        mod.append(ModuleInstall("jaraco.util", "pip",
                                 purpose="General utility modules that supply commonly-used functionality"))
        mod.append(ModuleInstall("jaraco.video", "pip",
                                 purpose="jaraco.video implements a framegrabber inteface for Windows Video Capture devices.", usage="VIDEO"))

    return [_ for _ in mod if _ is not None]


def teachings_set():
    """
    .. index:: ENSAE, teachings

    Modules implemented for my teachings.
    """
    mod = [
        ModuleInstall(
            "pyquickhelper", "pip", purpose="helpers to generation documentation", usage="TEACH"),
        ModuleInstall(
            "pymyinstall", "pip", purpose="easy installation of modules including Windows", usage="TEACH"),
        ModuleInstall("pymmails", "pip",
                      purpose="read/send emails", usage="TEACH"),
        ModuleInstall(
            "pyensae", "pip", purpose="helpers, Hadoop, SQL, financial times series, ...", usage="TEACH"),
        ModuleInstall("pyrsslocal", "pip",
                      purpose="RSS readers", usage="TEACH"),
        ModuleInstall(
            "code_beatrix", "pip", purpose="teaching programming to kids, lesenfantscodaient.fr", usage="TEACH"),
        ModuleInstall(
            "actuariat_python", "pip", purpose="teachings, insurance examples", usage="TEACH"),
        ModuleInstall("ensae_teaching_cs", "pip",
                      purpose="teachings, introduction to programmaing, machine learning, map/reduce", usage="TEACH"),
    ]
    #
    return [_ for _ in mod if _ is not None]
