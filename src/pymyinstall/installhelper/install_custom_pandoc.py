# coding: latin-1
"""
@file
@brief Various function to install some application such as `pandoc <http://johnmacfarlane.net/pandoc/>`_.
"""
import sys, re, platform, os, urllib, urllib.request, imp, zipfile,time, subprocess

from .install_cmd import run_cmd, ModuleInstall, unzip_files
from .install_custom import download_page
from .link_shortcuts import add_shortcut_to_desktop, suffix

def IsPandocInstalled():
    """
    @return     True of False whether or not it was installed
    """
    if sys.platform.startswith("win"):
        path = r"C:\Users\{0}\AppData\Local\Pandoc\pandoc.exe".format(os.environ["USERNAME"])
        return os.path.exists(path)
    else:
        raise NotImplementedError("not available on platform " + sys.platform)

def install_pandoc(temp_folder=".", fLOG = print, install = True):
    """
    Install `pandoc <http://johnmacfarlane.net/pandoc/>`_.
    It does not do it a second time if it is already installed.
    
    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @return                     temporary file
    """
    if IsPandocInstalled():
        return True
        
    link  = "https://github.com/jgm/pandoc/releases/latest"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("href=\\\"(.*?[.]msi)\\\"") 
        all = reg.findall(page)
        if len(all) == 0 :
            raise Exception("unable to find a link on a .msi file on page: " + url)

        file = all[0].split("/")[-1]
        filel = "https://github.com/jgm/pandoc/releases/download/{0}/pandoc-{1}-windows.msi"
        version = file.replace("pandoc-","").replace("-windows.msi","")
        fLOG("pandoc, version ", version)
        vershort = version.split("-")[0]
        full = filel.format(vershort, version)
        outfile = os.path.join( temp_folder, full.split("/")[-1])
        fLOG("download ", full)
        local = download_file(full, outfile)
        if install :
            run_cmd("msiexec /i " + local,fLOG=fLOG,wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
        
    
            
