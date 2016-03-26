"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import warnings

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


from src.pymyinstall.setuphelper.ipython_helper import setup_ipython
from pyquickhelper.loghelper import fLOG


class TestSetupIPython (unittest.TestCase):

    def test_setup(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        warnings.warn("not implemented for jupyter 4.0")
        return
        if sys.platform.startswith("win"):
            r = setup_ipython(r"C:\temp", [], apply_modification=False)
            assert len(r) > 0
            fLOG(r)
            for _ in r:
                assert os.path.exists(_)
        else:
            return

            fold = os.environ["HOME"]
            fold = os.path.join(fold, "temp")
            if not os.path.exists(fold):
                os.mkdir(fold)
            r = setup_ipython(fold, [], apply_modification=False)
            assert len(r) > 0
            fLOG(r)
            for _ in r:
                assert os.path.exists(_)

if __name__ == "__main__":
    unittest.main()
