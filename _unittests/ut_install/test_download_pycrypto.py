"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.packaged import find_module_install
from pymyinstall.installhelper.module_install_exceptions import MissingWheelException


class TestDownloadPyCrypto (unittest.TestCase):

    def test_install_pycrypto(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win") and sys.version_info[0] == 2:
            # no pycrypto on Python 2.7 for Windows
            return

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_pycrypto")
            fLOG("install", "pycrypto")
            m = find_module_install("pycrypto")
            m.fLOG = fLOG
            try:
                exe = m.download(
                    temp_folder=temp,
                    file_save=os.path.join(
                        temp,
                        "out_page.html"), source="2")
            except MissingWheelException as e:
                if sys.version_info[:2] >= (3, 7):
                    # Not ready yet, issue #57.
                    warnings.warn("PyCrypto not available on Python 3.7")
                    return
                else:
                    raise e
            self.assertTrue(os.path.exists(exe))
            self.assertTrue(os.stat(exe).st_size > 100000)
            if "cp{0}{1}-cp{0}{1}m-win_amd64".format(*sys.version_info[:2]) not in exe and \
               "cp{0}{1}-none-win_amd64".format(*sys.version_info[:2]) not in exe:
                raise Exception(exe)


if __name__ == "__main__":
    unittest.main()
