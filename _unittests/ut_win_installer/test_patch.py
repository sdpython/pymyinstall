"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
import re
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.filehelper import synchronize_folder

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


from src.pymyinstall.win_installer.win_patch import win_patch_paths


if sys.version_info[0] == 2:
    FileNotFoundError = Exception


class TestPatch(unittest.TestCase):

    def test_patch(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            # not setup for python 2.7
            return

        pattern = "([#][!](([A-Za-z][:])?[/\\\\]?[-a-zA-Z0-9_.]+[/\\\\])*pythonw?[.]exe)"
        reg_exe = re.compile(pattern, re.IGNORECASE)
        text = "#!C:\\github\\pymyinstall\\dist\\win_python_setup\\python\\python.exe"
        assert len(reg_exe.findall(text)) > 0

        temp = get_temp_folder(__file__, "temp_patch")
        data = os.path.join(temp, "..", "data", "Scripts")
        dest = os.path.join(temp, "Scripts")
        if not os.path.exists(dest):
            os.mkdir(dest)

        if not os.path.exists(data):
            warnings.warn(
                "pyquickhelper forgot to copy this folder for python 2.7")
            raise FileNotFoundError(data)
        synchronize_folder(data, dest)

        op = win_patch_paths(dest, "", fLOG=fLOG)
        into = "#!python.exe"
        binto = bytes(into, encoding="ascii")
        assert len(op) > 0
        i = 0
        for _, full in op:
            with open(full, "rb") as f:
                content = f.read()
            if binto not in content:
                raise Exception("file:{}\ncontent:\n{}".format(full, content))
            i += 1
        exp = 3
        if i != exp:
            raise Exception("i != " + str(exp) + "\n" + str(op))

        op = win_patch_paths(dest, None, fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
