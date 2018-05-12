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


from src.pymyinstall.installcustom import install_chromedriver

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


class TestChromeDriver(unittest.TestCase):

    def test_install_ChromeDriver(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            return

        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_chromedriver")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            f = os.path.join(temp, _)
            if os.path.isfile(f):
                os.remove(f)

        r = install_chromedriver(temp, fLOG=fLOG, install=True)
        for _ in r:
            fLOG(_)
        if sys.platform.startswith("win"):
            found = os.path.join(temp, "chromedriver.exe")
        if not os.path.exists(found):
            raise FileNotFoundError(found)


if __name__ == "__main__":
    unittest.main()
