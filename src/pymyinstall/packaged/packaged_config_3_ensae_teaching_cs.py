# -*- coding: utf-8 -*-
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
        "bayespy",
        "bkcharts",
        "bokeh",
        "cartopy",
        "click",
        "click_plugins",
        "cligj",
        "cloudpickle",
        "cvxopt",
        "cython",
        "cytoolz",
        "dask",
        "descartes",
        "django",
        "ete3",
        "fairtest",
        "feedparser",
        "fiona",
        "foolbox",
        "geopandas",
        "ggplot",
        "graphviz",
        "h5py",
        "html2text",
        "ipyparallel",
        "locket",
        "mlstatpy",
        "munch",
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
        "PyQt5",
        "PyQt5-sip",
        "pytables",
        "python_utils",
        "rpy2",
        "scikit-plot",
        "seaborn",
        "seasonal",
        "shapefile",
        "shapely",
        "sip",
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
        "manydataapi",
        "mlstatpy",
        "pyensae",
        "pyenbc",
        "pymmails",
        "pyrsslocal",
        "teachpyx",
        "tkinterquickhelper",
    ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
