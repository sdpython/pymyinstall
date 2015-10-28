"""
@brief      test log(time=14s)
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


from src.pymyinstall.packaged import find_module_install
from pyquickhelper import fLOG, get_temp_folder


class TestDownloadPyWin32 (unittest.TestCase):

    def test_install_pywin32(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_pywin32")

        if sys.platform.startswith("win"):
            m = find_module_install("pywin32", must_exist=True)
            fLOG(m)
            fLOG(m.__module__)
            m.fLOG = fLOG
            whl = m.download(temp_folder=temp)
            assert os.path.exists(whl)


if __name__ == "__main__":
    unittest.main()
