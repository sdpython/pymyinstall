"""
@file
@brief Various functions to install some applications such as `7z <http://www.7-zip.org/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from ..installhelper.install_cmd_helper import run_cmd, unzip_files
from .install_custom import download_page, download_file


def install_graphviz(temp_folder=".", fLOG=print, install=True,
                     force_download=False, version=None, source=None):
    """
    Install `Graphviz <http://www.graphviz.org/>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of Graphviz
    @param      version         specify a version (unused)
    @param      source          change the source
    @return                     temporary file
    """
    if version is not None:
        raise ValueError("cannot specify a version")
    if sys.platform.startswith("win"):
        if source == "2":
            url = "http://www.xavierdupre.fr/enseignement/setup/"
            full = "graphviz-2.38.msi"
            url += full
            outfile = os.path.join(temp_folder, full)
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)
        elif source == "zip":
            url = "http://www.xavierdupre.fr/enseignement/setup/"
            full = "Graphviz.zip"
            url += full
            outfile = os.path.join(temp_folder, full)
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)
        else:
            link = "http://www.graphviz.org/Download_windows.php"
            repl = "http://www.graphviz.org"
            page = download_page(link)
            reg = re.compile("href=\\\"(.*?[.]msi)\\\"")
            alls = reg.findall(page)
            if len(alls) == 0:
                raise ValueError(
                    "unable to find a link on a .msi file on page: " +
                    page)

            url = repl + alls[0]
            full = url.split("/")[-1]
            outfile = os.path.join(temp_folder, full)

        fLOG("[pymy] download ", url)
        local = download_file(url, outfile)
        if install:
            if source == "zip":
                fLOG("[pymy] dest ", os.path.abspath(temp_folder))
                unzip_files(local, temp_folder, fLOG=fLOG)
            else:
                run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
