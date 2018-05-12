"""
@brief      test log(time=10s)
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

from src.pymyinstall import download_revealjs


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
