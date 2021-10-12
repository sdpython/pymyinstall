"""
@brief      test log(time=1s)
"""
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pandashelper import df2rst
from pymyinstall.installhelper.module_install_version import get_module_version, get_module_metadata
from pymyinstall.packaged import small_set


class TestInstallModuleVersion(unittest.TestCase):

    def test_module_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = get_module_version("matplotlib")
        self.assertTrue(len(str(res)) > 0)

        res = get_module_metadata("matplotlib")
        fLOG(res)
        self.assertTrue(isinstance(res, dict))

    def test_all_module_summary(self):

        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = small_set()
        mod.sort()
        df = pandas.DataFrame(_.as_dict(rst_link=True) for _ in mod)
        df = df[["usage", "rst_link", "kind", "version", "installed",
                 "license", "purpose", "classifier"]]
        df.columns = ["usage", "name", "kind", "version", "installed",
                      "license", "purpose", "classifier"]
        lic = df[~df.license.isnull()]
        # fLOG(lic[["name","license"]])
        fLOG("license", lic.shape)
        nolic = df[df.license.isnull()]
        fLOG("no license", nolic.shape)
        fLOG(nolic[["name", "license"]])
        self.assertTrue(lic.shape[0] > 0)

        rst = df2rst(df)
        # fLOG(rst)
        self.assertTrue(len(rst) > 1000)


if __name__ == "__main__":
    unittest.main()
