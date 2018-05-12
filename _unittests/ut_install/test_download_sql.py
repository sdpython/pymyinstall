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


from src.pymyinstall.installhelper.module_install import ModuleInstall


class TestDownloadSQLAlchemy (unittest.TestCase):

    def test_install_ipython(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_sqlalchemy")

        if sys.platform.startswith("win"):
            m = ModuleInstall("SQLAlchemy", "wheel", fLOG=fLOG)
            whl = m.download(temp_folder=temp, source="2")
            self.assertTrue(os.path.exists(whl))


if __name__ == "__main__":
    unittest.main()
