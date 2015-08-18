"""
@file
@brief Functions to prepare a setup on Windows, R functions
"""

import io
import json
import os
import sys

if sys.version_info[0] == 2:
    from codecs import open


r_kernel = {
    "display_name": "R%s",
    "language": "R",
    "argv": [
        "%R_HOME%\\bin\\x64\\R.exe",
        "--quiet",
        "-e",
        "IRkernel::main()",
        "--args",
        "{connection_file}"
    ]
}

python_kernel = {
    "language": "python",
    "display_name": "Python 3%s",
    "argv": [
        "%PYTHON_WINHOME%\\python.exe",
        "-m",
        "IPython.kernel",
        "-f",
        "{connection_file}"
    ]
}

julia_kernel = {
    "display_name": "Julia%s",
    "language": "julia",
    "argv": [
        "%JULIA_HOME%\\bin\\julia.exe",
        "-i",
        "-F",
        "%JULIA_PKGDIR%\\v0.3\\IJulia\\src\\kernel.jl",
        "{connection_file}"
    ],
    "codemirror_mode": "julia"
}


def add_kernel_jupyter(kernel, path, tools_path, python_path, suffix="WP"):
    """
    add a kernel to jupyter

    @param      kernel          dictionary (see global variable in this module)
    @param      path            where to add it
    @param      tools_path      tools paths
    @param      python_path     python path
    @param      suffix          added in bracket at the end of the display name
    @return                     created file
    """
    kernel = kernel.copy()
    suffix = " (%s)" % suffix
    kernel["display_name"] = kernel["display_name"] % suffix
    name = kernel["display_name"]
    name = name.replace(" ", "_").replace("(", "").replace(")", "")
    fold = os.path.join(path, name)
    if not os.path.exists(fold):
        os.mkdir(fold)
    st = io.StringIO()

    # replacements
    argv = kernel["argv"]
    for i in range(len(argv)):
        if "%" in argv[i]:
            argv[i] = argv[i].replace("%PYTHON_WINHOME%", python_path) \
                             .replace("%R_HOME%", os.path.join(tools_path, "R")) \
                             .replace("%JULIA_HOME%", os.path.join(tools_path, "Julia")) \
                             .replace("%JULIA_PKGDIR%", os.path.join(tools_path, "Julia", "pkg"))

    # dump
    json.dump(kernel, st)
    ker = os.path.join(fold, "kernel.json")
    with open(ker, "w", encoding="utf8") as f:
        f.write(st.getvalue())
    return ker


def install_kernels(tools_path, python_path, suffix="WP"):
    """
    install available kernels on Windows

    @param      tools_path      tools paths
    @param      python_path     python path
    @param      suffix          suffix
    @return                     list of creating files
    """
    dest = os.environ["ProgramData"]
    jupyter = os.path.join(dest, "jupyter", "kernels")
    if not os.path.exists(jupyter):
        os.makedirs(jupyter)
    res = []
    if os.path.exists(python_path):
        res.append(
            add_kernel_jupyter(python_kernel, jupyter, tools_path, python_path, suffix))
    if os.path.exists(os.path.join(tools_path, "R")):
        res.append(
            add_kernel_jupyter(r_kernel, jupyter, tools_path, python_path, suffix))
    if os.path.exists(os.path.join(tools_path, "Julia")):
        res.append(
            add_kernel_jupyter(julia_kernel, jupyter, tools_path, python_path, suffix))
    return res
