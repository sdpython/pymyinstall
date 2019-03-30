"""
@brief      test log(time=2s)

skip this test for regular run
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.packaged import find_module_install


class TestFindModule(unittest.TestCase):

    def test_find_module_install(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = find_module_install("docutils==0.8")
        fLOG(mod)
        assert mod.version == "0.8"


if __name__ == "__main__":
    unittest.main()
