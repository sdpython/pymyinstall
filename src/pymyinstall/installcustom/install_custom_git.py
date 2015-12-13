"""
@file
@brief Various functions to install some applications such as `Git <http://www.git-scm.com/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from ..installhelper.install_cmd_helper import run_cmd
from .install_custom import download_page, download_file


def install_git(
        temp_folder=".", fLOG=print, install=True, force_download=False, version=None):
    """
    Install `Git <http://www.git-scm.com/>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of Git
    @param      version         specify a version (unused)
    @return                     temporary file
    """
    if version is not None:
        raise ValueError("cannot specify a version")
    if sys.platform.startswith("win"):
        link = "http://www.git-scm.com/download/win"
        page = download_page(link)
        reg = re.compile("href=\\\"(.*?64-bit[.]((msi)|(exe)))\\\"")
        alls = reg.findall(page)
        if len(alls) == 0:
            raise Exception(
                "unable to find a link on a .msi file on page: " + link + "\n" +
                page)

        url = alls[0][0]
        full = url.split("/")[-1]
        outfile = os.path.join(temp_folder, full)
        fLOG("download ", url)
        local = download_file(url, outfile)
        if install:
            run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
