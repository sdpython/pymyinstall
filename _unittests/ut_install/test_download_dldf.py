"""
@brief      test log(time=20s)

skip this test for regular run
"""

import sys
import os
import unittest
import re

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
    import pyquickhelper
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
    import pyquickhelper


from src.pymyinstall.installhelper.module_install_page_wheel import _cg_dl1 as dl1, _cg_dl as dl
from pyquickhelper import fLOG


class TestPrivateFunctions(unittest.TestCase):

    def test_private_function(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        dd = dl([45, 106, 108, 50, 99, 51, 46, 55, 97, 109, 104, 112, 56, 95, 53, 47, 52, 118, 105, 54, 111, 110, 119, 100, 101, 120, 48],
                "ABI&lt;@&lt;F1?2I92056&#62;6J04;370EDEH0FBE=89GC@6F:2",
                fLOG=fLOG)
        self.assertEqual("vix848wj/lxml-3.5.0-cp27-none-win_amd64.whl", dd)

        dd = dl([114, 110, 108, 57, 122, 119, 105, 121, 104, 112, 99, 72, 95, 82, 45, 117, 118, 101, 111, 97, 53, 120, 47, 109, 100, 51, 46, 54, 48, 52],
                "4;=?03@7F2EG2&#62;IJDJL&#62;:9IM&#62;1B1A&#62;561&lt;CGHKMJ582", fLOG=fLOG)
        fLOG(dd)

        dd = dl([54, 119, 120, 99, 108, 105, 47, 52, 104, 111, 95, 118, 112, 97, 110, 100, 48, 101, 56, 45, 46, 106, 109, 53, 51],
                ";52B7B1E642F4CHDGD@C3&lt;H7C&#62;9&#62;AC15&#62;:=F?07D184", fLOG=fLOG)
        fLOG(dd)

        dd = dl([52, 51, 97, 111, 118, 110, 99, 47, 95, 100, 109, 108, 104, 112, 119, 54, 46, 101, 120, 105, 53, 45, 106, 48, 56],
                "4CBH0H&gt;F7;B:;E1@D@GE6=10E535AE&gt;C582:9?0@&gt;&lt;;", fLOG=fLOG)
        fLOG(dd)


if __name__ == "__main__":
    unittest.main()
