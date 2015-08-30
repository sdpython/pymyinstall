"""
@file
@brief Guess missing dependencies
"""
import pip
import sys


def _main_pipdeptree(local_only=False, addw=False, freeze=True, list_all=True):
    """
    replicate pipdeptree.main to catch the standard output
    """
    from pipdeptree import req_version, top_pkg_name, non_top_pkg_name, top_pkg_src
    from pipdeptree import non_top_pkg_src, has_multi_versions, confusing_deps, render_tree
    from pipdeptree import cyclic_deps, peek_into

    default_skip = ['setuptools', 'pip', 'python', 'distribute']
    skip = default_skip + ['pipdeptree']
    pkgs = pip.get_installed_distributions(local_only=local_only, skip=skip)

    pkg_index = dict((p.key, p) for p in pkgs)
    req_map = dict((p, p.requires()) for p in pkgs)

    # show warnings about possibly confusing deps if found and
    # warnings are enabled
    if addw:
        confusing = confusing_deps(req_map)
        if confusing:
            sys.stderr.write(
                'Warning!!! Possible confusing dependencies found:\n')
            for xs in confusing:
                for i, (p, d) in enumerate(xs):
                    if d.key in skip:
                        continue
                    pkg = top_pkg_name(p)
                    req = non_top_pkg_name(d, pkg_index[d.key])
                    tmpl = '  {0} -> {1}' if i > 0 else '* {0} -> {1}'
                    sys.stderr.write(tmpl.format(pkg, req))
                    sys.stderr.write("\n")
            sys.stderr.write('-' * 72)
            sys.stderr.write("\n")

        is_empty, cyclic = peek_into(cyclic_deps(pkgs, pkg_index))
        if not is_empty:
            sys.stderr.write('Warning!!! Cyclic dependencies found:\n')
            for xs in cyclic:
                sys.stderr.write('- {0}\n'.format(xs))
            sys.stderr.write('-' * 72 + "\n")

    if freeze:
        top_pkg_str, non_top_pkg_str = top_pkg_src, non_top_pkg_src
    else:
        top_pkg_str, non_top_pkg_str = top_pkg_name, non_top_pkg_name

    tree = render_tree(pkgs,
                       pkg_index=pkg_index,
                       req_map=req_map,
                       list_all=list_all,
                       top_pkg_str=top_pkg_str,
                       non_top_pkg_str=non_top_pkg_str,
                       bullets=not freeze)
    return tree


def missing_dependencies():
    """
    return the list of missing dependencies for the installed modules

    @return         list of missing dependencies as dictionary (module, missing dependencies)

    the function relis on module pipdeptree.
    """
    tree = _main_pipdeptree()
    lines = tree.split("\n")
    installed = set()
    stack = {}
    parent = None
    for line in lines:
        if line.startswith(" "):
            if "==" not in line:
                if line.strip() not in ["setuptools", "astroid", "logilab-common"]:
                    if parent not in stack:
                        stack[parent] = []
                    stack[parent].append(line.strip())
        else:
            parent = line.split("==")[0]
            installed.add(parent)
    for k in stack:
        v = list(sorted(set(stack[k])))
        v = [_ for _ in v if _ not in installed]
        v.sort()
        stack[k] = v
    return stack
