"""
@file
@brief Various functions to install some application such as `scala-sbt <http://www.scala-sbt.org/download.html>`_.
"""
from __future__ import print_function
import sys
import re
import os

from ..installhelper.install_cmd_helper import run_cmd
from .install_custom import download_page, download_file


def install_scala_sbt(
        temp_folder=".", fLOG=print, install=True, force_download=False, version=None):
    """
    Install `scala-sbt <http://www.scala-sbt.org/download.html>`_.
    It does not do it a second time if it is already installed.

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

    link = "http://www.scala-sbt.org/download.html"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("href=\\\"(https://cocl.*?msi)\\\"")
        alls = reg.findall(page)
        if len(alls) == 0:
            raise Exception(
                "unable to find a link on a .msi file on page: " +
                page)

        file = alls[0]
        filel = file
        full = filel
        version = file.split("/")[-2]
        fLOG("scala-sbt, version ", version)
        outfile = os.path.join(temp_folder, full.split("/")[-1])
        if not outfile.endswith(".msi"):
            outfile += ".msi"
        fLOG("download ", full)
        local = download_file(full, outfile)
        if install and not bb:
            run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
