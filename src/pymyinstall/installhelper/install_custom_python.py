"""
@file
@brief Various functions to install `python <http://www.python.org/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from .install_cmd_helper import run_cmd
from .install_custom import download_page, download_file


def install_python(
        temp_folder=".", fLOG=print, install=True, force_download=False):
    """
    Install `python <http://www.python.org/>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of pandoc
    @return                     temporary file

    The version is fixed to 3.4.3. and amd64.
    """
    link = "https://www.python.org/downloads/release/python-343/"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("href=\\\"(.*?amd64[.]msi)\\\"")
        alls = reg.findall(page)
        if len(alls) == 0:
            raise Exception(
                "unable to find a link on a .exe file on page: " +
                page)

        url = alls[0]
        full = url.split("/")[-1]
        outfile = os.path.join(temp_folder, full)
        fLOG("download ", url)
        local = download_file(url, outfile)
        if install:
            run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
