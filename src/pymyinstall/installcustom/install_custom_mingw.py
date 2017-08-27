"""
@file
@brief Various functions to install `MinGW <http://www.mingw.org/>`_.
"""
from __future__ import print_function
import sys
import os

from .install_custom import download_from_sourceforge


def install_mingw(dest_folder=".", fLOG=print, install=True, version=None):
    """
    install `MinGW <http://www.mingw.org/>`_ (only on Windows)

    @param      dest_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      version         version to install (unused)
    @return                     temporary file

    Packages to install:
        * gcc
        * g77 3.4.5
        * binutils
        * mingw-runtime
        * w32api
        * gcc-core - C compiler
        * gcc-g++ - C++ compiler
        * gcc-objc - Objective C compiler
        * gcc-gfortran - Fortran 90/95 compiler
        * gcc-java - Java compiler
        * gcc-ada - Ada compiler
        * mingw-gdb - Windows native build of GNU debugger
        * mingw32-make - Windows native build of GNU make
        * mingw-utils - Miscellaneous utilities

    ::

        mingw-get install binutils gcc g++ mingw32 fortran gdb mingw32 mingw w32api g77==3.4.5

    """
    if version is not None:
        raise ValueError("cannot specify a version")
    if not sys.platform.startswith("win"):
        raise NotImplementedError(
            "MinGW can only be installed on Windows at the moment")

    name = "mingw-get-setup.exe"
    newurl = "http://sourceforge.net/projects/mingw/files/Installer/{0}/download?use_mirror=autoselect".format(
        name)
    outfile = os.path.join(dest_folder, name)
    fLOG("[pymy] mingw, download from ", newurl)
    file = download_from_sourceforge(
        newurl,
        outfile,
        fLOG=fLOG,
        temp_folder=dest_folder)

    if install:
        raise NotImplementedError()
    else:
        return file
