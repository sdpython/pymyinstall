"""
@file
@brief Various functions to install `MinGW <http://www.mingw.org/>`_.
"""
from __future__ import print_function
import sys
import os

from .install_custom import download_from_sourceforge
from .install_custom import download_file


def install_vs(dest_folder=".", fLOG=print, install=True):
    """
    install `Visual Studio Express <https://www.visualstudio.com/en-us/products/visual-studio-express-vs.aspx>`_ (only on Windows)

    @param      dest_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @return                     temporary file

    """
    if not sys.platform.startswith("win"):
        raise NotImplementedError(
            "Visual Studio can only be installed on Windows at the moment")

    name = "vs_community.exe"
    newurl = "https://go.microsoft.com/?linkid=9863608"
    outfile = os.path.join(dest_folder, name)
    fLOG("Visual Studio, download from ", newurl)
    local = download_file(newurl, outfile)

    if install and not bb:
        run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
    return local
