"""
@file
@brief Various functions to install `Putty <http://www.putty.org/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from .install_custom import download_page, download_file

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def IsPuttyInstalled(dest_folder):
    """
    check if Scite was already installed

    @param      dest_folder     where it was installed
    @return                     boolean
    """
    if sys.platform.startswith("win"):
        file = os.path.join(dest_folder, "putty.exe")
        return os.path.exists(file)
    else:
        raise NotImplementedError("not available on platform " + sys.platform)


def install_putty(dest_folder=".", fLOG=print, install=True, version=None):
    """
    install `Putty <http://www.putty.org/>`_ (only on Windows)

    @param      dest_folder     where to download putty
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      version         version to install (unused)
    @return                     temporary file
    """
    if version is not None:
        raise ValueError("cannot specify a version")
    if IsPuttyInstalled(dest_folder):
        return os.path.join(
            os.path.abspath(dest_folder), "putty.exe")

    if not sys.platform.startswith("win"):
        raise NotImplementedError(
            "SciTE can only be installed on Windows at the moment")

    url = "http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html"
    page = download_page(url)

    reg = re.compile(
        "<a href=\\\"(.*latest/x86/putty.exe)\\\"><code>putty.exe</code></a>")
    find = reg.findall(page)
    if len(find) != 1:
        mes = "unable to find the file to download at {0}\nfound: {1}\npattern: {2}\nOUT:\n{3}".format(
            url, len(find), reg.pattern, "\n".join(find))
        raise Exception(mes)

    # should be something like http://www.scintilla.org/wscite356.zip
    newurl = find[0]
    outfile = os.path.join(dest_folder, "putty.exe")
    if not os.path.exists(outfile):
        download_file(newurl, outfile)

        if not os.path.exists(outfile):
            raise FileNotFoundError(outfile)

    return outfile
