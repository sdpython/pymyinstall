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


from src.pymyinstall.installhelper.module_install_version import get_wheel_version
from pyquickhelper.loghelper import fLOG


class TestInstallHelper(unittest.TestCase):

    def test_version_name(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        v = get_wheel_version("rpy2-2.6.0-cp34-none-win_amd64.whl")
        if v != "2.6.0":
            raise Exception(v)

        v = get_wheel_version("tornado-4.2-cp34-none-win_amd64.whl")
        if v != "4.2":
            raise Exception(v)

if __name__ == "__main__":
    unittest.main()
