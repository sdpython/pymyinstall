import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
from pymyinstall import ds_complete, ds_huge
skip = ["pyquickhelper", "pyensae", "ensae_teaching_cs"]
ds_complete(fLOG=print, azure=True, skip=skip)
ds_huge(fLOG=print, skip=skip)
