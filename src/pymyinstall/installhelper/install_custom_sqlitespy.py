# coding: latin-1
"""
@file
@brief Various function to install some application such as `pandoc <http://johnmacfarlane.net/pandoc/>`_.
"""
import sys, re, platform, os, urllib, urllib.request, imp, zipfile,time, subprocess

from .install_cmd import run_cmd, ModuleInstall, unzip_files
from .link_shortcuts import add_shortcut_to_desktop, suffix
from .install_custom import download_page, download_file, download_from_sourceforge

def IsSQLiteSpyInstalled(dest_folder):
    """
    check if Scite was already installed
    
    @param      dest_folder     where it was installed
    @return                     boolean
    """
    if sys.platform.startswith("win"):
        file = os.path.join(dest_folder, "wscite", "SciTE.exe")
        return os.path.exists(file)
    else:
        raise NotImplementedError("not available on platform " + sys.platform)

def install_sqlitespy(temp_folder=".", fLOG = print, install = True):
    """
    Install `SQLiteSpy <http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index>`_.
    It does not do it a second time if it is already installed.
    
    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @return                     temporary file
    """
    if IsSQLiteSpyInstalled(temp_folder):
        return True
        
    link  = "http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("href=\\\"(/delphi/lib/exe.*?[.]zip)\\\"") 
        all = reg.findall(page)
        if len(all) == 0 :
            raise Exception("unable to find a link on a .zip file on page: " + url)

        file = all[0].replace("&amp;","&")
        full = "http://www.yunqa.de{0}".format(file)
        version = file.split("_")[-1].replace(".zip","")
        fLOG("SQLiteSpy, version ", version)
        outfile = os.path.join( temp_folder, "{0}_{1}.zip".format("SQLiteSpy", version))
        fLOG("download ", full)
        local = download_from_sourceforge(full, outfile, temp_folder = temp_folder, fLOG=fLOG)
        files = unzip_files(outfile, temp_folder, fLOG=fLOG)
        local = [ f for f in files if f.endswith(".exe") ][0]
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
        
def add_shortcut_to_desktop_for_sqlitespy(exe):
    """
    create a shortcut on your desktop
    
    @param      exe        exe location (SQLiteSpy.exe)
    @return                filename
    """
    return add_shortcut_to_desktop(scite, "SQLiteSpy", "SQLiteSpy")
    
    
            
