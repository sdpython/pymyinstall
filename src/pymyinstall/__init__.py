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

__version__ = "0.3"
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
    
def datascientist(  folder = "install", 
                    modules = True, 
                    website = True, 
                    scite = True,
                    pandoc = True,
                    ipython = True,
                    ipython_folder = ".",
                    fLOG = print):
    """
    
    install all necessary modules for a data scientist
    
    @param      folder          where to install everything
    @param      modules         go through the list of necessary modules
    @param      website         open website when the routine to install a software is not implemented yet
    @param      scite           install Scite (and modify the config file to remove tab, adjust python path)
    @param      ipython         setup ipython
    @param      ipython_folder  current folder for ipython
    @param      pandoc          install pandoc
    
    @example(Install manything for a Data Scientist)
    @code
    from pymyinstall import datascientist
    datascientist ("install")
    @endcode
    @endexample
    
    """
    if modules :
        for _ in complete_installation() :
            _.install(temp_folder=folder)    

    if website :
        get_install_list()
        
    if scite :
        install_scite(folder, fLOG = fLOG)
    
    if pandoc :
        install_pandoc(folder, fLOG = fLOG)
        
    if ipython :
        setup_ipython(ipython_folder, fLOG = fLOG)
    
    
from .installhelper.install_cmd import run_cmd, ModuleInstall, complete_installation, unzip_files
from .installhelper.install_custom import install_pandoc, install_scite, download_from_sourceforge, download_file, download_page
from .installhelper.install_manual import get_install_list, open_tool_on_browser
from .setuphelper.ipython_helper import setup_ipython
