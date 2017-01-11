"""
@file
@brief Shortuts
"""
from .install_cmd_helper import run_cmd, update_pip, has_pip, add_shortcut_to_desktop_for_module, get_pip_program
from .install_venv_helper import run_cmd_path, run_venv_script, venv_install, create_virtual_env
from .module_install import ModuleInstall
from .module_dependencies import missing_dependencies
from .module_install_version import get_module_dependencies, get_module_version, get_pypi_version, get_module_metadata
from .module_install_version import version_consensus, numeric_version, compare_version, is_installed, get_wheel_version
from .status_helper import get_installed_modules


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
