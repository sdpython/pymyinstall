"""
@brief      test log(time=20s)
"""

import sys, os, unittest, re

try :
    import src
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    import src

try :
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..","pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import pyquickhelper


from src.pymyinstall.installhelper.install_cmd import ModuleInstall
from pyquickhelper import fLOG

class TestDownloadPyQt (unittest.TestCase):

    def test_install_pyqt(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold,"temp_download")
        if not os.path.exists(temp) : os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp,_)) :
                os.remove(os.path.join(temp,_))

        if sys.platform.startswith("win"):
            fLOG("install", "pyqt")
            m = ModuleInstall("PyQt", "exe", mname = "pyqt", fLOG = fLOG)
            exe = m.download(temp_folder = temp, file_save = os.path.join(temp, "out_page.html"))
            assert os.path.exists(exe)

    def test_regex(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        file = os.path.join(fold,"data","page.html")
        with open(file,"r",encoding="utf8") as f : content = f.read()
        reg = ModuleInstall.expKPageQt.replace("Py3.3",
                        "Py{0}.{1}".format(sys.version_info.major,sys.version_info.minor))
        fLOG(reg)
        reg = re.compile(reg)
        find = reg.findall(content)
        assert len(find) > 0
        fLOG(find)

if __name__ == "__main__"  :
    unittest.main ()