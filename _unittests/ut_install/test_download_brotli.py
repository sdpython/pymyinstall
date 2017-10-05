"""
@brief      test log(time=20s)
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


from src.pymyinstall.packaged import find_module_install
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestDownloadBrotli(unittest.TestCase):

    def test_install_brotli(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win") and sys.version_info[0] >= 3:
            temp = get_temp_folder(__file__, "temp_download_brotli")
            m = find_module_install("Brotli")
            whl = m.download(temp_folder=temp, source="2")
            fLOG(m.version)
            self.assertTrue(os.path.exists(whl))


if __name__ == "__main__":
    unittest.main()
