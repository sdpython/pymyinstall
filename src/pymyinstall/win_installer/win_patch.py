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


def win_patch_paths(folder, python_path, path_to_python="", fLOG=print):
    """
    path are absolute when they are installed,
    see `Create a portable Python with Pip on Windows <http://www.clemens-sielaff.com/create-a-portable-python-with-pip-on-windows/>`_

    @param      folder          folder when to find the executable
    @param      python_path     python path (string to replace)
    @param      path_to_python  new python path (replace by)
    @param      fLOG            logging function
    @return                     list of tuple ('exe or py', 'modified file')

    The first three parameter can be environment variables.
    They will be replaced by their values.
    """
    if isinstance(python_path, list):
        operations = []
        for pyt in python_path:
            op = win_patch_paths(folder, pyt, path_to_python, fLOG)
            operations.extend(op)
        return operations
    else:
        if folder in os.environ:
            folder = os.environ[folder]
        if python_path in os.environ:
            python_path = os.environ[python_path]
            if python_path == "EMPTY_STRING":
                python_path = ""
        if path_to_python in os.environ:
            path_to_python = os.environ[path_to_python]

        files = os.listdir(folder)

        if len(python_path) > 0 and not python_path.endswith("\\"):
            python_path += "\\"
        if len(path_to_python) > 0 and not path_to_python.endswith("\\"):
            path_to_python += "\\"

        pattern = "([#][!](([A-Za-z][:])?[/\\\\]?[-a-zA-Z0-9_.]+[/\\\\])*pythonw?[.]exe)"
        reg_exe = re.compile(pattern, re.IGNORECASE)
        breg_exe = re.compile(bytes(pattern, encoding="ascii"), re.IGNORECASE)

        all_she = set()
        bintos = set()

        operations = []
        for prog in ["python.exe", "pythonw.exe"]:
            shebangs = ["#!" + python_path + prog,
                        "#!" + python_path[0].upper() + python_path[1:] + prog,
                        "#!" + python_path[0].lower() + python_path[1:] + prog]
            bshebangs = [bytes(shebang, encoding="ascii")
                         for shebang in shebangs]
            into = "#!" + os.path.normpath(path_to_python + prog)
            binto = bytes(into, encoding="ascii")
            bintos.add(into)
            bintos.add(binto)

            for shebang in shebangs:
                fLOG("SHEBANG: replace {0} by {1}".format(shebang, into))

            for file in files:
                full = os.path.join(folder, file)
                if os.path.isfile(full):
                    ext = os.path.splitext(full)[-1]

                    if ext in {".py", ""}:
                        with open(full, "r") as f:
                            content = f.read()
                        fall = set(_[0] for _ in reg_exe.findall(content))
                        if len(fall) > 0:
                            for shebang in shebangs:
                                if shebang in content:
                                    content = content.replace(shebang, into)
                                    fLOG("update ", full)
                                    operations.append(("update", full))
                                    with open(full, "w") as f:
                                        f.write(content)
                            fall2 = set(_[0] for _ in reg_exe.findall(content))
                            if len(fall2) > 0:
                                all_she.update(fall2)

                    elif ext == ".exe":
                        with open(full, "rb") as f:
                            content = f.read()
                        fall = set(_[0] for _ in breg_exe.findall(content))
                        if len(fall) > 0:
                            for bshebang in bshebangs:
                                if bshebang in content:
                                    content = content.replace(bshebang, binto)
                                    fLOG("update ", full)
                                    operations.append(("update", full))
                                    with open(full, "wb") as f:
                                        f.write(content)
                            fall2 = set(_[0]
                                        for _ in breg_exe.findall(content))
                            if len(fall2) > 0:
                                all_she.update(fall2)
                    else:
                        pass

        for i, she in enumerate(all_she):
            fLOG("  shebang ", i, ":", type(she), she)
        intersection = bintos.intersection(all_she)
        if len(intersection) == 0:
            raise ShebangException("no expected shebang was found\nFOUND:\n{0}\nEXPECTED:\n{1}".format(
                "\n".join(str(_) for _ in all_she), "\n".join(str(_) for _ in bintos)))

        return operations
