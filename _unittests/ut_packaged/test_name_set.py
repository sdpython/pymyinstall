"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pandashelper import df2rst

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


from src.pymyinstall.packaged import get_package_set, name_sets_dataframe


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

        if sys.version_info[0] == 2:
            # less tests on Python 2.7
            return

        nb = 0
        for mod in r:
            lp = get_package_set(mod["name"])
            if len(lp()) == 0 and mod["name"] != "pywin32":
                raise Exception("issue with module '{0}'".format(mod["name"]))
            nb += 1
        assert nb > 0


if __name__ == "__main__":
    unittest.main()
