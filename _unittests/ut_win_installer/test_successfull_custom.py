"""
@brief      test log(time=100s)
"""
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.win_installer import import_every_module


class TestSuccessfulCustom(unittest.TestCase):

    def test_long_import_every_module(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        subset = ["xlrd"]
        subset.extend("docutils pandas numpy".split())
        res = import_every_module(
            sys.executable, subset, fLOG=fLOG)
        nb = 0
        for r in res:
            if not r[0]:
                fLOG("---------------------------------")
                fLOG("FAILED", r[1], "\nOUT\n", r[2], "\nERR\n", r[3])
            else:
                nb += 1
        assert nb > 0


if __name__ == "__main__":
    unittest.main()
