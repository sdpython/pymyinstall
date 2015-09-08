"""
@file
@brief Various functions to install some applications such as `7z <http://www.7-zip.org/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from .install_cmd_helper import run_cmd
from .install_custom import download_page, download_file


def install_7z(
        temp_folder=".", fLOG=print, install=True, force_download=False, version=None):
    """
    Install `7z <http://www.7-zip.org/>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of 7z
    @param      version         specify a version (unused)
    @return                     temporary file
    """
    if version is not None:
        raise ValueError("cannot specify a version")
    link = "http://www.7-zip.org/"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("href=\\\"(.*?[.]msi)\\\"")
        alls = reg.findall(page)
        if len(alls) == 0:
            raise Exception(
                "unable to find a link on a .msi file on page: " +
                page)

        url = link + alls[0]
        full = url.split("/")[-1]
        outfile = os.path.join(temp_folder, full)
        fLOG("download ", url)
        local = download_file(url, outfile)
        if install:
            run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
