import sys
sys.path.append("src")
skip = ["actuariat_python", "code_beatrix", "ensae_teaching_cs",
        "jupytalk", "jyquickhelper", "mlstatpy",
        "pyquickhelper", "pyensae", "pyrsslocal", "pymyinstall",
        "pymmails", "teachpyx",
        ]
from pymyinstall.packaged import install_all
install_all(temp_folder="build/update_modules", verbose=True,
            skip_module=skip, source="2")
