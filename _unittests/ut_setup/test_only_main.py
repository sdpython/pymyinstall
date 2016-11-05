"""
@brief      test log(time=3s)
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


from src.pymyinstall.installhelper import add_shortcut_to_desktop_for_module
from pyquickhelper.loghelper import fLOG


class TestOnlyMain (unittest.TestCase):

    def test_spyder(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if __name__ == "__main__":
            add_shortcut_to_desktop_for_module("spyder")


if __name__ == "__main__":
    unittest.main()
