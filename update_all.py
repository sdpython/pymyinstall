import sys
sys.path.append("src")
from pymyinstall.packaged import update_all
update_all(temp_folder="build/update_modules", verbose=True,
           skip_module=["dataspyre", "pycuda", "cubehelix"],
           source="2")
