#!python
"""
script which updates all modules,
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
        '--set',
        default="-",
        help='set of module to install, see documentation of function get_name_set to get a comprehensive list, this option is ignored if a module is specified on the command line')
    parser.add_argument(
        '--source',
        default="",
        help='overwrite the source of the wheels')
    parser.add_argument(
        '--schedule',
        action='store_true',
        help='do not update the modules, returned the list scheduled to be updated')
    parser.add_argument(
        'module',
        nargs="*",
        default="all",
        help='update only the list of modules included in this list or all modules if not specified or equal to all')
    return parser


def do_main(temp_folder="build/update_modules",
            skip_module=["ete", "dataspyre", "pycuda", "cubehelix"],
            list_module=None, schedule_only=False, source=None):
    """
    calls function @see fn update_all but is meant to be added to scripts folder

    @param      temp_folder     folder where modules will be downloaded
    @param      skip_module     skip the module on this list
    @param      list_module     list of modules to update or None for all
    @param      schedule_only   if True, the function returns the list of modules scheduled to be installed
    @param      source          overwrite the source of the wheels
    """
    try:
        from pymyinstall import is_travis_or_appveyor
    except ImportError:
        folder = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", ".."))
        sys.path.append(folder)
        from pymyinstall import is_travis_or_appveyor
    if is_travis_or_appveyor() and source is None:
        source = "2"

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
    try:
        from pymyinstall.packaged import update_all
    except ImportError:
        folder = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", ".."))
        sys.path.append(folder)
        from pymyinstall.packaged import update_all
    res = update_all(temp_folder=temp_folder, verbose=True,
                     skip_module=skip_module, list_module=list_module,
                     schedule_only=schedule_only, source=source)
    if schedule_only:
        print("SCHEDULED")
        for r in res:
            print(r)


def main():
    """
    calls function @see fn update_all but is meant to be added to scripts folder,
    parse command line arguments
    """
    parser = get_parser()
    try:
        res = parser.parse_args()
    except SystemExit:
        print(parser.format_usage())
        res = None

    if res is not None:
        skip_module = None if res.skip in [
            "", "-", None, []] else res.skip.split(",")
        list_module = None if res.module in [
            "all", "", "-", None, []] else res.module
        if list_module is None and res.set is not None and len(res.set) > 0 and res.set != "-":
            list_module = res.set
        do_main(temp_folder=res.folder, skip_module=skip_module,
                list_module=list_module, schedule_only=res.schedule,
                source=res.source if res.source else None)


if __name__ == "__main__":
    main()
