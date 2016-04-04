"""
@brief      test log(time=140s)

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


from src.pymyinstall.installcustom import install_pandoc
from pyquickhelper.loghelper import fLOG


class TestLONGPandoc (unittest.TestCase):

    def test_install_pandoc(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])

        if sys.platform.startswith("win"):
            temp = os.path.join(fold, "temp_pandoc")
            if not os.path.exists(temp):
                os.mkdir(temp)
            for _ in os.listdir(temp):
                if ".msi" in _:
                    os.remove(os.path.join(temp, _))
            r = install_pandoc(
                temp_folder=temp,
                fLOG=fLOG,
                install=False,
                force_download=True)
            assert os.path.exists(r)


if __name__ == "__main__":
    unittest.main()
