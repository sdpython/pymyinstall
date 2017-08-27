"""
@file
@brief Various functions to install `Java JDK <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_
"""
from __future__ import print_function
import sys
import re
import os

from ..installhelper.install_cmd_helper import run_cmd
from .install_custom import download_page, download_file
from .install_custom_exceptions import ManualDownloadException


def install_javajdk(
        temp_folder=".", fLOG=print, install=True, force_download=False, version=None):
    """
    Install `Java JDK <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of pandoc
    @param      version         version to install (unused)
    @return                     temporary file
    """
    if version is not None:
        raise ValueError("cannot specify a version")
    #bb = IsPandocInstalled()
    bb = False
    if bb and not force_download:
        return True

    link = "http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("(http.*?jdk.*?windows-x64[.]exe)")
        alls = reg.findall(page)
        if len(alls) == 0:
            raise Exception(
                "unable to find a link on a .exe file on page: " +
                page)

        file = alls[-1].split("/")[-1]
        version = file.split("-")[1]
        b18 = int(version.replace("8u", "")) + 18 - 66
        root = "http://download.oracle.com/otn-pub/java/jdk/{0}-b{1}/".format(
            version, b18)

        filel = root + file
        fLOG("[pymy] java-jdk, version ", version)
        vershort = version.split("-")[0]
        full = filel.format(vershort, version)
        outfile = os.path.join(temp_folder, full.split("/")[-1])
        fLOG("[pymy] download ", full)
        local = download_file(full, outfile)
        size = os.stat(local).st_size
        if size < 2 ** 20:
            raise ManualDownloadException(
                "You should directly download the file from:\n{0}".format(link))
        if install and not bb:
            run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
