import sys
print(sys.executable)
sys.path.append("src")
from pymyinstall import ds_small
ds_small(fLOG=print)