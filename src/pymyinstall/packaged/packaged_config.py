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
        ModuleInstall("virtualenv", "wheel"),
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
        ModuleInstall("openpyxl", "pip"),
        ModuleInstall("xlrd", "pip"),
        #
        ModuleInstall("certifi", "pip"),
        ModuleInstall("tornado", "wheel"),
        ModuleInstall("pyzmq", "wheel", mname="zmq"),
        #
        ModuleInstall("pycparser", "wheel"),
        ModuleInstall("Cython", "wheel"),
        ModuleInstall("numpy", "wheel"),
        ModuleInstall("matplotlib", "wheel"),
        # ModuleInstall("seaborn", "pip"),   # it seems problematic for this
        # small config
        ModuleInstall("scipy", "wheel"),
        ModuleInstall("statsmodels", "wheel"),  # needs scipy
        # ModuleInstall("networkx", "wheel"), # it seems problematic for this
        # small config
        ModuleInstall("graphviz", "pip"),
        ModuleInstall("jsonschema", "pip"),
        ModuleInstall("mistune", "pip"),
        ModuleInstall("wheel", "pip"),
        ModuleInstall("alabaster", "wheel"),
        ModuleInstall("Babel", "wheel"),
        ModuleInstall("sphinx", "pip"),
        ModuleInstall("pep8", "pip", version="1.5.7"),
        ModuleInstall("autopep8", "pip"),
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
        ModuleInstall("spyder", "wheel", script="spyder.bat"),
        #
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
        #
        # 2015-02-05
        #
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
    mod = [
        ModuleInstall("virtualenv", "wheel"),
        # ModuleInstall("setuptools",     "wheel"),                # removed with 3.4
        # ModuleInstall("pip",            "wheel"),
        # # removed with 3.4
        ModuleInstall("typecheck-decorator", "pip", mname="typecheck"),
        ModuleInstall("decorator", "pip"),
        #
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
        ModuleInstall("werkzeug", "pip"),
        ModuleInstall("itsdangerous", "pip"),
        ModuleInstall("SQLAlchemy", "wheel", mname="sqlalchemy"),
        ModuleInstall("flask-sqlalchemy", "pip", mname="flask.ext.sqlalchemy"),
        ModuleInstall("pyreadline", "pip", mname="pyreadline"),
        ModuleInstall("simplejson", "wheel"),
        ModuleInstall("husl", "pip"),
        ModuleInstall("pipdeptree", "pip"),
        #
        ModuleInstall("openpyxl", "pip"),
        ModuleInstall("xlrd", "pip"),
        ModuleInstall("python-pptx", "pip"),
        ModuleInstall("XlsxWriter", "pip", mname="xlsxwriter"),
        #
        ModuleInstall("tornado", "wheel"),
        ModuleInstall("flask", "pip"),
        ModuleInstall("pyzmq", "wheel", mname="zmq"),
        #
        ModuleInstall("pycparser", "wheel"),
        ModuleInstall("Cython", "wheel"),
        ModuleInstall("cffi", "wheel"),
        ModuleInstall("numpy", "wheel"),
        ModuleInstall('odo', 'wheel'),                # for blaze
        ModuleInstall('cytoolz', 'wheel'),          # for blaze
        ModuleInstall('toolz', 'wheel'),            # for blaze
        ModuleInstall('datashape', 'pip'),          # for blaze
        ModuleInstall('multipledispatch', 'pip'),   # for blaze
        # see https://binstar.org/blaze/blaze
        ModuleInstall("dynd", "wheel"),
        # see https://binstar.org/blaze/blaze
        ModuleInstall("blaze", "wheel"),
        ModuleInstall("scipy", "wheel"),
        ModuleInstall("matplotlib", "wheel"),
        ModuleInstall("seaborn", "pip"),
        ModuleInstall("sympy", "pip"),
        ModuleInstall("gmpy2", "wheel"),
        ModuleInstall("llvmpy", "wheel", mname="llvm"),
        ModuleInstall("numba", "wheel"),
        ModuleInstall("networkx", "pip"),
        ModuleInstall("graphviz", "pip"),
        ModuleInstall("jsonschema", "pip"),
        ModuleInstall("mistune", "pip"),
        ModuleInstall("wheel", "pip"),
        #
        ModuleInstall("snowballstemmer", "pip"),
        ModuleInstall("sphinx-rtd-theme", "pip", mname="sphinx_rtd_theme"),
        ModuleInstall("pandas", "wheel"),
        ModuleInstall("scikit-learn", "wheel", mname="sklearn"),
        ModuleInstall("scikit-image", "wheel", mname="skimage"),
        ModuleInstall("patsy", "pip"),
        ModuleInstall("statsmodels", "wheel"),  # needs scipy
        ModuleInstall("ipython", "wheel", mname="IPython"),
        ModuleInstall("cvxopt", "wheel"),
        ModuleInstall("pymc", "wheel"),
        ModuleInstall("PyWavelets", "wheel", mname="pywt"),
        ModuleInstall("fastcluster", "wheel"),
        #
        ModuleInstall("mpld3", "pip"),
        ModuleInstall("pycosat", "wheel"),
        ModuleInstall("PyYAML", "wheel", mname="yaml"),
        ModuleInstall("bokeh", "pip"),
        ModuleInstall("pyshp", "pip", mname="shapefile"),
        # needed by shapely
        ModuleInstall("Shapely", "wheel", mname="shapely"),
        # exe on Windows to get geos.dll
        ModuleInstall("vispy", "pip"),
        #
        ModuleInstall("rpy2", "wheel"),
        # ModuleInstall("pythonnet",      "wheel", mname="clr"),  # included in ensae_teaching_cs
        #
        ModuleInstall("selenium", "pip"),
        ModuleInstall("Pillow", "wheel", mname="PIL"),
        ModuleInstall("pygame", "wheel"),
        ModuleInstall("markupsafe", "pip"),
        ModuleInstall("requests", "pip"),
        ModuleInstall("Kivy", "wheel", mname="kivy"),
        ModuleInstall("kivy-garden", "pip", mname="kivy.garden", version="0.1.1"),
        #ModuleInstall("PyQt",           "wheel", mname="PyQt4"),
        ModuleInstall("PySide", "wheel"),
        ModuleInstall("spyder", "wheel", script="spyder.bat"),
        #
        ModuleInstall("py4j", "pip"),
        ModuleInstall("python-igraph", "wheel", mname="igraph"),
        #
        ModuleInstall("lockfile", "pip"),
        ModuleInstall("python-daemon", "pip", mname="daemon"),
        ModuleInstall("luigi", "pip"),
        #
        #ModuleInstall("Cartopy",        "wheel", mname="cartopy"),
        ModuleInstall("smopy", "pip"),
        ModuleInstall("folium", "pip"),
        ModuleInstall("basemap", "wheel", mname="mpl_toolkits.basemap"),
        #
        ModuleInstall("alabaster", "wheel"),
        ModuleInstall("Babel", "wheel"),
        ModuleInstall("sphinx", "pip"),
        ModuleInstall("docutils", "pip"),
        ModuleInstall("mccabe", "pip"),
        ModuleInstall("pyflakes", "pip"),
        ModuleInstall("flake8", "pip"),
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
        ModuleInstall("feedparser", "wheel"),   # to parse RSS streams

        #
        ModuleInstall("ecdsa", "pip"),
        ModuleInstall("pycrypto", "exe_xd", mname="Crypto"),
        ModuleInstall("paramiko", "pip"),
        #
        ModuleInstall("pattern", "pip") if sys.version_info[
            0] < 3 else None,  # to read dbase format
        #
        ModuleInstall("nodeenv", "pip"),   # node.js
        ModuleInstall("pbr", "pip"),
        ModuleInstall("python-jenkins", "pip", mname="jenkins"),  # for Jenkins
        ModuleInstall("psutil", "wheel"),  #
        #
        # 2015-02-05
        #
        ModuleInstall("autopy3", "wheel", mname="autopy3"),  # simulate events
        ModuleInstall("bigfloat", "wheel"),  # large double
        # convex optimization, depends on CVXOPT
        ModuleInstall("scs", "wheel"),
        ModuleInstall("ecos", "wheel"),
        ModuleInstall("cvxpy", "wheel"),
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
        ModuleInstall("pep8", "pip", version="1.5.7"),
        ModuleInstall("autopep8", "pip"),
        ModuleInstall("pybrain", "pip"),
        ModuleInstall("pymc", "wheel"),
        # ModuleInstall("libsvm", "wheel"),   # does not work on Windows
        # ModuleInstall("HDDM", "wheel", mname="hddm"),  # Bayesian, does not
        # work, it expects to have pymc with some optimization
        ModuleInstall("bayespy", "pip"),  # Bayesian
        # ModuleInstall("kabuki", "pip"),  # Bayesian, does not work, it expects to have pymc with some optimization
        #
        #
        ModuleInstall("glueviz", "wheel"),
        ModuleInstall("pypiserver", "pip"),
        #
        ModuleInstall("charts", "pip"),  # javascript graphs
        #
        ModuleInstall("jedi", "pip"), 
        ModuleInstall("docopt", "pip"), 
        ModuleInstall("markdown2", "pip"), 
        #ModuleInstall("rodeo", "pip"), 

    ]

    if sys.platform.startswith("win"):
        mod.append(ModuleInstall("pywin32", "wheel", mname="win32com"))
        mod.append(ModuleInstall("winshell", "pip"))

    return [_ for _ in mod if _ is not None]


def installation_teachings():
    """
    Modules used for teachings.
    """
    mod = [
        ModuleInstall("pyquickhelper", "pip"),
        ModuleInstall("pyensae", "pip"),
        ModuleInstall("ensae_teaching_cs", "pip"),
        ModuleInstall("actuariat_python", "pip"),
        ModuleInstall("pymmails", "pip"),
        ModuleInstall("pymyinstall", "pip"),
        ModuleInstall("pyrsslocal", "pip"),
        ModuleInstall("code_beatrix", "pip"),
    ]
    #
    return mod


def installation_cubes():
    """
    A cube is a multidimensional array.
    This functions gathers the dependencies for module `cubes <https://github.com/Stiivi/cubes>`_
    (`documentation <http://cubes.databrewery.org/dev/doc/>`_)
    and `cubesviewer <https://github.com/jjmontesl/cubesviewer>`_.

    """
    mod = [
        ModuleInstall("python-dateutil", "pip", "dateutil"),
        ModuleInstall("django", "pip"),
        ModuleInstall("pytz", "pip"),
        ModuleInstall("jsonschema", "pip"),
        # the PyPI version does not work with Python 3
        ModuleInstall("cubes", "github", "Stiivi"),
    ]

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
