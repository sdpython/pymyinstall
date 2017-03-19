#-*- coding: utf-8 -*-
"""
@file
@brief Modules for Orange
"""
from ..installhelper.module_install import ModuleInstall


def orange_set():
    """
    modules implemented for Orange, it requires the modules in set *ml*
    """
    mod = [
        ModuleInstall(
            "bottlechest", "wheel2", purpose="Bottlechest is a fork of bottleneck specialized for use in Orange", usage="ORANGE"),
        ModuleInstall(
            "setuptools-git", "pip", mname="setuptools_git",
            purpose="This is a plugin for setuptools that enables git integration. Once installed, Setuptools " +
            "can be told to include in a package distribution all the files tracked by git. " +
            "This is an alternative to explicit inclusion specifications with MANIFEST.in."),
        ModuleInstall(
            "scikit-fusion", "pip", mname="skfusion",
            purpose="A Python module for data fusion built on top of factorized models."),
        ModuleInstall(
            "hyper", "pip",
            purpose="HTTP/2 Client for Python"),
        ModuleInstall(
            "orange3", "pip", mname="Orange",
            usage="ORANGE", purpose="Orange is a component-based data mining software. It includes a range of data visualization, exploration, " +
            "preprocessing and modeling techniques. It can be used through a nice and intuitive user interface or, for more advanced users, " +
            "as a module for the Python programming language."),
        ModuleInstall(
            "orange3-text", "pip", mname="orangecontrib.text", usage="ORANGE",
            purpose="Orange3 Text extends Orange3, a data mining software package, with common functionality for text mining. " +
            "It provides access to publicly available data, like NY Times, Twitter and PubMed. Further, it provides tools for preprocessing, " +
            "constructing vector spaces (like bag-of-words, topic modeling and word2vec) and visualizations like word cloud end geo map. " +
            "All features can be combined with powerful data mining techniques from the Orange data mining framework."),
        ModuleInstall(
            "orange3-associate", "pip", mname="orangecontrib.associate", usage="ORANGE",
            purpose="This module implements FP-growth [1] frequent pattern mining algorithm with bucketing " +
            "optimization [2] for conditional databases of few items."),
        # has a dependency on Orange (Python 2)
        # ModuleInstall(
        #     "orange3-datafusion", "pip", mname="orangecontrib.datafusion", usage="ORANGE",
        #     purpose="This is a data fusion add-on for [Orange3](http://orange.biolab.si). Add-on wraps scikit-fusion, " +
        #     "a Python library for data fusion, and implements a set of widgets for loading of the data, definition of data fusion schema, " +
        #     "collective matrix factorization and exploration of latent factors."),
        # ModuleInstall(
        #     "orange3-network", "github", "biolab", mname="orangecontrib.network", custom=["build", "install"], usage="ORANGE",
        # purpose="Orange Network is an add-on for Orange data mining software
        # package. It provides network visualization and analysis tools."),
        ModuleInstall(
            "Orange3-Network", "pip", mname="orangecontrib.network", usage="ORANGE",
            purpose="Orange Network is an add-on for Orange data mining software package. It provides network visualization and analysis tools."),
        ModuleInstall(
            "Orange3-ImageAnalytics", "pip", mname="orangecontrib.imageanalytics", usage="ORANGE",
            purpose="Orange3 add-on for image data mining."),
        # weird
        # ModuleInstall(
        #     "orange3-prototypes", "pip", mname="orangecontrib.prototypes", usage="ORANGE",
        #     purpose="Prototype Orange widgets. Only for the brave."),
        # weird
        # ModuleInstall(
        #     "orange3-spark", "pip", mname="orangecontrib.spark", usage="ORANGE",
        # purpose="A set of widgets for Orange data mining suite to work with
        # Apache Spark ML API."),
    ]
    #
    return [_ for _ in mod if _ is not None]
