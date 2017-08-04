"""
@brief      test log(time=75s)
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


from src.pymyinstall.installhelper.module_install import ModuleInstall
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestDownloadGuiData(unittest.TestCase):

    def test_install_guidata(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[0] == 2:
            # disabled on python 2.7
            return
        fold = get_temp_folder(__file__, "temp_download_guidata")
        # This test can fail if the latest version of pyquickhelper is not
        # available for Python 2.7
        m = ModuleInstall("guidata", "wheel2", fLOG=fLOG)
        out = m.download(temp_folder=fold)
        self.assertTrue(os.path.exists(out))
        self.assertTrue("guidata" in out)
        out = m.download(temp_folder=fold)
        self.assertTrue(os.path.exists(out))
        self.assertTrue("guidata" in out)


if __name__ == "__main__":
    unittest.main()
