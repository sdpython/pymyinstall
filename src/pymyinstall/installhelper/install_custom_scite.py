"""
@file
@brief Various function to install some application such as `pandoc <http://johnmacfarlane.net/pandoc/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from .install_cmd_helper import unzip_files
from .install_custom import download_page, download_from_sourceforge
from .link_shortcuts import add_shortcut_to_desktop, suffix

if sys.version_info[0] == 2:
    from codecs import open


def IsSciteInstalled(dest_folder):
    """
    check if Scite was already installed

    @param      dest_folder     where it was installed
    @return                     boolean
    """
    if sys.platform.startswith("win"):
        file = os.path.join(dest_folder, "wscite", "SciTE.exe")
        return os.path.exists(file)
    else:
        raise NotImplementedError("not available on platform " + sys.platform)


def install_scite(dest_folder=".", fLOG=print, install=True):
    """
    install `SciTE <http://www.scintilla.org/SciTE.html>`_ (only on Windows)

    @param      dest_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @return                     temporary file

    @example(install SciTE)
    The function downloads the latest version of SciTE.
    It also changes some settings for Python (no tabs, Courier New as a police).
    @code
    install_scite("my_folder_for_scite")
    @endcode
    @endexample
    """
    if IsSciteInstalled(dest_folder):
        return os.path.join(
            os.path.abspath(dest_folder), "wscite", "SciTE.exe")

    if not sys.platform.startswith("win"):
        raise NotImplementedError(
            "SciTE can only be installed on Windows at the moment")

    url = "http://www.scintilla.org/SciTEDownload.html"
    page = download_page(url)

    rel = re.compile("Release ([0-9.]+)")
    rel = rel.findall(page)
    if len(rel) == 0:
        raise Exception("unable to find the release version")
    rel = rel[0]
    fLOG("SciTE, release version ", rel)

    #reg = re.compile("<a href=\\\"(.*zip.*)\\\">full download</a>")
    #find = reg.findall(page)
    # if len(find) != 1 :
    #    raise Exception("unable to find the file to download at " + url + "\nfound: " + str(len(find)) + "\n" + "\n".join(find))

    newurl = "http://sourceforge.net/projects/scintilla/files/SciTE/{0}/wscite{1}.zip/download?use_mirror=autoselect".format(
        rel,
        rel.replace(
            ".",
            ""))
    outfile = os.path.join(dest_folder, "scite.zip")
    fLOG("SciTE, download from ", newurl)
    file = download_from_sourceforge(
        newurl,
        outfile,
        fLOG=fLOG,
        temp_folder=dest_folder)
    unzip_files(file, whereTo=dest_folder, fLOG=fLOG)

    # we change the path
    config = os.path.join(dest_folder, "wscite", "python.properties")
    with open(config, "r") as f:
        content = f.read()
    content = content.replace("=pythonw", "=" + sys.executable)
    with open(config, "w") as f:
        f.write(content)

    # we change the options
    config = os.path.join(dest_folder, "wscite", "SciTEGlobal.properties")
    with open(config, "r", encoding="utf8", errors="ignore") as f:
        content = f.read()
    content = content.replace("tabsize=8", "tabsize=4")
    content = content.replace("indent.size=8", "indent.size=4")
    content = content.replace("use.tabs=1", "use.tabs=0")
    content = content.replace("font:Verdana,", "font:Consolas,")
    with open(config, "w", encoding="utf8") as f:
        f.write(content)

    return os.path.join(os.path.abspath(dest_folder), "wscite", "SciTE.exe")


def add_shortcut_to_desktop_for_scite(scite):
    """
    create a shortcut on your desktop

    @param      scite      scite location (SciTE.exe
    @return                filename
    """
    ver = suffix()
    return add_shortcut_to_desktop(scite, "SciTE." + ver, "SciTE." + ver)
