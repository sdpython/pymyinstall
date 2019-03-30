"""
@brief      test log(time=75s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installhelper.module_install import ModuleInstall


class TestDownloadGuiData(unittest.TestCase):

    def test_install_guidata(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[0] == 2:
            # disabled on python 2.7
            return
        if not sys.platform.startswith("win"):
            # only for windows
            return
        fold = get_temp_folder(__file__, "temp_download_guidata")
        # This test can fail if the latest version of pyquickhelper is not
        # available for Python 2.7
        m = ModuleInstall("guidata", "wheel2", fLOG=fLOG)
        out = m.download(temp_folder=fold)
        self.assertTrue(os.path.exists(out))
        self.assertTrue("guidata" in out)
        out = m.download(temp_folder=fold)
        self.assertTrue(os.path.exists(out))
        self.assertTrue("guidata" in out)


if __name__ == "__main__":
    unittest.main()
