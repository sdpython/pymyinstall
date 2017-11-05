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
        "basemap",
        "bayespy",
        "bkcharts",
        "bokeh",
        "cartopy",
        "cloudpickle",
        "cvxopt",
        "cython",
        "cytoolz",
        "dask",
        "django",
        "feedparser",
        "foolbox",
        "fuel",
        "ggplot",
        "graphviz",
        "h5py",
        "html2text",
        "ipyparallel",
        "locket",
        "mlstatpy",
        "mpld3",
        "natgrid",
        "numexpr",
        "partd",
        "patsy",
        "picklable-itertools",
        "pocket",
        "progressbar2",
        "psutil",
        "psycopg2",
        "pycurl",
        "pydub",
        "pygal",
        "pygame",
        "pylzma",
        "pyproj",
        "pytables",
        "python_utils",
        "rpy2",
        "seaborn",
        "seasonal",
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
        "ensae_projects",
        "ensae_teaching_cs",
        "jupytalk",
        "jyquickhelper",
        "mlstatpy",
        "pyensae",
        "pymmails",
        "pyrsslocal",
        "teachpyx",
        "tkinterquickhelper",
    ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
