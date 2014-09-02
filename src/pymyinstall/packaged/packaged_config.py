"""
@file
@brief Defines differents set of modules to install.
"""
import sys
from ..installhelper.install_cmd import ModuleInstall

def small_installation():
    """
    returns a list of modules to work with pandas and ipython.
    
    @return             a list of modules to install
    
    To install them:
    @code
    for _ in complete_installation() :
        _.install(temp_folder="install")
    @endcode
    """
    mod = [   
                ModuleInstall("setuptools",     "exe"),
                ModuleInstall("pip",            "exe"),
                #
                ModuleInstall("six",            "pip"),
                ModuleInstall("lxml",           "exe"),
                ModuleInstall("jinja2",         "pip"),
                ModuleInstall("pygments",       "pip"),
                ModuleInstall("pyparsing",      "pip"),
                ModuleInstall("python-dateutil","pip", "dateutil"),
                ModuleInstall("html5lib",       "pip"),
                ModuleInstall("beautifulsoup4", "pip", mname="bs4"),
                ModuleInstall("coverage",       "pip"),
                ModuleInstall("pytz",           "pip"),
                ModuleInstall("pyreadline",     "pip",mname="pyreadline"),
                ModuleInstall("husl",           "pip"),
                #
                ModuleInstall("openpyxl",       "pip", version="1.8.6"),
                # 
                ModuleInstall("tornado",        "exe"),
                ModuleInstall("pyzmq",          "exe", mname="zmq"),
                #
                ModuleInstall("pycparser",      "exe"),
                ModuleInstall("Cython",         "exe"),
                ModuleInstall("numpy",          "exe"),
                ModuleInstall("matplotlib",     "exe"),
                ModuleInstall("scipy",          "exe"),
                ModuleInstall("statsmodels",    "exe"),  # needs scipy
                ModuleInstall("networkx",       "exe"),
                ModuleInstall("graphviz",       "pip"),
                #
                ModuleInstall("pandas",         "exe"),
                ModuleInstall("scikit-learn",   "exe", mname="sklearn"),
                ModuleInstall("ipython",        "exe"),
                #
                ModuleInstall("ggplot",         "pip"),  # needs statsmodels
                ModuleInstall("mpld3",          "pip"),
                #
                ModuleInstall("pyquickhelper",  "github", "sdpython"),
                ModuleInstall("pyensae",        "github", "sdpython"),
                ModuleInstall("ensae_teaching_cs", "github", "sdpython"),
                #
                ModuleInstall("typecheck-decorator", "github", "prechelt", mname="typecheck"),
                #
                ModuleInstall("requests",       "pip"),
                #ModuleInstall("PyQt",           "exe", mname="PyQt4"),
                ModuleInstall("PySide",         "exe"),
                ModuleInstall("spyder",         "exe", script="spyder.bat"),
                #
                #
                ModuleInstall("dbfread",        "pip"),   # to read dbase format
                ]
    
    if sys.platform.startswith("win"):
        mod.append ( ModuleInstall("pywin32",   "exe", mname = "win32com") )
        mod.append ( ModuleInstall("winshell",  "pip") )
    
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
                ModuleInstall("virtualenv",     "exe"),
                ModuleInstall("setuptools",     "exe"),
                ModuleInstall("pip",            "exe"),
                ModuleInstall("typecheck-decorator", "pip", mname="typecheck"),
                #
                ModuleInstall("six",            "pip"),
                ModuleInstall("lxml",           "exe"),
                ModuleInstall("jinja2",         "pip"),
                ModuleInstall("pygments",       "pip"),
                ModuleInstall("pyparsing",      "pip"),
                ModuleInstall("python-dateutil","pip", "dateutil"),
                ModuleInstall("html5lib",       "pip"),
                ModuleInstall("beautifulsoup4", "pip", mname="bs4"),
                ModuleInstall("coverage",       "pip"),
                ModuleInstall("pytz",           "pip"),
                ModuleInstall("SQLAlchemy",     "exe"),
                ModuleInstall("flask-sqlalchemy","pip",mname="flask.ext.sqlalchemy"),
                ModuleInstall("pyreadline",     "pip",mname="pyreadline"),
                ModuleInstall("simplejson",     "exe"),
                ModuleInstall("husl",           "pip"),
                #
                ModuleInstall("openpyxl",       "pip", version="1.8.6"),
                ModuleInstall("python-pptx",    "github", "sdpython"),
                ModuleInstall("XlsxWriter",     "pip"),
                # 
                ModuleInstall("tornado",        "exe"),
                ModuleInstall("flask",          "pip"),
                ModuleInstall("pyzmq",          "exe", mname="zmq"),
                #
                ModuleInstall("pycparser",      "exe"),
                ModuleInstall("Cython",         "exe"),
                ModuleInstall("cffi",           "exe"),
                ModuleInstall("numpy",          "exe"),
                ModuleInstall("blaze",          "exe"),
                ModuleInstall("scipy",          "exe"),
                ModuleInstall("matplotlib",     "exe"),
                ModuleInstall("tables",         "exe", mname="tables"),
                ModuleInstall("sympy",          "pip"),
                ModuleInstall("gmpy2",          "exe"),
                ModuleInstall("llvmpy",         "exe", mname="llvm"),
                ModuleInstall("numba",          "exe"),
                ModuleInstall("networkx",       "exe"),
                ModuleInstall("graphviz",       "pip"),
                #
                ModuleInstall("pandas",         "exe"),
                ModuleInstall("scikit-learn",   "exe", mname="sklearn"),
                ModuleInstall("scikit-image",   "exe", mname="skimage"),
                ModuleInstall("patsy",          "pip"),
                ModuleInstall("statsmodels",    "exe"),  # needs scipy
                ModuleInstall("ipython",        "exe"),
                ModuleInstall("cvxopt",         "exe"),
                ModuleInstall("pymc",           "exe"),
                ModuleInstall("PyWavelets",     "exe", mname="pywt"),
                #
                ModuleInstall("ggplot",         "pip"),  # needs statsmodels
                ModuleInstall("d3py",           "github", "sdpython"),
                ModuleInstall("mpld3",          "pip"),
                ModuleInstall("prettyplotlib",  "pip"),
                ModuleInstall("bokeh",          "pip"),
                ModuleInstall("pyshp",          "pip", mname="shapefile"), # needed by shapely
                ModuleInstall("Shapely",        "exe", mname="shapely"),  # exe on Windows to get geos.dll
                ModuleInstall("vispy",          "pip"),
                #
                #ModuleInstall("tessera-client", "github", "sdpython", mname="tessera_client"),  
                #ModuleInstall("tessera",        "github", "sdpython"),   # does not really work yet
                #
                ModuleInstall("rpy2",           "exe"),
                #ModuleInstall("pythonnet",      "exe", mname="clr"),  # included in ensae_teaching_cs
                #
                ModuleInstall("pyquickhelper",  "github", "sdpython"),
                ModuleInstall("pyensae",        "github", "sdpython"),
                ModuleInstall("ensae_teaching_cs", "github", "sdpython"),
                #
                ModuleInstall("typecheck-decorator", "github", "prechelt", mname="typecheck"),
                #
                ModuleInstall("selenium",       "pip"),
                ModuleInstall("Pillow",         "exe", mname = "PIL"),
                ModuleInstall("pygame",         "exe"),
                ModuleInstall("markupsafe",     "pip"),
                ModuleInstall("requests",       "pip"),
                ModuleInstall("Kivy",           "exe"),
                #ModuleInstall("PyQt",           "exe", mname="PyQt4"),
                ModuleInstall("PySide",         "exe"),
                ModuleInstall("spyder",         "exe", script="spyder.bat"),
                #
                ModuleInstall("py4j",           "pip"),
                ModuleInstall("python-igraph",  "exe", mname="igraph"),
                #
                ModuleInstall("luigi",          "pip"),
                #
                ModuleInstall("basemap",        "exe", mname="mpl_toolkits.basemap"),
                #ModuleInstall("Cartopy",        "exe", mname="cartopy"),
                ModuleInstall("smopy",          "pip"),
                ModuleInstall("folium",         "github", "sdpython"),
                #
                ModuleInstall("sphinx",         "pip"),
                ModuleInstall("sphinxcontrib-fancybox",     "pip", mname="sphinxcontrib.fancybox"),
                ModuleInstall("sphinx_rtd_theme",           "pip"),
                ModuleInstall("sphinxjp.themes.basicstrap", "pip"),
                ModuleInstall("solar_theme",                "pip"),
                ModuleInstall("cloud_sptheme",              "pip"),
                ModuleInstall("sphinx_readable_theme",      "pip"),
                ModuleInstall("hachibee-sphinx-theme",      "pip", mname="hachibee_sphinx_theme"),            
                ModuleInstall("wild_sphinx_theme",          "pip"),
                ModuleInstall("sphinx_bootstrap_theme",     "pip"),
                ModuleInstall("sphinxjp.themes.revealjs",   "github", "sdpython"),
                
                
                #
                ModuleInstall("dbfread",                    "pip"),   # to read dbase format
                ModuleInstall("antlr4-python3-runtime",     "pip", mname="antlr4"),
                #ModuleInstall("unqlite",                    "pip"),   # key/value store (NoSQL)
                ModuleInstall("typecheck-decorator",        "pip", mname="typecheck"),
                
                #
                #ModuleInstall("pyrsslocal", "github", "sdpython"),
                #ModuleInstall("python-nvd3", "github", "sdpython"),
                #ModuleInstall("splinter", "github", "cobrateam"),
                #ModuleInstall("pypdf2", "pip"),
                #ModuleInstall("pdfminer", "pip"),
                #ModuleInstall("liblinear",      "exe"),
                #ModuleInstall("lsqfit",      "exe"),
                #ModuleInstall("marisa-trie",      "exe", mname="marisa_trie"),
                #ModuleInstall("boost_python",   "exe"),
                ]
    
    if sys.platform.startswith("win"):
        mod.append ( ModuleInstall("pywin32",   "exe", mname = "win32com") )
        mod.append ( ModuleInstall("winshell",  "pip") )
    
    return mod

def installation_cubes():
    """
    A cube is a multidimensional array.
    This functions gathers the dependencies for module `cubes <https://github.com/Stiivi/cubes>`_
    (`documentation <http://cubes.databrewery.org/dev/doc/>`_)
    and `cubesviewer <https://github.com/jjmontesl/cubesviewer>`_.
    
    """
    mod = [   
                ModuleInstall("python-dateutil","pip", "dateutil"),
                ModuleInstall("django",         "pip"),
                ModuleInstall("pytz",           "pip"),
                ModuleInstall("jsonschema",     "pip"),
                ModuleInstall("cubes",          "github", "Stiivi"),  # the PyPI version does not work with Python 3
            ]
            
    return mod
    
def installation_huge_datasets():
    """
    Modules to handle huge datasets on disk, hierarchical datasets.
    
    """
    mod = [   
                ModuleInstall("h5py",           "exe"),
                ModuleInstall("blosc",          "exe"),
                ModuleInstall("numexpr",        "exe"),
                ModuleInstall("tables",         "exe"),
            ]
            
    return mod

    