"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installhelper.module_install import ModuleInstall


class TestDownloadlxml (unittest.TestCase):

    def test_install_lxml(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_lxml")
            fLOG("install", "lxml")
            m = ModuleInstall("lxml", "wheel", fLOG=fLOG, source="2")
            exe = m.download(
                temp_folder=temp,
                file_save=os.path.join(
                    temp,
                    "out_page.html"), source="2")
            self.assertTrue(os.path.exists(exe))
            self.assertTrue(os.stat(exe).st_size > 100000)


if __name__ == "__main__":
    unittest.main()
