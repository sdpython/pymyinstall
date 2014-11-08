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


from src.pymyinstall.setuphelper.ipython_helper import setup_ipython
from pyquickhelper import fLOG

class TestSetupIPython (unittest.TestCase):

    def test_setup(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        if sys.platform.startswith("win"):
            r = setup_ipython(r"C:\temp", [], apply_modification = False)
            assert len(r) > 0
            fLOG(r)
            for _ in r : assert os.path.exists(_)
        else:
            return

            fold = os.environ["HOME"]
            fold = os.path.join(fold, "temp")
            if not os.path.exists(fold): os.mkdir(fold)
            r = setup_ipython(fold, [], apply_modification = False)
            assert len(r) > 0
            fLOG(r)
            for _ in r : assert os.path.exists(_)

if __name__ == "__main__"  :
    unittest.main ()