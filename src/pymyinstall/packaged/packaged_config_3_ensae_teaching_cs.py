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
        "bokeh",
        "cartopy",
        "cvxopt",
        "cython",
        "cytoolz",
        "dask",
        "django",
        "ggplot",
        "graphviz",
        "ipyparallel",
        "keyring",
        "mpld3",
        "networkx",
        "pillow",
        "pygal",
        "pygame",
        "pyximport",
        "rpy2",
        "seaborn",
        "shapefile",
        "smopy",
        "toolz",
        "ujson",
    ]

    from . import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
