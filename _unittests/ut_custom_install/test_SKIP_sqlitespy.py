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


from src.pymyinstall.installcustom import install_sqlitespy


class TestSqliteSpy (unittest.TestCase):

    def test_install_sqllitespy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_sqllitespy")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        if sys.platform.startswith("win"):
            fLOG(
                "http://www.yunqa.de/delphi/lib/exe/fetch.php?hash=938481&media=" +
                "http%3A%2F%2Fwww.yunqa.de%2Fdelphi%2Fdownloads%2FSQLiteSpy_1.9.7.zip")
            exe = install_sqlitespy(temp, fLOG=fLOG, backup=True)
            fLOG("exe", exe)
            self.assertTrue(os.path.exists(exe))

# http://www.yunqa.de/delphi/lib/exe/fetch.php?hash=938481;media=http%3A%2F%2Fwww.yunqa.de%2Fdelphi%2Fdownloads%2FSQLiteSpy_1.9.7.zip
# http://www.yunqa.de/delphi/lib/exe/fetch.php?hash=938481&media=http%3A%2F%2Fwww.yunqa.de%2Fdelphi%2Fdownloads%2FSQLiteSpy_1.9.7.zip


if __name__ == "__main__":
    unittest.main()
