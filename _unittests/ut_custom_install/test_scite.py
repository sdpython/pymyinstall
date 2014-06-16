"""
@brief      test log(time=45s)
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
    

from src.pymyinstall.installhelper.install_custom import install_scite
from pyquickhelper import fLOG

class TestScite (unittest.TestCase):
    
    def test_install(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold,"temp_scite")
        if not os.path.exists(temp) : os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp,_)) :
                os.remove(os.path.join(temp,_))
        
        exe = install_scite(temp, fLOG = fLOG)
        assert os.path.exists(exe)
        conf = exe.replace("SciTE.exe", "python.properties")
        assert os.path.exists(conf)
        with open(conf,"r") as f : content = f.read()
        assert sys.executable in content
        


if __name__ == "__main__"  :
    unittest.main ()    
