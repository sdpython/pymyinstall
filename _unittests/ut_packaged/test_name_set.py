"""
@brief      test log(time=2s)

skip this test for regular run
"""

import sys
import os
import unittest
import re
import pandas

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


from src.pymyinstall.packaged import get_package_set, name_sets_dataframe
from pyquickhelper import fLOG, df2rst


class TestNameSet(unittest.TestCase):

    def test_documentation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        r = name_sets_dataframe()
        for m in r:
            fLOG("**", m)
        assert len(r) >= 6
        df = pandas.DataFrame(r)
        df = df[["name", "description"]]
        rst = df2rst(df)
        fLOG(rst)
        assert len(rst) > 0

        nb = 0
        for mod in r:
            l = get_package_set(mod["name"])
            assert len(l()) > 0
            nb += 1
        assert nb > 0

if __name__ == "__main__":
    unittest.main()
