"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.fix import fix_win32ctypes_core_cffi__advapi32_py


class TestFixEol(unittest.TestCase):

    def test_fix_eol(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 6):
            temp = get_temp_folder(__file__, "temp_fix_eol")
            data = os.path.join(temp, "..", "data", "_file.pytry")
            out = os.path.join(temp, "out.py")
            fix_win32ctypes_core_cffi__advapi32_py(data, out, fLOG=fLOG)
            self.assertTrue(os.path.exists(out))


if __name__ == "__main__":
    unittest.main()
