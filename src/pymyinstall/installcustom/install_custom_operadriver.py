"""
@file
@brief Various functions to install `MinGW <http://www.mingw.org/>`_.
"""
from __future__ import print_function
import sys
import os
import re

from .install_custom import download_page, download_file
from ..installhelper.install_cmd_helper import unzip_files


def install_operadriver(dest_folder=".", fLOG=print, install=True, version=None):
    """
    Installs `operadriver <https://github.com/operasoftware/operachromiumdriver/releases>`_.

    @param      dest_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      version         version to install (unused)
    @return                     zip file in a list or list of unzipped files

    This is required for `Selenium <https://selenium-python.readthedocs.io/>`_.
    """
    if version is None:
        content = download_page(
            "https://github.com/operasoftware/operachromiumdriver/releases")
        reg = re.compile(
            "/tag/v([.][0-9]+[.][0-9]+)")
        f = reg.findall(content)
        if not f:
            raise Exception(
                "unable to get the last version number for OperaDriver")
        version = f[0]
    if sys.platform.startswith("win"):
        url = "https://github.com/operasoftware/operachromiumdriver/releases/download/v{0}/operadriver_win64.zip".format(
            version)
    elif sys.platform.startswith("mac"):
        url = "https://github.com/operasoftware/operachromiumdriver/releases/download/v{0}/operadriver_mac64.zip".format(
            version)
    else:
        url = "https://github.com/operasoftware/operachromiumdriver/releases/download/v{0}/operadriver_linux64.zip".format(
            version)
    name = url.split("/")[-1]

    outfile = os.path.join(dest_folder, name)
    fLOG("[pymy] operadriver, download from ", url)
    download_file(url, outfile, fLOG=fLOG)

    if install:
        return unzip_files(outfile, whereTo=dest_folder, fLOG=fLOG)
    else:
        return [outfile]
