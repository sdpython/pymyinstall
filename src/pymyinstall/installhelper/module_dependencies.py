"""
@file
@brief Guess missing dependencies
"""


def _main_pipdeptree(local_only=False):
    """
    replicate pipdeptree.main to catch the standard output
    """
    from pip import get_installed_distributions

    default_skip = ['setuptools', 'pip', 'python', 'distribute']
    skip = default_skip + ['pipdeptree']
    pkgs = get_installed_distributions(local_only=local_only, skip=skip)
    req_map = dict((p.key, (p, p.requires())) for p in pkgs)
    return req_map


def missing_dependencies(specific=None):
    """
    return the list of missing dependencies for the installed modules

    @param      specific    look dependencies only for a specific module
    @return                 list of missing dependencies as dictionary (module, missing dependencies)

    the function relis on module pipdeptree.
    """
    skip = {"setuptools", "pip", "distribute", "ordereddict", "argparse", "futures",
            "pywin32", "pywin32_ctypes"}
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
