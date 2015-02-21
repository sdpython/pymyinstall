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


from src.pymyinstall import add_shortcut_to_desktop_for_module
from pyquickhelper import fLOG

class TestOnlyMain (unittest.TestCase):

    def test_spyder(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        if __name__ == "__main__":
            add_shortcut_to_desktop_for_module("spyder")

if __name__ == "__main__"  :
    unittest.main ()