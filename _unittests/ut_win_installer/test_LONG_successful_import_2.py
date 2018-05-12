"""
@brief      test log(time=102s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG

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


from src.pymyinstall.win_installer import import_every_module


if sys.version_info[0] == 2:
    FileNotFoundError = Exception


class TestLONGSuccessfulImport2(unittest.TestCase):

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
        assert nb > 0


if __name__ == "__main__":
    unittest.main()
