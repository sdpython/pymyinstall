"""
@file
@brief Shortuts
"""
from __future__ import print_function

from .install_custom_pandoc import install_pandoc
from .install_custom_R import install_R
from .install_custom_julia import install_julia
from .install_custom_scite import install_scite
from .install_custom_sqlitespy import install_sqlitespy
from .install_custom_python import install_python
from .install_custom_mingw import install_mingw
from .install_custom_7z import install_7z
from .install_cmd_helper import run_cmd, update_pip
from .install_custom import download_page
from .module_install import ModuleInstall, get_module_version


def update_all(temp_folder=".", fLOG=print, verbose=True):
    """
    update all installed modules assuming they are described in
    @see fn installation_ensae

    @param  temp_folder     temporary folder
    @param  fLOG            logging function
    """
    from ..packaged.packaged_config import installation_ensae
    import os
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    modules = installation_ensae()
    for mod in modules:
        if mod.is_installed() and mod.has_update():
            ver = mod.get_pypi_version()
            inst = mod.get_installed_version()
            fLOG(
                "updating module  {0} --- {1} --> {2} (kind={3})".format(mod.name, inst, ver, mod.kind))
            mod.update(temp_folder=temp_folder, log=verbose)
