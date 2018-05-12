"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG


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
