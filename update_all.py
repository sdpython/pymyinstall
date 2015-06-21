import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
print("----")
from pymyinstall import update_all

update_all(temp_folder="build\\update_modules", verbose=True)
