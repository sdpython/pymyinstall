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
        default="",  # "ete,dataspyre,pycuda,cubehelix",
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
        '--check',
        default="",
        help='check every installed module by importing them, all others options are ignored, the value can be null, a module name or a list comma separated, two integers semi-colon separated 1:end')
    parser.add_argument(
        '--deep-deps',
        action='store_true',
        help='install a module or the modules with their dependencies, check dependencies of dependencies are installed')
    parser.add_argument(
        '--set',
        default="-",
        help='set of module to install, see documentation of function get_name_set to get a comprehensive list, this option is ignored if a module is specified on the command line')
    parser.add_argument(
        '--schedule',
        action='store_true',
        help='do not install the modules, returned the list scheduled to be installed')
    parser.add_argument(
        '-t',
        '--task',
        default="install",
        choices=['install', 'shebang'],
        help='default task is install but the script can patch shebang in their current location (task=shebang)')
    parser.add_argument(
        'module',
        nargs='*',
        default="all",
        help='update only the list of modules included in this list or all modules if not specified or equal to all')
    parser.add_argument(
        '--source',
        default="",
        help='overwrite the source of the wheels')
    return parser


def do_main(temp_folder="build/update_modules",
            skip_module=None,  # ["ete", "dataspyre", "pycuda", "cubehelix"],
            list_module=None, deps=False, schedule_only=False,
            deep_deps=False, checkings=None,
            task="install", source=None):
    """
    calls function @see fn install_all but is meant to be added to scripts folder

    @param      temp_folder     folder where modules will be downloaded
    @param      skip_module     skip the module on this list
    @param      list_module     list of modules to update or None for all
    @param      deps            install a module with its dependencies
    @param      schedule_only   if True, the function returns the list of modules scheduled to be installed
    @param      deep_deps       check dependencies for dependencies
    @param      checkings       if True, run checkings, do not install anything, example of values
    @param      task            *install* or *shebang* or *download*
                                ``""``, ``matplotlib``, ``100,end``,
                                option *download* is equivalent to *checkings*
    @param      source          overwrite the source of the wheel

    If *deps* is True, *list_module* cannot be empty.

    .. versionchanged:: 1.1
        Parameter *source* was added.
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

    if task in ("install", "download"):
        checkings = checkings or task == "download"
        if checkings:
            try:
                from pymyinstall.win_installer import import_every_module
            except ImportError:
                folder = os.path.normpath(os.path.join(
                    os.path.abspath(os.path.dirname(__file__)), "..", ".."))
                sys.path.append(folder)
                from pymyinstall.win_installer import import_every_module

                def to_int(s):
                    if "end" in s:
                        return -1
                    try:
                        return int(s)
                    except:
                        return -1

                if checkings in ("", "0,end", "0,-1"):
                    module_list = None
                    start = 0
                    end = -1
                elif ":" in checkings:
                    module_list = None
                    spl = checkings.split(":")
                    if len(spl) == 2:
                        start = to_int(spl[0])
                        end = to_int(spl[1])
                    else:
                        raise ValueError("unable to interpret: " + checkings)
                else:
                    module_list = [_.strip() for _ in checkings.split(",")]
                    start = 0
                    end = -1

                print("CHECKINGS {}:{} -- {}".format(start, end,
                                                     "all" if module_list is None else ",".join(module_list)))
                import_every_module(None, module_list, start=start, end=end)
        else:
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
                              schedule_only=schedule_only,
                              deep_deps=deep_deps, source=source)
            if schedule_only:
                print("SCHEDULED")
                for r in res:
                    print(r)
    elif task == "shebang":
        try:
            from pymyinstall.win_installer import win_patch_paths
            from pymyinstall.installhelper import get_pip_program
        except ImportError:
            folder = os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", ".."))
            sys.path.append(folder)
            from pymyinstall.win_installer import win_patch_paths
            from pymyinstall.installhelper import get_pip_program
        pip = get_pip_program()
        folder = os.path.dirname(os.path.abspath(pip))
        win_patch_paths(folder, None, fLOG=print)
    else:
        raise ValueError("unable to interpret task: " + task)


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
        skip_module = None if res.skip in [
            "", "-", None, []] else res.skip.split(",")
        list_module = None if res.module in [
            "all", "", "-", None, []] else res.module
        if list_module is None and res.set is not None and len(res.set) > 0 and res.set != "-":
            list_module = res.set
        do_main(temp_folder=res.folder, skip_module=skip_module,
                list_module=list_module, deps=res.deps, schedule_only=res.schedule,
                deep_deps=res.deep_deps, checkings=res.check, task=res.task,
                source=res.source if res.source else None)


if __name__ == "__main__":
    main()
