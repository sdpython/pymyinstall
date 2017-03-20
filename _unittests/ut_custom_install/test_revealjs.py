"""
@brief      test log(time=10s)

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


from src.pymyinstall import download_revealjs
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestRevealjs(unittest.TestCase):

    def test_install_revealjs(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_install_revealjs")
        dest = get_temp_folder(__file__, "temp_install_revealjs_dest")
        fs = download_revealjs(temp, dest, fLOG=fLOG)
        fLOG(fs)
        self.assertTrue(len(fs) > 0)
        for a in fs:
            self.assertTrue(os.path.exists(a))


if __name__ == "__main__":
    unittest.main()
