"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper import get_module_dependencies, get_module_metadata, version_consensus
from pymyinstall.installhelper.module_install_exceptions import WrongVersionError
from pymyinstall.installhelper.install_cmd_helper import is_conda_distribution
from pymyinstall.installhelper.pip_helper import get_installed_distributions


class TestModuleDependencies(unittest.TestCase):

    def common_function(self, name, use_pip=None):
        res = get_module_dependencies(name, deep=True, use_pip=use_pip)
        for k, v in sorted(res.items()):
            assert isinstance(v, tuple)
            fLOG(k, "-->", v)
        if len(res) < 3:
            pkgs = get_installed_distributions(
                local_only=False, skip=[])
            req_map = dict((p.key, (p, p.requires())) for p in pkgs)
            mat = req_map.get(name, None)
            raise AssertionError(
                "len(res)={0}\nres={1}\ndata={2}\nmat={3}".format(
                    len(res), res, get_module_metadata(name), mat))

    def test_dependencies_matplotlib(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if not is_conda_distribution():
            self.common_function("matplotlib")
        else:
            # issue with Anaconda, not investigated
            return

    def test_version_consensus(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertEqual(version_consensus('>=2.3', '>=2.4'), '>=2.4')
        self.assertEqual(version_consensus('>=2.5', '>=2.4'), '>=2.5')
        self.assertEqual(version_consensus('>2.3', '>2.4'), '>2.4')
        self.assertEqual(version_consensus('>2.5', '>2.4'), '>2.5')
        self.assertEqual(version_consensus('>=2.3', '>2.4'), '>2.4')
        self.assertEqual(version_consensus('>2.3', '>=2.4'), '>=2.4')
        self.assertEqual(version_consensus('>2.5', '>2.4'), '>2.5')
        self.assertEqual(version_consensus('>=2.5', '>2.4'), '>=2.5')
        self.assertEqual(version_consensus('>2.5', '>=2.4'), '>2.5')

        self.assertEqual(version_consensus('<=2.3', '<=2.4'), '<=2.3')
        self.assertEqual(version_consensus('<=2.5', '<=2.4'), '<=2.4')
        self.assertEqual(version_consensus('<2.3', '<2.4'), '<2.3')
        self.assertEqual(version_consensus('<2.5', '<2.4'), '<2.4')
        self.assertEqual(version_consensus('<=2.3', '<2.4'), '<=2.3')
        self.assertEqual(version_consensus('<2.3', '<=2.4'), '<2.3')
        self.assertEqual(version_consensus('<2.5', '<2.4'), '<2.4')
        self.assertEqual(version_consensus('<=2.5', '<2.4'), '<2.4')
        self.assertEqual(version_consensus('<2.5', '<=2.4'), '<=2.4')

        self.assertEqual(version_consensus('==2.3', '<=2.4'), '==2.3')
        self.assertEqual(version_consensus('<=2.5', '==2.4'), '==2.4')
        self.assertEqual(version_consensus('==2.3', '<2.4'), '==2.3')
        self.assertEqual(version_consensus('<2.5', '==2.4'), '==2.4')
        self.assertEqual(version_consensus('>2.3', '==2.4'), '==2.4')
        self.assertEqual(version_consensus('==2.5', '>2.4'), '==2.5')
        self.assertEqual(version_consensus('==2.5', '>2.4'), '==2.5')
        self.assertEqual(version_consensus('==2.5', '>=2.4'), '==2.5')

        try:
            version_consensus('<=2.3', '>=2.4')
        except WrongVersionError:
            pass

        try:
            version_consensus('<=2.3', '==2.4')
        except WrongVersionError:
            pass


if __name__ == "__main__":
    # TestModuleDependencies().test_dependencies_matplotlib()
    unittest.main()
