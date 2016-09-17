#-*- coding: utf-8 -*-
"""
@file
@brief Defines a set of modules for more machine learning, tools, networks, visualization.
"""
import sys
from ..installhelper.module_install import ModuleInstall
from .config_helper import is_64bit


def extended_set():
    """
    list of modules to install, an rich set, to work with data and more, it requires the modules in set *small*
    """
    mod = [
        ModuleInstall(
            "natgrid", "wheel", mname="mpl_toolkits.natgrid",
            purpose="Python interface to NCAR natgrid library (for matplotlib)"),
        ModuleInstall(
            "py", "pip", purpose="library with cross-python path, ini-parsing, io, code, log facilities"),
        ModuleInstall("pytest", "pip",
                      purpose="pytest: simple powerful testing with Python"),
        ModuleInstall(
            "bitarray", "wheel",
            purpose="efficient arrays of booleans -- C extension"),
        ModuleInstall(
            "blist", "wheel",
            purpose="a list-like type with better asymptotic performance and similar performance on small lists"),
        ModuleInstall(
            "blz", "wheel",
            purpose="blz: a compressed data container"),
        ModuleInstall("pamela", "pip",
                      purpose="An interface to the Pluggable Authentication Modules (PAM) " +
                      "library on linux, written in pure python (using ctypes)")
        if not sys.platform.startswith("win") else None,
        ModuleInstall(
            "jupyterhub", "pip", purpose="JupyterHub: A multi-user server for Jupyter notebooks", usage="JUPYTER")
        if not sys.platform.startswith("win") else None,
        ModuleInstall('rpy2', 'wheel', purpose="interact with R (R_HOME needs to be set up on Linux)",
                      usage="DATA/ML"),
        ModuleInstall('python-pptx', 'pip', mname="pptx",
                      purpose="read/write PowerPoint presentation"),
        ModuleInstall(
            'python-docx', 'pip', mname="docx", purpose="read/write Word document"),
        # ModuleInstall('flasksphinx', 'pip', purpose="serves Sphinx
        # documentation through a Flask server"), # issue with Python 3
        ModuleInstall(
            'cffi', 'wheel', purpose="Foreign Function Interface for Python calling C code."),
        ModuleInstall(
            'odo', 'pip', purpose="usually used with blaze, handles dataframe in various type of containers", usage="DATA/ML"),
        ModuleInstall(
            'cytoolz', 'wheel', purpose="Cython implementation of Toolz: High performance functional utilities", usage="DATA/ML"),
        ModuleInstall(
            'ordereddict', 'pip', purpose="Python's collections.OrderedDict") if sys.version_info[0] == 2 else None,
        ModuleInstall(
            'cyordereddict', 'wheel', purpose="Cython implementation of Python's collections.OrderedDict"),
        ModuleInstall(
            'toolz', 'pip', purpose="Toolz provides a set of utility functions for iterators, functions, and dictionaries.", usage="DATA/ML"),
        ModuleInstall(
            'datashape', 'pip', purpose="A data description language."),
        ModuleInstall('dynd', 'wheel',
                      purpose="DyND-Python, a component of the Blaze project, " +
                      "is the Python exposure of the DyND dynamic multi-dimensional array library.")
        if sys.version_info[0] >= 3 else None,
        ModuleInstall(
            'sympy', 'pip', purpose="SymPy is a Python library for symbolic mathematics."),
        ModuleInstall('gmpy2', 'wheel',
                      purpose="big real numbers (issue on Linux and Anaconda)"),
        ModuleInstall('llvmpy', 'wheel', mname='llvm',
                      purpose="Python bindings for LLVM, C++ library which allows simple access to compiler tools, not maintained anymore, use llvmlite instead")
        if sys.version_info[:2] <= (3, 4) else None,
        ModuleInstall('llvmlite', 'wheel',
                      purpose="lightweight wrapper around basic LLVM functionality, check issue " +
                      "https://github.com/cmderdev/cmder/issues/490 for missing api-ms-win-crt-runtime-l1-1-0.dll"),
        ModuleInstall(
            'blaze', 'pip', purpose="separate expression from computation (works with iterators), used with odo, " +
            "avoids doing everything in memory, handle better large datasets, check " +
            "issue https://github.com/cmderdev/cmder/issues/490 for missing api-ms-win-crt-runtime-l1-1-0.dll",
            usage="DATA/ML"),
        ModuleInstall(
            'numba', 'wheel', purpose="Numba is an Open Source NumPy-aware optimizing compiler for Python sponsored by Continuum Analytics, Inc."),
        ModuleInstall('scikit-image', 'wheel', mname='skimage',
                      purpose="scikit-image is a collection of algorithms for image processing."),
        ModuleInstall(
            'cvxopt', 'wheel', purpose="linear, quadratique optimization", usage="OPTIM"),
        ModuleInstall(
            'PyWavelets', 'wheel', mname='pywt', purpose="wavelets computation", usage="DATA/ML"),
        ModuleInstall('fastcluster', 'wheel',
                      purpose="clustering, AHC, ... (issue on Linux and Anaconda)", usage="DATA/ML"),
        ModuleInstall(
            'pycosat', 'wheel', purpose="PicoSAT is a popular SAT solver written by Armin Biere in pure C."),
        ModuleInstall('pyshp', 'github', 'GeospatialPython', mname='shapefile',
                      purpose="Pure Python read/write support for ESRI Shapefile format"),
        ModuleInstall('Shapely', 'wheel', mname='shapely',
                      purpose="Manipulation and analysis of geometric objects in the Cartesian plane."),
        ModuleInstall(
            'vispy', 'pip', purpose="Vispy is a high-performance interactive 2D/3D data visualization library."),
        ModuleInstall(
            'selenium', 'pip', purpose="Python wrapper for Selenium", usage="NETWORK"),
        ModuleInstall(
            'splinter', 'pip', purpose="browser abstraction for web acceptance testing", usage="NETWORK"),
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
        ModuleInstall('python-daemon', 'pip', mname="daemon",
                      purpose="Library to implement a well-behaved Unix daemon process (for luigi)") if not sys.platform.startswith("win") else None,
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
            'osmapi', 'pip', purpose="Python wrapper for the OSM API", usage="VIZ"),
        ModuleInstall('geopy', 'pip',
                      purpose="Python Geocoding Toolbox", usage="VIZ"),
        ModuleInstall('basemap', 'wheel', mname='mpl_toolkits.basemap',
                      purpose="maps extension for matplotlib", usage="VIZ"),
        ModuleInstall('pyproj', 'wheel',
                      purpose="python interface to PROJ4 library for cartographic transformations " +
                      "https://jswhit.github.io/pyproj, needed by cartopy", usage="VIZ"),
        ModuleInstall('Cartopy', 'wheel', mname="cartopy",
                      purpose="Cartopy is a Python package designed to make drawing maps for data analysis " +
                      "and visualisation as easy as possible (issue on Linux and Anaconda)", usage="VIZ"),
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
        ModuleInstall("pycontracts", "pip", mname="contracts",  # version="1.7.6",
                      purpose="PyContracts is a Python package that allows to declare constraints on function parameters " +
                      "and return values, setup for version 1.7.7 is bugged"),
        #
        ModuleInstall(
            "ecdsa", "pip", purpose="ECDSA cryptographic signature library (pure python)"),
        ModuleInstall("winrandom", "wheel2", mname="winrandom",
                      purpose="This module gives direct access to Windows Cryptographic API CryptGetRandom() function, " +
                      "which is cryptographically strong pseudo-random number generator (PRNG) on Windows:"),
        ModuleInstall("pycrypto", "wheel2", mname="Crypto",
                      purpose="Cryptographic modules for Python (not available on x64 and Python 3)"),
        ModuleInstall("pycryptodomex", "pip", mname="Cryptodome",
                      purpose="Cryptographic modules for Python (not available on x64 and Python 3)"),
        ModuleInstall("xxhash", "pip",
                      purpose="xxHash is an Extremely fast Hash algorithm, running at RAM speed limits."),
        ModuleInstall("paramiko", "pip",
                      purpose="SSH2 protocol library", usage="NETWORK"),
        #
        # ModuleInstall("pattern", "pip", purpose="Web mining module for Python, with tools for scraping, natural language processing, machine learning, network analysis and visualization.") #only works on Python 2.7
        #
        #
        # 2015-02-05
        #
        ModuleInstall("autopy3", "wheel", mname="autopy3",
                      purpose="A simple, cross-platform GUI automation toolkit for Python 3 " +
                      "(issue on Linux and Anaconda)") if sys.version_info[0] >= 3 else None,  # simulate events
        # large double
        ModuleInstall("bigfloat", "wheel",
                      purpose="big float (issue with Linux and Anaconda)"),
        # convex optimization, depends on CVXOPT
        ModuleInstall(
            "scs", "wheel", purpose="Solves convex cone programs via operator splitting.", usage="OPTIM"),
        ModuleInstall(
            "ecos", "wheel", purpose="ECOS is a numerical software for solving convex second-order cone programs (SOCPs)", usage="OPTIM"),
        ModuleInstall(
            "CVXcanon", "wheel", purpose="A low-level library to perform the matrix building step in cvxpy, " +
            "a convex optimization modeling software.", usage="OPTIM") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("cvxpy", "pip", usage="OPTIM",
                      purpose="linear, quadratic optimization, depends on cvxopt") if sys.version_info[:2] >= (3, 5) else None,
        # to install packages with conda
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
            "psycopg2", "wheel", mname="psycopg2",
            purpose="Python-PostgreSQL Database Adapter"),
        ModuleInstall(
            "PyOpenGL", "wheel", mname="OpenGL", purpose="use OpenGL in Python"),
        ModuleInstall(
            "PyOpenGL_accelerate", "wheel", mname="OpenGL_accelerate", purpose="Acceleration code for PyOpenGL"),
        ModuleInstall(
            "libpython", "wheel",
            purpose="needed for theano (C++ compilation), compilation of libpython with mingw") if sys.version_info[:2] <= (3, 4) else None,
        ModuleInstall(
            "Theano", "pip", mname="theano", purpose="deep learning, GPU", usage="DATA/ML"),
        ModuleInstall('pymc', 'wheel',
                      purpose="Monte Carlo computation", usage="DATA/ML"),
        ModuleInstall('pymc', 'wheel', web="https://github.com/pymc-devs/pymc",
                      purpose="Monte Carlo computation", usage="DATA/ML") if sys.version_info[0] >= 3 else None,
        ModuleInstall('pymc3', 'github', "pymc-devs", web="https://github.com/pymc-devs/pymc3",
                      purpose="Monte Carlo computation (Python 3 only)", usage="DATA/ML") if sys.version_info[0] >= 3 else None,
        ModuleInstall('pysterior', 'pip',
                      purpose="pysterior is a machine learning library for Python which aims to make Bayesian parametric regression and " +
                      "classification models accessible and easy to use. The library allows users to construct " +
                      "supervised learning models using an intuitive interface similar to that used by scikit-learn.",
                      usage="DATA/ML") if sys.version_info[0] >= 3 else None,
        ModuleInstall(
            "pyqtgraph", "pip", purpose="Scientific Graphics and GUI Library for Python, depends on PySide", usage="GUI"),
        ModuleInstall("deap", "pip", purpose="deep learning"),
        # for gensim and distributed
        ModuleInstall("jmespath", "pip", purpose="JSON Matching Expressions"),
        ModuleInstall("botocore", "pip", usage="AWS",
                      purpose="A low-level interface to a growing number of Amazon Web Services. " +
                      "The botocore package is the foundation for the AWS CLI as well as boto3."),
        ModuleInstall("s3transfer", "pip", usage="AWS",
                      purpose="An Amazon S3 Transfer Manager"),
        ModuleInstall("boto3", "pip", usage="AWS",
                      purpose="A Python interface to Amazon Web Services"),
        # for gensim
        ModuleInstall("bz2file", "pip", purpose="process bz2 files"),
        # for gensim
        ModuleInstall("boto", "pip",
                      purpose="Amazon Web Services Library"),
        ModuleInstall("smart_open", "pip",
                      purpose="Utils for streaming large files (S3, HDFS, gzip, bz2...), provides the same API for many format"),
        ModuleInstall("httpretty", "pip",
                      purpose="HTTP client mock for Python"),
        ModuleInstall("gensim", "wheel", purpose="genetic algorithm"),
        # ModuleInstall("pybrain", "pip"),   # some issues with the code
        # (relative import are not well handled in version 0.3.3
        ModuleInstall(
            "h5py", "wheel", purpose="The h5py package is a Pythonic interface to the HDF5 binary data format. Trillion-Particle Simulation.", usage="DATA/ML"),
        ModuleInstall("keras", "pip", purpose="deep learning",
                      usage="DATA/ML"),
        # Bayesian
        ModuleInstall(
            "bayespy", "pip", purpose="bayesian modelling and computation", usage="DATA/ML"),
        ModuleInstall(
            "numexpr", "wheel", purpose="Fast numerical array expression evaluator for Python, NumPy, PyTables, pandas, bcolz and more."),
        #
        ModuleInstall("glueviz", "pip", mname="glue",
                      purpose="ploting, Multidimensional data visualzation across files", usage="DATA/ML"),
        #
        ModuleInstall("pandas-highcharts", "pip", mname="pandas_highcharts",
                      purpose="plotting in javascript and pandas", usage="VIZ"),
        #
        ModuleInstall(
            "chest", "pip",
            purpose="Simple on-disk dictionary"),
        ModuleInstall(
            "heapdict", "pip",
            purpose="a heap with decrease-key and increase-key operations"),
        ModuleInstall(
            "partd", "pip",
            purpose="Appendable key-value storage"),
        ModuleInstall(
            "locket", "pip",
            purpose="File-based locks for Python for Linux and Windows"),
        ModuleInstall(
            "dill", "pip", purpose="serialize all of python (almost), Dill extends python's pickle module for serializing " +
            "and de-serializing python objects to the majority of the built-in python types."),  # for dask
        ModuleInstall("cloudpickle", "pip",
                      purpose="Extended pickling support for Python objects") if sys.version_info[:2] >= (3, 5) else None,
        # parallel computation
        ModuleInstall(
            "dask", "pip", purpose="parallization of operations with dataframe", usage="DATA/ML"),
        ModuleInstall(
            "scoop", "pip", purpose="SCOOP (Scalable COncurrent Operations in Python) " +
            "is a distributed task module allowing concurrent parallel programming on various environments, " +
            "from heterogeneous grids to supercomputers", usage="DATA/ML"),
        #
        ModuleInstall(
            "jedi", "pip", purpose="An autocompletion tool for Python that can be used for text editors."),
        ModuleInstall(
            "docopt", "pip", purpose="Pythonic argument parser, that will make you smile"),
        ModuleInstall("markdown2", "pip", purpose="markdown parser"),
        ModuleInstall(
            "structures", "pip", purpose="User-friendly library for creating data structures."),
        ModuleInstall(
            "py2exe", "wheel",
            purpose="convert a python program into an exe program") if sys.platform.startswith("win") and sys.version_info[:2] <= (3, 4) else None,
        # rodeo disappeared from pipy
        # ModuleInstall(
        #     "rodeo", "pip", purpose="Scientific IDE, mixed between Spyder and IPython", usage="VIZ"),
        ModuleInstall(
            "tzlocal", "pip", purpose="tzinfo object for the local timezone"),
        ModuleInstall(
            "funcsigs", "pip", purpose="Python function signatures from PEP362"),
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
        # ModuleInstall("ete", "github", "jhcepas", mname="ete3",
        #               web="http://etetoolkit.org/",
        # purpose="tree visualisation", usage="VIZ"),  # graph visualization
        ModuleInstall("ete3", "pip",
                      web="http://etetoolkit.org/",
                      purpose="tree visualisation", usage="VIZ"),  # graph visualization
        # visualisation
        ModuleInstall(
            "pyexecjs", "pip", mname="execjs", purpose="Run JavaScript code from Python (for pyreact)", usage="NETWORK"),
        ModuleInstall("pyreact", "pip", mname="react",
                      purpose="Python bridge to JSX & the React JavaScript library. (for pyxley)", usage="NETWORK"),
        ModuleInstall(
            "pyxley", "pip", purpose="A pure-Python SNMPv1/v2c/v3 library", usage="NETWORK"),

        #
        # 2015-08
        #
        ModuleInstall(
            "pysmi", "pip", purpose="SNMP SMI/MIB Parser (for pysnmp)"),
        ModuleInstall(
            "pyasn1", "pip", purpose="ASN.1 types and codecs (for pysnmp)"),
        ModuleInstall(
            "pysnmp", "pip", purpose="A pure-Python SNMPv1/v2c/v3 library", usage="NETWORK"),
        # pyinstaller does not install properly on Windows
        # ModuleInstall(
        #    "pyinstaller", "pip", purpose="Converts (packages) Python programs into stand-alone executables, under Windows, Linux, Mac OS X, AIX and Solaris."),
        ModuleInstall(
            "imageio", "pip", purpose="Library for reading and writing a wide range of image, video, " +
            "scientific, and volumetric data formats (for moviepy)", usage="VIDEO"),
        ModuleInstall(
            "tqdm", "pip", purpose="A Simple Python Progress Meter (for moviepy)", usage="VIDEO"),
        ModuleInstall(
            "moviepy", "pip", purpose="Video editing with Python", usage="VIDEO"),
        ModuleInstall(
            "xgboost", "wheel2", purpose="Parallelized Stochastic Gradient Descent (only available on " +
            "Python 3 and x64)", usage="DATA/ML") if sys.version_info[0] >= 3 and is_64bit() else None,
        ModuleInstall("pygling", "pip",
                      purpose="to build makefile with python") if sys.version_info[0] == 2 else None,
        ModuleInstall("cuda4py", "pip",
                      purpose="Python cffi CUDA bindings and helper classes"),
        ModuleInstall("whoosh", "pip", purpose="search engine in Python"),
        ModuleInstall("pymatbridge", "pip",
                      purpose="pymatbridge is a set of python and matlab functions to allow these two systems to talk to each other"),
        ModuleInstall("scilab2py", "pip",
                      purpose="Python to Scilab bridge", usage="DATA/ML"),
        # ModuleInstall("scilab_kernel", "pip",
        #              purpose="A Scilab kernel for IPython", usage="JUPYTER"),
        # does not work
        ModuleInstall("pymssql", "wheel", usage="SQL",
                      purpose="A simple database interface for Python that builds on top of FreeTDS " +
                      "to provide a Python DB-API (PEP-249) interface to Microsoft SQL Server."),

        ModuleInstall("PyMySQL", "pip", mname="pymysql",
                      purpose="Pure-Python MySQL Driver", usage="SQL"),
        ModuleInstall("mysqlclient", "wheel", mname="MySQLdb",
                      purpose="MySQL driver written in Python which does not depend on MySQL C client libraries and " +
                      "implements the DB API v2.0 specification (PEP-249).", usage="SQL"),
        ModuleInstall("line-profiler", "wheel", mname="line_profiler",
                      purpose="line_profiler is a module for doing line-by-line profiling of functions. kernprof " +
                      "is a convenient script for running either line_profiler or the " +
                      "Python standard library's cProfile or profile modules, depending on what is available.",
                      usage="PROFILING"),
        ModuleInstall("memory-profiler", "pip", mname="memory_profiler",
                      purpose="A module for monitoring memory usage of a python program", usage="PROFILING"),
        ModuleInstall("pyinstrument", "pip", usage="PROFILING",
                      purpose="A Python profiler that records the call stack of the executing code, " +
                      "instead of just the final function in it."),
        ModuleInstall("gprof2dot", "pip", usage="PROFILING",
                      purpose="This is a Python script to convert the output from many profilers into a dot graph."),
        ModuleInstall("vprof", "pip", usage="PROFILING",
                      purpose="vprof is a Python package providing rich and interactive visualizations for various Python " +
                      "program characteristics such as running time and memory usage."),
        ModuleInstall("snakeviz", "pip",
                      purpose="SnakeViz is a browser based graphical viewer for the output of Python’s cProfile module.", usage="PROFILING"),
        ModuleInstall("mpmath", "pip",
                      purpose="mpmath is a free (BSD licensed) Python library for real and complex floating-point arithmetic with arbitrary precision."),
        ModuleInstall("httplib2", "pip",
                      purpose="A comprehensive HTTP client library."),
        ModuleInstall("oauth2client", "pip",
                      purpose="The oauth2client is a client library for OAuth 2.0."),
        ModuleInstall("uritemplate", "pip",
                      purpose="URI templates"),
        ModuleInstall("google-api-python-client", "pip", mname="googleapiclient",
                      purpose="The Google API Client for Python is a client library for accessing the Plus, Moderator, and many other Google APIs."),
        ModuleInstall("googlemaps", "pip",
                      purpose="Python client library for Google Maps API Web Services"),
        ModuleInstall("python-gmaps", "pip", mname="gmaps",
                      purpose="Google Maps API client http://python-gmaps.readthedocs.org"),
        ModuleInstall("keyring", "pip",
                      purpose="Store and access your passwords safely."),
        ModuleInstall("param", "wheel", source="2",
                      purpose="Declarative Python programming using Parameters."),
        ModuleInstall("holoviews", "pip", usage="VIZ",
                      purpose="Composable, declarative data structures for building complex visualizations easily."),
        ModuleInstall("plotly", "pip", usage="VIZ",
                      purpose="Plotly's Python graphing library makes interactive, publication-quality graphs online. Examples of how to make line plots, " +
                              "scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, " +
                              "polar charts and bubble charts."),
        ModuleInstall("colorlover", "pip", usage="VIZ",
                      purpose="Color scales for IPython notebook"),
        ModuleInstall("cufflinks", "pip", usage="VIZ",
                      purpose="Productivity Tools for Plotly + Pandas"),
        ModuleInstall("lightning-python", "pip", mname="lightning", usage="VIZ",
                      purpose="Python client for the lightning API"),
        ModuleInstall("passlib", "pip",
                      purpose="comprehensive password hashing framework supporting over 30 schemes"),
        ModuleInstall("plac", "pip",
                      purpose="The smartest command line arguments parser in the world"),
        ModuleInstall("idna", "pip",
                      purpose="Internationalized Domain Names in Applications (IDNA)"),
        ModuleInstall("ipaddress", "pip",
                      purpose="IPv4/IPv6 manipulation library") if sys.version_info[0] == 2 else None,
        ModuleInstall("cryptography", "pip",
                      purpose="cryptography is a package which provides cryptographic recipes and primitives to Python developers."),
        ModuleInstall("pyOpenSSL", "pip", mname="pyopenssl",
                      purpose="Python wrapper module around the OpenSSL library"),
        ModuleInstall("w3lib", "pip",
                      purpose="Library of web-related functions"),
        # ModuleInstall('python-cloudfiles-hubic', 'github', "Gu1", mname="cloudfiles",
        #                   web="https://github.com/Gu1/python-cloudfiles-hubic",
        #              purpose="access to Hubic"),
        ModuleInstall('onedrive-sdk-python', 'github', "OneDrive", mname="onedrivesdk",
                      web="https://github.com/Gu1/python-cloudfiles-hubic/",
                      purpose="access to OneDrive"),
        # ModuleInstall('rlpy', 'pip', usage="DATA/ML",
        # purpose="RLPy is a framework to conduct sequential decision making
        # experiments. The current focus of this project lies on
        # value-function-based reinforcement learning, specifically using
        # linear function approximators (only Python 2.7)."),
        ModuleInstall('wordcloud', 'wheel', usage="VIZ",
                      purpose="A little word cloud generator in Python."),
        ModuleInstall('pytagcloud', 'pip',
                      purpose="Create beautiful tag clouds as images or HTML"),

        # distributed
        ModuleInstall('tblib', 'pip',
                      purpose="Traceback fiddling library. For now allows you to pickle tracebacks and raise exceptions with pickled " +
                      "tracebacks in different processes. This allows better error handling when running code over " +
                      "multiple processes (imagine multiprocessing, billiard, futures, celery etc)"),
        ModuleInstall("zict", "pip",
                      purpose="The dictionary / mutable mapping interface is powerful and multi-faceted."),
        ModuleInstall("click", "pip",
                      purpose="A simple wrapper around optparse for powerful command line utilities."),
        ModuleInstall('distributed', 'pip',
                      purpose="Distributed is a lightweight library for distributed computing in Python. It extends both the concurrent.futures " +
                      "and dask APIs to moderate sized clusters. Distributed provides data-local computation " +
                      "by keeping data on worker nodes, running computations where data lives, " +
                      "and by managing complex data dependencies between tasks."),

        # mezzanine
        ModuleInstall(
            "chardet", "pip", usage="WEB",
            purpose="Universal encoding detector."),
        ModuleInstall("bleach", "pip", usage="WEB",
                      purpose="An easy whitelist-based HTML-sanitizing tool."),
        ModuleInstall("grappelli_safe", "pip", usage="WEB",
                      purpose="A snapshot of the grappelli_2 branch of django-grappelli, packaged as a dependency for the Mezzanine CMS for Django."),
        ModuleInstall("filebrowser_safe", "pip", usage="WEB",
                      purpose="A snapshot of the filebrowser_3 branch of django-filebrowser, packaged as a dependency for the Mezzanine CMS for Django."),
        ModuleInstall("django-contrib-comments", "pip", usage="WEB", mname="django_comments",
                      purpose="Django used to include a comments framework; since Django 1.6 it’s " +
                      "been separated to a separate project. This is that project."),
        ModuleInstall("mezzanine", "pip", usage="WEB",
                      purpose="Mezzanine is a powerful, consistent, and flexible content management platform."),
        # pdf
        ModuleInstall("pyPdf", "github", "sdpython",
                      branch="trunk", purpose="read PDF"),
        # 2016-05
        ModuleInstall("pydub", "pip", usage="MUSIC",
                      purpose="Pydub lets you do stuff to audio in a way that isn't stupid."),
        ModuleInstall("cobble", "pip", purpose="Cobble is a Python library that allows easy creation of data objects, " +
                      "including implementations of common methods such as __eq__ and __repr__."),
        ModuleInstall("parsimonious", "pip",
                      purpose="(Soon to be) the fastest pure-Python PEG parser I could muster"),
        ModuleInstall(
            "mammoth", "pip", purpose="Convert Word documents from docx to simple and clean HTML and Markdown"),
        #
        # 2016-06
        #
        # ModuleInstall("ipython-sql", "pip", purpose="RDBMS access via IPython", usgae="JUPYTER"),
        ModuleInstall("julia", "pip",
                      purpose="Julia/Python bridge with IPython support", usage="DATA/ML"),
        ModuleInstall("lazy-object-proxy", "pip", mname="lazy_object_proxy",
                      purpose="A fast and thorough lazy object proxy"),
        ModuleInstall("mpmath", "pip", usage="OPTIM",
                      purpose="mpmath is a free (BSD licensed) Python library for real and complex floating-point arithmetic with arbitrary precision."),
        ModuleInstall("oct2py", "pip",
                      purpose="Python to GNU Octave bridge --> run m-files from python.", usage="DATA/ML"),
        ModuleInstall("pg8000", "pip",
                      purpose="A Pure-Python PostgreSQL", usage="SQL"),
        ModuleInstall("PyMeta3", "pip", mname="pymeta",
                      purpose="Pattern-matching language based on OMeta for Python 3 and 2"),
        # ModuleInstall("ViTables", "pip", mname="vitables",
        #               purpose="A viewer for PyTables package"),
        ModuleInstall("pybars3", "pip",
                      purpose="Handlebars.js templating"),
        ModuleInstall("db.py", "pip", mname="db.tables",
                      purpose="db.py is an easier way to interact with your databases. It makes it easier to explore tables, columns, views, etc. " +
                      "It puts the emphasis on user interaction, information display, and providing easy to use helper functions."),
        ModuleInstall("clyent", "pip",
                      purpose="Command line client Library for windows and posix"),
        ModuleInstall("chalmers", "pip",
                      purpose="Chalmers is an application that allows its users to monitor and control a number of processes on any " +
                      "operating system (Posix and Win32 included)"),
        ModuleInstall("datashader", "github", "sdpython", usage="VIZ",
                      purpose="Datashader is a graphics pipeline system for creating meaningful representations " +
                      "of large amounts of data.") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("dnspython", "pip", usage="WEB",
                      purpose="dnspython is a DNS toolkit for Python. It supports almost all record types. It can be used for queries, " +
                      "zone transfers, and dynamic updates. It supports TSIG authenticated messages and EDNS0."),
        ModuleInstall("gdata", "pip", usage="GOOGLE",
                      purpose="Python client library for Google data APIs"),
        ModuleInstall("grin", "pip", usage="CLI",
                      purpose="A grep program configured the way I like it."),
        ModuleInstall("idna", "pip", usage="WEB",
                      purpose="A library to support the Internationalised Domain Names in Applications (IDNA) protocol as specified in RFC 5891. " +
                      "This version of the protocol is often referred to as 'IDNA2008'."),
        ModuleInstall("ldap3", "pip", usage="WEB",
                      purpose="ldap3 is a strictly RFC 4510 conforming LDAP V3 pure Python client library."),
        ModuleInstall("mpi4py", "pip",
                      purpose="MPI for Python"),
        ModuleInstall("mss", "pip", mname="mms",
                      purpose="An ultra fast cross-platform multiple screenshots module in pure python using ctypes"),
        #
        # June 2016
        #
        ModuleInstall("pyglet", "pip", usage="GUI",
                      purpose="a cross-platform windowing and multimedia library for Python"),
        ModuleInstall("geoplotlib", "pip", usage="VIZ",
                      purpose="geoplotlib is a python toolbox for visualizing geographical data and making maps"),
        ModuleInstall("leather", "pip", usage="VIZ",
                      purpose="Leather is the Python charting library for those who need charts now and don’t care if they’re perfect."),
        ModuleInstall("pythreejs", "pip", usage="VIZ",
                      purpose="A Python / ThreeJS bridge utilizing the Jupyter widget infrastructure."),
        ModuleInstall("missingno", "pip", usage="VIZ",
                      purpose="Messy datasets? Missing values? missingno provides a small toolset of flexible and easy-to-use " +
                      "missing data visualizations and utilities that allows you to get a quick visual summary of the completeness " +
                      "(or lack thereof) of your dataset."),
        ModuleInstall("vega", "pip", usage="VIZ",
                      purpose="Python/Jupyter notebook module for Vega, and Vega-Lite, Polestar, and Voyager. Notebooks " +
                      "with embedded visualizations can be viewed on github and nbviewer."),
        ModuleInstall("pydy", "pip",
                      purpose="Multibody Dynamics with Python"),
        ModuleInstall("vispy", "pip",
                      purpose="isPy: interactive scientific visualization in Python"),
        ModuleInstall("apache-libcloud", "pip", mname="libcloud",
                      purpose="A standard Python library that abstracts away differences among multiple cloud provider APIs."),
        ModuleInstall("click-plugins", "pip", mname="click_plugins",
                      purpose="An extension module for click to enable registering CLI commands via setuptools entry-points."),
        ModuleInstall("clickj", "pip",
                      purpose="Click params for commmand line interfaces to GeoJSON"),
        ModuleInstall("munch", "pip",
                      purpose="A dot-accessible dictionary (a la JavaScript objects)."),
        ModuleInstall("Fiona", "wheel", usage="GEO", mname="fiona",
                      purpose="Fiona is OGR’s neat, nimble, no-nonsense API for Python programmers."),
        ModuleInstall("brythonmagic", "pip",
                      purpose="Magics to use brython in Jupyter notebook."),
        # ModuleInstall("lmfit", "pip", purpose="Least-Squares Minimization with Bounds and Constraints", usgae="OPTIM"),
        # enable?
        #

        #
        # August, September 2016
        #
        ModuleInstall('qinfer', 'pip', usage="DATA/ML",
                      purpose="QInfer is a library using Bayesian sequential Monte Carlo for quantum parameter estimation."),
        ModuleInstall('flexx', 'pip', usage="GUI",
                      purpose="Flexx is a pure Python toolkit for creating graphical user interfaces (GUI's), " +
                      "that uses web technology for its rendering. Apps are written purely in Python; Flexx' " +
                      "transpiler generates the necessary JavaScript on the fly."),
        ModuleInstall('pypng', 'pip',
                      purpose="Pure Python PNG image encoder/decoder"),
        ModuleInstall('colormath', 'pip',
                      purpose="Color math and conversion library."),
        ModuleInstall('arrow', 'pip',
                      purpose="Better dates and times for Python"),
        ModuleInstall('toyplot', 'pip', usage="VIZ",
                      purpose="The kid-sized plotting toolkit for Python with grownup-sized goals."),
        ModuleInstall('images2gif', 'pip',
                      purpose="Create a GIF from a list of images."),
        ModuleInstall('hypothesis', 'pip',
                      purpose="Hypothesis is an advanced testing library for Python. It lets you write tests which are parametrized " +
                      "by a source of examples, and then generates simple and comprehensible examples that make your tests fail. " +
                      "This lets you find more bugs in your code with less work."),
    ]

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall('pythonnet', 'wheel',
                                 mname="clr", source="2" if sys.version_info[:2] >= (3, 5) else None,
                                 purpose="Python binding for C#"))

    return [_ for _ in mod if _ is not None]
