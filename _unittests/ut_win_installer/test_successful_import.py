"""
@brief      test log(time=7s)
"""
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.win_installer import import_every_module


class TestSuccessfulImport(unittest.TestCase):

    def test_import_every_module(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = import_every_module(
            sys.executable, None, fLOG=fLOG, start=0, end=10)
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
