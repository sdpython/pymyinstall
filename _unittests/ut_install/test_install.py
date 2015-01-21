# coding: latin-1
"""
@brief      test log(time=1s)
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
from src.pymyinstall.installhelper.install_cmd_helper import run_cmd
from pyquickhelper import fLOG

class TestInstall (unittest.TestCase):

    def test_run_cmd (self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        out,err = run_cmd("find", wait=True, do_not_log = True)

    def test_install(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        m = ModuleInstall("pip", "pip")
        assert m.install()
        m = ModuleInstall("pip", "exe")
        assert m.install()



if __name__ == "__main__"  :
    unittest.main ()