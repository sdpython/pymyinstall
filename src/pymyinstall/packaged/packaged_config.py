"""
@file
@brief Defines different set of modules to install.
"""
import sys
from ..installhelper.module_install import ModuleInstall


def small_installation():
    """
    returns a list of modules to work with pandas, numpy, ipython, ...

    @return             a list of modules to install

    To install them:
    @code
    for _ in complete_installation() :
        _.install(temp_folder="install")
    @endcode
    """
    mod = [
        # ModuleInstall("setuptools",     "wheel"),        # removed with 3.4
        # ModuleInstall("pip",            "wheel"),            # removed with 3.4
        #
        ModuleInstall("virtualenv", "pip"),
        ModuleInstall("six", "pip"),
        ModuleInstall("lxml", "wheel"),
        ModuleInstall("jinja2", "pip"),
        ModuleInstall("pygments", "pip"),
        ModuleInstall("pyparsing", "pip"),
        ModuleInstall("python-dateutil", "pip", "dateutil"),
        ModuleInstall("html5lib", "pip"),
        ModuleInstall("beautifulsoup4", "pip", mname="bs4"),
        ModuleInstall("coverage", "pip"),
        ModuleInstall("nose", "pip"),
        ModuleInstall("pytz", "pip"),
        ModuleInstall("pyreadline", "pip", mname="pyreadline"),
        ModuleInstall("husl", "pip"),
        ModuleInstall("pipdeptree", "pip"),
        #
        ModuleInstall("openpyxl", "pip", version="1.8.6"),
        ModuleInstall("xlrd", "pip"),
        ModuleInstall("xlwt", "pip"),
        ModuleInstall("xlwings", "pip"),
        #
        ModuleInstall("certifi", "pip"),
        ModuleInstall("tornado", "wheel"),
        ModuleInstall("pyzmq", "wheel", mname="zmq"),
        #
        ModuleInstall("pycparser", "wheel"),
        ModuleInstall("Cython", "wheel"),
        ModuleInstall("numpy", "wheel"),
        ModuleInstall("matplotlib", "wheel"),
        ModuleInstall("gr", "wheel"),
        # ModuleInstall("seaborn", "pip"),   # it seems problematic for this
        # small config
        ModuleInstall("scipy", "wheel"),
        ModuleInstall("statsmodels", "wheel"),  # needs scipy
        ModuleInstall("networkx", "wheel"),  # it seems problematic for this
        # small config
        ModuleInstall("graphviz", "pip"),
        ModuleInstall("jsonschema", "pip"),
        ModuleInstall("mistune", "pip"),
        ModuleInstall("wheel", "pip"),
        # sphinx
        ModuleInstall("alabaster", "wheel"),
        ModuleInstall("Babel", "wheel", mname="babel"),
        ModuleInstall("colorama", "pip"),
        ModuleInstall("docutils", "pip"),
        ModuleInstall("sphinx", "pip"),
        ModuleInstall('pypiserver', 'pip'),
        # flake8, pep8
        ModuleInstall("pep8", "pip", version="1.5.7"),
        ModuleInstall("autopep8", "pip"),
        ModuleInstall("mccabe", "pip"),
        ModuleInstall("pyflakes", "pip"),
        ModuleInstall("flake8", "pip"),
        ModuleInstall('markupsafe', 'pip'),
        #
        #
        ModuleInstall("pandas", "wheel"),
        ModuleInstall("scikit-learn", "wheel", mname="sklearn"),
        ModuleInstall("ipython", "pip", mname="IPython"),
        #
        ModuleInstall("mpld3", "pip"),
        #
        ModuleInstall("typecheck-decorator", "pip", mname="typecheck"),
        ModuleInstall("decorator", "pip"),
        #
        ModuleInstall("requests", "pip"),
        #ModuleInstall("PyQt",           "wheel", mname="PyQt4"),
        ModuleInstall("PySide", "wheel"),
        ModuleInstall("psutil", "wheel"),  #
        ModuleInstall("rope_py3k", "pip", mname="rope"),  #
        ModuleInstall("pylint", "pip"),  #
        ModuleInstall("spyder", "wheel", mname="spyderlib"),
        #
        ModuleInstall("brewer2mpl", "pip"),
        ModuleInstall("ggplot", "pip"),
        ModuleInstall("goslate", "pip"),
        ModuleInstall("dbfread", "pip"),   # to read dbase format
        ModuleInstall("xmltodict", "pip"),   # XML to JSON
        ModuleInstall("ansiconv", "pip"),   # shell to plain
        ModuleInstall("ansi2html", "pip"),   # shell to HTML
        #
        ModuleInstall("nodeenv", "pip"),   # node.js
        ModuleInstall('sphinxjp.themes.revealjs', 'pip'),
        #
        # 2015-06-05
        #
        ModuleInstall('PyYAML', 'wheel', mname='yaml'),
        ModuleInstall('bokeh', 'pip'),
        ModuleInstall('rpy2', 'wheel'),
        ModuleInstall('seaborn', 'pip'),
        ModuleInstall("sphinxjp.themes.revealjs", "pip"),
        ModuleInstall("feedparser", "wheel"),   # to parse RSS streams
        ModuleInstall("python-jenkins", "pip", mname="jenkins"),  # for Jenkins
        #
        # 2015-06-15
        #
        ModuleInstall('envoy', 'pip'),
        ModuleInstall('Logbook', 'wheel', mname='logbook'),
    ]

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall("pywin32", "wheel", mname="win32com"))
        mod.append(ModuleInstall("winshell", "pip"))

    return mod


def complete_installation():
    """
    returns a list of modules to install, an rich set
    to work with data and more

    @return             a list of modules to install

    To install them:
    @code
    for _ in complete_installation() :
        _.install(temp_folder="install")
    @endcode
    """
    mod = small_installation() + [
        ModuleInstall('werkzeug', 'pip'),
        ModuleInstall('itsdangerous', 'pip'),
        ModuleInstall('SQLAlchemy', 'wheel', mname='sqlalchemy'),
        ModuleInstall('flask-sqlalchemy', 'pip', mname='flask.ext.sqlalchemy'),
        ModuleInstall('simplejson', 'wheel'),
        ModuleInstall('python-pptx', 'pip', mname="pptx"),
        ModuleInstall('python-docx', 'pip', mname="docx"),
        ModuleInstall('XlsxWriter', 'pip', mname='xlsxwriter'),
        ModuleInstall('flask', 'pip'),
        ModuleInstall('cffi', 'wheel'),
        ModuleInstall('odo', 'wheel'),
        ModuleInstall('cytoolz', 'wheel'),
        ModuleInstall('toolz', 'wheel'),
        ModuleInstall('datashape', 'pip'),
        ModuleInstall('multipledispatch', 'pip'),
        ModuleInstall('dynd', 'wheel'),
        ModuleInstall('blaze', 'wheel'),
        ModuleInstall('sympy', 'pip'),
        ModuleInstall('gmpy2', 'wheel'),
        ModuleInstall('llvmpy', 'wheel', mname='llvm'),
        ModuleInstall('llvmlite', 'wheel'),
        ModuleInstall('numba', 'wheel'),
        ModuleInstall('networkx', 'pip'),
        ModuleInstall('snowballstemmer', 'pip'),
        ModuleInstall('sphinx-rtd-theme', 'pip', mname='sphinx_rtd_theme'),
        ModuleInstall('scikit-image', 'wheel', mname='skimage'),
        ModuleInstall('patsy', 'pip'),
        ModuleInstall('cvxopt', 'wheel'),
        ModuleInstall('pymc', 'wheel'),
        ModuleInstall('PyWavelets', 'wheel', mname='pywt'),
        ModuleInstall('fastcluster', 'wheel'),
        ModuleInstall('pycosat', 'wheel'),
        ModuleInstall('pyshp', 'pip', mname='shapefile'),
        ModuleInstall('Shapely', 'wheel', mname='shapely'),
        ModuleInstall('vispy', 'pip'),
        ModuleInstall('selenium', 'pip'),
        ModuleInstall('Pillow', 'wheel', mname='PIL'),
        ModuleInstall('pygame', 'wheel'),
        ModuleInstall('Kivy', 'wheel', mname='kivy'),
        ModuleInstall('kivy-garden', 'pip', mname='kivy.garden'),
        ModuleInstall('py4j', 'pip'),
        ModuleInstall('python-igraph', 'wheel', mname='igraph'),
        ModuleInstall('lockfile', 'pip'),
        ModuleInstall('python-daemon', 'pip', mname='daemon'),
        ModuleInstall('luigi', 'pip'),
        #
        ModuleInstall('setproctitle', 'wheel', mname='setproctitle'),
        # thrift only works only for Python 2.7
        ModuleInstall('thriftpy', 'pip'),
        # ModuleInstall('airflow', 'pip'),  # does not work on Python 3
        ModuleInstall('smopy', 'pip'),
        ModuleInstall('folium', 'pip'),
        ModuleInstall('basemap', 'wheel', mname='mpl_toolkits.basemap'),
        ModuleInstall('snowballstemmer', 'pip'),
        ModuleInstall('sphinx-rtd-theme', 'pip', mname='sphinx_rtd_theme'),
        ModuleInstall(
            'sphinxcontrib-images', 'pip', mname='sphinxcontrib.images'),
        ModuleInstall('sphinx_rtd_theme', 'pip'),
        ModuleInstall('sphinxjp.themes.basicstrap', 'pip'),
        ModuleInstall('solar_theme', 'pip'),
        ModuleInstall('cloud_sptheme', 'pip'),
        ModuleInstall('sphinx_readable_theme', 'pip'),
        ModuleInstall(
            "hachibee-sphinx-theme", "pip", mname="hachibee_sphinx_theme"),
        ModuleInstall("wild_sphinx_theme", "pip"),
        ModuleInstall("sphinx_bootstrap_theme", "pip"),
        ModuleInstall("sphinxjp.themes.sphinxjp", "pip"),
        ModuleInstall("sphinx_py3doc_enhanced_theme", "pip"),
        ModuleInstall("epfl-sphinx-theme", "pip", mname="epfl_theme"),
        ModuleInstall("sphinxjp.themes.revealjs", "pip"),

        #
        ModuleInstall("brewer2mpl", "pip"),
        ModuleInstall("ggplot", "pip"),
        ModuleInstall("dbfread", "pip"),   # to read dbase format
        ModuleInstall("xmltodict", "pip"),   # XML to JSON
        ModuleInstall("python-linkedin", "pip", mname="linkedin"),
        # access to linkedin
        ModuleInstall("oauthlib", "pip"),
        ModuleInstall("requests_oauthlib", "pip"),
        ModuleInstall("antlr4-python3-runtime", "pip", mname="antlr4"),
        # ModuleInstall("unqlite",                    "pip"),   #
        # key/value store (NoSQL)
        ModuleInstall("pycontracts", "pip", mname="contracts"),
        ModuleInstall("ansiconv", "pip"),   # shell to plain
        ModuleInstall("ansi2html", "pip"),   # shell to HTML

        #
        ModuleInstall("ecdsa", "pip"),
        ModuleInstall("pycrypto", "wheel_xd", mname="Crypto"),
        ModuleInstall("paramiko", "pip"),
        #
        ModuleInstall("pattern", "pip") if sys.version_info[
            0] < 3 else None,  # to read dbase format
        #
        ModuleInstall("nodeenv", "pip"),   # node.js
        ModuleInstall("pbr", "pip"),
        #
        # 2015-02-05
        #
        ModuleInstall("autopy3", "wheel", mname="autopy3"),  # simulate events
        ModuleInstall("bigfloat", "wheel"),  # large double
        # convex optimization, depends on CVXOPT
        ModuleInstall("scs", "wheel"),
        ModuleInstall("ecos", "wheel"),
        ModuleInstall("cvxpy", "pip"),
        ModuleInstall("blist", "wheel"),    # better large list
        ModuleInstall("conda", "pip"),      # to install packages with conda
        ModuleInstall("libLAS", "wheel", mname="liblas"),
        ModuleInstall("liblinear", "wheel"),
        ModuleInstall("marisa_trie", "wheel"),
        ModuleInstall("mlpy", "wheel"),
        ModuleInstall("pygit2", "wheel"),
        ModuleInstall("pymongo", "wheel"),
        ModuleInstall("PyOpenGL", "wheel", mname="OpenGL"),
        ModuleInstall("Theano", "wheel", mname="theano"),
        ModuleInstall("pyqtgraph", "pip"),
        ModuleInstall("deap", "pip"),
        ModuleInstall("boto", "pip"),      # for gensim
        ModuleInstall("bz2file", "pip"),      # for gensim
        ModuleInstall("smart_open", "wheel"),      # for gensim
        ModuleInstall("gensim", "wheel"),
        # ModuleInstall("pybrain", "pip"),   # some issues with the code
        # (relative import are not well handled in version 0.3.3
        ModuleInstall("h5py", "wheel"),  # Bayesian
        ModuleInstall("bayespy", "pip"),  # Bayesian
        ModuleInstall("numexpr", "wheel"),
        #
        ModuleInstall("glueviz", "wheel", mname="glue"),
        ModuleInstall("pypiserver", "pip"),
        #
        ModuleInstall("charts", "pip"),  # javascript graphs
        #
        ModuleInstall("dill", "pip"),  # for dask
        ModuleInstall("dask", "pip"),  # parallel computation
        #
        ModuleInstall("jedi", "pip"),
        ModuleInstall("docopt", "pip"),
        ModuleInstall("markdown2", "pip"),
        ModuleInstall("structures", "pip"),
        ModuleInstall("py2exe", "wheel"),
        ModuleInstall("rodeo", "pip"),
        #
        # ModuleInstall("pdfminer", "pip"),  # PDF extraction (no python 3 version)
        # ModuleInstall("minecart", "pip"),  # PDF extraction (no python 3 version)
        #
        # ModuleInstall("pygauss", "pip"),  # molecule, bio-informatic,
        # requires PIL which is deprecated
    ]

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall("pywin32", "wheel", mname="win32com"))
        mod.append(ModuleInstall("winshell", "pip"))

    return [_ for _ in mod if _ is not None]


def installation_azure():
    """
    Modules to handle huge datasets on disk, hierarchical datasets.

    """
    mod = [
        ModuleInstall("azure", "pip"),
    ]

    return mod


def extend_anaconda():
    """
    list of modules to complete anaconda
    """

    mod = [
        ModuleInstall("cvxopt", "wheel"),
        ModuleInstall("goslate", "pip"),
        ModuleInstall("dbfread", "pip"),
        ModuleInstall("rpy2", "wheel"),
        ModuleInstall("mpld3", "pip"),
        ModuleInstall("folium", "pip"),
        ModuleInstall("graphviz", "pip"),
        ModuleInstall("numexpr", "wheel"),
        ModuleInstall("deap", "pip"),
        ModuleInstall("antlr4-python3-runtime", "pip", mname="antlr4"),
        #
        ModuleInstall("pep8", "pip", version="1.5.7"),
        ModuleInstall("autopep8", "pip"),
        ModuleInstall("wheel", "pip"),
        ModuleInstall("coverage", "pip"),
        ModuleInstall("mccabe", "pip"),
        ModuleInstall("snowballstemmer", "pip"),
        ModuleInstall("sphinx-rtd-theme", "pip", mname="sphinx_rtd_theme"),
        ModuleInstall("pyflakes", "pip"),
        ModuleInstall("flake8", "pip"),
        ModuleInstall(
            "sphinxcontrib-images", "pip", mname="sphinxcontrib.images"),
        ModuleInstall("sphinx_rtd_theme", "pip"),
        ModuleInstall("sphinxjp.themes.basicstrap", "pip"),
        ModuleInstall("solar_theme", "pip"),
        ModuleInstall("cloud_sptheme", "pip"),
        ModuleInstall("sphinx_readable_theme", "pip"),
        ModuleInstall(
            "hachibee-sphinx-theme", "pip", mname="hachibee_sphinx_theme"),
        ModuleInstall("wild_sphinx_theme", "pip"),
        ModuleInstall("sphinx_bootstrap_theme", "pip"),
        ModuleInstall("sphinxjp.themes.sphinxjp", "pip"),
        ModuleInstall("sphinxjp.themes.revealjs", "pip"),
        ModuleInstall("sphinx_py3doc_enhanced_theme", "pip"),
        ModuleInstall("epfl-sphinx-theme", "pip", mname="epfl_theme"),
        ModuleInstall("pypiserver", "pip"),
        ModuleInstall("bayespy", "pip"),  # Bayesian
        #
        ModuleInstall("charts", "pip"),  # javascript graphs
        ModuleInstall("invoke", "pip"),  # dependency for ablog
        ModuleInstall("ablog", "pip"),  # blogging
    ]

    return mod


def extend_winpython():
    """
    list of modules to complete anaconda
    """

    mod = [
        ModuleInstall("virtualenv", "pip"),
        ModuleInstall("cvxopt", "wheel"),
        ModuleInstall("goslate", "pip"),
        ModuleInstall("dbfread", "pip"),
        ModuleInstall("bokeh", "pip"),
        ModuleInstall("pywin32", "wheel", mname="win32com"),
        ModuleInstall("folium", "pip"),
        ModuleInstall("graphviz", "pip"),
        ModuleInstall("deap", "pip"),
        ModuleInstall("antlr4-python3-runtime", "pip", mname="antlr4"),
        #
        ModuleInstall("pep8", "pip", version="1.5.7"),
        ModuleInstall("autopep8", "pip"),
        ModuleInstall("coverage", "pip"),
        ModuleInstall("bokeh", "pip"),
        ModuleInstall("snowballstemmer", "pip"),
        ModuleInstall("sphinx-rtd-theme", "pip", mname="sphinx_rtd_theme"),
        ModuleInstall(
            "sphinxcontrib-images", "pip", mname="sphinxcontrib.images"),
        ModuleInstall("sphinx_rtd_theme", "pip"),
        ModuleInstall("sphinxjp.themes.basicstrap", "pip"),
        ModuleInstall("solar_theme", "pip"),
        ModuleInstall("cloud_sptheme", "pip"),
        ModuleInstall("sphinx_readable_theme", "pip"),
        ModuleInstall(
            "hachibee-sphinx-theme", "pip", mname="hachibee_sphinx_theme"),
        ModuleInstall("wild_sphinx_theme", "pip"),
        ModuleInstall("sphinx_bootstrap_theme", "pip"),
        ModuleInstall("sphinxjp.themes.sphinxjp", "pip"),
        ModuleInstall("sphinxjp.themes.revealjs", "pip"),
        ModuleInstall("sphinx_py3doc_enhanced_theme", "pip"),
        ModuleInstall("epfl-sphinx-theme", "pip", mname="epfl_theme"),
        ModuleInstall("pypiserver", "pip"),
        ModuleInstall("bayespy", "pip"),  # Bayesian
        # may 2015
        ModuleInstall("charts", "pip"),  # javascript graphs
    ]

    return mod


def extension_ensae():
    """
    .. index:: ENSAE

    Modules introduced by students and some others added after some reading.
    """
    mod = [
        ModuleInstall("celery", "pip"),
        ModuleInstall("tweepy", "pip"),
        #ModuleInstall("newspaper3k", "pip", mname="newspaper"),
        ModuleInstall("django", "pip"),
        ModuleInstall("django-audiotracks", "pip", mname="audiotracks"),
        ModuleInstall("Quandl", "pip"),
        #ModuleInstall("Lasagne", "pip", mname="lasagne"),
        ModuleInstall("pymunk", "pip"),
        ModuleInstall("nltk", "wheel"),
        ModuleInstall("textblob", "pip"),
        ModuleInstall("dev", "pip"),
        ModuleInstall("opencv_python", "wheel", mname="cv"),
        ModuleInstall("PyAudio", "wheel", mname="pyaudio"),
        ModuleInstall("zope.interface", "wheel"),
        ModuleInstall("persistent", "wheel"),
        # requires zope.interface, persistents
        ModuleInstall("BTrees", "wheel"),
        ModuleInstall("datrie", "wheel"),
        # ModuleInstall("pysparse", "pip"), #does not work
        ModuleInstall("la", "wheel"),
        ModuleInstall("mahotas", "wheel"),
        ModuleInstall("milk", "wheel"),
        ModuleInstall("minepy", "wheel"),
        ModuleInstall("NLopt", "wheel", mname="nlopt"),
        ModuleInstall("Pmw", "wheel", mname="Pmw"),
        ModuleInstall("py2exe", "wheel"),
        ModuleInstall("pytools", "pip"),
        ModuleInstall("pycuda", "wheel"),
        # ModuleInstall("scikits.cuda", "pip", mname="skcuda"), # no stable
        # version
        ModuleInstall("pylzma", "wheel"),
        ModuleInstall("pymvpa2", "wheel", mname="mvpa2"),
        ModuleInstall("pyodbc", "wheel"),
        ModuleInstall("pypmc", "wheel"),
        ModuleInstall("pyserial", "wheel", mname="serial"),
        ModuleInstall("PyX", "wheel", mname="pyx"),
        ModuleInstall("scandir", "wheel"),
        ModuleInstall("VideoCapture", "wheel"),
        ModuleInstall("zs", "wheel"),
        # machine learning
        ModuleInstall("joblib", "pip"),
        #
        # teachings
        #
        ModuleInstall("tutormagic", "pip"),  # tutor magic in a notebook
        # cache resuls from a long computation
        ModuleInstall("ipycache", "pip"),
        ModuleInstall("nbupload", "pip"),  # to upload a file in a notebook
        # see https://github.com/PetterS/numpy_display/blob/master/numpy_display.py
        # https://github.com/damiendr/callipy
        #
        ModuleInstall("libsvm", "wheel", mname="svm"),
        ModuleInstall("abcpmc", "pip"),  # Bayesian ABC
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
        ModuleInstall("zipline", "pip"),  # finance
        ModuleInstall("vincent", "pip"),  # graph
        ModuleInstall("pygal", "pip"),  # graph
        ModuleInstall("pygal_maps_world", "pip"),  # graph
        #
        # 2015-06-30
        #
        ModuleInstall("sas7bdat", "pip"),  # SAS
        

    ]
    return mod


def installation_teachings():
    """
    .. index:: ENSAE, teachings

    Modules implemented for my teachings.
    """
    mod = [
        ModuleInstall("pyquickhelper", "pip"),
        ModuleInstall("pymyinstall", "pip"),
        ModuleInstall("pymmails", "pip"),
        ModuleInstall("pyensae", "pip"),
        ModuleInstall("pyrsslocal", "pip"),
        ModuleInstall("code_beatrix", "pip"),
        ModuleInstall("actuariat_python", "pip"),
        ModuleInstall("ensae_teaching_cs", "pip"),
    ]
    #
    return mod


def installation_huge_datasets():
    """
    Modules to handle huge datasets on disk, hierarchical datasets.

    """
    mod = [
        ModuleInstall("h5py", "wheel"),
        ModuleInstall("blosc", "wheel"),
        ModuleInstall("numexpr", "wheel"),
        ModuleInstall("tables", "wheel"),
    ]

    return mod


def installation_ensae():
    """
    .. index:: ENSAE

    Installation of all possible modules for my teachings at the ENSAE.
    """
    base = complete_installation() +  \
        installation_huge_datasets() + \
        installation_azure() + \
        extension_ensae()

    return base
