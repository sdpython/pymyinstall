"""
@brief      test log(time=45s)
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


from src.pymyinstall.installhelper.link_shortcuts import suffix


class Testinks (unittest.TestCase):

    def test_links(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        suf = suffix()
        fLOG("*", suf)
        self.assertTrue("." in suf)
        self.assertEqual(len(suf.split(".")), 3)


if __name__ == "__main__":
    unittest.main()
