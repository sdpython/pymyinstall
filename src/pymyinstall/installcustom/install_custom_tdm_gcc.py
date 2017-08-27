"""
@file
@brief Various functions to install `TDM-GCC <http://tdm-gcc.tdragon.net/>`_.
"""
from __future__ import print_function
import sys
import os
import re

from .install_custom import download_page, download_from_sourceforge


def install_tdm_gcc(dest_folder=".", fLOG=print, install=False, version=None):
    """
    install `TDM-GCC <http://tdm-gcc.tdragon.net/>`_ (only on Windows)

    @param      dest_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      version         version to download (unused)
    @return                     downloaded file

    It should
    ::

        mingw-get install binutils gcc g++ mingw32 fortran gdb mingw32 mingw w32api g77==3.4.5

    """
    if version is not None:
        raise ValueError("cannot specify a version")
    if not sys.platform.startswith("win"):
        raise NotImplementedError(
            "TDM-GCC can only be installed on Windows at the moment")

    url = "http://tdm-gcc.tdragon.net/download"
    page = download_page(url, is406=True)

    reg = re.compile(
        "<a href=\\\"http://sourceforge.net/projects/tdm-gcc/files/TDM-GCC[%]20Installer/(tdm64-.*?[.]exe)/download\\\"")
    find = reg.findall(page)
    if len(find) == 0:
        raise Exception("unable to find the file to download at " +
                        url + "\nfound: " + str(len(find)) + "\n" + "\n".join(find))
    name = find[0]

    newurl = "http://sourceforge.net/projects/tdm-gcc/files/TDM-GCC%20Installer/{0}/download?use_mirror=autoselect".format(
        name)
    outfile = os.path.join(dest_folder, name)
    fLOG("[pymy] tdm-gcc, download from ", newurl)
    file = download_from_sourceforge(
        newurl,
        outfile,
        fLOG=fLOG,
        temp_folder=dest_folder)

    if install:
        raise NotImplementedError()
    else:
        return file
