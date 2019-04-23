"""
@brief      test log(time=45s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper.link_shortcuts import suffix


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
