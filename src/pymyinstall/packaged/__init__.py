"""
@file
@brief Shortcuts to packaged
"""

from .config_helper import is_64bit
from .automate_install import update_all, install_all, find_module_install, install_module_deps
from .automate_install import install_module, update_module, download_module
from .packaged_config import minimal_set, small_set, sphinx_theme_set, extended_set, ensae_set, teachings_set, scraping_set, ensae_fullset, all_set, pyquickhelper_set, ml_set, anaconda_set
from .packaged_config import get_package_set, name_sets_dataframe, classifiers2string
from .packaged_config import ensae_teaching_cs_set, pyensae_set
