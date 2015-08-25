"""
@file
@brief Patch the distribution to make it portable
"""
from __future__ import print_function

import os


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

        operations = []
        for prog in ["python.exe", "pythonw.exe"]:
            shebangs = ["#!" + python_path + prog,
                        "#!" + python_path[0].lower() + python_path[1:] + prog]
            bshebangs = [bytes(shebang, encoding="ascii") for shebang in shebangs]
            into = "#!" + os.path.normpath(path_to_python + prog)
            binto = bytes(into, encoding="ascii")

            for shebang in shebangs:
                fLOG("SHEBANG: replace {0} by {1}".format(shebang, into))

            for file in files:
                full = os.path.join(folder, file)
                if os.path.isfile(full):
                    ext = os.path.splitext(full)[-1]

                    if ext in {".py", ""}:
                        with open(full, "r") as f:
                            content = f.read()
                        for shebang in shebangs:
                            if shebang in content:
                                content = content.replace(shebang, into)
                                fLOG("update ", full)
                                operations.append(("update", full))
                                with open(full, "w") as f:
                                    f.write(content)
                    elif ext == ".exe":
                        with open(full, "rb") as f:
                            content = f.read()
                        for bshebang in bshebangs:
                            if bshebang in content:
                                content = content.replace(bshebang, binto)
                                fLOG("update ", full)
                                operations.append(("update", full))
                                with open(full, "wb") as f:
                                    f.write(content)
                    else:
                        pass

        return operations
