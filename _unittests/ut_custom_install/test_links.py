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


from src.pymyinstall.installhelper.link_shortcuts import suffix
from pyquickhelper import fLOG

class Testinks (unittest.TestCase):

    def test_install(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        suf = suffix()
        fLOG("*",suf)
        assert "." in suf
        assert len(suf.split(".")) == 3


if __name__ == "__main__"  :
    unittest.main ()