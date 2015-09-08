"""
@file
@brief Various functions to install `Julia <http://www.julialang.org/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from .install_cmd_helper import run_cmd
from .install_custom import download_page, download_file


def get_julia_version():
    """
    returns the version of installed R,
    we only focus on the x64 version

    @return     tuple (bin, version), None if R is not installed
    """
    if sys.platform.startswith("win"):
        path = "{0}\\Julia".format(os.environ["ProgramFiles"])
        if os.path.exists(path):
            vers = os.listdir(path)
            vers.sort()
            if len(vers) == 0:
                return None
            vers = vers[-1]
            bin = os.path.join(path, vers, "bin", "x64")
            if not os.path.exists(bin):
                return None
            return (bin, vers)
        return
    else:
        raise NotImplementedError("not available on platform " + sys.platform)


def IsJuliaInstalled():
    """
    @return     True of False whether or not it was installed
    """
    r = get_julia_version()
    return r is not None


def install_julia(
        temp_folder=".", fLOG=print, install=True, force_download=False, version=None):
    """
    Install `R <http://www.r-project.org/>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of Julia
    @param      version         version to download (unused)
    @return                     temporary file
    """
    if version is not None:
        raise ValueError("cannot specify a version")
    bb = IsJuliaInstalled()
    if bb and not force_download:
        return True

    link = "http://julialang.org/downloads/"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile("href=\\\"(.*?win64[.]exe)\\\"")
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
        if install and not bb:
            run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
