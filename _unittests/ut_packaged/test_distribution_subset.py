"""
@brief      test log(time=2s)

skip this test for regular run
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


from pyquickhelper.loghelper import fLOG
from src.pymyinstall.packaged import find_module_install
from src.pymyinstall.packaged import ensae_set, pyensae_set, ensae_teaching_cs_set, all_set, ensae_fullset


class TestDisributionSubSet(unittest.TestCase):

    def walk_text(self, set_mod):
        nb = 0
        for mod in set_mod:
            assert mod
            nb += 1
            find = find_module_install(mod.name, must_exist=True)
            assert find
        assert nb > 0
        return nb

    def test_ensae_set(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb = self.walk_text(ensae_set())
        fLOG(self._testMethodName, nb)

    def test_pyensae_set(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb = self.walk_text(pyensae_set())
        fLOG(self._testMethodName, nb)

    def test_ensae_teaching_cs_set(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb = self.walk_text(ensae_teaching_cs_set())
        fLOG(self._testMethodName, nb)

    def test_all_set(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb = self.walk_text(all_set())
        fLOG(self._testMethodName, nb)

    def test_ensae_fullset(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb = self.walk_text(ensae_fullset())
        fLOG(self._testMethodName, nb)


if __name__ == "__main__":
    unittest.main()
