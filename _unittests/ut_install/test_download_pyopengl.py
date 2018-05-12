"""
@brief      test log(time=20s)
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


from src.pymyinstall.packaged import find_module_install


class TestDownloadPyOpenGL(unittest.TestCase):

    def test_install_pyopengl(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win"):
            temp = get_temp_folder(__file__, "temp_download_pyopengl")
            m = find_module_install("OpenGL")
            exe = m.download(
                temp_folder=temp,
                file_save=os.path.join(
                    temp,
                    "out_page.html"), source="2")
            self.assertTrue(os.path.exists(exe))
            if "accelerate" in m.name:
                raise Exception(m.name)
            down = os.listdir(temp)
            if len(down) != 1:
                raise Exception(down)
            if "accelerate" in down[0]:
                raise Exception(down[0])


if __name__ == "__main__":
    unittest.main()
