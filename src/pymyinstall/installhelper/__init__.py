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


def module_as_table(list_module, as_df=False):
    """
    returns a list of dictionaries or a dataframe
    for a list of modules

    @param      list_module     list of @see cl ModuleInstall
    @param      as_df           as a dataframe or not
    @return                     list of dictionaries or dataframe
    """
    res = [_.as_dict() for _ in list_module]
    if as_df:
        import pandas
        return pandas.DataFrame(res)
    else:
        return res
