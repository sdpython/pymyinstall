#!python
"""
script which goes through all installed modules
"""
from __future__ import print_function
import sys
import os
import argparse


def get_parser():
    """
    defines the way to parse the script ``pymy_status``
    """
    typstr = str  # unicode#
    parser = argparse.ArgumentParser(
        description='information about installed modules')
    parser.add_argument(
        '-o',
        '--out',
        default="python_module.xlsx",
        type=typstr,
        help='output the results into a file (required pandas)')
    parser.add_argument(
        '-p',
        '--pypi',
        default=True,
        type=bool,
        help='checks the version on PyPi')
    parser.add_argument(
        'module',
        nargs="*",
        default="all",
        help='update only the list of modules included in this list or all modules if not specified or equal to all')
    parser.add_argument(
        '--set',
        default="-",
        type=typstr,
        help='set of module to install, see documentation of function get_name_set to get a comprehensive list, ' +
             'this option is ignored if a module is specified on the command line')
    return parser


def do_main(list_module=None, outfile="python_module.xlsx", pypi=True):
    """
    Calls function @see fn update_all but is meant to be added to scripts folder.

    @param      list_module     list of modules to update or None for all
    @param      outfile         output the results into a flat file or an excel file (required pandas)
    @param      pypi            check version on PyPi
    """
    try:
        from pymyinstall.installhelper import get_installed_modules
    except ImportError:
        pfolder = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", ".."))
        sys.path.append(pfolder)
        if "pymyinstall" in sys.modules:
            del sys.modules["pymyinstall"]
        if "pymyinstall.installhelper" in sys.modules:
            del sys.modules["pymyinstall.installhelper"]
        from pymyinstall.installhelper import get_installed_modules
    if list_module is not None and len(list_module) == 0:
        list_module = None
    if outfile:
        import pandas
    res = get_installed_modules(short_list=list_module, fLOG=print, pypi=True)
    if outfile:
        df = pandas.DataFrame(res)
        cols = list(df.columns)
        cols.sort()
        df = df[cols]
        if ".xls" in os.path.split(outfile)[-1]:
            print("Saving into:", outfile)
            df.to_excel(outfile, index=False)
        else:
            print("Saving into (sep=tab, encoding=utf-8):", outfile)
            df.to_csv(outfile, seo="\t", encoding="utf-8", index=False)


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
        list_module = None if res.module in [
            "all", "", "-", None, []] else res.module
        if list_module is None and res.set is not None and len(res.set) > 0 and res.set != "-":
            list_module = res.set
        do_main(list_module=list_module, outfile=res.out, pypi=res.pypi)


if __name__ == "__main__":
    main()
