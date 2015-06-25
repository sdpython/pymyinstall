import sys
sys.path.append("src")
from pymyinstall import update_all
update_all(temp_folder="build/update_modules", verbose=True)
