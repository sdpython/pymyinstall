"""
@file
@brief Guess missing dependencies
"""


def get_default_ignore_modules():
    """
    A couple of modules have some dependencies on not supported modules
    or modules integrated to the standard distributiion such
    `enum34 <https://pypi.python.org/pypi/enum34>`_.
    This function returns this list.
    """
    return [
        "argparse",          # standard distribution (>= 3.5)
        "backports.weakref",  # standard distribution (>= 3.4)
        "distribute",        # standard distribution
        "enum",              # standard distribution (>= 3.4)
        "enum34",            # standard distribution (>= 3.4)
        "enum_compat",       # standard distribution (>= 3.4)
        "enum-compat",       # standard distribution (>= 3.4)
        "futures",           # standard distribution (>= 3.5)
        "keyrings.alt",      # weird this one on Windows
        # "guidata",
        # "monotonic",
        "ordereddict",      # standard distribution (>= 3.4)
        "pathlib",          # standard distribution (>= 3.5)
        "pip",              # almost standard distribution, should be rare
        # manny names for this one (PTable, not maintained anymore)
        "prettytable",
        "pycryptodome",     # many names for this one
        "pydocstyle",       # does not seem to be maintained
        "pyopengl",         # weird this one
        "pypiwin32",        # manny names for this one
        "pywin32",          # manny names for this one
        "pywin32_ctypes",   # manny names for this one
        "rope",             # for spyder
        "setuptools",       # standard distribution
        "typing",           # standard distribution (>= 3.6)
    ]


def _main_pipdeptree(local_only=False):
    """
    The function relies on module
    `pipdeptree.main <https://pypi.python.org/pypi/pipdeptree>`_.
    """
    try:
        # pip >= 10.0
        from pip._internal.utils.misc import get_installed_distributions
    except ImportError:
        # pip < 10.0
        from pip import get_installed_distributions

    default_skip = ['setuptools', 'pip', 'python', 'distribute']
    skip = default_skip + ['pipdeptree']
    pkgs = get_installed_distributions(local_only=local_only, skip=skip)
    req_map = dict((p.key, (p, p.requires())) for p in pkgs)
    return req_map


def missing_dependencies(specific=None, ignore_module=get_default_ignore_modules()):
    """
    return the list of missing dependencies for the installed modules

    @param      specific        look dependencies only for a specific module
    @param      ignore_module   list of modules not to consider as a missing dependency
                                even if they are installed
    @return                     list of missing dependencies as dictionary (module, missing dependencies)

    .. versionchanged:: 1.5
        Parameters *ignore_module*.
    """
    skip = set(ignore_module)
    tree = _main_pipdeptree()
    stack = {}
    for k, v in tree.items():
        if specific is not None and specific != k:
            continue
        for mod in v[1]:
            dep = mod.key
            if dep in skip:
                continue
            if dep not in tree:
                if "-" in dep:
                    dep = dep.replace("-", "_")
                elif "_" in dep:
                    dep = dep.replace("_", "_")
            if dep not in tree:
                if k not in stack:
                    stack[k] = []
                stack[k].append(dep)
    return stack
