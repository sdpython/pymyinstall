"""
@brief      test log(time=131s)
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


from src.pymyinstall.installhelper import install_graphviz
from pyquickhelper import fLOG


class TestGraphviz(unittest.TestCase):

    def test_install_graphviz(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            return

        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_graphviz")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            f = os.path.join(temp, _)
            if os.path.isfile(f):
                os.remove(f)

        if sys.platform.startswith("win"):
            r = install_graphviz(temp, fLOG=fLOG, install=False)
            exe = os.path.abspath(r)
            assert os.path.exists(exe)


if __name__ == "__main__":
    unittest.main()
