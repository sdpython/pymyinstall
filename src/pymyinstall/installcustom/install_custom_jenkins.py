"""
@file
@brief Various functions to install `Jenkins <http://jenkins-ci.org/>`_.

.. versionadded:: 1.1
"""
from __future__ import print_function
import sys
import re
import os

from ..installhelper.install_cmd_helper import unzip_files
from .install_custom import download_page, download_from_sourceforge, download_file
from ..installhelper.link_shortcuts import add_shortcut_to_desktop, suffix

if sys.version_info[0] == 2:
    from codecs import open


def install_jenkins(dest_folder=".", fLOG=print, install=True, version=None):
    """
    install `Jenkins <http://jenkins-ci.org/>`_ (only on Windows)

    @param      dest_folder         where to download the setup
    @param      fLOG                logging function
    @param      install             install (otherwise only download)
    @param      version             version to install (unused)
    @return                         temporary file

    .. versionadded:: 1.1
    """
    if version is not None:
        raise ValueError("cannot specify a version")

    if not sys.platform.startswith("win"):
        raise NotImplementedError(
            "SciTE can only be installed on Windows at the moment")

    url = "http://mirrors.jenkins-ci.org/windows/latest"

    outfile = os.path.join(dest_folder, "jenkins.zip")
    if not os.path.exists(outfile):
        download_file(url, outfile)

    if install:
        unzip_files(file, whereTo=dest_folder, fLOG=fLOG)
        return outfile
    else:
        return outfile
