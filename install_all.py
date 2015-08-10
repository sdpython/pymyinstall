import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
from pymyinstall import installation_ensae
skip = ["pyquickhelper", "pyensae", "pyrsslocal",
        "pymmails", "ensae_teaching_cs", "code_beatrix",
        "actuariat_python"]
for mod in installation_ensae():
    if mod.name in skip:
        continue
    mod.install(log=True)
