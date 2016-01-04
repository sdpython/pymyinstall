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
        "bokeh",
        "cartopy",
        "cvxopt",
        "cython",
        "cytoolz",
        "dask",
        "django",
        "fuel",
        "ggplot",
        "graphviz",
        "h5py",
        "ipyparallel",
        "keyring",
        "locket",
        "mpld3",
        "networkx",
        "partd",
        "picklable-itertools",
        "pillow",
        "progressbar2",
        "psutil",
        "pygal",
        "pygame",
        "pyximport",
        "rpy2",
        "seaborn",
        "shapefile",
        "smopy",
        "statsmodels",
        "toolz",
        "ujson",
        "rlpy",
        "wordcloud",
        #
        "pyquickhelper",
        "pyrsslocal"
        "pymmails",
        "pyensae",
        "ensae_teaching_cs",
        "code_beatrix",
        "actuariat_python",
        #"ensae_projects",
    ]

    from . import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
