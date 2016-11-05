"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest

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

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
        sys.path.append(os.environ["PYQUICKHELPER"])
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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
