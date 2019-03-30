"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper.module_install import ModuleInstall


class TestDownloadPyQt (unittest.TestCase):

    def test_install_pyqt(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_download_pyqt")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        if sys.platform.startswith("win"):
            fLOG("install", "pyqt")
            m = ModuleInstall("PyQt5", "pip", mname="pyqt", fLOG=fLOG)
            exe = m.download(
                temp_folder=temp,
                file_save=os.path.join(
                    temp,
                    "out_page.html"), source="2")
            assert os.path.exists(exe)


if __name__ == "__main__":
    unittest.main()
