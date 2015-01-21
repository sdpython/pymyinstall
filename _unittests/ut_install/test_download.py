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

class TestDownload (unittest.TestCase):

    def test_install(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold,"temp_download")
        if not os.path.exists(temp) : os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp,_)) :
                os.remove(os.path.join(temp,_))
        if os.path.exists(os.path.join(temp,"jsdifflib-master")) :
            for _ in os.listdir(os.path.join(temp,"jsdifflib-master")):
                os.remove(os.path.join(os.path.join(temp,"jsdifflib-master"),_))

        m = ModuleInstall("jsdifflib","github",gitrepo="cemerick", fLOG = fLOG)
        files = m.download(temp_folder = temp, unzipFile=True)
        assert len(files)>0
        for _ in files: assert os.path.exists(_)

    def test_install_mlpy(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold,"temp_download_mlpy")
        if not os.path.exists(temp) : os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp,_)) :
                os.remove(os.path.join(temp,_))
                
        if sys.platform.startswith("win"):
            m = ModuleInstall("mlpy", "wheel", fLOG = fLOG)
            exe = m.download(temp_folder = temp)
            assert os.path.exists(exe)




if __name__ == "__main__"  :
    unittest.main ()