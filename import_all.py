import sys
print(sys.executable)
import platform
print(platform.architecture())
sys.path.append("src")
from pymyinstall import installation_ensae
skip = ["pyquickhelper", "pyensae", "pyrsslocal",
        "pymmails", "ensae_teaching_cs"]
for mod in installation_ensae():
    mod.install(log =True)
