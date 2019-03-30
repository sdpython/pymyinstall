"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.win_installer.win_packages import get_modules_version


class TestPackages(unittest.TestCase):

    def test_modules_list(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mods = get_modules_version(os.path.dirname(sys.executable))
        assert len(mods) > 0
        lastv = ""
        for v in mods.values():
            lastv = v
            break
        self.assertIn(".", lastv)

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
