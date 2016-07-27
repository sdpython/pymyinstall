"""
@file
@grief Functions to help using pywin32.
"""

from __future__ import print_function

import sys
import os
import shutil

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def import_pywin32():
    """
    For the module ``pywin32``,
    this function tries to add the path to the DLL to ``PATH``
    before throwing the exception:
    ``DLL load failed: The specified module could not be found``.

    It checks the instruction ``import win32com``.
    """
    try:
        import win32com
    except ImportError as e:
        if "DLL load failed:" in str(e):
            import os
            import sys
            import numpy
            from distutils.sysconfig import get_python_lib

            paths = set([os.path.join(
                os.path.split(sys.executable)[0], "Lib", "site-packages", "pywin32_system32"),
                os.path.join(get_python_lib(), "pywin32_system32"),
                os.path.join(
                    os.path.dirname(numpy.__file__), "..", "pywin32_system32"),
            ])

            epath = os.environ["PATH"]
            for path in paths:
                # exe = os.path.abspath(os.path.dirname(sys.executable))
                os.environ["PATH"] = epath + ";" + path

                try:
                    import win32com
                    return win32com
                except ImportError:
                    # we try the next path
                    pass

            try:
                import win32com
                return win32com
            except ImportError:
                # addition for WinPython
                exe = os.path.abspath(os.path.dirname(sys.executable))
                os.environ["PATH"] = os.environ["PATH"] + ";" + exe
                try:
                    import win32com
                    return win32com
                except ImportError:
                    dll = os.listdir(path)
                    dll = [os.path.join(path, _) for _ in dll if "dll" in _]
                    if len(dll) == 0:
                        raise ImportError("Did you install pywin32?") from e
                    else:
                        raise ImportError(
                            "Some DLL must be copied:\n" + "\n".join(dll)) from e
        else:
            raise e


def fix_pywin32_installation(python_path=None, fLOG=print):
    """
    copy DLL at the right place

    @param      python_path     python path
    @param      fLOG            logging function

    .. faqref::
        :title: pywin32 does not work)

        To check module `pywin32 <https://pypi.python.org/pypi/pywin32>`_ is installed,
        you must run::

            import win32com

        If it displays the message ``ImportError: DLL load failed``, it means
        it was not able to find DLLs *pythoncom34.dll*, *pythoncom34.dll*.
        Two solutions:

        * Add the folder ``C:\\Python34_x64\\Lib\\site-packages\\pywin32_system32``
        to environment variable ``PATH``. That's what function
        @see fn import_pywin32 is doing every time it is called.
        * Copy the two DLLs to ``C:\\Windows\\System32``, that's what function
        @see fn fix_pywin32_installation does if it is run with admin rights.

    .. versionadded:: 1.1
    """
    if python_path is None:
        python_path = sys.executable.replace("w.exe", ".exe")
    if os.path.isfile(python_path):
        python_path = os.path.dirname(python_path)
    fdll = os.path.join(python_path, "Lib",
                        "site-packages", "pywin32_system32")
    dest_fold = [python_path, os.path.join(python_path, "DLLs"),
                 "C:\\Windows\\System32"]
    for dll in os.listdir(fdll):
        full = os.path.join(fdll, dll)
        if os.path.isdir(full):
            continue
        for destf in dest_fold:
            dest = os.path.join(destf, dll)
            if not os.path.exists(dest):
                shutil.copy(full, destf)
                fLOG("copy", full, "to", destf)
            else:
                fLOG("already copied", dest)
