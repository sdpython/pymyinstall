import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
from pymyinstall import ds_small
ds_small(fLOG=print)
