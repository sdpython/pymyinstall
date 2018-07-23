"""
@file
@brief Some fixes for deprecated functions and not updated packages.
"""
import os
import sys


def fix_win32ctypes_core_cffi__advapi32_py(filename=None, fileout=None, fLOG=None):
    """
    Fixes the following issue:

    ::

          File "C:\\Python37-x64\\lib\\site-packages\\win32ctypes\\pywin32\\__init__.py", line 21, in <module>
            from win32ctypes.pywin32 import win32api
          File "C:\\Python37-x64\\lib\\site-packages\\win32ctypes\\pywin32\\win32api.py", line 23, in <module>
            from win32ctypes.core import _common, _kernel32, _backend
          File "C:\\Python37-x64\\lib\\site-packages\\win32ctypes\\core\\__init__.py", line 39, in <module>
            from .cffi import _advapi32, _common, _kernel32
          File "C:\\Python37-x64\\lib\\site-packages\\win32ctypes\\core\\cffi\\_advapi32.py", line 198

            ^
        SyntaxError: invalid syntax
        Command exited with code 1

    If that errors happens, you could add:

    ::

        python -c "from pymyinstall.fix import fix_win32ctypes_core_cffi__advapi32_py;fix_win32ctypes_core_cffi__advapi32_py(fLOG=print)"
    """
    if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 6):
        if filename is None:
            filename = os.path.join(os.path.dirname(
                sys.executable), "lib\\site-packages\\win32ctypes\\core\\cffi\\_advapi32.py")
        if not os.path.exists(filename):
            if fLOG:
                fLOG(
                    "[fix_win32ctypes_core_cffi__advapi32_py] '{0}' not found".format(filename))
            return
        if fileout is None:
            fileout = filename
        if fLOG:
            fLOG(
                "[fix_win32ctypes_core_cffi__advapi32_py] found '{0}'".format(filename))
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("\r", "\n").replace("\n\n", "\n")
        with open(fileout, "w", encoding="utf-8") as f:
            f.write(content)


if __name__ == "__main__":
    fix_win32ctypes_core_cffi__advapi32_py()
