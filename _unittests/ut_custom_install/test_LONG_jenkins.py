"""
@brief      test log(time=45s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder

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


from src.pymyinstall.installcustom import install_jenkins


class TestJenkins(unittest.TestCase):

    def test_install_jenkins(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            return

        temp = get_temp_folder(__file__, "temp_jenkins")

        if sys.platform.startswith("win"):
            r = install_jenkins(temp, fLOG=fLOG, install=False)
            fLOG(r)
            z = os.path.join(temp, "jenkins.war")
            self.assertTrue(os.path.exists(z))


if __name__ == "__main__":
    unittest.main()
