# -*- coding: utf-8 -*-
"""
*pymyinstall* installs package on Windows and Linux.
It automatically chooses a location for a
:ref:`long list of package <l-ensae_fullset-table>`.
To install a list of modules for a machine learner:

::

    from pymyinstall import complete_installation, install_scite, install_pandoc, open_tool_on_browser
    for _ in complete_installation():
        _.install(temp_folder="install")

You can also install some useful tools:

::

    from pymyinstall import install_scite, install_pandoc

    install_scite("install")
    install_pandoc("install")

To download a module:

::

    from pymyinstall import download_module
    download_module("module_name")

To install a module:

::

    from pymyinstall import install_module
    install_module("module_name")
"""
from .installhelper.install_cmd_helper import run_cmd, unzip_files
from .installhelper.module_install import ModuleInstall
from .installcustom.install_custom import download_from_sourceforge, download_file, download_page
from .installhelper.install_manual import get_install_list
from .installhelper import get_module_version, get_pypi_version
from .installcustom.install_custom_revealjs import download_revealjs
from .installhelper.requirements import build_requirements
from .win_installer.win_setup_main import win_python_setup
from .packaged import install_module, update_module, download_module


__version__ = "1.4.1936"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/pymyinstall"
__url__ = "http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html"
__license__ = "MIT License"


def _setup_hook():
    """
    does nothing
    """
    # we clean the cache
    ModuleInstall.clear_cache()


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.
    If you want to disable the logs:

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True


def is_travis_or_appveyor():
    """
    tells if is a travis environment or appveyor

    :return:        travis, appveyor or None

    .. versionadded:: 1.1
    """
    import sys
    if "travis" in sys.executable:
        return "travis"
    import os
    if os.environ.get("USERNAME", os.environ.get("USER", "")) == "appveyor":
        return "appveyor"
    return None
