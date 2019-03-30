"""
@brief      test tree node (time=3s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installhelper.install_venv_helper import create_virtual_env, run_venv_script


class TestInstallWithDeps(unittest.TestCase):

    def test_venv_install_deps(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fold = os.path.dirname(os.path.abspath(__file__))
        src_ = os.path.normpath(os.path.abspath(
            os.path.join(fold, "..", "..", "src")))
        assert os.path.exists(src_)
        temp = get_temp_folder(__file__, "temp_venv_install_deps")

        if __name__ != "__main__":
            warnings.warn("does not work well from a virtual environment")
            return

        if sys.version_info[0] == 2:
            # using nose so previous test is true
            warnings.warn(
                "does not work well from a virtual environment (Python 2.7)")
            return

        out = create_virtual_env(temp, fLOG=fLOG)
        src_ = src_.replace("\\", "/")
        temp = temp.replace("\\", "/")

        script = ["import sys",
                  "sys.path.append('{0}')".format(src_),
                  "from pymyinstall.packaged import install_module_deps",
                  "install_module_deps('imbox', temp_folder='{0}', source='2')".format(
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
