"""
@brief      test log(time=20s)
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


from src.pymyinstall.packaged import find_module_install
from src.pymyinstall.installhelper import compare_version, get_wheel_version


class TestDownloadAzure(unittest.TestCase):

    def test_install_azure(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_azure")

        r1 = compare_version("2.0.0rc5", "1.0.3")
        r2 = compare_version("1.0.3", "2.0.0rc5")
        self.assertTrue(r1 * r2 < 0)
        self.assertTrue(r1 > 0)
        if sys.platform.startswith("win") and sys.version_info[0] >= 3:
            m = find_module_install("azure")
            if m.pip_options is None:
                raise Exception("no pip_options, issue '{0}'".format(m))
            m.fLOG = fLOG
            name = m.download(temp_folder=temp)
            v = get_wheel_version(name)
            r = compare_version(v, "1.9.9")
            if r <= 0:
                raise Exception(
                    "unexception version for '{0}',\nshould be >= 1.9.9 not '{1}'".format(name, v))
            fLOG(m.version, v, name)
            self.assertTrue(os.path.exists(name))
            self.assertTrue("azure" in name)


if __name__ == "__main__":
    unittest.main()
