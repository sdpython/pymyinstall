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


from src.pymyinstall.installhelper.module_install import ModuleInstall
from src.pymyinstall import build_requirements
from src.pymyinstall.packaged import small_set, sphinx_theme_set, extended_set, azure_set, ensae_set, teachings_set, bigdata_set
from pyquickhelper import fLOG, get_temp_folder


class TestRequirements (unittest.TestCase):

    def test_update_module(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod_list = small_set() + sphinx_theme_set() + extended_set() + \
            azure_set() + ensae_set() + teachings_set() + bigdata_set()
        res = build_requirements(mod_list)
        fLOG(res)
        assert "pep8==1.5.7" in res


if __name__ == "__main__":
    unittest.main()
