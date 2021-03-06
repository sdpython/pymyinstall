"""
@brief      test log(time=140s)

skip this test for regular run
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installcustom import install_pandoc


class TestLONGPandoc (unittest.TestCase):

    def test_install_pandoc(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])

        if sys.platform.startswith("win"):
            temp = os.path.join(fold, "temp_pandoc")
            if not os.path.exists(temp):
                os.mkdir(temp)
            for _ in os.listdir(temp):
                if ".msi" in _:
                    os.remove(os.path.join(temp, _))
            r = install_pandoc(
                temp_folder=temp,
                fLOG=fLOG,
                install=False,
                force_download=True)
            self.assertTrue(os.path.exists(r))


if __name__ == "__main__":
    unittest.main()
