"""
@brief      test log(time=45s)
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

from src.pymyinstall.installcustom import install_tdm_gcc


class TestTDMGCC (unittest.TestCase):

    def test_install_tdm_gcc(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            return

        temp = get_temp_folder(__file__, "temp_tdc_gcc")

        if sys.platform.startswith("win"):
            r = install_tdm_gcc(temp, fLOG=fLOG)
            exe = os.path.abspath(r)
            self.assertTrue(os.path.exists(exe))


if __name__ == "__main__":
    unittest.main()
