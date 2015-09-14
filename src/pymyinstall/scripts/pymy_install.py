#!python
"""
script which installs all modules,
works on Linux and Windows if the module is
included the list of modules handled by this module
"""
from __future__ import print_function
import sys
import os
import argparse


def get_parser():
    """
    defines the way to parse the magic command ``%head``
    """
    parser = argparse.ArgumentParser(
        description='update modules, consider wheels when the module includes C++ files')
    parser.add_argument(
        '-s',
        '--skip',
        default="ete,dataspyre,pycuda,cubehelix",
        help='list of modules to skip (not to be updated) separated by a comma')
    parser.add_argument(
        '-f',
        '--folder',
        default="build/update_modules",
        help='folder where modules will be downloaded')
    parser.add_argument(
        '-d',
        '--deps',
        action='store_true',
        help='install a module or the modules with their dependencies')
    parser.add_argument(
        '--set',
        default="-",
        help='set of module to install, see documentation of function get_name_set to get a comprehensive list, this option is ignored if a module is specified on the command line')
    parser.add_argument(
        '--schedule',
        action='store_true',
        help='do not install the modules, returned the list scheduled to be installed')
    parser.add_argument(
        'module',
        nargs='*',
        default="all",
        help='update only the list of modules included in this list or all modules if not specified or equal to all')
    return parser


def do_main(temp_folder="build/update_modules",
            skip_module=["ete", "dataspyre", "pycuda", "cubehelix"],
            list_module=None, deps=False, schedule_only=False):
    """
    calls function @see fn install_all but is meant to be added to scripts folder

    @param      temp_folder     folder where modules will be downloaded
    @param      skip_module     skip the module on this list
    @param      list_module     list of modules to update or None for all
    @param      deps            install a module with its dependencies
    @param      schedule_only   if True, the function returns the list of modules scheduled to be installed

    If *deps* is True, *list_module* cannot be empty.
    """
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    try:
        from pymyinstall.packaged import install_all
    except ImportError:
        folder = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", ".."))
        sys.path.append(folder)
        from pymyinstall.packaged import install_all
    res = install_all(temp_folder=temp_folder, verbose=True,
                      skip_module=skip_module, list_module=list_module, deps=deps,
                      schedule_only=schedule_only)
    if schedule_only:
        print("SCHEDULED")
        for r in res:
            print(r)


def main():
    """
    calls function @see fn install_all but is meant to be added to scripts folder,
    parse command line arguments
    """
    parser = get_parser()
    try:
        res = parser.parse_args()
    except SystemExit:
        print(parser.format_usage())
        res = None

    if res is not None:
        skip_module = res.skip.split(",")
        list_module = None if res.module in [
            "all", "", None, []] else res.module
        if list_module is None and res.set is not None and len(res.set) > 0:
            list_module = res.set
        do_main(temp_folder=res.folder, skip_module=skip_module,
                list_module=list_module, deps=res.deps, schedule_only=res.schedule)


if __name__ == "__main__":
    main()
