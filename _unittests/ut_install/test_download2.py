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
from pyquickhelper import fLOG

class TestDownload2 (unittest.TestCase):

    def test_install_gmpy2(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold,"temp_download_gmpy2")
        if not os.path.exists(temp) : os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp,_)) :
                os.remove(os.path.join(temp,_))

        if sys.platform.startswith("win"):
            m = ModuleInstall("gmpy2", "wheel", fLOG = fLOG)
            whl = m.download(temp_folder = temp)
            assert os.path.exists(whl)


if __name__ == "__main__"  :
    unittest.main ()