import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
print("----")
from pymyinstall import win_python_setup, installation_ensae, installation_teachings

list_modules = installation_ensae() + installation_teachings()

win_python_setup(module_list=list_modules, verbose=True, download_only=False)
