import sys
sys.path.append("src")
skip = ["pyquickhelper", "pyensae", "pyrsslocal",
        "pymmails", "ensae_teaching_cs", "code_beatrix",
        "actuariat_python"]
from pymyinstall.packaged import install_all
install_all(temp_folder="build/update_modules", verbose=True,
            skip_module=["ete", "dataspyre"] + skip)
