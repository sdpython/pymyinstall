"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.packaged import find_module_install


class TestDownloadPyscopg2(unittest.TestCase):

    def test_install_tables(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_psycopg2")

        if sys.platform.startswith("win"):
            m = find_module_install("psycopg2")
            m.fLOG = fLOG
            whl = m.download(temp_folder=temp, source="2")
            self.assertTrue(os.path.exists(whl))


if __name__ == "__main__":
    unittest.main()
