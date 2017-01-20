"""
@file
@brief Various functions to install `Jenkins <http://jenkins-ci.org/>`_.

.. versionadded:: 1.1
"""
from __future__ import print_function
import sys
import os

from .install_custom import download_file


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

    url = "http://mirrors.jenkins.io/war/latest/jenkins.war"

    outfile = os.path.join(dest_folder, "jenkins.war")
    if not os.path.exists(outfile):
        download_file(url, outfile)

    if install:
        raise NotImplementedError("Does not install jenkins.war")
    else:
        return outfile
