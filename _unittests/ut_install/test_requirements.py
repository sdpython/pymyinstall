"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall import build_requirements
from pymyinstall.packaged import small_set


class TestRequirements (unittest.TestCase):

    def test_update_module(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod_list = small_set()
        res = build_requirements(mod_list)
        lines = res.split("\n")
        fLOG(len(lines))
        for i, line in enumerate(lines):
            fLOG(i, line)
        assert 'pep8' in res
        assert len(lines) >= 550

    def test_sort(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod_list = small_set()
        mod_list.sort()
        build_requirements(mod_list)
        k = [_.usage for _ in mod_list if _.usage is not None]
        k2 = list(sorted(_.usage for _ in mod_list if _.usage is not None))
        fLOG(k)
        fLOG(k2)
        assert k == k2


if __name__ == "__main__":
    unittest.main()
