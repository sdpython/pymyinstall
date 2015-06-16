#-*- coding: utf-8 -*-
"""
Helpers to install many modules for a specific usage.
"""
from __future__ import print_function
from ..installhelper.install_cmd_helper import add_shortcut_to_desktop_for_module
from ..installhelper.install_manual import get_install_list
from .packaged_config import complete_installation, small_installation, installation_huge_datasets, installation_azure
from .packaged_config import installation_ensae, installation_teachings
from ..installhelper.install_custom_scite import install_scite, add_shortcut_to_desktop_for_scite
from ..installhelper.install_custom_pandoc import install_pandoc
from ..installhelper.install_custom_sqlitespy import install_sqlitespy, add_shortcut_to_desktop_for_sqlitespy
from ..setuphelper.ipython_helper import setup_ipython, add_shortcut_to_desktop_for_ipython


def datascientist(folder="install",
                  modules=True,
                  azure=False,
                  teachings=False,
                  website=False,
                  scite=False,
                  pandoc=False,
                  ipython=False,
                  sqlitespy=False,
                  shortcuts=False,
                  ipython_folder=".",
                  fLOG=print,
                  browser=None,
                  skip=None,
                  full=False,
                  ensae=False,
                  additional_path=None,
                  download_only=False,
                  list_only=False):
    """

    install all necessary modules for a data scientist

    @param      additional_path     additional paths to add to ipython (a list)
    @param      folder              where to install everything
    @param      modules             go through the list of necessary modules
    @param      azure               add modules for Azure (Blob Storage)
    @param      teachings           add modules for teachings
    @param      ensae               add modules for ENSAE
    @param      website             open website when the routine to install a software is not implemented yet
    @param      scite               install Scite (and modify the config file to remove tab, adjust python path)
    @param      ipython             setup ipython
    @param      ipython_folder      current folder for ipython
    @param      sqlitespy           install SQLiteSpy
    @param      pandoc              install pandoc
    @param      shortcuts           add shortcuts on the desktop (scite, ipython, spyder)
    @param      browser             browser to use for the notebooks if not the default one (ie, firefox, chrome)
    @param      skip                to skip some modules if they fail (a list)
    @param      full                if True, install many modules including the ones used to generate the documentation
    @param      fLOG                logging function
    @param      download_only       only download the module, do not install
    @param      list_only           return the list of modules, no download, no install
    @return                         the list of installed modules

    @example(Install many things for a Data Scientist)
    @code
    from pymyinstall import datascientist
    datascientist ("install", full=True)
    @endcode
    @endexample

    If you run this command from the python interpreter::

        >>> from pymyinstall import datascientist
        >>> datascientist ("install")

    The module installed with pip do not appear in the list of available modules
    unless the python interpreter is started again. The best way is to run those two commands
    from the Python IDLE and to restart the interpreter before a second run.
    The second time, the function does not install again what was already installed.
    """
    res = []

    if modules:
        modules = complete_installation() if full else small_installation()

        if list_only:
            res.extend(modules)
        else:
            for _ in modules:
                if skip is not None and (_.name in skip or _.mname in skip):
                    fLOG("skip module", _.name, " import name:", _.mname)
                else:
                    if download_only:
                        _.download(temp_folder=folder)
                    else:
                        _.install(temp_folder=folder)
                    res.append(_)

    if azure:
        modules = installation_azure()

        if list_only:
            res.extend(modules)
        else:
            for _ in modules:
                if skip is not None and (_.name in skip or _.mname in skip):
                    fLOG("skip module", _.name, " import name:", _.mname)
                else:
                    if download_only:
                        _.download(temp_folder=folder)
                    else:
                        _.install(temp_folder=folder)
                    res.append(_)

    if ensae:
        modules = installation_ensae()

        if list_only:
            res.extend(modules)
        else:
            for _ in modules:
                if skip is not None and (_.name in skip or _.mname in skip):
                    fLOG("skip module", _.name, " import name:", _.mname)
                else:
                    if download_only:
                        _.download(temp_folder=folder)
                    else:
                        _.install(temp_folder=folder)
                    res.append(_)

    if teachings:
        modules = installation_teachings()

        if list_only:
            res.extend(modules)
        else:
            for _ in modules:
                if skip is not None and (_.name in skip or _.mname in skip):
                    fLOG("skip module", _.name, " import name:", _.mname)
                else:
                    if download_only:
                        _.download(temp_folder=folder)
                    else:
                        _.install(temp_folder=folder)
                    res.append(_)

    if list_only:
        return res

    if website:
        get_install_list()

    if scite:
        scite = install_scite(folder, fLOG=fLOG)

    if pandoc:
        install_pandoc(folder, fLOG=fLOG)

    if ipython:
        setup_ipython(
            ipython_folder,
            additional_path=additional_path,
            browser=browser)

    if sqlitespy:
        sqlitespy_file = install_sqlitespy(folder, fLOG=fLOG)

    if shortcuts:
        if ipython:
            add_shortcut_to_desktop_for_ipython(ipython_folder)
        if scite:
            add_shortcut_to_desktop_for_scite(scite)
        if ipython:
            add_shortcut_to_desktop_for_module("spyder")
        if sqlitespy:
            add_shortcut_to_desktop_for_sqlitespy(sqlitespy_file)

    return res


def ds_complete(**params):
    """
    calls @see fn datascientist with ``full=True``
    """
    params = params.copy()
    params["full"] = True
    datascientist(**params)


def ds_small(**params):
    """
    calls @see fn datascientist with ``full=False``
    """
    params = params.copy()
    params["full"] = False
    datascientist(**params)


def ds_teach(**params):
    """
    calls @see fn datascientist with ``full=False, teachings=True``
    """
    params = params.copy()
    params["full"] = True
    params["teachings"] = True
    datascientist(**params)


def ds_ensae(**params):
    """
    calls @see fn datascientist with ``full=False, teachings=True, ensae=True``,
    """
    params = params.copy()
    params["full"] = True
    params["ensae"] = True
    params["teachings"] = True
    datascientist(**params)


def ds_huge(folder="install",
            modules=True,
            skip=None,
            fLOG=print):
    """
    Install all the necessary modules to manipulate huge datasets.

    @param      folder              where to install everything
    @param      modules             go through the list of necessary modules
    @param      skip                to skip some modules if they fail (a list)
    @param      fLOG                logging function
    """
    if modules:
        modules = installation_huge_datasets()

        for _ in modules:
            if skip is not None and (_.name in skip or _.mname in skip):
                fLOG("skip module", _.name, " import name:", _.mname)
            else:
                _.install(temp_folder=folder)


def process_installation(
        modules_list,
        folder="install",
        fLOG=print,
        skip=None,
        full=False,
        additional_path=None):
    """

    install all modules within a list

    @param      modules_list        install a list of modules
    @param      additional_path     additional paths to add to ipython (a list)
    @param      folder              where to install everything
    @param      skip                to skip some modules if they fail (a list)
    @param      full                if True, install many modules including the ones used to generate the documentation
    @param      fLOG                logging function

    @example(Extend Anaconda)
    @code
    from pymyinstall import process_installation, extend_anaconda
    process_installation(extend_anaconda(), full=True)
    @endcode
    @endexample

    If you run this command from the python interpreter::

        >>> from pymyinstall import datascientist
        >>> datascientist ("install")

    The module installed with pip do not appear in the list of available modules
    unless the python interpreter is started again. The best way is to run those two commands
    from the Python IDLE and to restart the interpreter before a second run.
    The second time, the function does not install again what was already installed.

    """
    for _ in modules_list:
        if skip is not None and (_.name in skip or _.mname in skip):
            fLOG("skip module", _.name, " import name:", _.mname)
        else:
            _.install(temp_folder=folder)
