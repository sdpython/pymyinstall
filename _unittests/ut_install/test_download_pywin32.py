"""
@brief      test log(time=14s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.packaged import find_module_install


class TestDownloadPyWin32 (unittest.TestCase):

    def test_install_pywin32(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_pywin32")

        if sys.platform.startswith("win"):
            m = find_module_install("pywin32", must_exist=True)
            fLOG(m)
            fLOG(m.__module__)
            m.fLOG = fLOG
            whl = m.download(temp_folder=temp, source="2")
            self.assertTrue(os.path.exists(whl))


if __name__ == "__main__":
    unittest.main()
