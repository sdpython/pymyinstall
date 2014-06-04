# coding: latin-1
"""
@file
@brief Various function to install some application such as `pandoc <http://johnmacfarlane.net/pandoc/>`_.
"""
import sys, re, platform, os, urllib, urllib.request, imp, zipfile,time, subprocess

from .install_cmd import run_cmd

def download_page(url):
    """
    download a page from a url
    
    @param      url     url
    @return             content
    """
    try :
        req = urllib.request.Request(url, headers= { 'User-agent': 'Mozilla/5.0' })
        u = urllib.request.urlopen(req)
        text = u.read()
        u.close()
    except urllib.error.HTTPError as e :
        raise Exception("unable to get archive from: " + zipurl) from e
        
    return str(text, encoding="utf8")
    
def download_file(url, outfile):
    """
    download a file from a url, the function does not download the file
    again if outfile already exists
    
    @param      url     url
    @param      outfile outfile
    @return             outfile
    """
    if os.path.exists(outfile):
        return outfile
        
    try :
        req = urllib.request.Request(url, headers= { 'User-agent': 'Mozilla/5.0' })
        u = urllib.request.urlopen(req)
        text = u.read()
        u.close()
    except urllib.error.HTTPError as e :
        raise Exception("unable to get archive from: " + url) from e
        
    with open(outfile,"wb") as f :
        f.write(text)
        
    return outfile

def install_pandoc(temp_folder=".", fLOG = print, install = True):
    """
    install `pandoc <http://johnmacfarlane.net/pandoc/>`_
    
    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @return                     temporary file
    """
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
            
