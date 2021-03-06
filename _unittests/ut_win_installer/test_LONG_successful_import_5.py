"""
@brief      test log(time=105s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.win_installer import import_every_module


class TestLONGSuccessfulImport5(unittest.TestCase):

    def test_long_import_every_module(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        nb = int("".join(_ for _ in os.path.split(
            __file__)[-1] if "0" <= _ <= "9"))

        res = import_every_module(
            sys.executable, None, fLOG=fLOG, start=50 * nb, end=50 * (nb + 1))
        nb = 0
        for r in res:
            if not r[0]:
                fLOG("---------------------------------")
                fLOG("FAILED", r[1], "\nOUT\n", r[2], "\nERR\n", r[3])
            else:
                nb += 1
        assert nb > 0 or sys.version_info[:2] <= (2, 7)


if __name__ == "__main__":
    unittest.main()
