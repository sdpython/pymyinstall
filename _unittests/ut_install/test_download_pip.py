"""
@brief      test log(time=75s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installhelper.module_install import ModuleInstall


class TestDownloadPip (unittest.TestCase):

    def test_install_pip(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[0] == 2:
            # disabled on python 2.7
            return
        fold = get_temp_folder(__file__, "temp_download_pip")
        # This test can fail if the latest version of pyquickhelper is not
        # available for Python 2.7
        m = ModuleInstall("pyquickhelper", "pip", fLOG=fLOG)
        out = m.download(temp_folder=fold)
        self.assertTrue(os.path.exists(out))
        self.assertTrue("pyquickhelper" in out)
        out = m.download(temp_folder=fold)
        self.assertTrue(os.path.exists(out))
        self.assertTrue("pyquickhelper" in out)

    def test_install_pip_deps(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[0] == 2:
            # disabled on python 2.7
            return
        fold = get_temp_folder(__file__, "temp_download_pip_deps")
        # This test can fail if the latest version of pyquickhelper is not
        # available for Python 2.7
        m = ModuleInstall("pyquickhelper", "pip", fLOG=fLOG)
        out = m.download(temp_folder=fold, deps=True)
        self.assertTrue(os.path.exists(out))
        self.assertTrue("pyquickhelper" in out)
        out = m.download(temp_folder=fold, source="2")
        self.assertTrue(os.path.exists(out))
        self.assertTrue("pyquickhelper" in out)


if __name__ == "__main__":
    unittest.main()
