"""
@brief      test log(time=120s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.packaged import find_module_install


class TestLONGDownloadCntk(unittest.TestCase):

    @unittest.skipIf(sys.version_info[:2] == (3, 7), reason="not released yet on python 3.7")
    def test_install_cntk(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_download_cntk")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        if sys.platform.startswith("win"):
            fLOG("install", "cntk")
            m = find_module_install("cntk")
            m.fLOG = fLOG
            exe = m.download(temp_folder=temp)
            assert os.path.exists(exe)
            assert os.stat(exe).st_size > 100000


if __name__ == "__main__":
    unittest.main()
