import sys
sys.path.append("src")
skip = ["pyquickhelper", "pyensae", "pyrsslocal", "pymyinstall",
        "pymmails", "ensae_teaching_cs", "code_beatrix",
        "actuariat_python"]
#skip += ["ete", "dataspyre"]
from pymyinstall.packaged import install_all
install_all(temp_folder="build/update_modules", verbose=True,
            skip_module=skip)
