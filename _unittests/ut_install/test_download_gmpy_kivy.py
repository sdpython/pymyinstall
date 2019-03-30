"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installhelper.module_install import ModuleInstall


class TestDownload2 (unittest.TestCase):

    def test_install_gmpy2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_gmpy2")

        if sys.platform.startswith("win"):
            m = ModuleInstall("gmpy2", "wheel", fLOG=fLOG)
            whl = m.download(temp_folder=temp, source="2")
            self.assertTrue(os.path.exists(whl))

    def test_install_kivy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_kivy")

        if sys.platform.startswith("win"):
            m = ModuleInstall("Kivy", "wheel", mname="kivy", fLOG=fLOG)
            whl = m.download(temp_folder=temp, source="2")
            self.assertTrue(os.path.exists(whl))


if __name__ == "__main__":
    unittest.main()
