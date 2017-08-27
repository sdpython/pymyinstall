"""
@file
@brief Various functions to install `SQLiteSpy <http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index>`_.
"""
from __future__ import print_function
import sys
import re
import os

from ..installhelper.install_cmd_helper import unzip_files
from ..installhelper.link_shortcuts import add_shortcut_to_desktop
from .install_custom import download_page, download_from_sourceforge


def IsSQLiteSpyInstalled(dest_folder):
    """
    check if SQLiteSpy was already installed

    @param      dest_folder     where it was installed
    @return                     boolean
    """
    if sys.platform.startswith("win"):
        file = os.path.join(dest_folder, "SQLiteSpy.exe")
        return os.path.exists(file)
    else:
        raise NotImplementedError("not available on platform " + sys.platform)


def install_sqlitespy(temp_folder=".", fLOG=print, install=True, version=None):
    """
    Install `SQLiteSpy <http://www.yunqa.de/delphi/products/sqlitespy/index>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      version         version to install (unused)
    @return                     temporary file
    """
    if version is not None:
        raise ValueError("cannot specify a version")
    if IsSQLiteSpyInstalled(temp_folder):
        return os.path.join(temp_folder, "SQLiteSpy.exe")

    link = "http://www.yunqa.de/delphi/products/sqlitespy/index"
    page = download_page(link)
    if sys.platform.startswith("win"):
        reg = re.compile(
            "href=[\\\"'](https://www.yunqa.de/delphi/downloads/SQLiteSpy.*?[.]zip)[\\\"']")
        alls = reg.findall(page)
        if len(alls) == 0:
            raise Exception(
                "unable to find a link on a .zip file on page: " +
                page)

        file = alls[0].replace("&amp;", "&")
        full = file
        version = file.split("_")[-1].replace(".zip", "")
        fLOG("[pymy] SQLiteSpy, version ", version)
        outfile = os.path.join(
            temp_folder,
            "{0}_{1}.zip".format(
                "SQLiteSpy",
                version))
        fLOG("[pymy] download ", full)
        download_from_sourceforge(
            full,
            outfile,
            temp_folder=temp_folder,
            fLOG=fLOG)
        if install:
            files = unzip_files(outfile, temp_folder, fLOG=fLOG)
            local = [f for f in files if f.endswith(".exe")][0]
            return local
        else:
            return outfile
    else:
        raise NotImplementedError("not available on platform " + sys.platform)


def add_shortcut_to_desktop_for_sqlitespy(exe):
    """
    create a shortcut on your desktop

    @param      exe        exe location (SQLiteSpy.exe)
    @return                filename
    """
    return add_shortcut_to_desktop(exe, "SQLiteSpy", "SQLiteSpy")
