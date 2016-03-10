"""
@brief      test log(time=20s)

skip this test for regular run
"""

import sys
import os
import unittest
import re

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


from src.pymyinstall.installhelper.module_install import ModuleInstall
from src.pymyinstall.packaged import find_module_install
from pyquickhelper import fLOG


class TestDownloadPyCrypto (unittest.TestCase):

    def test_install_pycrypto(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_download_lxml")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        if sys.platform.startswith("win"):
            fLOG("install", "pycrypto")
            m = find_module_install("pycrypto")
            m.fLOG = fLOG
            exe = m.download(
                temp_folder=temp,
                file_save=os.path.join(
                    temp,
                    "out_page.html"), source="2")
            assert os.path.exists(exe)
            assert os.stat(exe).st_size > 100000
            assert "cp34-none-win_amd64" in exe

if __name__ == "__main__":
    unittest.main()
