"""
@file
@brief Various functions to install `InkScape <https://inkscape.org/>`_.
"""
from __future__ import print_function
import sys
import os
import re
from ..installhelper.install_cmd_helper import run_cmd
from .install_custom import download_page, download_file


def install_inkscape(dest_folder=".", fLOG=print, install=True, version=None):
    """
    Installs `InkScape <https://inkscape.org/en/>`_ (only on Windows).

    @param      dest_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      version         version to install (unused)
    @return                     temporary file

    """
    if version is not None:
        raise ValueError("cannot specify a version")
    if not sys.platform.startswith("win"):
        raise NotImplementedError(
            "MinGW can only be installed on Windows at the moment")

    link = "https://inkscape.org/en/download/windows/"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("href=\\\"(.*x64[.]msi)\\\"")
        alls = reg.findall(page)
        if len(alls) == 0:
            raise RuntimeError(
                "unable to find a link on a .exe file on page: " +
                page)

        url = alls[0]
        outfile = os.path.join(dest_folder, url.split("/")[-1])
        if not os.path.exists(outfile):
            fLOG("[pymy] download ", url)
            local = download_file(url, outfile)
        else:
            return outfile
        if install:
            run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
