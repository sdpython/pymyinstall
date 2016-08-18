#-*- coding: utf-8 -*-
"""
@file
@brief Defines a set of modules for more machine learning or student projects.
"""
import sys
from ..installhelper.module_install import ModuleInstall


def ml_set():
    """
    modules introduced by students or needed for student projects
    """
    return ensae_set()


def ensae_set():
    """
    modules introduced by students or needed for student projects, it requires the modules in set *extended*
    """
    mod = [
        ModuleInstall(
            "billiard", "pip", purpose="Python multiprocessing fork with improvements and bugfixes (for celery)"),
        ModuleInstall(
            "amqp", "pip", purpose="Low-level AMQP client for Python (fork of amqplib) (for celery)"),
        ModuleInstall(
            "anyjson", "pip", purpose="Wraps the best available JSON implementation available in a common interface (for celery)"),
        ModuleInstall(
            "kombu", "pip", purpose="Messaging library for Python (for celery)"),
        ModuleInstall(
            "celery", "pip", purpose="Celery is an asynchronous task queue/job queue based on distributed message passing."),

        ModuleInstall('html2text', 'pip',
                      purpose="Turn HTML into equivalent Markdown-structured text."),
        ModuleInstall('easy-thumbnails', 'pip', mname="easy_thumbnails",
                      purpose="Easy thumbnails for Django"),
        ModuleInstall('Versio', 'pip', mname="versio",
                      purpose="localshop dependency, manages versions"),
        ModuleInstall('django', 'pip',
                      purpose="Django"),
        ModuleInstall('django-celery', 'pip', mname="djcelery",
                      purpose="localshop dependency, Old django celery integration project."),
        ModuleInstall('django-configurations', 'pip', mname="configurations",
                      purpose="localshop dependency, A helper for organizing Django settings."),
        ModuleInstall('django-environ', 'pip', mname="environ",
                      purpose="localshop dependency, Django-environ allows you to utilize 12factor " +
                      "inspired environment variables to configure your Django application."),
        ModuleInstall('django-model-utils', 'pip', mname="model_utils",
                      purpose="localshop dependency, Django model mixins and utilities."),
        ModuleInstall('django-storages', 'pip', mname="storages",
                      purpose="localshop dependency, django-storages is a collection of custom storage backends for Django."),
        ModuleInstall('django-guardian', 'pip', mname="guardian",
                      purpose="localshop dependency, Implementation of per object permissions for Django 1.2 or later."),
        ModuleInstall('django-userena', 'pip', mname="userena",
                      purpose="localshop dependency, Accounts for Django made beautifully simple"),
        ModuleInstall('django-uuidfield', 'pip', mname="uuidfield",
                      purpose="localshop dependency, UUIDField in Django"),
        ModuleInstall(
            'gunicorn', 'pip', purpose="localshop dependency, WSGI HTTP Server for UNIX"),
        ModuleInstall(
            'netaddr', 'pip', purpose="Pythonic manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses"),
        # ModuleInstall('localshop', 'pip',
        # purpose="run a local pypi server (install it in virtual env as it
        # overwrites many versions)"),

        ModuleInstall(
            "tweepy", "pip", purpose="Python wrapper for the twitter API"),
        #ModuleInstall("newspaper3k", "pip", mname="newspaper"),
        ModuleInstall(
            "mutagenx", "pip", purpose="ead and write audio tags for many formats in Python 3"),
        ModuleInstall("django-audiotracks", "pip",
                      mname="audiotracks", purpose="read audio with django"),
        ModuleInstall("Quandl", "pip", purpose="access Quandl API"),
        ModuleInstall(
            "nltk", "pip", purpose="NLP, natural language processing", usage="NLP"),
        ModuleInstall(
            "textblob", "pip", purpose="TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for " +
            "diving into common natural language processing (NLP) tasks such as part-of-speech tagging, " +
            "noun phrase extraction, sentiment analysis, classification, translation, and more."),
        ModuleInstall("dev", "pip",
                      purpose="Header files, a static library and development tools for building Python modules, " +
                      "extending the Python interpreter or embedding Python in applications."),
        ModuleInstall(
            "opencv_python", "wheel", mname="cv2", purpose="OpenVC wrapper",
            web="https://opencv-python-tutroals.readthedocs.org/en/latest/"),
        ModuleInstall("dlib", "pip",
                      purpose="A toolkit for making real world machine learning and data analysis applications"),
        ModuleInstall("PyAudio", "wheel", mname="pyaudio",
                      purpose="PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library. " +
                      "With PyAudio, you can easily use Python to play and record audio " +
                      "streams on a variety of platforms (e.g., GNU/Linux, Microsoft Windows, and Mac OS X)."),
        ModuleInstall(
            "zope.interface", "wheel", purpose="interfaces for python"),
        ModuleInstall(
            "zope.exceptions", "pip", purpose="Zope exception"),
        ModuleInstall(
            "persistent", "wheel", purpose="Objets persistants translucides"),
        # requires zope.interface, persistents
        ModuleInstall("BTrees", "wheel", usage="ALGO",
                      purpose="This package contains a set of persistent object containers built around a modified " +
                      "BTree data structure."),
        ModuleInstall(
            "datrie", "wheel", purpose="Fast, efficiently stored Trie for Python.", usage="ALGO"),
        # ModuleInstall("pysparse", "pip"), #does not work
        ModuleInstall(
            "Bottleneck", "wheel", mname="bottleneck", purpose="Fast NumPy array functions written in Cython, needed by la"),
        ModuleInstall(
            "la", "wheel",
            purpose="Label the rows, columns, any dimension, of your NumPy arrays."),
        ModuleInstall(
            "mahotas", "wheel", purpose="Mahotas: Computer Vision Library", usage="VIZ"),
        ModuleInstall("nitime", "wheel",
                      purpose="Nitime is a library for time-series analysis of data from neuroscience experiments.", usage="DATA/ML"),
        ModuleInstall("milk", "wheel",
                      purpose="machine learning toolkit", usage="DATA/ML"),
        ModuleInstall("minepy", "wheel", purpose="interface to MineCraft"),
        ModuleInstall(
            "NLopt", "wheel", mname="nlopt", purpose="linear, quadratic optimization",
            web="http://ab-initio.mit.edu/wiki/index.php/NLopt", usage="DATA/ML"),
        ModuleInstall("Pmw", "pip", mname="Pmw",
                      purpose="Pmw is a toolkit for building high-level compound widgets in Python using the Tkinter module."),
        ModuleInstall(
            "pytool", "pip", purpose="A collection of tools for Python"),
        ModuleInstall(
            "py", "pip", purpose="library with cross-python path, ini-parsing, io, code, log facilities"),
        ModuleInstall(
            "pytools", "pip", purpose="A collection of tools for Python"),
        ModuleInstall(
            "pytest", "pip", purpose="pytest allows you to use the standard python assert for verifying expectations and values in Python tests."),
        ModuleInstall("pycuda", "wheel", usage="GPU",
                      purpose="PyCUDA lets you access Nvidia's CUDA parallel computation API from Python."),
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
        ModuleInstall("PyX", "wheel", mname="pyx",
                      purpose="plotting", usage="VIZ"),
        ModuleInstall(
            "scandir", "wheel", purpose="Better directory iterator and faster os.walk(), " +
            "now in the Python 3.5 stdlib") if sys.version_info[:2] <= (3, 4) else None,
        ModuleInstall(
            "zs", "wheel", purpose="S is a compressed, read-only file format for efficiently distributing, " +
            "querying, and archiving arbitrarily large record-oriented datasets."),
        # machine learning
        ModuleInstall(
            "joblib", "pip", purpose="distribute jobs, parallelization"),
        #
        # teachings
        #
        ModuleInstall(
            "tutormagic", "pip", purpose="brings PythonTutor in a notebok", usage="TEACH"),
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
        # ModuleInstall("pyjs", "pip"), # needs manual installation
        # ModuleInstall("pyjs", "github", "pyjs"), #does not work really
        # ModuleInstall("pyjsdl", "github", "jggatc"), # no setup.py

        #
        #
        #
        # ModuleInstall("contextlib2", "pip", purpose="Backports and enhancements for the contextlib module"),
        ModuleInstall("contextlib2", "pip",
                      purpose="Backports and enhancements for the contextlib module"),
        ModuleInstall(
            "zipline", "pip",
            purpose="A backtester for financial algorithms.") if sys.version_info[:2] >= (3, 5) else None,  # finance
        ModuleInstall("vincent", "pip", purpose="plotting",
                      usage="VIZ"),  # graph
        # graph, pygal_maps_world only accepts the latest version
        #ModuleInstall("pygal", "github", "Kozea", purpose="plotting"),
        ModuleInstall(
            "pygal", "pip", "Kozea", purpose="plotting (javascript)", usage="VIZ"),
        ModuleInstall(
            "pygal_maps_world", "pip", purpose="extension to pygal (maps)", usage="VIZ"),  # graph
        ModuleInstall(
            "pygal_maps_fr", "pip", purpose="French maps for pygal", usage="VIZ"),  # graph
        ModuleInstall(
            "pygal_maps_ch", "pip", purpose="Swiss canton map for pygal", usage="VIZ"),  # graph
        ModuleInstall(
            "pygal_sphinx_directives", "pip", purpose="Pygal sphinx integration", usage="SPHINX"),  # graph
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
        #
        # pydata
        #
        ModuleInstall("CherryPy", "pip", mname="cherrypy",
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
        ModuleInstall("lifelines", "pip",
                      purpose="survival analysis", usage="OPTIM"),
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
            "tables", "wheel", purpose="PyTables is a package for managing hierarchical datasets " +
            "and designed to efficiently and easily cope with extremely large amounts of data."),
        ModuleInstall(
            "heatmap", "wheel", purpose="draw heatmap", usage="VIZ"),
        ModuleInstall("planar", "wheel",
                      purpose="2D planar geometry library for Python."),
        ModuleInstall("GDAL", "wheel", mname="osgeo",
                      purpose="GDAL is a translator library for raster and vector geospatial data formats that is released under an X/MIT style " +
                      "Open Source license by the Open Source Geospatial Foundation."),
        # ModuleInstall("rasterio", "wheel",
        # purpose="Fast and direct raster I/O for use with Numpy and SciPy,
        # Rasterio reads and writes geospatial raster datasets."),
        ModuleInstall("cgal_bindings", "wheel", mname="CGAL",
                      purpose="The CGAL Bindings project allows to use some packages of CGAL, the Computational Algorithms Library, " +
                      "in languages other than C++, as for example Java and Python.",
                      web="https://github.com/cgal/cgal-swig-bindings") if sys.version_info[:2] <= (3, 4) else None,
        ModuleInstall("tifffile", "wheel",
                      purpose="Read and write image data from and to TIFF files. (for pims)"),
        ModuleInstall("slicerator", "pip",
                      purpose="A lazy-loading, fancy-sliceable iterable."),
        ModuleInstall("PIMS", "pip", mname="pims",
                      purpose="Python Image Sequence (for trackpy)"),
        ModuleInstall("trackpy", "pip",
                      purpose="trackpy is a Python package for particle tracking in 2D, 3D, and higher dimensions.", usage="DATA/ML"),
        ModuleInstall("triangle", "wheel",
                      purpose="Python Triangle is a python wrapper around Jonathan Richard Shewchuk's " +
                      "two-dimensional quality mesh generator and delaunay triangulator library."),
        ModuleInstall("redis", "pip",
                      purpose="Python client for Redis key-value store"),
        # this module is not on pypi and the py3k version is in a separate folder
        # i don't want to write too much specific code for it
        # i compile it into a wheel
        ModuleInstall("skdata", "wheel2",
                      purpose="Data Sets for Machine Learning in Python", usage="DATA"),
        ModuleInstall("hebel", "pip",
                      purpose="GPU-Accelerated Deep Learning Library in Python", usage="DATA/ML"),
        # ModuleInstall("vowpal_porpoise", "pip",
        #              purpose="Lightweight python wrapper for vowpal_wabbit.", purpose="DATA/ML"),
        # it requires to build vowpal_wabbit for Windows
        # ModuleInstall("ua-parser", "pip", mname="ua_parser",
        #              purpose="Python port of Browserscope's user agent parser"),
        # ModuleInstall("user-agents", "pip", mname="user_agents",
        # purpose="A library to identify devices (phones, tablets) and their
        # capabilities by parsing (browser/HTTP) user agent strings"),
        ModuleInstall("user-agent", "pip", mname="user_agent",
                      purpose="A library to identify devices (phones, tablets) and their capabilities by parsing (browser/HTTP) user agent strings"),
        ModuleInstall("tinydb", "pip",
                      purpose="TinyDB is a tiny, document oriented database optimized for your happiness :) " +
                      "It's written in pure Python and has no external requirements.", usage="noSQL"),
        ModuleInstall("urllib3", "pip",
                      purpose="urllib2 extension"),
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
        ModuleInstall("cssselect", "pip",
                      purpose="cssselect parses CSS3 Selectors and translates them to XPath 1.0"),
        ModuleInstall("jieba", "pip",
                      purpose="Chinese Words Segementation Utilities"),
        # goose still depends on BeautifulSoup which does not work on Python 3
        # ModuleInstall("goose-extractor", "pip", mname="goose",
        # purpose="Html Content / Article Extractor, web scrapping lib in
        # Python"),
        ModuleInstall("untangle", "pip",
                      purpose="Converts XML to Python objects"),
        # promising but not released yet
        # ModuleInstall("code2flow", "pip",
        # purpose="Turn your Python and Javascript code into DOT flowcharts"),

        # biokit
        ModuleInstall("wrapt", "wheel",
                      purpose="A Python module for decorators, wrappers and monkey patching."),
        ModuleInstall("colormap", "pip", usage="VIZ",
                      purpose="Utilities to ease manipulation of matplotlib colormaps and color codecs (e.g., hex2rgb)"),
        ModuleInstall("easydev", "pip",
                      purpose="Common utilities to ease the development of Python packages"),
        ModuleInstall("suds-jurko", "pip", mname="suds",
                      purpose="Lightweight SOAP client (Jurko's fork)"),
        # bugged and still uses ordereddict
        # ModuleInstall("bioservices", "pip",
        #              purpose="Access to Biological Web Services from Python"),
        # ModuleInstall("biokit", "github", "biokit", usage="VIZ",
        # purpose="Access to Biological Web Services from Python"),

        #
        #
        #
        ModuleInstall("lz4", "wheel",
                      purpose="LZ4 Bindings for Python (for dpark)"),
        ModuleInstall("fabric", "pip",
                      purpose="Fabric is a Python library and command-line tool for streamlining " +
                      "the use of SSH for application deployment or systems administration tasks."),
        ModuleInstall("invoke", "pip",
                      purpose="Invoke is a Python task execution tool & library, drawing inspiration " +
                      "from various sources to arrive at a powerful & clean feature set."),
        ModuleInstall("msgpack-python", "pip", mname="msgpack",
                      purpose="MessagePack (de)serializer."),
        ModuleInstall("cymem", "pip",
                      purpose="Manage calls to calloc/free through Cython") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("murmurhash", "pip",
                      purpose="Cython .pxd files for some of the MurmurHash 2 and 3 hash functions, with a slightly more Pythonic API. " +
                      "The only access to these functions is via Cython — I don’t see why they should be " +
                      "useful from pure Python.") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("preshed", "pip",
                      purpose="Cython hash table that trusts the keys are pre-hashed") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("text-unidecode", "pip", mname="text_unidecode",
                      purpose="The most basic Text::Unidecode port") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("thinc", "pip", usage="OPTIM",
                      purpose="Learn sparse linear models") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("spacy", "pip", usage="NLP",
                      purpose="Industrial-strength NLP") if sys.version_info[:2] >= (3, 5) else None,

        #
        #  2015-12
        #
        ModuleInstall("picklable-itertools", "pip", mname="picklable_itertools",
                      purpose="A reimplementation of the Python standard library's itertools, in Python, using picklable iterator objects. (fuel)"),
        ModuleInstall("progressbar2", "pip", usage="VIZ",
                      purpose="Text progress bar library for Python. (fuel)"),
        ModuleInstall("fuel", "pip", usage="DATA/VIZ",
                      purpose="Fuel is a data pipeline framework which provides your machine learning models with the data they need."),
        ModuleInstall("Lasagne", "pip", mname="lasagne", usage="DEEP LEARNING",
                      purpose="Lasagne is a lightweight library to build and train neural networks in Theano."),
        ModuleInstall("blocks", "github", "mila-udem",
                      purpose="Blocks is a framework that helps you build neural network models on top of Theano."),
        ModuleInstall("gatspy", "pip",
                      purpose="General tools for Astronomical Time Series in Python"),
        ModuleInstall("supersmoother", "pip",
                      purpose="This is an efficient implementation of Friedman's SuperSmoother [1] algorithm in pure Python. " +
                      "It makes use of numpy for fast numerical computation."),

        #
        # 2016-03
        #
        ModuleInstall("prettytable", "pip",
                      purpose="A simple Python library for easily displaying tabular data in a visually appealing ASCII table format. (for streamparse)"),
        ModuleInstall("ruamel.yaml", "pip",
                      purpose="uamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order"),
        ModuleInstall("skll", "pip", usage="ML",
                      purpose="SciKit-Learn Laboratory makes it easier to run machinelearning experiments with scikit-learn."),
        ModuleInstall("sklearn_pandas", "pip", usage="ML",
                      purpose="This module provides a bridge between Scikit-Learn's machine learning methods and pandas-style Data Frames."),
        ModuleInstall("ad3", "wheel", source="2", usage="ML",
                      purpose="AD3 (approximate MAP decoder with Alternating Direction Dual Decomposition)"),
        ModuleInstall("pystruct", "wheel", usage="ML", source="2",
                      purpose="Learning Structured Prediction in Python"),
        ModuleInstall("py-earth", "wheel", mname="pyearth", usage="ML", source="2",
                      purpose="A Python implementation of Jerome Friedman's Multivariate Adaptive Regression Splines algorithm, in the style of scikit-learn."),
        ModuleInstall("seqlearn", "wheel", usage="ML",
                      purpose="sequence classification toolkit for Python"),
        ModuleInstall("hmmlearn", "wheel", usage="ML",
                      purpose="Hidden Markov Models in Python, with scikit-learn like API"),
        ModuleInstall("gplearn", "pip", usage="ML",
                      purpose="gplearn implements Genetic Programming in Python, with a scikit-learn inspired and compatible API."),
        ModuleInstall("gdbn", "pip", usage="ML",
                      purpose="This package contains python code for pre-trained deep neural networks"),
        ModuleInstall("gnumpy", "pip",
                      purpose="Gnumpy: an easy way to use GPU boards in Python"),
        ModuleInstall("nolearn", "pip", usage="ML",
                      purpose="nolearn contains a number of wrappers and abstractions " +
                      "around existing neural network libraries, most notably Lasagne, along with a " +
                      "few machine learning utility modules. All code is written to be compatible with scikit-learn."),
        ModuleInstall("mlxtend", "pip", usage="ML",
                      purpose="A library consisting of useful tools and extensions for the day-to-day data science tasks."),
        ModuleInstall("sacred", "pip", usage="ML",
                      purpose="Facilitates automated and reproducible experimental research"),
        ModuleInstall("astropy", "wheel",
                      purpose="Community-developed python astronomy tools"),
        # h2o
        ModuleInstall("future", "pip",
                      purpose="Clean single-source support for Python 3 and 2 (h2o)"),
        ModuleInstall("h2o", "pip", usage="ML",
                      purpose="H2O, Fast Scalable Machine Learning, for python"),
        #
        # June 2016
        #
        ModuleInstall("kabuki", "pip", usage="ML",
                      purpose="kabuki is a python toolbox that allows easy creation of hierarchical bayesian models for the cognitive sciences."),
        ModuleInstall("HDDM", "wheel", mname="hddm", usage="ML",
                      purpose="HDDM is a python module that implements Hierarchical Bayesian estimation of Drift Diffusion Models."),
        ModuleInstall("reportlab", "wheel",
                      purpose="This is the ReportLab PDF Toolkit. It allows rapid creation of rich PDF documents, and also creation of " +
                      "charts in a variety of bitmap and vector formats."),
        ModuleInstall("biopython", "wheel", mname="Bio", usage="BIO",
                      purpose="The Biopython Project is an international association of developers of freely available Python tools for " +
                      "computational molecular biology."),
        ModuleInstall("grako", "wheel",
                      purpose="Grako (for grammar compiler) is a tool that takes grammars in a variation of EBNF " +
                      "as input, and outputs memoizing (Packrat) PEG parsers in Python."),
        ModuleInstall("expressions", "pip",
                      purpose="Arithmetic expression parser library. Embed customized expression evaluation into your application or library."),
        ModuleInstall("cubes", "pip",
                      purpose="Cubes is a light-weight Python framework and set of tools for development of reporting and analytical applications, " +
                      "Online Analytical Processing (OLAP), multidimensional analysis and browsing of aggregated data. It is part of Data Brewery."),
        ModuleInstall("MDP", "pip", usage="ML",
                      purpose="Python data processing framework."),
        ModuleInstall("pyamg", "wheel", usage="OPTIM",
                      purpose="PyAMG is a library of Algebraic Multigrid (AMG) solvers with a convenient Python interface."),
        ModuleInstall("pysal", "pip", usage="MATHS",
                      purpose="PySAL is an open source library of spatial analysis functions written in Python intended " +
                      "to support the development of high level applications."),
        #
        # July 2016
        #
        ModuleInstall("hyperopt", "github", "hyperopt", usage="ML",
                      purpose="Hyperopt is a Python library for serial and parallel optimization over awkwardsearch spaces, " +
                      "which may include real-valued, discrete, and conditional dimensions."),
        ModuleInstall("mlxtend", "pip", usage="ML",
                      purpose="Mlxtend (machine learning extensions) " +
                      "is a Python library of useful tools for the day-to-day data science tasks."),
        #
        # August 2016
        #
        ModuleInstall('pydispatcher', 'pip',
                      purpose="Multi-producer-multi-consumer signal dispatching mechanism"),
        ModuleInstall('twisted', 'pip',
                      purpose="An asynchronous networking framework written in Python"),
        ModuleInstall('attrs', 'pip',
                      purpose="Attributes without boilerplate."),
        ModuleInstall('parsel', 'pip',
                      purpose="Parsel is a library to extract data from HTML and XML using XPath and CSS selectors."),
        ModuleInstall('pyasn1-modules', 'pip', mname="pyasn1_modules",
                      purpose="A collection of ASN.1-based protocols modules."),
        ModuleInstall('service_identity', 'pip',
                      purpose="Service identity verification for pyOpenSSL."),
        ModuleInstall("scrapy", "pip", usage="ML",
                      purpose="A high-level Web Crawling and Web Scraping framework"),

        #
        # 2015-08-11
        #
        ModuleInstall("sklearn_contrib_lightning", "wheel", mname="lightning", usage="ML",
                      purpose="large-scale linear classification, regression and ranking"),
        ModuleInstall("imbalanced-learn", "github", "scikit-learn-contrib",
                      mname="imblearn", usage="ML",
                      purpose="imbalanced-learn is a python package offering a number of re-sampling " +
                      "techniques commonly used in datasets showing strong between-class imbalance. " +
                      "It is compatible with scikit-learn and is part of scikit-learn-contrib projects."),
        ModuleInstall("forest-confidence-interval", "github", "scikit-learn-contrib",
                      mname="forestci", usage="ML",
                      purpose="Python module for calculating variance and adding confidence intervals to scikit-learn random forest regression " +
                      "or classification objects. The core functions calculate an in-bag and error bars for random forest objects"),
        ModuleInstall("py_earth", "wheel", source="2", mname="pyearth", usage="ML",
                      purpose="A Python implementation of Jerome Friedman's Multivariate Adaptive Regression Splines algorithm, in the style of " +
                      "scikit-learn. The py-earth package implements Multivariate Adaptive Regression Splines using Cython and provides an " +
                      "interface that is compatible with scikit-learn's Estimator, Predictor, Transformer, and Model interfaces. For more " +
                      "information about Multivariate Adaptive Regression Splines, see the references below."),
        ModuleInstall("polylearn", "wheel", source="2", usage="ML",
                      purpose="A library for factorization machines and polynomial networks for classification and regression in Python."),
        #
        # 2015-08-18: weidelin.core
        #
        ModuleInstall("lda", "pip", usage="ML",
                      purpose="lda implements latent Dirichlet allocation (LDA) using collapsed Gibbs sampling."),
        #
        # 2015-08-18: weidelin.core
        #
        ModuleInstall("ZConfig", "pip",
                      purpose="Structured Configuration Library"),
        ModuleInstall("transaction", "pip",
                      purpose="Transaction management for Python. " +
                      "This package contains a generic transaction implementation for Python. It is mainly used by the ZODB."),
        ModuleInstall("zc.lockfile", "pip",
                      purpose="Basic inter-process locks"),
        ModuleInstall("zodbpickle", "wheel",
                      purpose="This package presents a uniform pickling interface for ZODB."),
        ModuleInstall("ZODB", "pip",
                      purpose="The Zope Object Database provides an object-oriented database for Python that provides a high-degree of transparency."),
        ModuleInstall("zdaemon", "pip",
                      purpose="Daemon process control library and tools for Unix-based systems"),
        ModuleInstall("ZEO", "pip",
                      purpose="ZEO provides a client-server storage implementation for ZODB."),
        ModuleInstall("ZODB3", "pip",
                      purpose="ZODB3 - Meta release for ZODB, persistent, BTrees and ZEO"),
        ModuleInstall("weidelin.core", "wheel", source="2",
                      purpose="Out-of-core NumPy arrays. " +
                      "Wendelin.core allows you to work with arrays bigger than RAM and local disk. Bigarrays are persisted to storage, " +
                      "and can be changed in transactional manner."),
    ]

    if sys.version_info[0] == 2:
        mod.extend([
            # (for dpark)"),
            ModuleInstall("mesos.interface", "pip",
                          purpose="Mesos interfaces (for dpark)"),
            ModuleInstall("pymesos", "pip",
                          purpose="Mesos interfaces (for dpark)"),
            ModuleInstall("streamparse", "pip",
                          purpose="Streamparse lets you run Python code against real-time streams of data via Apache Storm."),
            # ModuleInstall("dpark", "wheel2",
            # purpose="DPark is a Python clone of Spark, MapReduce(R) alike
            # computing framework supporting iterative computation., see
            # https://github.com/douban/dpark", usage="DATA/ML"),
        ])

    if sys.platform.startswith("win"):
        ModuleInstall(
            "xlwings", "pip", purpose="reads/writes Excel files", usage="WINDOWS") if sys.platform.startswith("win") else None,
        mod.append(ModuleInstall("VideoCapture", "wheel",
                                 purpose="A Win32 Python Extension for Accessing Video Devices", usage="VIDEO"))
        mod.append(ModuleInstall("comtypes", "pip",
                                 purpose="Pure Python COM package"))
        mod.append(ModuleInstall("jaraco.structures", "pip",
                                 purpose="jaraco.structures"))
        mod.append(ModuleInstall("jaraco.util", "pip",
                                 purpose="General utility modules that supply commonly-used functionality"))
        mod.append(ModuleInstall("jaraco.video", "pip",
                                 purpose="jaraco.video implements a framegrabber inteface for Windows Video Capture devices.", usage="VIDEO"))

    for name in ['azure-nspkg', 'azure-common', 'azure-mgmt-nspkg', 'azure-mgmt-authorization',
                 'azure-mgmt-batch', 'azure-mgmt-cdn', 'azure-mgmt-cognitiveservices', 'azure-mgmt-commerce',
                 'azure-mgmt-compute', 'azure-mgmt-logic', 'azure-mgmt-graphrbac', 'azure-mgmt-network',
                 'azure-mgmt-notificationhubs', 'azure-mgmt-powerbiembedded', 'azure-mgmt-redis',
                 'azure-mgmt-resource', 'azure-mgmt-scheduler', 'azure-mgmt-storage',
                 'azure-mgmt-web', 'azure-graphrbac', 'azure-batch', 'azure-servicebus',
                 'azure-servicemanagement-legacy', 'azure']:
        # azure part
        m = ModuleInstall(
            name, "pip", pip_options=["--pre"],
            purpose="Python wrapper for Azure API (HDInsight, Blog Storage)", usage="AZURE")
        mod.append(m)

    return [_ for _ in mod if _ is not None]
