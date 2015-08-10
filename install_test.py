import sys
print(sys.executable)
sys.path.append("src")
from pymyinstall.packaged import update_all, install_all, find_module_install
install_all(temp_folder="c:\\python34_x64vir\\downloads",
            list_module=["docutils==0.8"])
