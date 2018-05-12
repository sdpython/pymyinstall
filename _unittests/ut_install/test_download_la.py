"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder

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


from src.pymyinstall.installhelper.module_install import ModuleInstall


class TestDownloadLa(unittest.TestCase):

    def test_install_la(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_la")
            fLOG("install", "la")
            m = ModuleInstall("la", "wheel", fLOG=fLOG)
            exe = m.download(
                temp_folder=temp,
                file_save=os.path.join(
                    temp,
                    "out_page.html"), source="2")
            self.assertTrue(os.path.exists(exe))
            fLOG(exe)
            self.assertTrue(os.stat(exe).st_size > 1000)


if __name__ == "__main__":
    unittest.main()
