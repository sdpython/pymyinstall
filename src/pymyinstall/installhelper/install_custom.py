# coding: latin-1
"""
@file
@brief Various function to install some application such as `pandoc <http://johnmacfarlane.net/pandoc/>`_.
"""
import sys, re, platform, os, urllib, urllib.request, imp, zipfile,time, subprocess

from .install_cmd import run_cmd, ModuleInstall, unzip_files
from .link_shortcuts import add_shortcut_to_desktop, suffix

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
    
    @param      url         url
    @param      outfile     outfile
    @return                 outfile
    """
    if os.path.exists(outfile):
        return outfile
        
    try :
        req = urllib.request.Request(url, headers= { 'User-agent': 'Mozilla/5.0' }, )
        u = urllib.request.urlopen(req)
        text = u.read()
        u.close()
    except urllib.error.HTTPError as e :
        raise Exception("unable to get archive from: " + url) from e
        
    with open(outfile,"wb") as f :
        f.write(text)
        
    return outfile
    
def download_from_sourceforge(url, outfile, fLOG = print, temp_folder = "."):
    """    
    download a file from a url using redirection, 
    the function does not download the file
    again if outfile already exists
    
    @param      url         url
    @param      outfile     outfile
    @param      fLOG        logging function
    @param      temp_folder only used if installation of module requests is needed
    @return                 outfile
    
    The function will install module `requests <http://docs.python-requests.org/en/latest/>`_ 
    if not present.
    """
    if os.path.exists(outfile):
        return outfile
        
    try :
        import requests
    except ImportError:
        fLOG("installing module requests")
        ModuleInstall ("requests", fLOG = fLOG).install(temp_folder = temp_folder)
        import requests
        
    try :
        req = requests.get(url, allow_redirects = True, stream=True)
        text = req.raw.read()
        fLOG("len ", len(text))
    except urllib.error.HTTPError as e :
        raise Exception("unable to get archive from: " + url) from e
        
    with open(outfile,"wb") as f :
        f.write(text)
        
    return outfile

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
        
def IsSciteInstalled(dest_folder):
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
        
def install_scite(dest_folder=".", fLOG = print, install = True):
    """
    install `SciTE <http://www.scintilla.org/SciTE.html>`_ (only on Windows)
    
    @param      dest_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @return                     temporary file
    
    @example(install SciTE)
    The function downloads the latest version of SciTE.
    It also changes some settings for Python (no tabs, Courier New as a police).
    @code
    install_scite("my_folder_for_scite")
    @endcode
    @endexample
    """
    if IsSciteInstalled(dest_folder):
        return os.path.join(os.path.abspath(dest_folder), "wscite", "SciTE.exe")
    
    if not sys.platform.startswith("win"):
        raise NotImplementedError("SciTE can only be installed on Windows at the moment")
    
    url = "http://www.scintilla.org/SciTEDownload.html"
    page = download_page(url)
    
    rel = re.compile ("Release ([0-9.]+)")
    rel = rel.findall(page)
    if len(rel) == 0 : raise Exception("unable to find the release version")
    rel = rel[0]
    fLOG("SciTE, release version ", rel)
    
    #reg = re.compile("<a href=\\\"(.*zip.*)\\\">full download</a>")
    #find = reg.findall(page)
    #if len(find) != 1 :
    #    raise Exception("unable to find the file to download at " + url + "\nfound: " + str(len(find)) + "\n" + "\n".join(find))
        
    newurl = "http://sourceforge.net/projects/scintilla/files/SciTE/{0}/wscite{1}.zip/download?use_mirror=autoselect".format(rel, rel.replace(".",""))
    outfile = os.path.join(dest_folder, "scite.zip")
    fLOG("SciTE, download from ", newurl)
    file = download_from_sourceforge(newurl, outfile, fLOG = fLOG, temp_folder = dest_folder)
    unzip_files(file, whereTo = dest_folder, fLOG = fLOG)
    
    # we change the path
    config = os.path.join(dest_folder, "wscite", "python.properties")
    with open(config,"r") as f : content = f.read()
    content = content.replace("=pythonw", "=" + sys.executable)
    with open(config,"w") as f : f.write(content)
    
    # we change the options
    config = os.path.join(dest_folder, "wscite", "SciTEGlobal.properties")
    with open(config,"r") as f : content = f.read()
    content = content.replace("tabsize=8", "tabsize=4")
    content = content.replace("indent.size=8", "indent.size=4")
    content = content.replace("use.tabs=1", "use.tabs=0")
    content = content.replace("font:Verdana,","font:Courier New,")
    with open(config,"w") as f : f.write(content)
    
    return os.path.join(os.path.abspath(dest_folder), "wscite", "SciTE.exe")
    
def add_shortcut_to_desktop_for_scite(scite):
    """
    create a shortcut on your desktop
    
    @param      scite      scite location (SciTE.exe
    @return                filename
    """
    ver = suffix()
    return add_shortcut_to_desktop(scite, "SciTE." + ver, "SciTE." + ver)
    
    
    
            
