"""
@file
@brief Various functions to install `python <http://www.python.org/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from .install_cmd_helper import run_cmd, python_version
from .install_custom import download_page, download_file


def install_python(
        temp_folder=".", fLOG=print, install=True, force_download=False, version=None):
    """
    Install `python <http://www.python.org/>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of python
    @param      version         version to download (by default the current version of Python)
    @return                     temporary file

    The version is fixed to the current version of Python and amd64.
    """
    if version is None:
        version = "%s.%s.%s" % sys.version_info[:3]
    link = "https://www.python.org/downloads/release/python-%s/" % version.replace(
        ".", "")
    page = download_page(link)
    if sys.platform.startswith("win"):
        o, b = python_version()
        if "32" in b:
            reg = re.compile("href=\\\"(.*?[.]msi)\\\"")
            alls = reg.findall(page)
            alls = [_ for _ in alls if "amd64" not in _]
        else:
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
