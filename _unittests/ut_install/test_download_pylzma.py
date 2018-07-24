"""
@brief      test log(time=20s)
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


from src.pymyinstall.packaged import find_module_install


class TestDownloadPylzma(unittest.TestCase):

    def test_install_pylzma(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win") and sys.version_info[0] == 2:
            # no pycrypto on Python 2.7 for Windows
            return

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_pylzma")
            fLOG("install", "pycrypto")
            m = find_module_install("pylzma")
            m.fLOG = fLOG
            exe = m.download(
                temp_folder=temp,
                file_save=os.path.join(
                    temp,
                    "out_page.html"), source="2")
            self.assertTrue(os.path.exists(exe))
            self.assertTrue(os.stat(exe).st_size > 59000)
            if "cp{0}{1}-cp{0}{1}m-win_amd64".format(*sys.version_info[:2]) not in exe and \
               "cp{0}{1}-none-win_amd64".format(*sys.version_info[:2]) not in exe:
                raise Exception(exe)


if __name__ == "__main__":
    unittest.main()
