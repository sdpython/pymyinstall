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
    import pyquickhelper as skip_
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
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from src.pymyinstall.win_installer.win_packages import get_modules_version


class TestPackages(unittest.TestCase):

    def test_modules_list(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mods = get_modules_version(os.path.dirname(sys.executable))
        assert len(mods) > 0
        for k, v in mods.items():
            break
        self.assertIn(".", v)

    def test_modules_list_ext(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        path = "C:\\github\\ensae_teaching_cs\\dist\\win_python_setup\\python"
        if os.path.exists(path):
            mods = get_modules_version(path)
            assert len(mods) > 0


if __name__ == "__main__":
    unittest.main()
