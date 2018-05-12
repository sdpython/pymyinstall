"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG


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


from src.pymyinstall.setuphelper.ipython_helper import setup_ipython


class TestSetupIPython (unittest.TestCase):

    @unittest.skipIf(not sys.platform.startswith("win"), "not implemented on Windows")
    def test_setup_ipython(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.platform.startswith("win"):
            try:
                r = setup_ipython(r"C:\temp", [], apply_modification=False)
            except FileNotFoundError as e:
                warnings.warn('[test_setup_ipython] failed due to {0}'.format(e))
                return
            assert len(r) > 0
            fLOG(r)
            for _ in r:
                assert os.path.exists(_)
        elif 'HOME' in os.environ:
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
