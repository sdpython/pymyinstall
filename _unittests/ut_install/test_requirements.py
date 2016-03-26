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


from src.pymyinstall import build_requirements
from src.pymyinstall.packaged import small_set, sphinx_theme_set, extended_set, ensae_set, teachings_set
from pyquickhelper.loghelper import fLOG


class TestRequirements (unittest.TestCase):

    def test_update_module(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod_list = small_set() + sphinx_theme_set() + extended_set() + \
            ensae_set() + teachings_set()
        res = build_requirements(mod_list)
        # fLOG(res)
        assert "pep8==1.5.7" in res

    def test_sort(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod_list = small_set() + sphinx_theme_set() + extended_set() + \
            ensae_set() + teachings_set()
        mod_list.sort()
        build_requirements(mod_list)
        k = [_.usage for _ in mod_list if _.usage is not None]
        k2 = list(sorted(_.usage for _ in mod_list if _.usage is not None))
        fLOG(k)
        fLOG(k2)
        assert k == k2

if __name__ == "__main__":
    unittest.main()
