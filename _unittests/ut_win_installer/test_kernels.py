"""
@brief      test log(time=3s)
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


from src.pymyinstall.win_installer.win_ipy_kernels import add_kernel_jupyter, python_kernel

if sys.version_info[0] == 2:
    from codecs import open


class TestKernels(unittest.TestCase):

    def test_kernels(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_kernels")
        ker = add_kernel_jupyter(
            python_kernel, temp, temp, os.path.dirname(sys.executable), suffix="ZZZ")
        with open(ker, "r", encoding="utf8") as f:
            content = f.read()
        fLOG(content)
        assert '"IPython.kernel", "-f", "{connection_file}"' in content


if __name__ == "__main__":
    unittest.main()
