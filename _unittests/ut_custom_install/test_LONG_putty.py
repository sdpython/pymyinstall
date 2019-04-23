"""
@brief      test log(time=45s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installcustom import install_putty


class TestPutty (unittest.TestCase):

    def test_install_putty(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_putty")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            f = os.path.join(temp, _)
            if os.path.isfile(f):
                os.remove(f)

        if sys.platform.startswith("win"):
            r = install_putty(temp, fLOG=fLOG)
            exe = os.path.abspath(r)
            fLOG(exe)
            self.assertTrue(os.path.exists(exe))


if __name__ == "__main__":
    unittest.main()
