import sys
print(sys.executable)
sys.path.append("src")
from pymyinstall import ds_complete, ds_huge
ds_complete(fLOG=print)
ds_huge(fLOG=print)