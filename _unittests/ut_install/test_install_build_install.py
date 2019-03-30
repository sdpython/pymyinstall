"""
@brief      test tree node (time=3s)
"""
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG, noLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installhelper.install_venv_helper import create_virtual_env, run_venv_script
from pymyinstall import ModuleInstall


class TestInstallBuildInstall(unittest.TestCase):

    def test_build_install(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        # module
        ModuleInstall("multi_key_dict", "github", "formiaczek",
                      custom=["build", "install"])

        if __name__ != "__main__":
            warnings.warn("does not work well from a virtual environment")
            return

        temp = get_temp_folder(__file__, "temp_build_install")

        create_virtual_env(temp, fLOG=fLOG)
        setup = os.path.normpath(os.path.join(
            temp, "..", "..", "..", "setup.py"))
        self.assertTrue(os.path.exists(setup))
        folder = os.path.split(setup)[0]
        cmd = "{0} install".format(setup)
        fLOG("CMD: " + cmd)
        cwd = os.getcwd()
        os.chdir(folder)
        try:
            run_venv_script(temp, cmd, fLOG=noLOG, is_cmd=True)
        except Exception as e:
            version = "1.1"
            g = os.path.join(temp, "Lib", "site-packages",
                             "pymyinstall-%s-py3.5.egg" % version, "pymyinstall")
            if not os.path.exists(g):
                raise e
        os.chdir(cwd)

        fLOG("INSTALL: module")
        script = """from pymyinstall import ModuleInstall
                    m = ModuleInstall('multi_key_dict', 'github', 'formiaczek', custom=['build', 'install'])
                    m.download(temp_folder='{0}')
                    m.install(temp_folder='{0}')
                    """.replace("                    ", "").format(temp.replace("\\", "/")).strip(" \n\r")
        fLOG(script)
        run_venv_script(temp, script, fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
