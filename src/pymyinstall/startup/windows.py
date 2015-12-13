"""
@file
@brief Function to start on Windows from scratch

.. versionadded:: 1.1
"""
from ..win_install.win_setup_main_helper import win_download, win_install


def windows_default_tools_list():
    """
    returns a list of tools to install

    @return     list of tools
    """
    return ["scite", "putty", "mingw", "SQLiteSpy", "R", "vs", "julia", "7z", "graphviz",
            "java", "jenkins", "firefox", "chrome",
            "git", "tgit", "github"]


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

    .. versionadded:: 1.1
    """
    if sys.version_info[0] == 2:
        raise SystemError("It requires Python 3+")

    # selection
    tools = params.get("tools", None)
    if tools is None:
        tools = windows_default_tools_list()

    op = win_download(temp_folder, fLOG=fLOG, selection=tools)
    return op
