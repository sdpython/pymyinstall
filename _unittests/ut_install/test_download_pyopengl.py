"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from pymyinstall.packaged import find_module_install


class TestDownloadPyOpenGL(ExtTestCase):

    def test_install_pyopengl(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_pyopengl")
            m = find_module_install("PyOpenGL_accelerate")
            exe = m.download(
                temp_folder=temp,
                file_save=os.path.join(
                    temp,
                    "out_page.html"), source="2")
            self.assertTrue(os.path.exists(exe))
            self.assertIn("accelerate", m.name)
            down = os.listdir(temp)
            if len(down) != 1:
                raise AssertionError(down)
            self.assertIn("accelerate", down[0])


if __name__ == "__main__":
    unittest.main()
