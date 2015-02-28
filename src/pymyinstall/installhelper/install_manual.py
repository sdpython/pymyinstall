# coding: latin-1
"""
@file
@brief Contains a list of web site with some useful tools.
"""
import webbrowser

_tools = {
    "7z": "http://www.7-zip.org/download.html",
    "miktex": "http://miktex.org/download",
    "texniccenter": "http://www.texniccenter.org/download/",
    "python": "https://www.python.org/downloads/release/python-341/",
    "mingw": "http://sourceforge.net/projects/mingw/files/Installer/",
    "VS": "http://www.microsoft.com/download/details.aspx?id=40787",
    "cygwin": "https://cygwin.com/install.html",
    "chrome": "http://www.google.com/chrome/browser/",
    "firefox": "http://www.mozilla.org/firefox/new/",
    "graphviz": "http://www.graphviz.org/",
    "doxygen": "http://www.stack.nl/~dimitri/doxygen/download.html",
    "nodejs": "http://nodejs.org/download/",
    # "innosetup":"http://www.jrsoftware.org/isdl.php",
}


def get_install_list():
    """
    returns the list of tools a developper might need
    """
    global _tools
    return list(_tools.keys())


def open_tool_on_browser(tool=None):
    """
    open a page on browser for a specific tool

    @param      tool        tool name
    """
    global _tools
    if isinstance(tool, str):
        tool = [tool]
    elif tool is None:
        tool = get_install_list()
    for t in tool:
        webbrowser.open_new_tab(_tools[t])

if __name__ == "__main__":
    open_tool_on_browser()
