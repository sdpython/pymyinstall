import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
print("----")
from pymyinstall import win_python_setup
from pymyinstall.packaged import all_set, minimal_set


if False:
    from pymyinstall.win_installer.win_setup_r import _script
    r = r"C:\github\pymyinstall\dist\win_python_setup\tools\R"
    out = r_run_script(r, _script)
    print(out)


if True:
    list_modules = all_set()
    win_python_setup(module_list=list_modules, verbose=True,
                     download_only=True,
                     no_setup=True,
                     selection={"R", "VS"})

if False:
    win_python_setup(module_list=minimal_set(), verbose=True,
                     download_only=False,
                     no_setup=True,
                     selection={},
                     notebooks=[])
