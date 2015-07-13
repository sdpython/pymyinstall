"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
        sys.path.append(os.environ["PYQUICKHELPER"])
    import pyquickhelper


from pyquickhelper import fLOG, get_temp_folder, synchronize_folder
from src.pymyinstall.win_installer.win_ipython_helper import ipython_create_profile, ipython_update_profile


class TestIPythonProfile(unittest.TestCase):

    def test_ipython_profile(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
            
        python_path = os.path.dirname(sys.executable)
        temp = get_temp_folder(__file__, "temp_ipython")
        path = ipython_create_profile(
            temp, python_path, name="ZZZ", fLOG=fLOG)
        fLOG(path)
        assert os.path.exists(path)
        
        ipython_update_profile(path)

        profile = os.path.join(path, "ipython_notebook_config.py")
        with open(profile, "r", encoding="utf8") as f:
            lines = f.readlines()

        exp = "c.ContentsManager.hide_globs = ['__pycache__',"
        nb = 0
        for line in lines:
            if line.startswith(exp):
                nb += 1
        assert nb > 0


if __name__ == "__main__":
    unittest.main()
