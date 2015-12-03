"""
@file
@brief Helpers for function @see fn win_python_setup
"""
from __future__ import print_function
import datetime
import os
import shutil
import sys
import fnmatch
import subprocess

from ..installcustom.install_custom_pandoc import install_pandoc
from ..installcustom.install_custom_R import install_R
from ..installcustom.install_custom_julia import install_julia
from ..installcustom.install_custom_scite import install_scite
from ..installcustom.install_custom_putty import install_putty
from ..installcustom.install_custom_sqlitespy import install_sqlitespy
from ..installcustom.install_custom_python import install_python
from ..installcustom.install_custom_mingw import install_mingw
from ..installcustom.install_custom_tdm_gcc import install_tdm_gcc
from ..installcustom.install_custom_7z import install_7z
from ..installcustom.install_custom_graphviz import install_graphviz
from ..installcustom.install_custom_vs import install_vs
from ..installcustom.install_custom import download_page
from ..installhelper.link_shortcuts import add_shortcut
from ..packaged import minimal_set

from .win_packages import _is_package_in_list
from .pywin32_helper import import_pywin32
from .win_extract import extract_msi, extract_exe, extract_archive, extract_copy
from .win_exception import WinInstallException
from .win_setup_mark_step import mark_step, is_step_done
from .win_setup_r import r_run_script, _script as _script_r
from .win_setup_julia import julia_run_script, _script_install as _script_julia_install, _script_build as _script_julia_build, _script_init as _script_julia_init


if sys.version_info[0] == 2:
    from codecs import open
    FileNotFoundError = Exception


def dtnow():
    """
    shortcut, return ``datetime.datetime.now()``
    """
    return datetime.datetime.now()


def copy_icons(src, dest):
    """
    copy all files from src to dest

    @param      src     source
    @param      dest    destination
    @return             operations
    """
    operations = []
    if not os.path.exists(dest):
        os.makedirs(dest)
        operations.append(("mkdir", dest))
    files = os.listdir(src)
    for file in files:
        if os.path.isdir(os.path.join(src, file)):
            continue
        d = os.path.join(dest, file)
        if not os.path.exists(d):
            shutil.copy(os.path.join(src, file), dest)
            operations.append(("copy", file))
    return operations


def win_download(folder=None,
                 module_list=None,
                 verbose=False,
                 fLOG=print,
                 download_only=False,
                 selection=None):
    """
    The function downloads everything needed to prepare a setup.

    @param      folder          where to prepare the python version (the user must replace None)
    @param      module_list     list of module to install (see @see fn minimal_set = default options)
    @param      fLOG            logging function
    @param      download_only   only downloads
    @param      verbose         print more information
    @param      selection       selection of tools to install
    @return                     list of completed operations
    """
    if selection is None:
        raise ValueError("selection must be specified")

    available = os.listdir(folder)

    def is_here(program, no_wheel=False):
        b = _is_package_in_list(program, available, no_wheel=no_wheel)
        return b

    operations = []

    if not is_here("scite") and "scite" in selection:
        fLOG("--- download", "scite")
        r = install_scite(dest_folder=folder, fLOG=fLOG,
                          install=False, version=selection.get("scite", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("putty") and "putty" in selection:
        fLOG("--- download", "putty")
        r = install_putty(dest_folder=folder, fLOG=fLOG,
                          install=False, version=selection.get("putty", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("mingw") and "mingw" in selection:
        fLOG("--- download", "mingw")
        r = install_mingw(dest_folder=folder, fLOG=fLOG,
                          install=False, version=selection.get("mingw", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("tdm") and "tdm" in selection:
        fLOG("--- download", "tdm")
        r = install_tdm_gcc(dest_folder=folder, fLOG=fLOG,
                            install=False, version=selection.get("tdm", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("SQLiteSpy") and "sqlitespy" in selection:
        fLOG("--- download", "sqllitespy")
        r = install_sqlitespy(temp_folder=folder, fLOG=fLOG,
                              install=False, version=selection.get("sqlitespy", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("python"):
        fLOG("--- download", "python")
        r = install_python(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True, version=selection.get("python", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("R-") and "r" in selection:
        fLOG("--- download", "R")
        r = install_R(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True, version=selection.get("r", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("vs") and "vs" in selection:
        fLOG("--- download", "Visual Studio Express")
        r = install_vs(folder, fLOG=fLOG, install=False,
                       version=selection.get("vs", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("julia") and "julia" in selection:
        fLOG("--- download", "julia")
        r = install_julia(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True, version=selection.get("julia", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("pandoc") and "pandoc" in selection:
        if verbose:
            fLOG("download", "pandoc")
        r = install_pandoc(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True, version=selection.get("pandoc", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("7z") and "7z" in selection:
        if verbose:
            fLOG("download", "7z")
        r = install_7z(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True, version=selection.get("7z", None))
        operations.append(("download", r))
        fLOG("done")

    if not is_here("graphviz", no_wheel=True) and "graphviz" in selection:
        if verbose:
            fLOG("download", "graphviz")
        r = install_graphviz(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True, version=selection.get("graphviz", None))
        operations.append(("download", r))
        fLOG("done")

    if module_list is None:
        module_list = minimal_set()

    for mod in module_list:
        if is_here(mod.name + "-"):
            continue
        if verbose:
            fLOG("download module", mod.name)
        res = mod.download(temp_folder=folder)
        if isinstance(res, list):
            for r in res:
                operations.append(("download", r))
        else:
            operations.append(("download", res))

    return operations


def win_install(folders,
                download_folder,
                verbose=False,
                fLOG=print,
                names=[
                    "Julia", "Scite", "7z", "TDM", "MinGW", "R", "pandoc", "Python", "SQLiteSpy", "VS", "Putty", "Graphviz"],
                selection=None):
    """
    Install setups

    @param      folders         dictionary of folders, must contain key tools, python
    @param      download_folder where the setup are
    @param      fLOG            logging function
    @param      verbose         print more information
    @param      names           name of subfolders to be created
    @param      selection       selection of tools to install
    @return                     list of completed operations, executable (to make shortcuts)

    The function installs every setup which starts by one of the string in *names*
    and whose extension is .exe, .msi or .zip.
    """
    operations = []
    dfunc = {".zip": extract_archive, ".exe": extract_exe,
             ".msi": extract_msi, "putty.exe": extract_copy}

    def location(file):
        ext = os.path.splitext(file)[-1]
        if ext not in [".msi", ".exe", ".zip"]:
            return None
        lf = file.lower()
        for name in names:
            if name.lower() in selection and lf.startswith(name.lower()):
                if name == "Python":
                    return folders["python"]
                else:
                    return os.path.join(folders["tools"], name)
        return None

    def find_exe(loc, name):
        name = name.lower()
        if name.lower() == "mingw":
            name = "gcc"
        elif name.lower() == "tdm":
            name = "gcc"
        elif name.lower() == "graphviz":
            name = "dot"
        exp = name + ".exe"

        for root, dirnames, filenames in os.walk(loc):
            for filename in fnmatch.filter(filenames, '*.exe'):
                exe = os.path.join(root, filename)
                file = os.path.split(exe)[-1].lower()
                if file == exp:
                    return exe
        return None

    # we sort to get 7z installed first as it is needed for exe files
    cands = os.listdir(download_folder)
    cands.sort()

    installed = {}

    for cand in cands:
        loc = location(cand)
        if loc is None:
            continue

        name = os.path.split(loc)[-1]
        if not os.path.exists(loc):
            os.mkdir(loc)

        # already installed, checking if there is any exe file
        exe = find_exe(loc, name)
        if exe is not None:
            # already done
            fLOG("--- already installed", exe)
            pass
        else:
            fLOG("--- install", cand, " in ", loc)
            full = os.path.join(download_folder, cand)
            if 'tdm' in cand and 'gcc' in cand:
                raise WinInstallException(
                    "TM must be manually installed from the setup\n{0}\nin\n{1}".format(full, loc))
            ext = os.path.splitext(cand)[-1]
            filename = os.path.split(cand)[-1]
            func = dfunc.get(filename, dfunc[ext])

            if ext == ".exe":
                func(
                    full, loc, verbose=verbose, fLOG=fLOG, szip=installed["7z"])
            else:
                func(full, loc, verbose=verbose, fLOG=fLOG)

            operations.append(("install", cand))
            fLOG("done")

        # add main executable
        found = find_exe(loc, name)

        # for MinGW, we check that the executable mingw-get.exe was installed
        if found is None:
            if name == "MinGW" and cand == "mingw-get-setup.exe":
                exe = os.path.join(loc, "bin", "mingw-get.exe")
                if os.path.exists(exe):
                    cmd = exe + \
                        " install binutils gcc g++ mingw32 fortran gdb mingw32 mingw w32api g77"
                    if verbose:
                        fLOG("install MinGW", cmd)
                    retcode = subprocess.call(
                        cmd, shell=True, stdout=sys.stderr)
                    if retcode < 0:
                        raise WinInstallException(
                            "unable to execute:\nCMD:\n{0}".format(cmd))
                    found = find_exe(loc, name)
            elif name == "VS" and cand == "vs_community.exe":
                # Visual Studio needs to be manually installed
                # we copy the setup to VS
                shutil.copy(os.path.join(download_folder, cand), loc)
                found = os.path.join(loc, cand)

        if found is None:
            raise FileNotFoundError("unable to find executable for name={0} in {1}, found: {2}, exe={3}, function={4}".format(
                name, loc, found, exe, func))
        installed[name] = found

    return operations, installed


def create_links_tools(folder, installed, verbose=False, fLOG=print):
    """
    create links for the tools

    @param      folder      where links will be stored
    @param      installed   dictionary *{ tool: exe file }*
    @param      verbose     display more information
    @param      fLOG        logging function
    @return                 operations, list of tuple *("link", link file)*
    """
    import_pywin32()
    operations = []

    for k, v in installed.items():
        if k == "R":
            name = "test R Gui"
            link_name = name + ".lnk"
            dest = os.path.join(folder, link_name)
            add_shortcut(target="tools\\R\\bin\\x64\\Rgui.exe",
                         name=name, arguments="", icon="~dp0\\tools\\icons\\r.ico",
                         folder=folder)
            if verbose:
                fLOG("create link", dest)
            operations.append(("link", link_name))

            name = "test R Console"
            link_name = name + ".lnk"
            dest = os.path.join(folder, link_name)
            add_shortcut(target="tools\\R\\bin\\x64\\R.exe",
                         name=name, arguments="", icon="~dp0\\tools\\icons\\r.ico",
                         folder=folder)
            if verbose:
                fLOG("create link", dest)
            operations.append(("link", link_name))

        elif k == "julia":
            name = "test Julia Console"
            link_name = name + ".lnk"
            dest = os.path.join(folder, link_name)
            add_shortcut(target="tools\\julia\\bin\\julia.exe",
                         name=name, arguments="", icon="~dp0\\tools\\icons\\julia.ico",
                         folder=folder)
            if verbose:
                fLOG("create link", dest)
            operations.append(("link", link_name))

        elif k == "python":
            name = "test Python Console"
            link_name = name + ".lnk"
            dest = os.path.join(folder, link_name)
            add_shortcut(target="python\\python.exe",
                         name=name, arguments="", icon="~dp0\\tools\\icons\\python.ico",
                         folder=folder)
            if verbose:
                fLOG("create link", dest)
            operations.append(("link", link_name))

    return operations


def win_download_notebooks(notebooks, folder, verbose=False, fLOG=print):
    """
    download notebooks and store them as documentation

    @param      notebooks       list of tuple (place, url)
    @param      folder          where to put them
    @param      verbose         verbose
    @param      fLOG            logging function
    @return                     list of operations
    """
    operations = []
    for path, urls in notebooks:
        if not isinstance(urls, list):
            urls = [urls]
        for url in urls:
            name = url.split("/")[-1]
            dest = os.path.join(folder, path)
            if not os.path.exists(dest):
                os.makedirs(dest)
                operations.append(("mkdir", dest))
            dfile = os.path.join(dest, name)
            if not os.path.exists(dfile):
                if verbose:
                    fLOG("download notebooks", name, "from", url)
                content = download_page(url)
                with open(dfile, "w", encoding="utf8") as f:
                    f.write(content)
                operations.append(("docs", dfile))
    return operations


def win_install_julia_step(folders, verbose=False, fLOG=print):
    """
    does necessary steps to setup Julia

    @param      folders     installation folders
    @param      verbose     verbose
    @param      fLOG        logging function
    @return                 list of processed operations
    """
    operations = []
    if not is_step_done(folders["logs"], "julia_init"):
        ##########################
        # init Julia packages
        #########################
        fLOG("--- init julia packages")
        jl = os.path.join(folders["tools"], "Julia")
        output = os.path.join(folders["logs"], "out.init.julia.txt")
        out = julia_run_script(
            jl, folders["python"], _script_julia_init, verbose=verbose, fLOG=fLOG)
        with open(output, "w", encoding="utf8") as f:
            f.write(out)
        operations.append(("Julia", _script_julia_init))
        operations.append(("time", dtnow()))
        mark_step(folders["logs"], "julia_init")

    if not is_step_done(folders["logs"], "julia_install"):
        ##########################
        # install Julia packages
        #########################
        fLOG("--- install julia packages")
        jl = os.path.join(folders["tools"], "Julia")
        output = os.path.join(folders["logs"], "out.install.julia.txt")
        out = julia_run_script(
            jl, folders["python"], _script_julia_install, verbose=verbose, fLOG=fLOG)
        with open(output, "w", encoding="utf8") as f:
            f.write(out)
        operations.append(("Julia", _script_julia_install))
        operations.append(("time", dtnow()))
        mark_step(folders["logs"], "julia_install")

    if not is_step_done(folders["logs"], "julia_build"):
        #########################
        # build Julia packages
        #########################
        fLOG("--- build julia packages")
        jl = os.path.join(folders["tools"], "Julia")
        output = os.path.join(folders["logs"], "out.build.julia.txt")
        out = julia_run_script(
            jl, folders["python"], _script_julia_build, verbose=verbose, fLOG=fLOG)
        with open(output, "w", encoding="utf8") as f:
            f.write(out)
        operations.append(("Julia", _script_julia_build))
        operations.append(("time", dtnow()))
        mark_step(folders["logs"], "julia_build")

    return operations


def win_install_r_step(folders, verbose=False, fLOG=print):
    """
    does necessary steps to setup R

    @param      folders     installation folders
    @param      verbose     verbose
    @param      fLOG        logging function
    @return                 list of processed operations
    """
    operations = []
    if not is_step_done(folders["logs"], "r_install"):
        ######################
        # install R packages
        ######################
        fLOG("--- install R packages")
        r = os.path.join(folders["tools"], "R")
        output = os.path.join(folders["logs"], "out.install.r.txt")
        out = r_run_script(r, _script_r, output)
        with open(output, "w", encoding="utf8") as f:
            f.write(out)
        operations.append(("R", _script_r))
        operations.append(("time", dtnow()))
        mark_step(folders["logs"], "r_install")
    else:
        fLOG(
            "--- skip installation of R packages or remove file log.step.r_install.txt")

    return operations
