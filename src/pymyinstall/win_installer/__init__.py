"""
@file
@breif shortcuts to win_installer
"""

from .win_exception import WinInstallException
from .win_extract import extract_msi, extract_exe
from .win_setup_r import r_run_script
from .win_setup_main import win_python_setup
from .win_innosetup_helper import inno_install_kernels
from .win_installer import win_install_package_other_python, is_package_installed
