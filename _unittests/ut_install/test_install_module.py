"""
@brief      test log(time=1s)
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


from src.pymyinstall.installhelper.module_install import compare_version
from src.pymyinstall.installhelper.module_install_version import get_module_version
from pyquickhelper.loghelper import fLOG


class TestInstallModule (unittest.TestCase):

    def test_module_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        d = get_module_version(None)
        if len(d) < 10:
            for k, v in sorted(d.items()):
                fLOG(k, v)
            raise Exception("el {0}\nD\n{1}".format(len(d), d))

    def test_compare_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        self.assertEqual(compare_version("0.16.0", "0.16.2"), -1)


if __name__ == "__main__":
    unittest.main()
