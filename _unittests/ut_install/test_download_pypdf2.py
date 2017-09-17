"""
@brief      test log(time=20s)

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


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.pymyinstall.packaged import find_module_install


class TestDownloadPyPDF2(unittest.TestCase):

    def test_install_pypdf2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_pypdf2")
            fLOG("install", "pyPDF2")
            m = find_module_install("pyPDF2")
            exe = m.download(temp_folder=temp)
            if not os.path.exists(exe):
                raise Exception(exe)
            self.assertTrue(os.stat(exe).st_size > 1000)

    def test_install_pypdf(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_pypdf")
            fLOG("install", "pyPdf")
            m = find_module_install("pyPdf", must_exist=True)
            self.assertEqual(m.name, "pyPdf")
            self.assertEqual(m.kind, "github")
            self.assertEqual(m.gitrepo, "sdpython")
            self.assertEqual(m.pipgit, True)
            exe = m.download(temp_folder=temp)
            if not os.path.exists(exe):
                raise Exception(exe)
            self.assertTrue(os.stat(exe).st_size > 1000)


if __name__ == "__main__":
    unittest.main()
