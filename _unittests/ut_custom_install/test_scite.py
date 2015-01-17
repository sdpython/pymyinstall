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


from src.pymyinstall import install_scite
from pyquickhelper import fLOG

class TestScite (unittest.TestCase):

    def test_install(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold,"temp_scite")
        if not os.path.exists(temp) : os.mkdir(temp)
        for _ in os.listdir(temp):
            f = os.path.join(temp,_)
            if os.path.isfile(f) :
                os.remove(f)

        tt = os.path.join(temp, "wscite")
        for _ in os.listdir(tt):
            f = os.path.join(tt,_)
            if os.path.isfile(f) :
                os.remove(f)

        if sys.platform.startswith("win"):
            r = install_scite(temp, fLOG = fLOG)
            exe = os.path.abspath(r)
            assert os.path.exists(exe)
            conf = exe.replace("SciTE.exe", "python.properties")
            fLOG(conf)
            assert os.path.exists(conf)
            with open(conf,"r") as f : content = f.read().lower()
            if sys.executable.lower() not in content and \
               sys.executable.lower().replace(".exe", "w.exe") not in content:
                raise Exception("{0} or {1} not in \n{2}".format(sys.executable, sys.executable.replace(".exe", "w.exe"), content))



if __name__ == "__main__"  :
    unittest.main ()