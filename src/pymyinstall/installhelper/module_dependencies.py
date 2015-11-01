"""
@file
@brief Guess missing dependencies
"""
import sys


def _main_pipdeptree(local_only=False):
    """
    replicate pipdeptree.main to catch the standard output
    """
    from pip import get_installed_distributions

    default_skip = ['setuptools', 'pip', 'python', 'distribute']
    skip = default_skip + ['pipdeptree']
    pkgs = get_installed_distributions(local_only=local_only, skip=skip)

    pkg_index = dict((p.key, p) for p in pkgs)
    req_map = dict((p.key, (p, p.requires())) for p in pkgs)
    return req_map


def missing_dependencies():
    """
    return the list of missing dependencies for the installed modules

    @return         list of missing dependencies as dictionary (module, missing dependencies)

    the function relis on module pipdeptree.
    """
    skip = {"setuptools", "pip", "distribute"}
    tree = _main_pipdeptree()
    stack = {}
    for k, v in tree.items():
        for mod in v[1]:
            dep = mod.key
            if dep in skip:
                continue
            if dep not in tree:
                if k not in stack:
                    stack[k] = []
                stack[k].append(dep)
    return stack
