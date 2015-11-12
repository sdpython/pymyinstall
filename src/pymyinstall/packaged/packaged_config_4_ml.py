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
            "kombu", "pip", purpose="Messaging library for Python (for celery)"),
        ModuleInstall(
            "anyjson", "pip", purpose="Wraps the best available JSON implementation available in a common interface (for celery)"),
        ModuleInstall(
            "amqp", "pip", purpose="Low-level AMQP client for Python (fork of amqplib) (for celery)"),
        ModuleInstall(
            "celery", "pip", purpose="Celery is an asynchronous task queue/job queue based on distributed message passing."),

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
        ModuleInstall('django', 'pip',
                      purpose="Django"),
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

        ModuleInstall(
            "tweepy", "pip", purpose="Python wrapper for the twitter API"),
        #ModuleInstall("newspaper3k", "pip", mname="newspaper"),
        ModuleInstall(
            "mutagenx", "pip", purpose="ead and write audio tags for many formats in Python 3"),
        ModuleInstall("django-audiotracks", "pip",
                      mname="audiotracks", purpose="read audio with django"),
        ModuleInstall("Quandl", "pip", purpose="access Quandl API"),
        #ModuleInstall("Lasagne", "pip", mname="lasagne"),
        ModuleInstall(
            "nltk", "wheel", purpose="NLP, natural language processing", usage="NLP"),
        ModuleInstall(
            "textblob", "pip", purpose="TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more."),
        ModuleInstall(
            "dev", "pip", purpose="Header files, a static library and development tools for building Python modules, extending the Python interpreter or embedding Python in applications."),
        ModuleInstall(
            "opencv_python", "wheel", mname="cv2", purpose="OpenVC wrapper",
            web="https://opencv-python-tutroals.readthedocs.org/en/latest/"),
        ModuleInstall("PyAudio", "wheel", mname="pyaudio",
                      purpose="PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio streams on a variety of platforms (e.g., GNU/Linux, Microsoft Windows, and Mac OS X)."),
        ModuleInstall(
            "zope.interface", "wheel", purpose="interfaces for python"),
        ModuleInstall(
            "zope.exceptions", "pip", purpose="Zope exception"),
        ModuleInstall(
            "persistent", "wheel", purpose="Objets persistants translucides"),
        # requires zope.interface, persistents
        ModuleInstall(
            "BTrees", "wheel", purpose="This package contains a set of persistent object containers built around a modified BTree data structure.", usage="ALGO"),
        ModuleInstall(
            "datrie", "wheel", purpose="Fast, efficiently stored Trie for Python.", usage="ALGO"),
        # ModuleInstall("pysparse", "pip"), #does not work
        ModuleInstall(
            "Bottleneck", "wheel", mname="bottleneck", purpose="Fast NumPy array functions written in Cython, needed by la"),
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
            "appdirs", "pip", purpose="for pytool, A small Python module for determining appropriate + platform-specific dirs, e.g. a 'user data dir'."),
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
            "scandir", "wheel", purpose="Better directory iterator and faster os.walk(), now in the Python 3.5 stdlib") if sys.version_info[:2] <= (3, 4) else None,
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
            "zipline", "github", "quantopian",
            purpose="Zipline is a Pythonic algorithmic trading library. The system is fundamentally event-driven and a close approximation of how live-trading systems operate."),  # finance
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
        # ModuleInstall("rasterio", "wheel",
        # purpose="Fast and direct raster I/O for use with Numpy and SciPy,
        # Rasterio reads and writes geospatial raster datasets."),
        ModuleInstall("cgal_bindings", "wheel", mname="CGAL",
                      purpose="The CGAL Bindings project allows to use some packages of CGAL, the Computational Algorithms Library, in languages other than C++, as for example Java and Python.",
                      web="https://github.com/cgal/cgal-swig-bindings"),
        ModuleInstall("tifffile", "wheel_xd",
                      purpose="Read and write image data from and to TIFF files. (for pims)"),
        ModuleInstall("slicerator", "pip",
                      purpose="A lazy-loading, fancy-sliceable iterable."),
        ModuleInstall("PIMS", "pip", mname="pims",
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
        # ModuleInstall("ua-parser", "pip", mname="ua_parser",
        #              purpose="Python port of Browserscope's user agent parser"),
        # ModuleInstall("user-agents", "pip", mname="user_agents",
        # purpose="A library to identify devices (phones, tablets) and their
        # capabilities by parsing (browser/HTTP) user agent strings"),
        ModuleInstall("user-agent", "pip", mname="user_agent",
                      purpose="A library to identify devices (phones, tablets) and their capabilities by parsing (browser/HTTP) user agent strings"),
        ModuleInstall("tinydb", "pip",
                      purpose="TinyDB is a tiny, document oriented database optimized for your happiness :) It's written in pure Python and has no external requirements.", usage="noSQL"),
        ModuleInstall("urllib3", "pip",
                      purpose="urllib2 extension"),
        ModuleInstall("gevent", "pip", version="1.1b6",
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


        # azure part
        ModuleInstall("azure-nspkg", "pip", usage="AZURE", mname="azure.mgmt",
                      purpose="Microsoft Azure Resource Management Namespace Package [Internal]"),
        ModuleInstall("azure-common", "pip", usage="AZURE", mname="azure.common",
                      purpose="Microsoft Azure Client Library for Python (Common)"),
        ModuleInstall("azure-mgmt-nspkg", "pip", usage="AZURE", mname="azure.mgmt.common",
                      purpose="Microsoft Azure Resource Management Namespace Package [Internal]"),
        ModuleInstall("azure-mgmt-common", "pip", usage="AZURE", mname="azure.mgmt.common",
                      purpose="Microsoft Azure Resource Management Client Library for Python (Common)"),
        ModuleInstall("azure-mgmt-compute", "pip", usage="AZURE", mname="azure.mgmt.compute",
                      purpose="Microsoft Azure Compute Resource Management Client Library for Python"),
        ModuleInstall("azure-mgmt-network", "pip", usage="AZURE", mname="azure.mgmt.network",
                      purpose="Microsoft Azure Network Resource Management Client Library for Python"),
        ModuleInstall("azure-mgmt-resource", "pip", usage="AZURE", mname="azure.mgmt.resource",
                      purpose=""),
        ModuleInstall("azure-mgmt-storage", "pip", usage="AZURE", mname="azure.mgmt.storage",
                      purpose="Microsoft Azure Storage Resource Management Client Library for Python"),
        ModuleInstall("azure-mgmt", "pip", usage="AZURE", mname="azure.mgmt",
                      purpose="Microsoft Azure Resource Management Client Libraries for Python"),
        ModuleInstall("azure-servicebus", "pip", usage="AZURE", mname="azure.servicebus",
                      purpose="Microsoft Azure Service Bus Client Library for Python"),
        ModuleInstall("azure-storage", "pip", usage="AZURE", mname="azure.storage",
                      purpose="Microsoft Azure Storage Client Library for Python"),
        ModuleInstall("azure-servicemanagement-legacy", "pip", usage="AZURE", mname="azure.servicemanagement",
                      purpose="Microsoft Azure Legacy Service Management Client Library for Python"),
        ModuleInstall(
            "azure", "pip", purpose="Python wrapper for Azure API (HDInsight, Blog Storage)", usage="AZURE"),
        ModuleInstall(
            "azureml", "pip", purpose="Python wrapper for Azure ML API (Azure ML Pipeline)", usage="AZURE"),
        ModuleInstall(
            "azure-batch-apps", "pip", usage="AZURE", mname="batchapps",
            purpose="Python wrapper for Azure ML API (Azure ML Pipeline)"),
        #
        #
        #
        ModuleInstall("lz4", "wheel",
                      purpose="LZ4 Bindings for Python (for dpark)"),
        ModuleInstall("fabric", "pip",
                      purpose="Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks."),
        ModuleInstall("invoke", "pip",
                      purpose="Invoke is a Python task execution tool & library, drawing inspiration from various sources to arrive at a powerful & clean feature set."),
        ModuleInstall("msgpack-python", "pip", mname="msgpack",
                      purpose="MessagePack (de)serializer."),
        ModuleInstall("cloudpickle", "pip",
                      purpose="Extended pickling support for Python objects"),
        ModuleInstall("cymem", "pip",
                      purpose="Manage calls to calloc/free through Cython"),
        ModuleInstall("murmurhash", "pip",
                      purpose="Cython .pxd files for some of the MurmurHash 2 and 3 hash functions, with a slightly more Pythonic API. The only access to these functions is via Cython — I don’t see why they should be useful from pure Python."),
        ModuleInstall("preshed", "pip",
                      purpose="Cython hash table that trusts the keys are pre-hashed"),
        ModuleInstall("text-unidecode", "pip", mname="text_unidecode",
                      purpose="The most basic Text::Unidecode port"),
        ModuleInstall("thinc", "pip", usage="OPTIM",
                      purpose="Learn sparse linear models"),
        ModuleInstall("spacy", "pip", usage="NLP",
                      purpose="Industrial-strength NLP"),

    ]

    if sys.version_info[0] == 2:
        mod.extend([
            # ModuleInstall("protobuf-py3", "pip", mname="google.protobuf",
            # purpose="Protocol Buffers are Google’s data interchange format
            # (for dpark)"),
            ModuleInstall("mesos.interface", "pip",
                          purpose="Mesos interfaces (for dpark)"),
            ModuleInstall("pymesos", "pip",
                          purpose="Mesos interfaces (for dpark)"),
            ModuleInstall("prettytable", "pip",
                          purpose="A simple Python library for easily displaying tabular data in a visually appealing ASCII table format. (for streamparse)"),
            ModuleInstall("streamparse", "pip",
                          purpose="Streamparse lets you run Python code against real-time streams of data via Apache Storm."),
            ModuleInstall("dpark", "wheel_xd",
                          purpose="DPark is a Python clone of Spark, MapReduce(R) alike computing framework supporting iterative computation., see https://github.com/douban/dpark", usage="DATA/ML"),
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

    return [_ for _ in mod if _ is not None]
