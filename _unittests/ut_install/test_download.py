"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper.module_install import ModuleInstall


class TestDownload (unittest.TestCase):

    def test_install(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_download")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))
        if os.path.exists(os.path.join(temp, "jsdifflib-master")):
            for _ in os.listdir(os.path.join(temp, "jsdifflib-master")):
                os.remove(
                    os.path.join(
                        os.path.join(
                            temp,
                            "jsdifflib-master"),
                        _))

        m = ModuleInstall("jsdifflib", "github", gitrepo="cemerick", fLOG=fLOG)
        files = m.download(temp_folder=temp, unzipFile=True, source="2")
        self.assertTrue(len(files) > 0)
        for _ in files:
            self.assertTrue(os.path.exists(_))

    def test_install_scikit(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_download_scikit")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        if sys.platform.startswith("win"):
            m = ModuleInstall(
                "scikit-learn",
                "wheel",
                mname="sklearn",
                fLOG=fLOG)
            whl = m.download(temp_folder=temp, source="2")
            self.assertTrue(os.path.exists(whl))
            if os.stat(whl).st_size < 1000:
                raise Exception("small file: " + whl)


if __name__ == "__main__":
    unittest.main()
