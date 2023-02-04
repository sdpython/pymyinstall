"""
@brief      test log(time=2s)
"""
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pandashelper import df2rst
from pymyinstall.packaged import get_package_set, name_sets_dataframe


class TestNameSet(unittest.TestCase):

    def test_documentation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        r = name_sets_dataframe()
        for m in r:
            fLOG("**", m)
        self.assertGreater(len(r), 1)
        df = pandas.DataFrame(r)
        df = df[["name", "description"]]
        rst = df2rst(df)
        fLOG(rst)
        self.assertGreater(len(rst), 1)

        nb = 0
        for mod in r:
            lp = get_package_set(mod["name"])
            if len(lp()) == 0 and mod["name"] != "pywin32":
                raise AssertionError(
                    "issue with module '{0}'".format(mod["name"]))
            nb += 1
        self.assertGreater(nb, 1)


if __name__ == "__main__":
    unittest.main()
