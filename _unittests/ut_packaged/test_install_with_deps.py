"""
@brief      test tree node (time=3s)
"""

import sys
import os
import unittest
import re
import shutil
import warnings
import pandas

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

from pyquickhelper import fLOG, get_temp_folder
from src.pymyinstall.installhelper.install_venv_helper import create_virtual_env, run_venv_script

if sys.version_info[0] == 2:
    from codecs import open


class TestInstallWithDeps(unittest.TestCase):

    def test_venv_install_deps(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fold = os.path.dirname(os.path.abspath(__file__))
        src = os.path.normpath(os.path.abspath(
            os.path.join(fold, "..", "..", "src")))
        assert os.path.exists(src)
        temp = get_temp_folder(__file__, "temp_venv_install_deps")

        if __name__ != "__main__":
            warnings.warn("does not work well from a virtual environment")
            return

        out = create_virtual_env(temp, fLOG=fLOG)
        src = src.replace("\\", "/")
        temp = temp.replace("\\", "/")

        script = ["import sys",
                  "sys.path.append('{0}')".format(src),
                  "from pymyinstall.packaged import install_module_deps",
                  "install_module_deps('imbox', temp_folder='{0}')".format(
                      temp),
                  ]

        file_script = os.path.join(temp, "test_install_deps.py")
        with open(file_script, "w") as f:
            f.write("\n".join(script))

        out = run_venv_script(temp, file_script, fLOG=fLOG, file=True)
        if "installing module  six" not in out:
            raise Exception(out)


if __name__ == "__main__":
    unittest.main()
