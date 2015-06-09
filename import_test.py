import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
print("----")
from pymyinstall import ModuleInstall
mod = ModuleInstall("pycrypto", "wheel_xd", mname="Crypto")
mod.install(temp_folder="temp_install")
