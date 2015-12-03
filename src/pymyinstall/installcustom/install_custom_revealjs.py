"""
@file
@brief Various functions to install `reveal.js <https://github.com/hakimel/reveal.js/releases>`_.
"""
from __future__ import print_function
import re
import os
import sys

from .install_custom import download_page, download_file
from ..installhelper.install_cmd_helper import unzip_files

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def download_revealjs(
        temp_folder=".",
        unzip_to=".",
        fLOG=print,
        force_download=False,
        location="https://github.com/hakimel/reveal.js/releases",
        clean=True,
        version=None):
    """
    Download `reveal.js <https://github.com/hakimel/reveal.js/releases>`_ release.
    and unzip it.

    @param      temp_folder     where to download the setup
    @param      unzip_to        where to unzip the files
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of pandoc
    @param      location        location of reveal.js release
    @param      clean           clean unnecessary files
    @param      version         version to download (unused)
    @return                     list of downloaded and unzipped files
    """
    if version is not None:
        raise ValueError("cannot specify a version")
    link = location
    page = download_page(link)
    reg = re.compile("href=\\\"(.*?[.]zip)\\\"")
    alls = reg.findall(page)
    if len(alls) == 0:
        raise Exception(
            "unable to find a link on a .zip file on page: " +
            page)

    filename = alls[0].split("/")[-1]
    filel = location.replace("releases", "") + "/archive/{0}".format(filename)
    outfile = os.path.join(temp_folder, "reveal.js." + filename)
    version = ".".join(filel.split("/")[-1].split(".")[:-1])
    fLOG("download ", filel, "to", outfile, "version", version)
    local = download_file(filel, outfile)
    res = unzip_files(local, whereTo=unzip_to, fLOG=fLOG)

    master = os.path.join(unzip_to, "reveal.js-%s" % version)
    if not os.path.exists(master):
        raise FileNotFoundError("unable to find: " + master)
    new_master = os.path.join(unzip_to, "reveal.js")

    os.rename(master, new_master)
    res = [r.replace(master, new_master) for r in res]

    keep = []
    for r in res:
        if os.path.isdir(r):
            continue
        if ".gitignore" in r or ".travis.yml" in r or "index.html" in r \
           or "README" in r or "CONTRIBUTING.md" in r:
            os.remove(r)
        elif "/test/" in r.replace("\\", "/"):
            os.remove(r)
        else:
            keep.append(r)

    return keep
