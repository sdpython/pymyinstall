import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
print("----", sys.version_info)
from pymyinstall import win_python_setup
from pymyinstall.packaged import all_set, minimal_set, get_package_set


if False:
    from pymyinstall.win_installer.win_setup_r import _script
    r = r"C:\github\pymyinstall\dist\win_python_setup\tools\R"
    out = r_run_script(r, _script)
    print(out)


if False:
    list_modules = all_set()
    win_python_setup(module_list=list_modules, verbose=True,
                     download_only=False, no_setup=True,
                     selection={"R", "VS", "jenkins"},
                     source="2")

elif False:
    win_python_setup(module_list=minimal_set(), verbose=True,
                     download_only=False, no_setup=True,
                     selection={}, notebooks=[], source="2")
else:
    win_python_setup(module_list=get_package_set("datascientistbase")(),
                     verbose=True, download_only=False, no_setup=True,
                     selection={}, notebooks=[], source="2", embed=False)
