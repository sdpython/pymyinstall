"""
@brief      test log(time=2s)

skip this test for regular run
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


class TestLONGScriptInstall(unittest.TestCase):

    def test_pypi(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            return
        import xmlrpc.client as xmlrpc_client
        module_name = "version_information"
        url = 'https://pypi.python.org/pypi'
        functions = []
        with xmlrpc_client.ServerProxy(url) as pypi:
            for f in pypi.system.listMethods():
                fLOG(f)
                sig = pypi.system.methodSignature(f)
                fLOG("    ", sig)
                h = pypi.system.methodHelp(f)
                fLOG("    ", h)
                functions.append(f)
                if len(functions) > 1:
                    break
            available = pypi.package_releases(module_name, True)
            fLOG(available)
        assert len(functions) > 1


if __name__ == "__main__":
    unittest.main()
