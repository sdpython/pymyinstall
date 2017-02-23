import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
sys.path.append("../pyquickhelper/src")
print("----")
import pyquickhelper
from pymyinstall import win_python_setup
from pymyinstall.packaged import small_set


if True:
    win_python_setup(module_list=small_set(), verbose=True,
                     download_only=False,
                     no_setup=False,
                     selection={},
                     notebooks=[],
                     tutorial=["french"])
