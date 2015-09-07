import sys
import os
sys.path.append("src")
from pymyinstall.win_installer import import_pywin32, fix_pywin32_installation

try:
    import win32com
except ImportError as e:
    fix_pywin32_installation()

#exe = os.path.abspath(os.path.dirname(sys.executable))
#os.environ["PATH"] = os.environ["PATH"] + ";" + exe

import win32com
