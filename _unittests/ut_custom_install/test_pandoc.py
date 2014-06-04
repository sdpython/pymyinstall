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
    

from src.pymyinstall.installhelper.install_custom import install_pandoc
from pyquickhelper import fLOG

class TestPandoc (unittest.TestCase):
    
    def test_pandoc(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold,"temp_pandoc")
        if not os.path.exists(temp) : os.mkdir(temp)
        for _ in os.listdir(temp):
            if ".msi" in _ :
                os.remove(os.path.join(temp,_))
        r = install_pandoc (temp_folder = temp, fLOG = fLOG, install = False)
        assert os.path.exists(r)
        
        


if __name__ == "__main__"  :
    unittest.main ()    
