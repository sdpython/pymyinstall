"""
@brief      test log(time=3s)
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


from src.pymyinstall import datascientist
from pyquickhelper import fLOG, get_temp_folder

class TestInstallMain (unittest.TestCase):

    def test_install_main(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = get_temp_folder(__file__, "temp_install_manual")
        if __name__ == "__main__":
            #exe = os.path.dirname(sys.executable)
            #scr = os.path.join(exe, "Script")
            #os.environ["PATH"] = os.environ["PATH"] + ";" + ";".join( [exe, scr] )
            datascientist(fold, full = True, fLOG=fLOG,
                    skip=["pyquickhelper","pyensae","ensae_teaching_cs","pymyinstall"])

if __name__ == "__main__"  :
    unittest.main ()