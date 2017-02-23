"""
@file
@brief Function to start on Windows from scratch

.. versionadded:: 1.1
"""
from __future__ import print_function
import sys
import os
from ..win_installer.win_setup_main_helper import win_download, win_install


def windows_default_tools_list():
    """
    returns a list of tools to install

    @return     list of tools
    """
    return ["7z", "scite", "putty", "mingw", "SQLiteSpy", "r", "vs",
            "julia", "graphviz", "tdm", "pandoc",
            "jdk", "jenkins",
            "miktex", "inkscape",
            "git", "python"]


def windows_startup(destination, temp_folder, params=None, fLOG=print):
    """
    Installs many tools.
    It does not work with Python 2.7.

    @param      destination     destination
    @param      temp_folder     temporary folder (not cleaned), for downloading purpose
    @param      fLOG            logging function
    @param      params          dictionary
    @return                     operations (what was done)

    About *params*, it can contains:

    * *tools*: list of tools to install, see @see fn win_download, if None, use a default list defined
      in @see fn windows_default_tools_list

    .. exref::
        :title: Setup a machine

        The following code tries to download many tools and packages
        to prepare a machine for a datascientist on Windows::

            from pymyinstall.startup import windows_startup
            windows_startup(r"d:\\datascientist", r"d:\\temp\\datascientist", fLOG=print)

    .. versionadded:: 1.1
    """
    if sys.version_info[0] == 2:
        raise SystemError("It requires Python 3+")

    # creating folders if they don't exists
    if not os.path.exists(destination):
        os.makedirs(destination)
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    if params is None:
        params = {}

    # selection
    tools = params.get("tools", None)
    if tools is None:
        tools = windows_default_tools_list()

    if isinstance(tools, list):
        tools = {k: None for k in tools}

    fLOG("------ download", tools)
    op = win_download(temp_folder, fLOG=fLOG, selection=tools, module_list=[])

    # copy de SQLiteSpy, putty, Scite
    names = ["Julia", "Scite", "7z", "TDM", "MinGW", "R", "pandoc",
             "SQLiteSpy", "Putty", "Graphviz", "Jdk", "Jenkins", "Git",
             "MikTex", "InkScape",
             "Python", ]

    fLOG("------ install", tools)
    folders = dict(tools=destination,
                   python=os.path.join(destination, "python"))
    op += win_install(folders, download_folder=temp_folder,
                      fLOG=fLOG, selection=tools, names=names)
    return op
