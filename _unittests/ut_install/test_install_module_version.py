"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
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


from pyquickhelper import fLOG, df2rst
from src.pymyinstall.installhelper.module_install_version import get_module_version, call_get_installed_distributions, get_module_metadata
from src.pymyinstall.packaged import ensae_fullset


class TestInstallModuleVersion(unittest.TestCase):

    def test_module_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = get_module_version("matplotlib")
        fLOG(res)
        assert len(res) > 0

        res = get_module_metadata("matplotlib")
        fLOG(res)
        assert isinstance(res, dict)

    def test_all_module_summary(self):

        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = ensae_fullset()
        mod.sort()
        df = pandas.DataFrame(_.as_dict(rst_link=True) for _ in mod)
        df = df[["usage", "rst_link", "kind", "version",
                 "license", "purpose", "classifier"]]
        df.columns = ["usage", "name", "kind", "version",
                      "license", "purpose", "classifier"]
        lic = df[~df.license.isnull()]
        # fLOG(lic[["name","license"]])
        fLOG("license", lic.shape)
        nolic = df[df.license.isnull()]
        fLOG("no license", nolic.shape)
        fLOG(nolic[["name", "license"]])
        assert lic.shape[0] > 0

        rst = df2rst(df)
        # fLOG(rst)
        assert len(rst) > 1000


if __name__ == "__main__":
    unittest.main()
