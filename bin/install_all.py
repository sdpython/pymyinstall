# execute in admin mode
import sys
sys.path.append("../src")
skip = ["actuariat_python", "code_beatrix", "ensae_teaching_cs",
        "jupytalk", "jyquickhelper", "mlstatpy",
        "pyquickhelper", "pyensae", "pyrsslocal", "pymyinstall",
        "pymmails", "teachpyx",
        # 2017
        'mlprodict', 'lightmlrestapi', 'lightmlboard', 'pandas_streaaming',
        'pyenbc', 'mlinsights', 'cpyquickhelper', 'tkinterquickhelper',
        ]
from pymyinstall.packaged import install_all
install_all(temp_folder="build/update_modules{0}{1}{2}".format(*sys.version_info[:3]),
            verbose=True, skip_module=skip, source="2")
