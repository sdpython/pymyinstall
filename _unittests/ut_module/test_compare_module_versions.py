"""
@brief      test log(time=0s)
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


from pyquickhelper import fLOG
from src.pymyinstall.packaged import all_set
from src.pymyinstall.installhelper import get_wheel_version, compare_version


class TestCompareVersion(unittest.TestCase):

    def test_compare_versions(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if not sys.platform.startswith("win"):
            # useful only on Windows
            return

        mods = [mod for mod in all_set() if mod.kind in ("wheel",)]
        fLOG(len(mods))
        assert len(mods) > 0

        diff = []
        for i, mod in enumerate(mods[0:]):
            if i % 10 == 0:
                fLOG(i, mod)
            url1 = mod.get_exewheel_url_link(wheel=True)
            url2 = mod.get_exewheel_url_link2(wheel=True, source="2")
            # fLOG(i, url1, url2)
            n1 = url1[-1]
            n2 = url2[-1]
            v1 = get_wheel_version(n1)
            v2 = get_wheel_version(n2)
            cmp = compare_version(v1, v2)
            if cmp != 0:
                fLOG("---", i, v1, v2, mod.name)
                diff.append(mod)

        assert len(diff) <= 5


if __name__ == "__main__":
    unittest.main()
