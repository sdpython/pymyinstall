#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""


def ensae_teaching_cs_set():
    """
    list of modules needed to for *ensae_teaching_cs* (teaching at ENSAE)
    """
    from .packaged_config_1_pyensae import pyensae_set
    names = pyensae_set()
    names += [
        "asn1crypto",
        "basemap",
        "bayespy",
        "beautifulsoup4",
        "bokeh",
        "branca",
        "cartopy",
        "cffi",
        "cloudpickle",
        "cvxopt",
        "cython",
        "cytoolz",
        "dask",
        "django",
        "feedparser",
        "fuel",
        "ggplot",
        "graphviz",
        "h5py",
        "idna",
        "ipyparallel",
        "keyring",
        "locket",
        "mlstatpy",
        "mpld3",
        "natgrid",
        "networkx",
        "numexpr",
        "olefile",
        "partd",
        "patsy",
        "picklable-itertools",
        "pillow",
        "progressbar2",
        "psutil",
        "psycopg2",
        "pydub",
        "pygal",
        "pygame",
        "pylzma",
        "pyproj",
        "pytables",
        "python_utils",
        "requests_oauthlib",
        "rpy2",
        "seaborn",
        "shapefile",
        "shapely",
        "smopy",
        "statsmodels",
        "toolz",
        "ujson",
        "xarray",
        "wikipedia",
        "wordcloud",
        "wptools",
        "yaml",
        #
        "actuariat_python",
        "code_beatrix",
        "ensae_teaching_cs",
        "jupytalk",
        "jyquickhelper",
        "pyensae",
        "pymmails",
        "pyquickhelper",
        "pyrsslocal",
        #"ensae_projects",
    ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
