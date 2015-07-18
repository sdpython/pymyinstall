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
from .install_cmd_helper import run_cmd, update_pip, has_pip
from .install_custom import download_page
from .module_install import ModuleInstall, get_module_version, get_pypi_version


def update_all(temp_folder=".", fLOG=print, verbose=True,
               list_module=None):
    """
    update modules in *list_module* (in that order)
    if None, this list will be returned by @see fn installation_ensae,
    the function starts by updating pip.

    @param  temp_folder     temporary folder
    @param  verbose         more display
    @param  list_module     None or of list of @see cl ModuleInstall
    @param  fLOG            logging function
    """
    import os
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    if not has_pip():
        from .get_pip import main
        main()

    if list_module is None:
        from ..packaged.packaged_config import installation_ensae
        list_module = installation_ensae()

    if verbose:
        fLOG("update pip if needed")
    update_pip()
    if verbose:
        fLOG("get module order")
    modules = list_module
    again = []
    for mod in modules:
        if verbose:
            fLOG("check module: ", mod.name)
        if mod.is_installed() and mod.has_update():
            ver = mod.get_pypi_version()
            inst = mod.get_installed_version()
            m = "    - updating module  {0} --- {1} --> {2} (kind={3})" \
                .format(mod.name, inst, ver, mod.kind)
            fLOG(m)
            b = mod.update(temp_folder=temp_folder, log=verbose)
            if b:
                again.append(m)

    if verbose:
        fLOG("")
        fLOG("updated modules")
        for m in again:
            fLOG(m)
