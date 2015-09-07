#-*- coding: utf-8 -*-
"""
@file
@brief Defines a set of modules for more machine learning or student projects.
"""
import sys
from ..installhelper.module_install import ModuleInstall


def ml_set():
    """
    other name for @see fn ensae_set
    """
    return ensae_set()


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
            "nltk", "wheel", purpose="NLP, natural language processing", usage="DATA/ML"),
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
        ModuleInstall("tifffile", "wheel_xd",
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
        ModuleInstall("dpark", "wheel_xd",
                      purpose="DPark is a Python clone of Spark, MapReduce(R) alike computing framework supporting iterative computation., see https://github.com/douban/dpark", usage="DATA/ML"),
        ModuleInstall("tinydb", "pip",
                      purpose="TinyDB is a tiny, document oriented database optimized for your happiness :) It's written in pure Python and has no external requirements.", usage="noSQL"),
        ModuleInstall("urllib3", "pip",
                      purpose="urllib2 extension"),
        ModuleInstall("greenlet", "wheel",
                      purpose="Greenlet allows lightweight in-process concurrent programming."),
        ModuleInstall("gevent", "wheel_xd",
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

        # azure part
        ModuleInstall("azure_nspkg", "pip", usage="AZURE",
                      purpose="Microsoft Azure Resource Management Namespace Package [Internal]"),
        ModuleInstall("azure_common", "pip", usage="AZURE",
                      purpose="Microsoft Azure Client Library for Python (Common)"),
        ModuleInstall("azure_mgmt_nspkg", "pip", usage="AZURE",
                      purpose="Microsoft Azure Resource Management Namespace Package [Internal]"),
        ModuleInstall("azure_mgmt_common", "pip", usage="AZURE",
                      purpose="Microsoft Azure Resource Management Client Library for Python (Common)"),
        ModuleInstall("azure_mgmt_compute", "pip", usage="AZURE",
                      purpose="Microsoft Azure Compute Resource Management Client Library for Python"),
        ModuleInstall("azure_mgmt_network", "pip", usage="AZURE",
                      purpose="Microsoft Azure Network Resource Management Client Library for Python"),
        ModuleInstall("azure_mgmt_resource", "pip", usage="AZURE",
                      purpose=""),
        ModuleInstall("azure_mgmt_storage", "pip", usage="AZURE",
                      purpose="Microsoft Azure Storage Resource Management Client Library for Python"),
        ModuleInstall("azure_mgmt", "pip", usage="AZURE",
                      purpose="Microsoft Azure Resource Management Client Libraries for Python"),
        ModuleInstall("azure_servicebus", "pip", usage="AZURE",
                      purpose="Microsoft Azure Service Bus Client Library for Python"),
        ModuleInstall("azure_storage", "pip", usage="AZURE",
                      purpose="Microsoft Azure Storage Client Library for Python"),
        ModuleInstall("azure_servicemanagement_legacy", "pip", usage="AZURE",
                      purpose="Microsoft Azure Legacy Service Management Client Library for Python"),
        ModuleInstall(
            "azure", "pip", purpose="Python wrapper for Azure API (HDInsight, Blog Storage)", usage="AZURE"),
        ModuleInstall(
            "azureml", "pip", purpose="Python wrapper for Azure ML API (Azure ML Pipeline)", usage="AZURE"),
        ModuleInstall(
            "azure_batch_apps", "pip", usage="AZURE", mname="batchapps",
            purpose="Python wrapper for Azure ML API (Azure ML Pipeline)"),
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
