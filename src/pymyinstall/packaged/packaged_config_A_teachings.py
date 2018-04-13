# -*- coding: utf-8 -*-
"""
@file
@brief Defines a set of module for teaching purpose.
"""
from ..installhelper.module_install import ModuleInstall


def teachings_set():
    """
    modules implemented for my teachings, it requires the modules in set *ml*
    """
    mod = [
        ModuleInstall(
            "jyquickhelper", "pip", purpose="Helpers for Jupyter notebooks.", usage="TEACH"),
        ModuleInstall(
            "pyquickhelper", "pip", purpose="helpers to generation documentation", usage="TEACH"),
        ModuleInstall(
            "tkinterquickhelper", "pip", purpose="windows on the top of tkinter", usage="TEACH"),
        ModuleInstall(
            "pymyinstall", "pip", purpose="easy installation of modules including Windows", usage="TEACH"),
        ModuleInstall("pymmails", "pip",
                      purpose="read/send emails", usage="TEACH"),
        ModuleInstall(
            "pyensae", "pip", purpose="helpers, Hadoop, SQL, financial times series, ...", usage="TEACH"),
        ModuleInstall("pyrsslocal", "pip",
                      purpose="RSS readers", usage="TEACH"),
        ModuleInstall(
            "code_beatrix", "pip", purpose="teaching programming to kids, lesenfantscodaient.fr", usage="TEACH"),
        ModuleInstall(
            "actuariat_python", "pip", purpose="teachings, insurance examples", usage="TEACH"),
        ModuleInstall("ensae_teaching_cs", "pip",
                      purpose="teachings, introduction to programming, machine learning, map/reduce", usage="TEACH"),
        ModuleInstall("jupytalk", "pip",
                      purpose="materials for presentations", usage="TEACH"),
        ModuleInstall("mlstatpy", "pip",
                      purpose="materials for machine learning", usage="TEACH"),
        ModuleInstall("teachpyx", "pip",
                      purpose="materials for teachings", usage="TEACH"),
        ModuleInstall("ensae_projects", "pip",
                      purpose="single use code", usage="TEACH"),
        ModuleInstall("mlinsights", "pip",
                      purpose="mlinsights implements functions to get insights on machine learned models.", usage="TEACH"),
        ModuleInstall("lightmlrestapi", "pip",
                      purpose="lightmlrestapi implements a light machine learning REST API based on falcon.", usage="TEACH"),
        ModuleInstall("lightmlboard", "pip",
                      purpose="lightmlboard implements a light machine learning leaderboard based on tornado.", usage="TEACH"),
        ModuleInstall("mlprodicts", "pip",
                      purpose="mlprodict implements a couple of ways to productionize machine learning predictions.", usage="TEACH"),
        ModuleInstall("pandas_streaming", "pip",
                      purpose="pandas_streaming aims at processing big files with pandas, too big to hold in memory," +
                      "too small to be parallelized with a significant gain. The module replicates a subset of pandas " +
                      "API and implements other functionalities for machine learning.", usage="TEACH"),
    ]
    #
    return [_ for _ in mod if _ is not None]
