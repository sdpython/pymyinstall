"""
@file
@brief Defines different set of modules to install.
"""
import sys
from ..installhelper.module_install import ModuleInstall


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
        ModuleInstall("pylint", "pip", purpose="script syntax analysis"),
    ]

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall(
            "pywin32", "wheel", mname="win32com", purpose="Python extensions for Windows"))
        mod.append(ModuleInstall(
            "winshell", "pip", purpose="light wrapper around the Windows shell functionality"))
        mod.append(
            ModuleInstall("pythonnet", "wheel", purpose="call .net DLL from python"))

    return mod


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
        ModuleInstall("xlwings", "pip", purpose="reads/writes Excel files"),
        ModuleInstall(
            'XlsxWriter', 'pip', mname='xlsxwriter', purpose="writes Excel files"),
        #
        ModuleInstall(
            "certifi", "pip", purpose="Certifi is a carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts."),
        ModuleInstall(
            "tornado", "wheel", purpose="python server, IPython relies on it"),
        ModuleInstall(
            "pyzmq", "wheel", mname="zmq", purpose="python librairies for Omz"),
        #
        ModuleInstall(
            "pycparser", "wheel", purpose="pycparser is a complete parser of the C language, written in pure Python using the PLY parsing library. It parses C code into an AST and can serve as a front-end for C compilers or analysis tools."),
        ModuleInstall("Cython", "wheel", purpose="pseudo C++ in python"),
        ModuleInstall("numpy", "wheel", purpose="matrix computation"),
        ModuleInstall("matplotlib", "wheel", purpose="plots"),
        ModuleInstall(
            "gr", "wheel", purpose="GR is a universal framework for cross-platform visualization applications."),
        # ModuleInstall("seaborn", "pip"),   # it seems problematic for this
        # small config
        ModuleInstall(
            "scipy", "wheel", purpose="scientific computation, eigen values, linear algebra"),
        ModuleInstall(
            "statsmodels", "wheel", purpose="statistical modelling, depends on scipy"),
        ModuleInstall(
            "networkx", "wheel", purpose="graph libraries, basic drawing"),
        # small config
        ModuleInstall(
            "graphviz", "pip", purpose="wrapper for graphviz (most famous tool to draw graphs"),
        ModuleInstall(
            "jsonschema", "pip", purpose="An implementation of JSON Schema validation for Python"),
        ModuleInstall(
            "mistune", "pip", purpose="The fastest markdown parser in pure Python with renderer features, inspired by marked."),
        ModuleInstall("wheel", "pip", purpose="handle wheels"),
        # sphinx
        ModuleInstall(
            "alabaster", "wheel", purpose="A configurable sidebar-enabled Sphinx theme"),
        ModuleInstall(
            "Babel", "wheel", mname="babel", purpose="Internationalization utilities"),
        ModuleInstall(
            "colorama", "pip", purpose="Cross-platform colored terminal text."),
        ModuleInstall("docutils", "pip", purpose="interpret RST format"),
        ModuleInstall(
            "sphinx", "pip", purpose="documentation generation based on RST"),
        ModuleInstall(
            'sphinxcontrib-images', 'pip', mname='sphinxcontrib.images'),
        ModuleInstall('pypiserver', 'pip', purpose="run a local pipy server"),
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
            "pandas", "wheel", purpose="manipulate table as SQL in memory"),
        ModuleInstall(
            "xray", "wheel", purpose="pandas like library for cubes (N-dimensional data)"),
        ModuleInstall(
            "bcolz", "wheel", puropose="compressed dataframe, in memory or on disk"),
        ModuleInstall(
            "scikit-learn", "wheel", mname="sklearn", purpose="machine learning"),
        ModuleInstall(
            "ipython", "pip", mname="IPython", purpose="IPython, notebooks, Jupyter"),
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
        #ModuleInstall("PyQt",           "wheel", mname="PyQt4"),
        ModuleInstall(
            "PySide", "wheel", purpose="open source version of PyQt"),
        ModuleInstall(
            "psutil", "wheel", purpose="cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python."),  #
        ModuleInstall(
            "rope_py3k", "pip", mname="rope", purpose="refactoring library"),  #
        ModuleInstall(
            "pylint", "pip", purpose="statistics on Python script style"),  #
        ModuleInstall(
            "spyder", "wheel", mname="spyderlib", purpose="scientific IDE"),
        #
        ModuleInstall(
            "brewer2mpl", "pip", purpose="Connect colorbrewer2.org color maps to Python and matplotlib"),
        ModuleInstall("ggplot", "pip", purpose="ggplot graphics style"),
        ModuleInstall("goslate", "pip", purpose="calls google translate"),
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
            'bokeh', 'pip', purpose="interactive graphs, zoomable, javascript"),
        ModuleInstall('rpy2', 'wheel', purpose="interact with R"),
        ModuleInstall(
            'seaborn', 'pip', purpose="nicer graphs than matplotlib for statistical purposes"),
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

    ]

    if sys.platform.startswith("win"):
        mod.append(
            ModuleInstall("pywin32", "wheel", mname="win32com", purpose="call Windows DLL"))
        mod.append(
            ModuleInstall("winshell", "pip", purpose="Windows shell functions"))

    return mod


def sphinx_theme_set():
    """
    list of sphinx themes
    """
    res = [ModuleInstall('sphinx-rtd-theme', 'pip', mname='sphinx_rtd_theme', purpose="sphinx theme"),
           ModuleInstall(
               'sphinxjp.themes.basicstrap', 'pip', purpose="sphinx theme"),
           ModuleInstall('solar_theme', 'pip', purpose="sphinx theme"),
           ModuleInstall('cloud_sptheme', 'pip', purpose="sphinx theme"),
           ModuleInstall(
               'sphinx_readable_theme', 'pip', purpose="sphinx theme"),
           ModuleInstall(
        "hachibee-sphinx-theme", "pip", mname="hachibee_sphinx_theme", purpose="sphinx theme"),
        ModuleInstall("wild_sphinx_theme", "pip", purpose="sphinx theme"),
        ModuleInstall("sphinx_bootstrap_theme", "pip", purpose="sphinx theme"),
        ModuleInstall(
            "sphinxjp.themes.sphinxjp", "pip", purpose="sphinx theme"),
        ModuleInstall(
            "sphinx_py3doc_enhanced_theme", "pip", purpose="sphinx theme"),
        ModuleInstall(
            "epfl-sphinx-theme", "pip", mname="epfl_theme", purpose="sphinx theme"),
        ModuleInstall(
            "sphinx-better-theme", "pip", mname="better", purpose="sphinx theme"),
        ModuleInstall("guzzle_sphinx_theme", "pip", purpose="sphinx theme"),
        ModuleInstall("flyingsphinx", "pip", purpose="sphinx theme"),
        ModuleInstall("itcase_sphinx_theme", "pip", purpose="sphinx theme"),
        ModuleInstall("sphinxtrap", "pip", purpose="sphinx theme"),
        ModuleInstall("guzzle_sphinx_theme", "pip", purpose="sphinx theme"),
    ]
    return res


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
                      purpose="model SQL queries as objects"),
        ModuleInstall('flask-sqlalchemy', 'pip', mname='flask.ext.sqlalchemy'),
        ModuleInstall('simplejson', 'wheel', purpose="json parser"),
        ModuleInstall('python-pptx', 'pip', mname="pptx",
                      purpose="read/write PowerPoint presentation"),
        ModuleInstall(
            'python-docx', 'pip', mname="docx", purpose="read/write Word document"),
        ModuleInstall('flask', 'pip', purpose="python server"),
        ModuleInstall(
            'flasksphinx', 'pip', purpose="serves Sphinx documentation through a Flask server"),
        ModuleInstall(
            'cffi', 'wheel', purpose="Foreign Function Interface for Python calling C code."),
        ModuleInstall(
            'odo', 'wheel', purpose="usually used with blaze, handles dataframe in various type of containers"),
        ModuleInstall(
            'cytoolz', 'wheel', purpose="Cython implementation of Toolz: High performance functional utilities"),
        ModuleInstall(
            'toolz', 'wheel', purpose="Toolz provides a set of utility functions for iterators, functions, and dictionaries."),
        ModuleInstall(
            'datashape', 'pip', purpose="A data description language."),
        ModuleInstall(
            'dynd', 'wheel', purpose="DyND-Python, a component of the Blaze project, is the Python exposure of the DyND dynamic multi-dimensional array library."),
        ModuleInstall(
            'blaze', 'wheel', purpose="separate expression from computation (works with iterators), used with odo, avoids doing everything in memory, handle better large datasets"),
        ModuleInstall(
            'sympy', 'pip', purpose="SymPy is a Python library for symbolic mathematics."),
        ModuleInstall('gmpy2', 'wheel', purpose="big real numbers"),
        ModuleInstall('llvmpy', 'wheel', mname='llvm',
                      purpose="Python bindings for LLVM, C++ library which allows simple access to compiler tools."),
        ModuleInstall(
            'llvmlite', 'wheel', purpose="lightweight wrapper around basic LLVM functionality"),
        ModuleInstall(
            'numba', 'wheel', purpose="Numba is an Open Source NumPy-aware optimizing compiler for Python sponsored by Continuum Analytics, Inc."),
        ModuleInstall(
            'networkx', 'pip', purpose="model graphs, basic drawings"),
        ModuleInstall('snowballstemmer', 'pip',
                      purpose="This package provides 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms."),
        ModuleInstall('scikit-image', 'wheel', mname='skimage',
                      purpose="scikit-image is a collection of algorithms for image processing."),
        ModuleInstall(
            'patsy', 'pip', purpose="A Python package for describing statistical models and for building design matrices (y ~ x1 + x2)"),
        ModuleInstall(
            'cvxopt', 'wheel', purpose="linear, quadratique optimization"),
        ModuleInstall('pymc', 'wheel', purpose="Monte Carlo computation"),
        ModuleInstall(
            'PyWavelets', 'wheel', mname='pywt', purpose="wavelets computation"),
        ModuleInstall('fastcluster', 'wheel', purpose="clustering, AHC, ..."),
        ModuleInstall(
            'pycosat', 'wheel', purpose="PicoSAT is a popular SAT solver written by Armin Biere in pure C."),
        ModuleInstall('pyshp', 'pip', mname='shapefile',
                      purpose="Pure Python read/write support for ESRI Shapefile format"),
        ModuleInstall('Shapely', 'wheel', mname='shapely',
                      purpose="Manipulation and analysis of geometric objects in the Cartesian plane."),
        ModuleInstall(
            'vispy', 'pip', purpose="Vispy is a high-performance interactive 2D/3D data visualization library."),
        ModuleInstall(
            'selenium', 'pip', purpose="Python wrapper for Selenium"),
        ModuleInstall(
            'Pillow', 'wheel', mname='PIL', purpose="read/create images"),
        ModuleInstall('pygame', 'wheel', purpose="GUI, interface for games"),
        ModuleInstall(
            'Kivy', 'wheel', mname='kivy', purpose="GUI, interface for games, mobile"),
        ModuleInstall('kivy-garden', 'pip', mname='kivy.garden',
                      purpose="Garden tool for kivy flowers."),
        ModuleInstall(
            'py4j', 'pip', purpose="Enables Python programs to dynamically access arbitrary Java objects"),
        ModuleInstall('python-igraph', 'wheel', mname='igraph',
                      purpose="High performance graph data structures and algorithms"),
        ModuleInstall(
            'lockfile', 'pip', purpose="Platform-independent file locking module"),
        ModuleInstall('python-daemon', 'pip', mname='daemon',
                      purpose="Library to implement a well-behaved Unix daemon process."),
        ModuleInstall('luigi', 'pip', purpose="workflows, data workflows"),
        #
        ModuleInstall('setproctitle', 'wheel', mname='setproctitle',
                      purpose="A Python module to customize the process title"),
        # thrift only works only for Python 2.7
        ModuleInstall(
            'thriftpy', 'pip', purpose="ure python implemention of Apache Thrift."),
        # ModuleInstall('airflow', 'pip'),  # does not work on Python 3
        ModuleInstall(
            'smopy', 'pip', purpose="OpenStreetMap image tiles in Python "),
        ModuleInstall(
            'folium', 'pip', purpose="Make beautiful maps with Leaflet.js & Python"),
        ModuleInstall('basemap', 'wheel', mname='mpl_toolkits.basemap',
                      purpose="maps extension for matplotlib"),
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
                      purpose="Cryptographic modules for Python."),
        ModuleInstall("paramiko", "pip", purpose="SSH2 protocol library"),
        #
        ModuleInstall(
            "pattern", "pip", purpose="Web mining module for Python, with tools for scraping, natural language processing, machine learning, network analysis and visualization.")
        if sys.version_info[0] < 3 else None,  # to read dbase format
        #
        ModuleInstall(
            "pbr", "pip", purpose="PBR is a library that injects some useful and sensible default behaviors into your setuptools run."),
        #
        # 2015-02-05
        #
        ModuleInstall("autopy3", "wheel", mname="autopy3",
                      purpose="A simple, cross-platform GUI automation toolkit for Python 3"),  # simulate events
        # large double
        ModuleInstall("bigfloat", "wheel", purpose="big float"),
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
            "pymongo", "wheel", purpose="Python wrapper for MongoDB"),
        ModuleInstall(
            "PyOpenGL", "wheel", mname="OpenGL", purpose="use OpenGL in Python"),
        ModuleInstall(
            "Theano", "wheel", mname="theano", purpose="deep learning, GPU"),
        ModuleInstall("keras", "pip", purpose="deep learning"),
        ModuleInstall("neon", "pip", purpose="deep learning"),
        ModuleInstall(
            "pyqtgraph", "pip", purpose="Scientific Graphics and GUI Library for Python, depends on PySide"),
        ModuleInstall("deap", "pip", purpose="deep learning"),
        # for gensim
        ModuleInstall(
            "boto", "pip", purpose="A Python interface to Amazon Web Services"),
        # for gensim
        ModuleInstall("bz2file", "pip", purpose="process bz2 files"),
        # for gensim
        ModuleInstall("smart_open", "wheel",
                      purpose="Utils for streaming large files (S3, HDFS, gzip, bz2...), provides the same API for many format"),
        ModuleInstall("gensim", "wheel", purpose="genetic algorithm"),
        # ModuleInstall("pybrain", "pip"),   # some issues with the code
        # (relative import are not well handled in version 0.3.3
        ModuleInstall(
            "h5py", "wheel", purpose="The h5py package is a Pythonic interface to the HDF5 binary data format. Trillion-Particle Simulation."),
        # Bayesian
        ModuleInstall(
            "bayespy", "pip", purpose="bayesian modelling and computation"),
        ModuleInstall(
            "numexpr", "wheel", purpose="Fast numerical array expression evaluator for Python, NumPy, PyTables, pandas, bcolz and more."),
        #
        ModuleInstall("glueviz", "wheel", mname="glue",
                      purpose="ploting, Multidimensional data visualzation across files"),
        #
        # javascript graphs
        ModuleInstall("charts", "pip", purpose="plotting in javascript"),
        #
        ModuleInstall(
            "dill", "pip", purpose="serialize all of python (almost), Dill extends python�s �pickle� module for serializing and de-serializing python objects to the majority of the built-in python types."),  # for dask
        # parallel computation
        ModuleInstall(
            "dask", "pip", purpose="parallization of operations with dataframe"),
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
            "rodeo", "pip", purpose="Scientific IDE, mixed between Spyder and IPython"),
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
                      purpose="tree visualisation"),  # graph visualization
        # visualisation
        ModuleInstall(
            "pyxley", "pip", purpose="plotting, visualization, javascript"),
    ]

    if sys.platform.startswith("win"):
        mod.append(
            ModuleInstall("pywin32", "wheel", mname="win32com", purpose="call Windows DLL"))
        mod.append(ModuleInstall("winshell", "pip"))

    return [_ for _ in mod if _ is not None]


def azure_set():
    """
    Modules to handle huge datasets on disk, hierarchical datasets.

    """
    mod = [
        ModuleInstall("azure", "pip", purpose="Python wrapper for Azure API"),
    ]

    return mod


def ensae_set():
    """
    .. index:: ENSAE

    Modules introduced by students and some others added after some reading.
    """
    mod = [
        ModuleInstall(
            "celery", "pip", purpose="Celery is an asynchronous task queue/job queue based on distributed message passing."),
        ModuleInstall(
            "tweepy", "pip", purpose="Python wrapper for the twitter API"),
        #ModuleInstall("newspaper3k", "pip", mname="newspaper"),
        ModuleInstall(
            "django", "pip", purpose="web application, most famous module about it, the only when to build a scalable website"),
        ModuleInstall("django-audiotracks", "pip",
                      mname="audiotracks", purpose="read audio with django"),
        ModuleInstall("Quandl", "pip", purpose="access Quandl API"),
        #ModuleInstall("Lasagne", "pip", mname="lasagne"),
        ModuleInstall(
            "pymunk", "pip", purpose="pymunk is a easy-to-use pythonic 2d physics library that can be used whenever you need 2d rigid body physics from Python. Perfect when you need 2d physics in your game, demo or other application! It is built on top of the very nice 2d physics library Chipmunk."),
        ModuleInstall(
            "nltk", "wheel", purpose="NLP, natural language processing"),
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
            "BTrees", "wheel", purpose="This package contains a set of persistent object containers built around a modified BTree data structure."),
        ModuleInstall(
            "datrie", "wheel", purpose="Fast, efficiently stored Trie for Python."),
        # ModuleInstall("pysparse", "pip"), #does not work
        ModuleInstall(
            "la", "wheel", purpose="Label the rows, columns, any dimension, of your NumPy arrays."),
        ModuleInstall(
            "mahotas", "wheel", purpose="Mahotas: Computer Vision Library"),
        ModuleInstall("milk", "wheel", purpose="machine learning toolkit"),
        ModuleInstall("minepy", "wheel", purpose="interface to MineCraft"),
        ModuleInstall(
            "NLopt", "wheel", mname="nlopt", purpose="linear, quadratic optimization"),
        ModuleInstall("Pmw", "wheel", mname="Pmw",
                      purpose="Pmw is a toolkit for building high-level compound widgets in Python using the Tkinter module."),
        ModuleInstall(
            "pytools", "pip", purpose="A collection of tools for Python"),
        ModuleInstall(
            "pycuda", "wheel", purpose="PyCUDA lets you access Nvidia�s CUDA parallel computation API from Python."),
        # ModuleInstall("scikits.cuda", "pip", mname="skcuda"), # no stable
        # version
        ModuleInstall(
            "pylzma", "wheel", purpose="Python bindings for the LZMA library by Igor Pavlov."),
        ModuleInstall("pymvpa2", "wheel", mname="mvpa2",
                      purpose="PyMVPA is a Python module intended to ease pattern classification analyses of large datasets."),
        ModuleInstall(
            "pyodbc", "wheel", purpose="access to protocal ODBC (SQL databases)"),
        ModuleInstall(
            "pypmc", "wheel", purpose="pypmc is a python package focusing on adaptive importance sampling."),
        ModuleInstall(
            "pyserial", "wheel", mname="serial", purpose="access to serial port"),
        ModuleInstall("PyX", "wheel", mname="pyx", purpose="plotting"),
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
            "tutormagic", "pip", purpose="brings PythonTutor in a notebok"),
        # cache resuls from a long computation
        ModuleInstall(
            "ipycache", "pip", purpose="Defines a %%cache cell magic in the IPython notebook to cache results of long-lasting computations in a persistent pickle file "),
        # to upload a file in a notebook
        ModuleInstall(
            "nbupload", "pip", purpose="widget to upload a file in a notebook"),
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
        ModuleInstall("vincent", "pip", purpose="plotting"),  # graph
        # graph, pygal_maps_world only accepts the latest version
        ModuleInstall("pygal", "github", "Kozea", purpose="plotting"),
        ModuleInstall(
            "pygal_maps_world", "pip", purpose="extension to pygal (maps)"),  # graph
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
                      purpose="linear, quadratique optimization with constraints"),
        # for pyensae unit test
        ModuleInstall("JSAnimation", "github", "jakevdp",
                      purpose="provides javascript script to display differences between two files"),
        #
        # pydata
        #
        ModuleInstall("CherryPy", "wheel", mname="cherrypy",
                      purpose="create web application, needed by Spyre"),
        ModuleInstall("Spyre", "pip", mname="spyre",
                      purpose="create simple web application to visualize data"),
        ModuleInstall(
            "python-recsys", "pip", mname="recsys", purpose="recommendation system"),
        ModuleInstall(
            "viscm", "pip", purpose="tool for analyzing colormaps and creating new colormaps."),
        ModuleInstall("cubehelix", "github", "jradavenport",
                      purpose="a full implementation of Dave Green's cubehelix colormap for Python"),
        ModuleInstall("lifelines", "pip", purpose="survival analysis"),
        ModuleInstall(
            "pysnptools", "pip", purpose="operation on DNA sequences"),
        #
        # 2015-07
        #
        ModuleInstall(
            "nuitka", "pip", purpose="C++ compilation, code optimization"),
        ModuleInstall(
            "tri", "pip", purpose="Delaunay triangulation"),

    ]
    if sys.platform.startswith("win"):
        mod.append(ModuleInstall("VideoCapture", "wheel",
                                 purpose="A Win32 Python Extension for Accessing Video Devices"))

    return mod


def teachings_set():
    """
    .. index:: ENSAE, teachings

    Modules implemented for my teachings.
    """
    mod = [
        ModuleInstall(
            "pyquickhelper", "pip", purpose="helpers to generation documentation"),
        ModuleInstall(
            "pymyinstall", "pip", purpose="easy installation of modules including Windows"),
        ModuleInstall("pymmails", "pip", purpose="read/send emails"),
        ModuleInstall(
            "pyensae", "pip", purpose="helpers, Hadoop, SQL, financial times series, ..."),
        ModuleInstall("pyrsslocal", "pip", purpose="RSS readers"),
        ModuleInstall(
            "code_beatrix", "pip", purpose="teaching programming to kids, lesenfantscodaient.fr"),
        ModuleInstall(
            "actuariat_python", "pip", purpose="teachings, insurance examples"),
        ModuleInstall("ensae_teaching_cs", "pip",
                      purpose="teachings, introduction to programmaing, machine learning, map/reduce"),
    ]
    #
    return mod


def bigdata_set():
    """
    Modules to handle huge datasets on disk, hierarchical datasets.

    """
    mod = [
        ModuleInstall(
            "blosc", "wheel", purpose="Blosc (http://blosc.org) is a high performance compressor optimized for binary data."),
        ModuleInstall(
            "tables", "wheel", purpos="PyTables is a package for managing hierarchical datasets and designed to efficiently and easily cope with extremely large amounts of data."),
    ]

    return mod
