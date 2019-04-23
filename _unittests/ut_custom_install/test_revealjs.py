"""
@brief      test log(time=10s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall import download_revealjs


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
