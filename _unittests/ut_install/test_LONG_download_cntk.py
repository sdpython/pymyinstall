"""
@brief      test log(time=120s)

skip this test for regular run
"""

import sys
import os
import unittest
import warnings


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


from pyquickhelper.loghelper import fLOG
from src.pymyinstall.packaged import find_module_install


class TestLONGDownloadCntk(unittest.TestCase):

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
            if sys.version_info[:2] != (3, 6):
                fLOG("install", "cntk")
                m = find_module_install("cntk")
                m.fLOG = fLOG
                exe = m.download(temp_folder=temp)
                assert os.path.exists(exe)
                assert os.stat(exe).st_size > 100000
            else:
                fLOG("CNTK not available for 3.6")
                warnings.warn("CNTK not available for 3.6")


if __name__ == "__main__":
    unittest.main()
