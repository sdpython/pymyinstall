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
        ModuleInstall("networkx", "wheel"),  # it seems problematic for this
        # small config
        ModuleInstall("graphviz", "pip"),
        ModuleInstall("jsonschema", "pip"),
        ModuleInstall("mistune", "pip"),
        ModuleInstall("wheel", "pip"),
        # sphinx
        ModuleInstall("alabaster", "wheel"),
        ModuleInstall("Babel", "wheel"),
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
        ModuleInstall('sphinxjp.themes.revealjs', 'pip'),
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
    mod = small_installation() + [
        ModuleInstall('werkzeug', 'pip'),
        ModuleInstall('itsdangerous', 'pip'),
        ModuleInstall('SQLAlchemy', 'wheel', mname='sqlalchemy'),
        ModuleInstall('flask-sqlalchemy', 'pip', mname='flask.ext.sqlalchemy'),
        ModuleInstall('simplejson', 'wheel'),
        ModuleInstall('python-pptx', 'pip'),
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
        ModuleInstall('seaborn', 'pip'),
        ModuleInstall('sympy', 'pip'),
        ModuleInstall('gmpy2', 'wheel'),
        ModuleInstall('llvmpy', 'wheel', mname='llvm'),
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
        ModuleInstall('PyYAML', 'wheel', mname='yaml'),
        ModuleInstall('bokeh', 'pip'),
        ModuleInstall('pyshp', 'pip', mname='shapefile'),
        ModuleInstall('Shapely', 'wheel', mname='shapely'),
        ModuleInstall('vispy', 'pip'),
        ModuleInstall('rpy2', 'wheel'),
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
            'hachibee-sphinx-theme', 'pip', mname='hachibee_sphinx_theme'),
        ModuleInstall('wild_sphinx_theme', 'pip'),
        ModuleInstall('sphinx_bootstrap_theme', 'pip'),
        ModuleInstall('sphinxjp.themes.sphinxjp', 'pip'),
        ModuleInstall('sphinx_py3doc_enhanced_theme', 'pip'),
        ModuleInstall('epfl-sphinx-theme', 'pip', mname='epfl_theme'),
        ModuleInstall('python-linkedin', 'pip', mname='linkedin'),
        ModuleInstall('oauthlib', 'pip'),
        ModuleInstall('requests_oauthlib', 'pip'),
        ModuleInstall('antlr4-python3-runtime', 'pip', mname='antlr4'),
        ModuleInstall('pycontracts', 'pip', mname='contracts'),
        ModuleInstall('feedparser', 'wheel'),
        ModuleInstall('ecdsa', 'pip'),
        ModuleInstall('pycrypto', 'exe_xd', mname='Crypto'),
        ModuleInstall('paramiko', 'pip'),
        ModuleInstall('pbr', 'pip'),
        ModuleInstall('python-jenkins', 'pip', mname='jenkins'),
        ModuleInstall('psutil', 'wheel'),
        ModuleInstall('autopy3', 'wheel', mname='autopy3'),
        ModuleInstall('bigfloat', 'wheel'),
        ModuleInstall('scs', 'wheel'),
        ModuleInstall('ecos', 'wheel'),
        ModuleInstall('cvxpy', 'wheel'),
        ModuleInstall('blist', 'wheel'),
        ModuleInstall('conda', 'pip'),
        ModuleInstall('libLAS', 'wheel', mname='liblas'),
        ModuleInstall('liblinear', 'wheel'),
        ModuleInstall('marisa_trie', 'wheel'),
        ModuleInstall('mlpy', 'wheel'),
        ModuleInstall('pygit2', 'wheel'),
        ModuleInstall('pymongo', 'wheel'),
        ModuleInstall('PyOpenGL', 'wheel', mname='OpenGL'),
        ModuleInstall('Theano', 'wheel', mname='theano'),
        ModuleInstall('pyqtgraph', 'pip'),
        ModuleInstall('deap', 'pip'),
        ModuleInstall('boto', 'pip'),
        ModuleInstall('bz2file', 'pip'),
        ModuleInstall('smart_open', 'wheel'),
        ModuleInstall('gensim', 'wheel'),
        ModuleInstall('pybrain', 'pip'),
        ModuleInstall('pymc', 'wheel'),
        ModuleInstall('bayespy', 'pip'),
        ModuleInstall('glueviz', 'wheel'),
        ModuleInstall('charts', 'pip'),
        ModuleInstall('jedi', 'pip'),
        ModuleInstall('docopt', 'pip'),
        ModuleInstall('markdown2', 'pip'),
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
