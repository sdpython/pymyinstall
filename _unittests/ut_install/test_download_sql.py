"""
@brief      test log(time=20s)
"""

import sys, os, unittest

try :
    import src
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    import src

try :
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..","pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import pyquickhelper


from src.pymyinstall.installhelper.module_install import ModuleInstall
from pyquickhelper import fLOG, get_temp_folder

class TestDownloadSQLAlchemy (unittest.TestCase):

    def test_install_ipython(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_sqlalchemy")

        if sys.platform.startswith("win"):
            m = ModuleInstall("SQLAlchemy", "wheel", fLOG = fLOG)
            whl = m.download(temp_folder = temp)
            assert os.path.exists(whl)


if __name__ == "__main__"  :
    unittest.main ()