"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


class TestMakeExe(unittest.TestCase):

    def test_make_exe(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_make_exe")

        from pip._vendor.distlib.scripts import ScriptMaker
        maker = ScriptMaker(os.path.join(temp, "..", "..", "..", "src"), temp)
        maker.make('run_update_all = pymyinstall:update_all')
        if sys.platform.startswith("win"):
            exe = os.path.join(temp, "run_update_all.exe")
            assert os.path.exists(exe)


if __name__ == "__main__":
    unittest.main()
