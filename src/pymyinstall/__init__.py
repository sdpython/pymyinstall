#-*- coding: utf-8 -*-
"""
Documentation for this file.

To install a list of modules for a machine learner:
@code
from pymyinstall import complete_installation, install_scite, install_pandoc, open_tool_on_browser
for _ in complete_installation() :
    _.install(temp_folder="install")
install_scite("install")
install_pandoc("install")
open_tool_on_browser()
@endcode
"""

import sys
if sys.version_info[0] < 3 :
    raise ImportError("pymyinstall only works with Python 3")

__version__ = "0.8"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/pymyinstall"
__url__ = "http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#pymyinstall"
__license__ = "BSD License"


def check( log = False):
    """
    Checks the library is working.
    It raises an exception.
    If you want to disable the logs:

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True

from .installhelper.install_cmd import run_cmd, ModuleInstall, unzip_files, add_shortcut_to_desktop_for_module
from .installhelper.install_custom import download_from_sourceforge, download_file, download_page
from .installhelper.install_manual import get_install_list, open_tool_on_browser
from .setuphelper.ipython_helper import setup_ipython, add_shortcut_to_desktop_for_ipython
from .installhelper.link_shortcuts import add_shortcut_to_desktop
from .installhelper.install_custom_pandoc import install_pandoc
from .installhelper.install_custom_scite import install_scite, add_shortcut_to_desktop_for_scite
from .installhelper.install_custom_sqlitespy import install_sqlitespy, add_shortcut_to_desktop_for_sqlitespy
from .packaged.packaged_functions import datascientist, ds_small, ds_complete, ds_cubes, ds_huge
from .packaged.packaged_config import complete_installation, small_installation, installation_huge_datasets, installation_cubes
from .packaged.packaged_config import installation_azure