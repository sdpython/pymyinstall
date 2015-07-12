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


from pyquickhelper import fLOG, get_temp_folder
from src.pymyinstall import installation_ensae, installation_teachings
from src.pymyinstall.win_installer.win_packages import get_modules_version


class TestPackages(unittest.TestCase):

    def test_modules_list(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mods = get_modules_version(os.path.dirname(sys.executable))
        assert len(mods) > 0

    def test_modules_list_ext(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        path = r"C:\github\ensae_teaching_cs\dist\win_python_setup\python"
        if os.path.exists(path):
            mods = get_modules_version(path)
            assert len(mods) > 0

if __name__ == "__main__":
    unittest.main()
