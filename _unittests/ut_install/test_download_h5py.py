"""
@brief      test log(time=20s)

skip this test for regular run
"""

import sys
import os
import unittest

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
    import pyquickhelper as skip_
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
    import pyquickhelper as skip_


from src.pymyinstall.installhelper.module_install import ModuleInstall
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestDownloadh5py (unittest.TestCase):

    def test_install_h5py(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_h5py")
            fLOG("install", "h5py")
            m = ModuleInstall("h5py", "wheel", fLOG=fLOG)
            exe = m.download(
                temp_folder=temp,
                file_save=os.path.join(
                    temp,
                    "out_page.html"), source="2")
            self.assertTrue(os.path.exists(exe))
            self.assertTrue(os.stat(exe).st_size > 1000)


if __name__ == "__main__":
    unittest.main()
