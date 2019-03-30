"""
@brief      test log(time=2s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.packaged import find_module_install
from pymyinstall.packaged import ensae_set, pyensae_set, all_set, ensae_fullset


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
