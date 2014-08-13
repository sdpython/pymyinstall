#-*- coding: utf-8 -*-
"""
Documentation for this file.

To install a list of modules for a machine learner:
@code
from pymyinstall import complete_installation, install_scite, install_pandoc, open_tool_on_browser
for _ in complete_installation() :
    _.install(temp_folder="install")
install_scite("install")  
install_pandoc("install")
open_tool_on_browser()
@endcode
"""

__version__ = "0.5"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/pymyinstall"
__url__ = "http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#pymyinstall"
__license__ = "BSD License"


def check( log = False):
    """
    Checks the library is working.
    It raises an exception.
    If you want to disable the logs:
    
    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True
    
def datascientist(  folder          = "install", 
                    modules         = True, 
                    website         = True, 
                    scite           = True,
                    pandoc          = True,
                    ipython         = True,
                    sqlitespy       = True,
                    ipython_folder  = ".",
                    shortcuts       = True,
                    fLOG            = print,
                    browser         = None,
                    skip            = [],
                    full            = False,
                    additional_path = []):
    """
    
    install all necessary modules for a data scientist
    
    @param      additional_path     additional paths to add to ipython
    @param      folder              where to install everything
    @param      modules             go through the list of necessary modules
    @param      website             open website when the routine to install a software is not implemented yet
    @param      scite               install Scite (and modify the config file to remove tab, adjust python path)
    @param      ipython             setup ipython
    @param      ipython_folder      current folder for ipython
    @param      sqlitespy           install SQLiteSpy
    @param      pandoc              install pandoc
    @param      shortcuts           add shortcuts on the desktop (scite, ipython, spyder)
    @param      browser             browser to use for the notebooks if not the default one (ie, firefox, chrome)
    @param      skip                to skip some modules if they fail
    @param      full                if True, install many modules including the ones used to generate the documentation
    
    @example(Install manything for a Data Scientist)
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
    if modules :
        modules = complete_installation() if full else small_installation() 
        for _ in modules :
            if _.name in skip or _.mname in skip :
                fLOG("skip module", _.name, " import name:", _.mname)
            else :
                _.install(temp_folder=folder)    

    if website :
        get_install_list()
        
    if scite :
        scite = install_scite(folder, fLOG = fLOG)
    
    if pandoc :
        install_pandoc(folder, fLOG = fLOG)
        
    if ipython :
        setup_ipython(ipython_folder, additional_path=additional_path, browser = browser)
        
    if sqlitespy:
        sqlitespy_file = install_sqlitespy(folder, fLOG = fLOG)
        
    if shortcuts :
        if ipython  : add_shortcut_to_desktop_for_ipython(ipython_folder)
        if scite    : add_shortcut_to_desktop_for_scite(scite)
        if ipython  : add_shortcut_to_desktop_for_module("spyder")
        if sqlitespy: add_shortcut_to_desktop_for_sqlitespy(sqlitespy_file)
    
    
from .installhelper.install_cmd import run_cmd, ModuleInstall, complete_installation, unzip_files, add_shortcut_to_desktop_for_module, small_installation
from .installhelper.install_custom import download_from_sourceforge, download_file, download_page
from .installhelper.install_manual import get_install_list, open_tool_on_browser
from .setuphelper.ipython_helper import setup_ipython, add_shortcut_to_desktop_for_ipython
from .installhelper.link_shortcuts import add_shortcut_to_desktop
from .installhelper.install_custom_pandoc import install_pandoc
from .installhelper.install_custom_scite import install_scite, add_shortcut_to_desktop_for_scite
from .installhelper.install_custom_sqlitespy import install_sqlitespy, add_shortcut_to_desktop_for_sqlitespy
