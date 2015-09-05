"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
import re

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
    import pyquickhelper
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
    import pyquickhelper


from pyquickhelper import fLOG, get_temp_folder, synchronize_folder
from src.pymyinstall.win_installer.win_patch import win_patch_paths


class TestPatch(unittest.TestCase):

    def test_patch(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pattern = "([#][!](([A-Za-z][:])?[/\\\\]?[-a-zA-Z0-9_.]+[/\\\\])*pythonw?[.]exe)"
        reg_exe = re.compile(pattern, re.IGNORECASE)
        text = "#!C:\\github\\pymyinstall\\dist\\win_python_setup\\python\\python.exe"
        assert len(reg_exe.findall(text)) > 0

        temp = get_temp_folder(__file__, "temp_patch")
        data = os.path.join(temp, "..", "Scripts")
        dest = os.path.join(temp, "Scripts")
        if not os.path.exists(dest):
            os.mkdir(dest)

        if not os.path.exists(data):
            warnings.warn(
                "pyquickhelper forgots to copy this folder for python 2.7")
            raise FileNotFoundError(data)
        synchronize_folder(data, dest)

        pp = r"C:\github\pymyinstall\dist\win_python_setup\python"
        op = win_patch_paths(dest, pp, fLOG=fLOG)
        into = "#!python.exe"
        binto = bytes(into, encoding="ascii")
        assert len(op) > 0
        i = 0
        for _, full in op:
            with open(full, "rb") as f:
                content = f.read()
            if binto not in content:
                raise Exception(full)
            i += 1
        assert i == 3

if __name__ == "__main__":
    unittest.main()
