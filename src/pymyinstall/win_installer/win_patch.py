"""
@file
@brief Patch the distribution to make it portable
"""
from __future__ import print_function

import os
import re


class ShebangException(Exception):
    """
    exception raised when the shebang is not correct
    """
    pass


def win_patch_paths(folder, path_to_python="", fLOG=print):
    """
    Paths are absolute when they are installed in all scripts *.exe*,
    we replaced them either by an empty string (``path_to_python == ""``)
    or the current folder.

    @param      folder          folder where to find the executable
    @param      path_to_python  new python path (replace by)
    @param      fLOG            logging function
    @return                     list of tuple ('exe or py', 'modified file')

    See `Create a portable Python with Pip on Windows <http://www.clemens-sielaff.com/create-a-portable-python-with-pip-on-windows/>`_
    The first three parameters can be environment variables.
    They will be replaced by their values.
    """
    if folder in os.environ:
        folder = os.environ[folder]
    if path_to_python not in (None, "") and path_to_python in os.environ:
        path_to_python = os.environ[path_to_python]
    if path_to_python is None:
        exe = os.path.join(folder, "python.exe")
        if os.path.exists(exe):
            path_to_python = os.path.absapth(folder)
        else:
            exe = os.path.join(folder, "..", "python.exe")
            path_to_python = os.path.normpath(
                os.path.abspath(os.path.join(folder, "..")))

    files = os.listdir(folder)

    if len(path_to_python) > 0 and not path_to_python.endswith("\\"):
        path_to_python += "\\"

    pattern = "([#][!]((([A-Za-z][:])?[/\\\\]?[-a-zA-Z0-9_.]+[/\\\\])*?)(pythonw?[.]exe))"
    reg_exe = re.compile(pattern, re.IGNORECASE)
    breg_exe = re.compile(bytes(pattern, encoding="ascii"), re.IGNORECASE)
    g_path_to_python = path_to_python.replace("\\", "\\\\")
    bg_path_to_python = bytes(g_path_to_python, encoding="ascii")
    b1 = bytes("#!", encoding="ascii")
    b2 = bytes("\\5", encoding="ascii")

    operations = []
    for file in files:
        full = os.path.join(folder, file)
        if os.path.isfile(full):
            ext = os.path.splitext(full)[-1]

            if ext in {".py", ""}:
                with open(full, "r") as f:
                    content = f.read()
                new_content = reg_exe.sub(
                    "#!" + g_path_to_python + "\\5", content)
                if new_content != content:
                    fLOG("update ", full)
                    operations.append(("update", full))
                    with open(full, "w") as f:
                        f.write(new_content)

            elif ext == ".exe":
                with open(full, "rb") as f:
                    content = f.read()
                new_content = breg_exe.sub(
                    b1 + bg_path_to_python + b2, content)
                if new_content != content:
                    fLOG("update ", full)
                    operations.append(("update", full))
                    try:
                        with open(full, "wb") as f:
                            f.write(new_content)
                    except PermissionError as e:
                        with open(full + ".replace", "wb") as f:
                            f.write(new_content)
                        mes = "unable to overwrite '{0}', it will have to be manually done, " + \
                              "another file was created with .replace as an extension".format(
                                  full)
                        raise Exception(mes) from e
            else:
                pass

    return operations
