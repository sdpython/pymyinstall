"""
@file
@brief Shortcuts to packaged
"""

from .config_helper import is_64bit
from .automate_install import update_all, install_all, find_module_install, install_module_deps
from .automate_install import install_module, update_module, download_module
from .packaged_config import minimal_set, small_set
from .packaged_config import get_package_set, name_sets_dataframe, classifiers2string
