"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
import pandas

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


from pyquickhelper import fLOG, df2rst
from src.pymyinstall.installhelper.module_install_version import choose_most_recent
from src.pymyinstall.packaged import ensae_fullset


class TestInstallModuleVersionFast(unittest.TestCase):

    def test_choose_most_recent(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mods = [("**", 'numpy-1.10.0+mkl-cp34-none-win_amd64.whl'),
                ("**", 'numpy-1.9.3+mkl-cp34-none-win_amd64.whl')]
        ch = choose_most_recent(mods)
        fLOG(ch)
        self.assertEqual(
            ch, ('**', 'numpy-1.10.0+mkl-cp34-none-win_amd64.whl'))


if __name__ == "__main__":
    unittest.main()
