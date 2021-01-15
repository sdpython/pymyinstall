"""
@brief      test log(time=2s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.packaged import find_module_install, minimal_set, small_set


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

    def test_small_set(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb = self.walk_text(small_set())
        fLOG(self._testMethodName, nb)

    def test_minimal_set(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb = self.walk_text(minimal_set())
        fLOG(self._testMethodName, nb)


if __name__ == "__main__":
    unittest.main()
