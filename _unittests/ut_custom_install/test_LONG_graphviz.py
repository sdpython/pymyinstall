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


from src.pymyinstall.installcustom import install_graphviz
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestGraphviz(unittest.TestCase):

    def _test_install_graphviz(self):
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
            r = install_graphviz(temp, fLOG=fLOG, install=False, source="2")
            exe = os.path.abspath(r)
            assert os.path.exists(exe)

    def test_install_graphviz_zip(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            return

        temp = get_temp_folder(__file__, "temp_graphviz_zip")

        if sys.platform.startswith("win"):
            r = install_graphviz(temp, fLOG=fLOG, install=True, source="zip")
            exe = os.path.abspath(r)
            assert os.path.exists(exe)
            exe = os.path.join(temp, "Graphviz", "bin", "dot.exe")
            assert os.path.exists(exe)


if __name__ == "__main__":
    unittest.main()
