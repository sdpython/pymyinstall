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


from pyquickhelper import fLOG, get_temp_folder
from src.pymyinstall.installhelper import get_module_dependencies, get_module_metadata


class TestModuleDependencies (unittest.TestCase):

    def test_dependencies(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = get_module_dependencies("matplotlib", deep=True)
        for r in res:
            assert isinstance(r, tuple)
            fLOG(r)
        if len(res) < 3:
            raise Exception(str(res) + "\n" + str(get_module_metadata("matplotlib")))


if __name__ == "__main__":
    unittest.main()
