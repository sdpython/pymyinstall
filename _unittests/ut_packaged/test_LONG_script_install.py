"""
@brief      test log(time=2s)
"""
import unittest
import warnings
from pyquickhelper.loghelper import fLOG


class TestLONGScriptInstall(unittest.TestCase):

    def test_pypi(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import xmlrpc.client as xmlrpc_client
        module_name = "version_information"
        url = 'https://pypi.org/pypi/pip/json'
        functions = []
        with xmlrpc_client.ServerProxy(url) as pypi:
            try:
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
            except xmlrpc_client.ProtocolError as e:
                warnings.warn("PyPI protocal has changed {0}".format(e))
                functions = [None, None]
            assert len(functions) > 1


if __name__ == "__main__":
    unittest.main()
