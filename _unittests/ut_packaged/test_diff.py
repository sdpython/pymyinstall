"""
@brief      test log(time=200s)

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


from src.pymyinstall import ModuleInstall, complete_installation, small_installation, datascientist
from pyquickhelper import fLOG


class TestDifference(unittest.TestCase):

    def test_diff(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        name = set(_.name for _ in small_installation())
        keep = []
        for mod in complete_installation():
            if mod.name not in name:
                keep.append(mod)
        assert len(keep) > 0

        for mod in keep:
            if mod.mname is None:
                fLOG(
                    "ModuleInstall('{0}', '{1}'),".format(mod.name, mod.kind))
            else:
                fLOG("ModuleInstall('{0}', '{1}', mname='{2}'),".format(
                    mod.name, mod.kind, mod.mname))

    def test_diff(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        res = datascientist(
            ensae=True, teachings=True, full=True, list_only=True)
        count = {}
        for mod in res:
            count[mod.name] = 1

        assert "pyquickhelper" in count
        assert "rodeo" in count
        assert "code_beatrix" in count


if __name__ == "__main__":
    unittest.main()
