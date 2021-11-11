# -*- coding: utf-8 -*-
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
            "vine", "pip", purpose="Promises, promises, promises"),
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
                      purpose="localshop dependency, Django-environ allows you to utilize 12factor "
                      + "inspired environment variables to configure your Django application."),
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
        ModuleInstall("grappelli_safe", "pip", usage="WEB",
                      purpose="A snapshot of the grappelli_2 branch of django-grappelli, packaged as a dependency "
                      + "for the Mezzanine CMS for Django."),
        ModuleInstall("filebrowser_safe", "pip", usage="WEB",
                      purpose="A snapshot of the filebrowser_3 branch of django-filebrowser, packaged as a "
                      + "dependency for the Mezzanine CMS for Django."),
        ModuleInstall("django-contrib-comments", "pip", usage="WEB", mname="django_comments",
                      purpose="Django used to include a comments framework; since Django 1.6 it’s "
                      + "been separated to a separate project. This is that project."),
        ModuleInstall("mezzanine", "pip", usage="WEB",
                      purpose="Mezzanine is a powerful, consistent, and flexible content management platform."),
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
            "mutagen", "pip", purpose="read and write audio tags for many formats in Python 3"),
        ModuleInstall(
            "mutagenx", "pip", purpose="read and write audio tags for many formats in Python 3"),
        ModuleInstall("django-audiotracks", "pip",
                      mname="audiotracks", purpose="read audio with django"),
        ModuleInstall("ndg-httpsclient", "pip", mname="ndg.httpsclient",
                      purpose="Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL"),
        ModuleInstall("inflection", "pip",
                      purpose="A port of Ruby on Rails inflector to Python"),
        ModuleInstall("more-itertools", "pip",
                      mname="more_itertools",
                      purpose="More routines for operating on iterables, beyond itertools"),
        ModuleInstall("Quandl", "pip", mname="quandl",
                      purpose="access Quandl API"),
        ModuleInstall("singledispatch", "pip", purpose="for nltk"),
        ModuleInstall(
            "nltk", "pip", purpose="NLP, natural language processing", usage="NLP"),
        ModuleInstall(
            "textblob", "pip", purpose="TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for "
            + "diving into common natural language processing (NLP) tasks such as part-of-speech tagging, "
            + "noun phrase extraction, sentiment analysis, classification, translation, and more."),
        ModuleInstall(
            "opencv_python", "wheel", mname="cv2", purpose="OpenVC wrapper",
            web="https://opencv-python-tutroals.readthedocs.org/en/latest/"),
        ModuleInstall("dlib", "pip" if sys.version_info[:2] >= (3, 6) else "wheel",
                      source="2" if sys.version_info[:2] >= (3, 6) else None,
                      usage="ML",
                      purpose="A toolkit for making real world machine learning and data analysis applications"),
        ModuleInstall("PyAudio", "wheel", mname="pyaudio",
                      purpose="PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library. "
                      + "With PyAudio, you can easily use Python to play and record audio "
                      + "streams on a variety of platforms (e.g., GNU/Linux, Microsoft Windows, and Mac OS X)."),
        ModuleInstall(
            "zope.interface", "wheel", purpose="interfaces for python"),
        ModuleInstall(
            "zope.exceptions", "pip", purpose="Zope exception"),
        ModuleInstall(
            "persistent", "wheel", purpose="Objets persistants translucides"),
        # requires zope.interface, persistents
        ModuleInstall("BTrees", "wheel", usage="ALGO",
                      purpose="This package contains a set of persistent object containers built around a modified "
                      + "BTree data structure."),
        ModuleInstall(
            "datrie", "wheel", purpose="Fast, efficiently stored Trie for Python.", usage="ALGO"),
        # ModuleInstall("pysparse", "pip"), #does not work
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
        ModuleInstall("Pmw", "pip",
                      purpose="Pmw is a toolkit for building high-level compound widgets in Python using the Tkinter module."),
        ModuleInstall(
            "pytool", "pip", purpose="A collection of tools for Python"),
        ModuleInstall(
            "pytools", "pip", purpose="A collection of tools for Python"),
        ModuleInstall("pycuda", "wheel", usage="GPU",
                      purpose="PyCUDA lets you access Nvidia's CUDA parallel computation API from Python."),
        ModuleInstall("pyopencl", "wheel", usage="GPU",
                      purpose="PyOpenCL lets you access the OpenCL parallel computation API from Python."),
        # ModuleInstall("scikits.cuda", "pip", mname="skcuda"), # no stable
        # version
        ModuleInstall(
            "pylzma", "wheel2", purpose="Python bindings for the LZMA library by Igor Pavlov."),
        ModuleInstall("nibabel", "pip",
                      purpose="Access a multitude of neuroimaging data formats."),
        ModuleInstall(
            "pyodbc", "wheel", purpose="access to protocal ODBC (SQL databases)", usage="SQL"),
        ModuleInstall(
            "pypmc", "wheel", purpose="pypmc is a python package focusing on adaptive importance sampling."),
        ModuleInstall("PyX", "wheel", mname="pyx",
                      purpose="plotting", usage="VIZ"),
        ModuleInstall(
            "scandir", "wheel", purpose="Better directory iterator and faster os.walk(), "
            + "now in the Python 3.5 stdlib") if sys.version_info[:2] <= (3, 4) else None,
        ModuleInstall(
            "backports.lzma", "wheel", purpose="Backport of Python 3.3's 'lzma' module for XZ/LZMA compressed files."),
        ModuleInstall(
            "zs", "wheel", purpose="S is a compressed, read-only file format for efficiently distributing, "
            + "querying, and archiving arbitrarily large record-oriented datasets."),
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
        ModuleInstall(
            "nuitka", "pip", usage="C++", purpose="C++ compilation, code optimization"),
        # ModuleInstall("tri", "pip", purpose="Delaunay triangulation"), # only
        # works on Python 2.7
        ModuleInstall(
            "blosc", "wheel", purpose="Blosc (http://blosc.org) is a high performance compressor optimized for binary data."),
        ModuleInstall(
            "tables", "wheel", purpose="PyTables is a package for managing hierarchical datasets "
            + "and designed to efficiently and easily cope with extremely large amounts of data."),
        ModuleInstall("contextlib2", "pip",
                      purpose="Backports and enhancements for the contextlib module"),
        ModuleInstall(
            "sortedcontainers", "pip",
            purpose="Python Sorted Container Types: SortedList, SortedDict, and SortedSet"),
        ModuleInstall("python-editor", "pip", mname="python_editor",
                      purpose="Programmatically open an editor, capture the result."),
        ModuleInstall(
            "alembic", "pip",
            purpose="A database migration tool for SQLAlchemy."),
        ModuleInstall(
            "intervaltree", "pip",
            purpose="Editable interval tree data structure for Python 2 and 3"),
        ModuleInstall(
            "cachetools", "pip",
            purpose="Extensible memoizing collections and decorators"),
        ModuleInstall(
            "empyrical", "pip",
            purpose="empyrical is a Python library with performance and risk statistics commonly used in quantitative finance"),
        ModuleInstall(
            "lru_dict", "pip", purpose="An Dict like LRU container."),
        ModuleInstall(
            "zipline", "wheel",
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
        ModuleInstall("jaraco.functools", "pip",
                      purpose="Additional functools in the spirit of stdlib’s functools."),
        ModuleInstall("tempora", "pip",
                      purpose="Objects and routines pertaining to date and time (tempora)"),
        ModuleInstall("portend", "pip",
                      purpose="TCP port monitoring utilities"),
        ModuleInstall("cheroot", "pip",
                      purpose="Highly-optimized, pure-python HTTP server"),
        ModuleInstall("CherryPy", "pip", mname="cherrypy",
                      purpose="create web application, needed by Spyre"),
        ModuleInstall("dataspyre", "pip", mname="spyre",
                      purpose="create simple web application to visualize data", usage="VIZ"),
        # ModuleInstall("python-recsys", "github", "ocelma", mname="recsys",
        # purpose="recommendation system", usage="DATA/ML"), #only works on
        # Python 2.7 + csc-pysparse + dividi2 (not maintained anymore)
        ModuleInstall(
            "colorspacious", "pip", purpose="A powerful, accurate, and easy-to-use Python library for doing "
            + "colorspace conversions (for viscm)"),
        ModuleInstall(
            "viscm", "pip", purpose="tool for analyzing colormaps and creating new colormaps."),
        # ModuleInstall("cubehelix", "github", "jradavenport",
        #               purpose="a full implementation of Dave Green's cubehelix colormap for Python",
        #              web="https://github.com/jradavenport/cubehelix"),
        ModuleInstall("lifelines", "pip",
                      purpose="survival analysis", usage="OPTIM"),
        # ModuleInstall("pysnptools", "pip", purpose="operation on DNA sequences"), # only available on Python 2.7
        #
        # 2015-07
        #
        ModuleInstall(
            "heatmap", "wheel", purpose="draw heatmap", usage="VIZ"),
        ModuleInstall("planar", "wheel",
                      purpose="2D planar geometry library for Python."),
        ModuleInstall("GDAL", "wheel", mname="osgeo",
                      purpose="GDAL is a translator library for raster and vector geospatial data formats "
                      + "that is released under an X/MIT style "
                      + "Open Source license by the Open Source Geospatial Foundation."),
        # ModuleInstall("rasterio", "wheel",
        # purpose="Fast and direct raster I/O for use with Numpy and SciPy,
        # Rasterio reads and writes geospatial raster datasets."),
        ModuleInstall("cgal_bindings", "wheel", mname="CGAL",
                      purpose="The CGAL Bindings project allows to use some packages of CGAL, the Computational Algorithms Library, "
                      + "in languages other than C++, as for example Java and Python.",
                      web="https://github.com/cgal/cgal-swig-bindings") if sys.version_info[:2] <= (3, 4) else None,
        ModuleInstall("slicerator", "pip",
                      purpose="A lazy-loading, fancy-sliceable iterable."),
        ModuleInstall("PIMS", "pip", mname="pims",
                      purpose="Python Image Sequence (for trackpy)"),
        ModuleInstall("trackpy", "pip",
                      purpose="trackpy is a Python package for particle tracking in 2D, 3D, and higher dimensions.", usage="DATA/ML"),
        ModuleInstall("triangle", "wheel",
                      purpose="Python Triangle is a python wrapper around Jonathan Richard Shewchuk's "
                      + "two-dimensional quality mesh generator and delaunay triangulator library."),
        ModuleInstall("redis", "pip",
                      purpose="Python client for Redis key-value store"),
        # ModuleInstall("vowpal_porpoise", "pip",
        #              purpose="Lightweight python wrapper for vowpal_wabbit.", purpose="DATA/ML"),
        # it requires to build vowpal_wabbit for Windows
        # ModuleInstall("ua-parser", "pip", mname="ua_parser",
        #              purpose="Python port of Browserscope's user agent parser"),
        # ModuleInstall("user-agents", "pip", mname="user_agents",
        # purpose="A library to identify devices (phones, tablets) and their
        # capabilities by parsing (browser/HTTP) user agent strings"),
        ModuleInstall("user-agent", "pip", mname="user_agent",
                      purpose="A library to identify devices (phones, tablets) and their capabilities by "
                      + "parsing (browser/HTTP) user agent strings"),
        ModuleInstall("tinydb", "pip",
                      purpose="TinyDB is a tiny, document oriented database optimized for your happiness :) "
                      + "It's written in pure Python and has no external requirements.", usage="noSQL"),
        ModuleInstall("gevent", "pip",
                      purpose="gevent is a coroutine-based Python networking library"),
        ModuleInstall("grequests", "pip",
                      purpose="GRequests allows you to use Requests with Gevent to make asynchronous HTTP Requests easily."),
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
        ModuleInstall('colorlog', 'pip',
                      purpose="Log formatting with colors!"),
        ModuleInstall("easydev", "pip",
                      purpose="Common utilities to ease the development of Python packages"),
        ModuleInstall("colormap", "pip", usage="VIZ",
                      purpose="Utilities to ease manipulation of matplotlib colormaps and color codecs (e.g., hex2rgb)"),
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
        ModuleInstall("linecache2", "pip",
                      purpose="A backport of linecache to older supported Pythons."),
        ModuleInstall("traceback2", "pip",
                      purpose="traceback2 is a backport of the new features added to the traceback "
                      + "testing framework in Python 2.7 and onwards."),
        ModuleInstall("unittest2", "pip",
                      purpose="unittest2 is a backport of the new features added to the unittest "
                      + "testing framework in Python 2.7 and onwards."),
        ModuleInstall("deprecation", "pip",
                      purpose="A library to handle automated deprecations"),
        ModuleInstall("lz4", "wheel",
                      purpose="LZ4 Bindings for Python (for dpark)"),
        ModuleInstall("fabric", "pip",
                      purpose="Fabric is a Python library and command-line tool for streamlining "
                      + "the use of SSH for application deployment or systems administration tasks."),
        ModuleInstall("invoke", "pip",
                      purpose="Invoke is a Python task execution tool & library, drawing inspiration "
                      + "from various sources to arrive at a powerful & clean feature set."),
        # ModuleInstall("msgpack", "wheel",
        #               purpose="MessagePack (de)serializer."),
        ModuleInstall("msgpack", "wheel",
                      purpose="MessagePack (de)serializer."),
        ModuleInstall("cymem", "pip",
                      purpose="Manage calls to calloc/free through Cython") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("murmurhash", "pip",
                      purpose="Cython .pxd files for some of the MurmurHash 2 and 3 hash functions, with a slightly more Pythonic API. "
                      + "The only access to these functions is via Cython — I don’t see why they should be "
                      + "useful from pure Python.") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("preshed", "wheel",
                      purpose="Cython hash table that trusts the keys are pre-hashed") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("text-unidecode", "pip", mname="text_unidecode",
                      purpose="The most basic Text::Unidecode port") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("termcolor", "pip",
                      purpose="ANSII Color formatting for output in terminal."),
        ModuleInstall("msgpack-numpy", "pip", mname="msgpack_numpy",
                      purpose="Numpy data serialization using msgpack"),
        ModuleInstall("thinc", "wheel", usage="OPTIM",
                      purpose="Practical Machine Learning for NLP. Thinc is the machine learning "
                      + "library powering spaCy.") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("semver", "pip",
                      purpose="Python helper for Semantic Versioning (http://semver.org/)"),
        ModuleInstall("sputnik", "pip",
                      purpose="Data package manager library") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("ftfy", "pip",
                      purpose="Fixes some problems with Unicode text after the fact"),
        ModuleInstall("regex", "wheel",
                      purpose="Alternative regular expression module, to replace re."),
        ModuleInstall("spacy", "wheel", usage="NLP",
                      purpose="Industrial-strength NLP") if sys.version_info[:2] >= (3, 5) else None,
        ModuleInstall("fr_core_news_sm", "wheel2", usage="NLP",
                      purpose="French ressources for spacy") if sys.version_info[:2] >= (3, 5) else None,

        #
        #  2015-12
        #
        ModuleInstall("picklable-itertools", "pip", mname="picklable_itertools",
                      purpose="A reimplementation of the Python standard library's itertools, in Python, "
                      + "using picklable iterator objects. (fuel)"),
        ModuleInstall("python-utils", "pip", mname="python_utils",
                      purpose="Python Utils is a module with some convenient utilities not included with the standard Python install"),
        ModuleInstall("progressbar2", "pip", usage="VIZ",
                      purpose="Text progress bar library for Python. (fuel)"),
        ModuleInstall("gatspy", "pip",
                      purpose="General tools for Astronomical Time Series in Python"),
        ModuleInstall("supersmoother", "pip",
                      purpose="This is an efficient implementation of Friedman's SuperSmoother [1] algorithm in pure Python. "
                      + "It makes use of numpy for fast numerical computation."),

        #
        # 2016-03
        #
        ModuleInstall("PTable", "pip", mname="prettytable",
                      purpose="A simple Python library for easily displaying tabular data in a visually "
                      + "appealing ASCII table format. (for streamparse)"),
        ModuleInstall("ruamel.yaml", "pip",
                      purpose="ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, "
                      + "seq/map flow style, and map key order"),
        ModuleInstall("logutils", "pip",
                      purpose="Logging utilities"),
        ModuleInstall("skll", "pip", usage="ML",
                      purpose="SciKit-Learn Laboratory makes it easier to run machinelearning experiments with scikit-learn."),
        ModuleInstall("sklearn_pandas", "pip", usage="ML",
                      purpose="This module provides a bridge between Scikit-Learn's machine learning methods and pandas-style Data Frames."),
        ModuleInstall("ad3", "wheel", source="2", usage="ML",
                      purpose="AD3 (approximate MAP decoder with Alternating Direction Dual Decomposition)"),
        ModuleInstall("pystruct", "wheel", usage="ML", source="2",
                      purpose="Learning Structured Prediction in Python"),
        ModuleInstall("sklearn_contrib_py_earth", "wheel", mname="pyearth", usage="ML", source="2",
                      purpose="A Python implementation of Jerome Friedman's Multivariate Adaptive Regression "
                      + "Splines algorithm, in the style of "
                      + "scikit-learn. The py-earth package implements Multivariate Adaptive Regression Splines using Cython and provides an "
                      + "interface that is compatible with scikit-learn's Estimator, Predictor, Transformer, and Model interfaces. For more "
                      + "information about Multivariate Adaptive Regression Splines, see the references below."),
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
        ModuleInstall("mlxtend", "pip", usage="ML",
                      purpose="A library consisting of useful tools and extensions for the day-to-day data science tasks."),
        ModuleInstall("jsonpickle", "pip",
                      purpose="Python library for serializing any arbitrary object graph into JSON."),
        ModuleInstall("py-cpuinfo", "pip", mname="py_cpuinfo",
                      purpose="Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work without "
                      + "any extra programs or libraries, beyond what your OS provides. It does not "
                      + "require any compilation(C/C++, assembly, et cetera) to use. It works with Python 2 and 3."),
        ModuleInstall("sacred", "pip", usage="ML",
                      purpose="Facilitates automated and reproducible experimental research"),
        ModuleInstall("astropy", "wheel",
                      purpose="Community-developed python astronomy tools"),
        # h2o
        ModuleInstall("h2o", "pip", usage="ML",
                      purpose="H2O, Fast Scalable Machine Learning, for python"),
        #
        # June 2016
        #
        ModuleInstall("kabuki", "pip", usage="ML",
                      purpose="kabuki is a python toolbox that allows easy creation of hierarchical bayesian "
                      + "models for the cognitive sciences."),
        ModuleInstall("HDDM", "wheel", mname="hddm", usage="ML",
                      purpose="HDDM is a python module that implements Hierarchical Bayesian estimation of Drift Diffusion Models."),
        ModuleInstall("reportlab", "wheel",
                      purpose="This is the ReportLab PDF Toolkit. It allows rapid creation of rich PDF documents, and also creation of "
                      + "charts in a variety of bitmap and vector formats."),
        ModuleInstall("biopython", "wheel", mname="Bio", usage="BIO",
                      purpose="The Biopython Project is an international association of developers of freely available Python tools for "
                      + "computational molecular biology."),
        ModuleInstall("grako", "wheel",
                      purpose="Grako (for grammar compiler) is a tool that takes grammars in a variation of EBNF "
                      + "as input, and outputs memoizing (Packrat) PEG parsers in Python."),
        ModuleInstall("expressions", "pip",
                      purpose="Arithmetic expression parser library. Embed customized expression evaluation "
                      + "into your application or library."),
        ModuleInstall("cubes", "pip",
                      purpose="Cubes is a light-weight Python framework and set of tools for development of reporting and "
                      + "analytical applications, "
                      + "Online Analytical Processing (OLAP), multidimensional analysis and browsing of aggregated data. "
                      + "It is part of Data Brewery."),
        ModuleInstall("MDP", "pip", usage="ML",
                      purpose="Python data processing framework."),
        ModuleInstall("pyamg", "wheel", usage="OPTIM",
                      purpose="PyAMG is a library of Algebraic Multigrid (AMG) solvers with a convenient Python interface."),
        ModuleInstall("PySAL", "pip", mname="pysal", usage="MATHS",
                      purpose="PySAL is an open source library of spatial analysis functions written in Python intended "
                      + "to support the development of high level applications."),
        #
        # July 2016
        #
        ModuleInstall("hyperopt", "github", "hyperopt", usage="ML",
                      purpose="Hyperopt is a Python library for serial and parallel optimization over awkwardsearch spaces, "
                      + "which may include real-valued, discrete, and conditional dimensions."),
        #
        # August 2016
        #
        ModuleInstall('incremental', 'pip',
                      purpose="Incremental is a small library that versions your Python projects."),
        ModuleInstall('constantly', 'pip',
                      purpose="Symbolic constants in Python"),
        ModuleInstall('PyDispatcher', 'pip', mname="pydispatcher",
                      purpose="Multi-producer-multi-consumer signal dispatching mechanism"),
        ModuleInstall('hyperlink', 'pip',
                      purpose="A featureful, correct URL for Python."),
        ModuleInstall('pyhamcrest', 'pip', purpose="for twisted"),
        ModuleInstall('Twisted', 'wheel', mname="twisted",
                      purpose="An asynchronous networking framework written in Python"),
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
        ModuleInstall("imbalanced-learn", "pip",
                      mname="imblearn", usage="ML",
                      purpose="imbalanced-learn is a python package offering a number of re-sampling "
                      + "techniques commonly used in datasets showing strong between-class imbalance. "
                      + "It is compatible with scikit-learn and is part of scikit-learn-contrib projects."),
        ModuleInstall("forestci", "pip", usage="ML",
                      purpose="Python module for calculating variance and adding confidence intervals "
                      + "to scikit-learn random forest regression "
                      + "or classification objects. The core functions calculate an in-bag and error bars for random forest objects"),
        #
        # 2015-08-18: weidelin.core
        #
        ModuleInstall("ZConfig", "pip",
                      purpose="Structured Configuration Library"),
        ModuleInstall("transaction", "pip",
                      purpose="Transaction management for Python. "
                      + "This package contains a generic transaction implementation for Python. It is mainly used by the ZODB."),
        ModuleInstall("zc.lockfile", "pip",
                      purpose="Basic inter-process locks"),
        ModuleInstall("zodbpickle", "wheel",
                      purpose="This package presents a uniform pickling interface for ZODB."),
        ModuleInstall("ZODB", "pip",
                      purpose="The Zope Object Database provides an object-oriented database for Python that "
                      + "provides a high-degree of transparency."),
        ModuleInstall("zdaemon", "pip",
                      purpose="Daemon process control library and tools for Unix-based systems"),
        ModuleInstall("trollius", "pip",
                      purpose="Port of the Tulip project (asyncio module, PEP 3156)"),
        ModuleInstall("ZEO", "pip",
                      purpose="ZEO provides a client-server storage implementation for ZODB."),
        ModuleInstall("ZODB3", "pip",
                      purpose="ZODB3 - Meta release for ZODB, persistent, BTrees and ZEO"),
        # ModuleInstall("wendelin.core", "wheel", source="2",
        #               purpose="Out-of-core NumPy arrays. " +
        #               "Wendelin.core allows you to work with arrays bigger than RAM and local disk. Bigarrays are persisted to storage, " +
        #               "and can be changed in transactional manner."),
        ModuleInstall("pystorm", "pip",
                      purpose="Battle-tested Apache Storm Multi-Lang implementation for Python."),
        ModuleInstall("Fabric3", "pip", mname="fabric",
                      purpose="Fabric is a simple, Pythonic tool for remote execution and deployment (py2.7/py3.4+ compatible fork)"),
        ModuleInstall("texttable", "pip",
                      purpose="module for creating simple ASCII tables"),
        ModuleInstall("streamparse", "pip",
                      purpose="Streamparse lets you run Python code against real-time streams of data via Apache Storm."),
        #
        # 2016-09-20: treeinterpreter
        #
        ModuleInstall("treeinterpreter", "pip", usage="ML",
                      purpose="Package for interpreting scikit-learn's decision tree and random forest predictions. Allows decomposing "
                      + "each prediction into bias and feature contribution components"),

        #
        # 2016-11/12
        #
        ModuleInstall("update_checker", "pip",
                      purpose="A python module that will check for package updates."),
        ModuleInstall("stopit", "pip",
                      purpose="Timeout control decorator and context managers, raise any exception in another thread."),
        ModuleInstall("TPOT", "pip", mname="tpot", usage="ML",
                      purpose="Consider TPOT your Data Science Assistant. TPOT is a Python tool that automatically "
                      + "creates and optimizes machine learning pipelines using genetic programming."),
        ModuleInstall("category_encoders", "pip", usage="ML",
                      purpose="A set of scikit-learn-style transformers for encoding categorical "
                      + "variables into numeric by means of different techniques."),
        #
        # 2017-01/02
        #
        # ModuleInstall(
        #    'backports.wearkef', 'pip', purpose="This package provides backports of new features in Python's weakref " +
        #    "module under the backports namespace. (for tensorflow)"),
        ModuleInstall('absl-py', 'pip', mname="absl",
                      purpose="Collection of Python library code for building Python applications."),
        ModuleInstall('protobuf', 'pip',
                      purpose="Protocol Buffers are Google's data interchange format"),
        ModuleInstall("gast", "pip",
                      purpose="A generic AST to represent Python2 and Python3’s Abstract Syntax Tree(AST)."),
        ModuleInstall("grpcio", "wheel",
                      purpose="Package for gRPC Python."),
        ModuleInstall("astor", "pip",
                      purpose="astor is designed to allow easy manipulation of Python source via the AST."),
        ModuleInstall("tensorboard", "pip", usage="DATA/ML",
                      purpose="TensorBoard lets you watch Tensors Flow"),
        ModuleInstall("tensorflow-estimator", "pip", usage="DEEP LEARNING",
                      mname="tensorflow_estimator", purpose="Deep Learning from Google"),
        ModuleInstall("tensorflow", "wheel", usage="DEEP LEARNING",
                      purpose="Deep Learning from Google"),
        ModuleInstall("edward", "pip", usage="DATA/ML",
                      purpose="Edward is a Python library for probabilistic modeling, inference, and criticism"),
        ModuleInstall("python_Levenshtein", "wheel", mname="Levenshtein",
                      purpose="C implementation of Levenshtein distance."),
        ModuleInstall("fuzzywuzzy", "pip",
                      purpose="Fuzzy string matching in python"),
        ModuleInstall("smmap", "pip",
                      purpose="A pure python implementation of a sliding window memory map manager"),
        ModuleInstall("gitdb", "pip",
                      purpose="GitDB is a pure-Python git object database"),
        ModuleInstall("GitPython", "pip", mname="git",
                      purpose="Python Git Library"),
        ModuleInstall("git-pandas", "pip", mname="gitpandas",
                      purpose=""),
        ModuleInstall("nbdime", "pip",
                      purpose="Comparison of notebooks"),
        ModuleInstall("cntk", "wheel", usage="DATA/ML",
                      overwrite="https://cntk.ai/PythonWheel/CPU-Only/cntk-2.0-cp{0}{1}-cp{0}{1}m-win_amd64.whl",
                      purpose="Deep Learning from Microsoft "
                      + "see https://docs.microsoft.com/en-us/cognitive-toolkit/setup-windows-python"),

        #
        # 2017-05/23
        #
        ModuleInstall('filelock', 'pip',
                      purpose="A platform independent file lock."),
        ModuleInstall('fasttext', 'wheel', usage="DATA/ML",
                      purpose="fastText is a library for efficient learning of word representations and sentence classification."),
        ModuleInstall('fastrlock', 'wheel',
                      purpose="Fast, re-entrant optimistic lock implemented in Cython (cupy)"),
        ModuleInstall('cupy', 'wheel', usage="DATA/DML",
                      purpose="CuPy : NumPy-like API accelerated with CUDA"),
        ModuleInstall('chainer', 'pip', usage="DATA/DML",
                      purpose="A flexible framework of neural networks (GPU)"),
        ModuleInstall('sfepy', 'wheel', usage="OPTIM",
                      purpose="Simple Finite Elements in Python"),
        ModuleInstall('palettable', 'pip',
                      purpose="Color palettes for Python"),
        ModuleInstall('monty', 'pip',
                      purpose="Monty is the missing complement to Python."),
        ModuleInstall('spglib', 'wheel',
                      purpose="Python bindings for C library for finding and handling crystal symmetries"),
        ModuleInstall('pymatgen', 'wheel', usage="PHYS",
                      purpose="Pymatgen (Python Materials Genomics) is a robust, open-source Python library for materials analysis."),
        ModuleInstall('gvar', 'wheel',
                      purpose="Utilities for manipulating correlated Gaussian random variables."),
        ModuleInstall('lsqfit', 'wheel', usage="OPTIM",
                      purpose="Utilities for nonlinear least-squares fits"),
        ModuleInstall('qutip', 'wheel', usage="OPTIM",
                      purpose="QuTiP is open-source software for simulating the dynamics of open quantum systems."),
        ModuleInstall('pyemd', 'wheel',
                      purpose="A Python wrapper for Ofir Pele and Michael Werman's implementation of the Earth Mover's Distance."),
        ModuleInstall('pint', 'pip',
                      purpose="Physical quantities module"),
        ModuleInstall('traits', 'pip',
                      purpose="explicitly typed attributes for Python"),
        ModuleInstall(
            'sparse', 'pip', purpose="This implements sparse arrays of arbitrary dimension on top of numpy and scipy.sparse"),
        ModuleInstall('hyperspy', 'wheel',
                      purpose="HyperSpy is an open source Python library which provides tools to facilitate "
                      + "the interactive data analysis of multi-dimensional "
                      + "datasets that can be described as multi-dimensional arrays of a given "
                      + "signal (e.g. a 2D array of spectra a.k.a spectrum image)."),
        ModuleInstall('emcee', 'pip',
                      purpose="Kick ass affine-invariant ensemble MCMC sampling"),
        ModuleInstall('h5netcdf', 'pip', purpose="netCDF4 via h5py"),
        ModuleInstall('HoloPy', 'wheel', mname="holopy",
                      purpose="Hologram processing and light scattering in python"),
        ModuleInstall('sounddevice', 'wheel',
                      purpose="This Python module provides bindings for the PortAudio library and a few "
                      + "convenience functions to play and record NumPy arrays containing audio signals."),
        ModuleInstall('drawtree', 'pip', usage="VIZ",
                      purpose="Draw binary tree in plain text"),
        ModuleInstall('JPype1', 'wheel', purpose="A Python to Java bridge."),
        ModuleInstall('pyflux', 'wheel', usage="DATA/ML",
                      purpose="An open source time series library for the Python Programming Language"),
        ModuleInstall('Rtree', 'wheel', usage="MATHS", mname="rtree",
                      purpose="R-Tree spatial index for Python GIS"),
        #
        # 2017-08/10
        #
        ModuleInstall('foolbox', 'pip', usage="ML",
                      purpose="Foolbox is a Python toolbox to create adversarial examples that fool neural networks."),
        #
        # 2017-08/25
        #
        # kealib: https://bitbucket.org/chchrsc/kealib/wiki/Home
        ModuleInstall('iso8601', 'pip',
                      purpose="Simple module to parse ISO 8601 dates"),
        ModuleInstall('translationstring', 'pip',
                      purpose="Utility library for i18n relied on by various Repoze and Pyramid packages"),
        ModuleInstall('colander', 'pip',
                      purpose="A simple schema-based serialization and deserialization library"),
        #
        ModuleInstall('climate-toolbox', 'pip', mname="climate_toolbox",
                      purpose="Command-line utilities (turn function into command line)"),
        ModuleInstall('knnimpute', 'pip', usage="ML",
                      purpose="k-Nearest Neighbor imputation"),
        # Depends on theano - not maintained anymore.
        # ModuleInstall('fancyimpute', 'pip', usage="ML",
        #               purpose="Matrix completion and feature imputation algorithms"),
        ModuleInstall('mnist', 'pip',
                      purpose="Python utilities to download and parse the MNIST dataset"),
        #
        # 2017-11
        #
        ModuleInstall('torch', 'wheel', usage="DEEP LEARNING",
                      purpose="PyTorch is a deep learning framework that puts Python first."),
        ModuleInstall('torchvision', 'pip', usage="DEEP LEARNING",
                      purpose="image and video datasets and models for torch deep learning"),
        ModuleInstall('fairtest', 'wheel', usage="ML", source="2",
                      purpose="FairTest enables developers or auditing entities to discover and test "
                      + "for unwarranted associations between an algorithm's outputs and certain user "
                      + "subpopulations identified by protected features."),
        ModuleInstall('libtiff', 'wheel',
                      purpose="PyLibTiff is a package that provides: a wrapper to the libtiff library to "
                      + "Python using ctypes, a pure Python module for reading and writing TIFF and LSM files. "
                      + "The images are read as numpy.memmap objects so that it is possible to open images "
                      + "that otherwise would not fit to computers RAM. Both TIFF strips and tiles are "
                      + "supported for low-level data storage."),
        ModuleInstall('OpenImageIO', 'wheel',
                      purpose="A library for reading and writing images with emphasis on animation and visual effects."),
        ModuleInstall('urwid', 'pip', purpose="for pyfm"),
        ModuleInstall('pyfm', 'wheel', usage="ML",
                      purpose="Factorization Machine"),
        ModuleInstall('indexed_gzip', 'wheel',
                      purpose="Fast random access of gzip files."),
        ModuleInstall(
            'mockextras', 'pip', purpose="Extensions to the mock library"),
        ModuleInstall(
            'swiglpk', 'wheel', purpose="swiglpk - Simple swig bindings for the GNU Linear Programming Kit"),
        ModuleInstall('optlang', 'pip', purpose="Formulate optimization problems using sympy expressions "
                      + "and solve them using interfaces to third-party optimization software (e.g. GLPK)."),
        ModuleInstall('depinfo', 'pip', purpose="A utility Python package intended for other library packages. "
                      + "Provides a function that when called with your package name, will print platform and dependency information."),
        ModuleInstall(
            'cobra', 'wheel', purpose="Constraint-based reconstruction and analysis in python."),
        ModuleInstall('spectrum', 'wheel', purpose="Spectrum contains tools to estimate Power Spectral Densities using "
                      + "methods based on Fourier transform, Parametric methods or eigenvalues analysis"),
        ModuleInstall('properties', 'pip',
                      purpose="An organizational aid and wrapper for validation and tab completion of class properties"),
        ModuleInstall('pymkl', 'pip', mname="pyMKL",
                      purpose="Python wrapper of Intel MKL routines"),
        ModuleInstall('pymatsolver', 'pip',
                      purpose="A (sparse) matrix solver for python."),
        ModuleInstall('vectormath', 'pip',
                      purpose="Vector math utilities for python (used by discretize)."),
        ModuleInstall('discretize', 'wheel',
                      purpose="A python package for finite volume discretization."),
        ModuleInstall('recordclass', 'wheel',
                      purpose="A mutable variant of collections.namedtuple, which supports assignments."),
        ModuleInstall('pyeda', 'wheel',
                      purpose="A library for electronic design automation."),
        ModuleInstall('Polygon3', 'wheel', mname="polygon", purpose="Handles polygonal shapes in 2D. This library is free "
                      + "for non-commercial use only."),

        #
        # 2017-12
        #
        ModuleInstall('chainercv', 'pip', usage="DATA/DML",
                      purpose="ChainerCV is a deep learning based computer vision library built on top of Chainer."),
        ModuleInstall(
            'fcn', 'pip', purpose="Fully Convolutional Networks", usage="ML"),

        #
        # 2018-14
        #
        ModuleInstall('pyltr', 'pip', usage="ML", purpose="pyltr is a Python learning-to-rank toolkit "
                      "with ranking models, evaluation metrics, data wrangling helpers, and more."),
        ModuleInstall('typing_extensions', 'pip', usage="ML",
                      purpose="Typing Extensions - Backported and Experimental Type Hints for Python"),
        ModuleInstall('onnx', 'wheel2', usage="ML",
                      purpose="Open Neural Network Exchange"),
        ModuleInstall('onnxmltools', 'pip', usage="ML",
                      purpose="Converts Machine Learning models to ONNX"),
        ModuleInstall('sklearn-onnx', 'pip', usage="ML",
                      purpose="Converts scikit-learn Machine Learning models to ONNX"),
        ModuleInstall('keras-onnx', 'pip', usage="ML",
                      purpose="Converts keras Machine Learning models to ONNX"),
        ModuleInstall('tensorflow-onnx', 'pip', usage="ML",
                      purpose="Converts tensorflow Machine Learning models to ONNX"),

        #
        # 2019-01
        #
        ModuleInstall('openTSNE', 'wheel', usage="ML", purpose="Fast t-SNE"),
        ModuleInstall('python-louvain', 'pip', usage="ML",
                      purpose="Louvain algorithm"),

        #
        # 2021-11
        #
        ModuleInstall('onnxruntime_training', 'wheel',
                      usage="ML", purpose="onnxruntime training"),
        ModuleInstall('aten_op_executor', 'wheel', usage="ML",
                      purpose="onnxruntime training"),
        ModuleInstall('torch_interop_utils', 'wheel', usage="ML",
                      purpose="onnxruntime training"),
    ]

    if sys.version_info[0] == 2:
        mod.extend([
            # (for dpark)"),
            ModuleInstall("google-common", "pip", mname="google_common",
                          purpose="Google namespace package"),
            ModuleInstall("mesos.interface", "pip",
                          purpose="Mesos interfaces (for dpark)"),
            ModuleInstall("pymesos", "pip",
                          purpose="Mesos interfaces (for dpark)"),
            # ModuleInstall("dpark", "wheel2",
            # purpose="DPark is a Python clone of Spark, MapReduce(R) alike
            # computing framework supporting iterative computation., see
            # https://github.com/douban/dpark", usage="DATA/ML"),
        ])

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall("comtypes", "pip",
                                 purpose="Pure Python COM package"))
        mod.append(ModuleInstall("xlwings", "pip",
                                 purpose="reads/writes Excel files", usage="WINDOWS") if sys.platform.startswith("win") else None),
        mod.append(ModuleInstall("VideoCapture", "wheel",
                                 purpose="A Win32 Python Extension for Accessing Video Devices", usage="VIDEO"))
        mod.append(ModuleInstall("jaraco.structures", "pip",
                                 purpose="jaraco.structures"))
        mod.append(ModuleInstall("jaraco.classes", "pip",
                                 purpose="Split from another package jaraco."))

    mod.append(ModuleInstall(
        "PyJWT", "pip", mname="jwt", purpose="JSON Web Token library for Python 3."))

    return [_ for _ in mod if _ is not None]
