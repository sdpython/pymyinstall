"""
@brief      test log(time=3s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper import add_shortcut_to_desktop_for_module


class TestOnlyMain (unittest.TestCase):

    def test_spyder(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if __name__ == "__main__":
            add_shortcut_to_desktop_for_module("spyder")


if __name__ == "__main__":
    unittest.main()
