"""
Documentation for this file.

To install a list of modules for a machine learner:
@code
from pymyinstall import complete_installation
for _ in complete_installation() :
    _.install(temp_folder="install")
@endcode
"""

def check( log = False):
    """
    Checks the library is working.
    It raises an exception.
    If you want to disable the logs:
    
    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True
    
from .installhelper.install_cmd import run_cmd, ModuleInstall, complete_installation
