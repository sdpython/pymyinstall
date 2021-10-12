"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper import get_module_dependencies, get_module_metadata
from pymyinstall.installhelper.install_cmd_helper import is_conda_distribution
from pymyinstall.installhelper import missing_dependencies
from pymyinstall.installhelper.pip_helper import get_installed_distributions


class TestModuleDependenciesBug(unittest.TestCase):

    def common_function(self, name, use_pip=None):
        res = get_module_dependencies(name, deep=True, use_pip=use_pip)
        for k, v in sorted(res.items()):
            self.assertTrue(isinstance(v, tuple))
            fLOG(k, "-->", v)
        if len(res) < 3:
            pkgs = get_installed_distributions(
                local_only=False, skip=[])
            req_map = dict((p.key, (p, p.requires())) for p in pkgs)
            mat = req_map.get(name, None)
            raise AssertionError("len(res)={0}\nres={1}\ndata={2}\nmat={3}".format(
                len(res), res, get_module_metadata(name), mat))

    def test_dependencies_luigi(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        try:
            import luigi
            mod = "luigi"
            self.assertTrue(luigi is not None)
        except ImportError:
            mod = "pandas"

        if not is_conda_distribution():
            dep = missing_dependencies(mod)
            self.assertEqual(dep, {})
            self.common_function(mod)
        else:
            # issue with Anaconda, not investigated
            return


if __name__ == "__main__":
    unittest.main()
