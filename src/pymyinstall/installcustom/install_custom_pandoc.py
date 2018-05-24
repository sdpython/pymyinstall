"""
@file
@brief Various functions to install some application such as `pandoc <http://johnmacfarlane.net/pandoc/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from ..installhelper.install_cmd_helper import run_cmd
from .install_custom import download_page, download_file


def IsPandocInstalled():
    """
    @return     True of False whether or not it was installed
    """
    if sys.platform.startswith("win"):
        path = "{0}\\AppData\\Local\\Pandoc\\pandoc.exe".format(
            os.environ["USERPROFILE"])
        return os.path.exists(path)
    else:
        raise NotImplementedError("not available on platform " + sys.platform)


def install_pandoc(
        temp_folder=".", fLOG=print, install=True, force_download=False, version=None):
    """
    Install `pandoc <http://johnmacfarlane.net/pandoc/>`_.
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
    bb = IsPandocInstalled()
    if bb and not force_download:
        return True

    link = "https://github.com/jgm/pandoc/releases"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("href=\\\"(.*?[.]msi)\\\"")
        alls = reg.findall(page)
        if len(alls) == 0:
            raise Exception(
                "unable to find a link on a .msi file on page: " +
                page)

        file = alls[0].split("/")[-1]
        filel = "https://github.com/jgm/pandoc/releases/download/{0}/pandoc-{0}-windows-x86_64.msi"
        version = file.replace("pandoc-", "").replace("-windows.msi", "")
        vershort = version.split("-")[0]
        fLOG("[pymy] pandoc, version ", vershort)
        full = filel.format(vershort)
        outfile = os.path.join(temp_folder, full.split("/")[-1])
        fLOG("[pymy] download ", full)
        local = download_file(full, outfile)
        if install and not bb:
            run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
