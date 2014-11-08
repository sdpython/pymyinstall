# coding: latin-1
"""
@file
@brief Various function to install some application such as `pandoc <http://johnmacfarlane.net/pandoc/>`_.
"""
import os, urllib, urllib.error, urllib.request

from .install_cmd import ModuleInstall

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
        raise Exception("unable to get archive from: " + url) from e

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

    if len(text) < 20 and text.decode("ascii").lower().startswith("bad request"):
        raise Exception("Bad Request for url: " + url)

    with open(outfile,"wb") as f :
        f.write(text)

    return outfile