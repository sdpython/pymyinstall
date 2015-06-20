#-*- coding: utf-8 -*-
"""
@file
@brief Functions to prepare a setup on Windows
"""
from __future__ import print_function

import os
import sys
import fnmatch
import shutil
import datetime
import subprocess

from ..installhelper.install_custom_pandoc import install_pandoc
from ..installhelper.install_custom_R import install_R
from ..installhelper.install_custom_julia import install_julia
from ..installhelper.install_custom_scite import install_scite
from ..installhelper.install_custom_sqlitespy import install_sqlitespy
from ..installhelper.install_custom_python import install_python
from ..installhelper.install_custom_mingw import install_mingw
from ..installhelper.install_cmd_helper import update_pip, run_cmd
from ..installhelper.install_custom_7z import install_7z
from ..installhelper.install_custom import download_page
from ..installhelper.install_custom_scite import modify_scite_properties
from ..installhelper.link_shortcuts import add_shortcut
from ..packaged.packaged_config import small_installation
from .import_pywin32 import import_pywin32
from .win_exception import WinInstallException
from .win_extract import extract_msi, extract_exe, extract_archive, clean_msi
from .win_packages import _is_package_in_list, win_install_packages_other_python
from .win_batch import create_win_batches
from .win_ipy_kernels import install_kernels
from .win_setup_mark_step import mark_step, is_step_done

from .win_setup_r import r_run_script, _script as _script_r
from .win_setup_julia import julia_run_script, _script_install as _script_julia_install, _script_build as _script_julia_build, _script_init as _script_julia_init

from .win_innosetup_helper import run_innosetup

license = """
Copyright (c) 2013-2015, Xavier Dupré

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

_default_notebooks = [
    ("docs/ensae", ["http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/_downloads/td1a_cenonce_session_12.ipynb",
                    "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/_downloads/td2a_cenonce_session_2A.ipynb",
                    "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/_downloads/td2a_cenonce_session_2B.ipynb",
                    "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/_downloads/td2a_cenonce_session_2C.ipynb",
                    ]),
    ("docs/actuariat", ["http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/_downloads/population_recuperation_donnees.ipynb",
                        ]),
]


def dtnow():
    """
    shortcut, return ``datetime.datetime.now()``
    """
    return datetime.datetime.now()


def win_python_setup(folder="dist/win_python_setup",
                     download_folder="build/win_python_setup",
                     module_list=None,
                     verbose=False,
                     fLOG=print,
                     download_only=False,
                     no_setup=False,
                     notebooks=None,
                     selection={"R"},
                     ):
    """
    Prepares a Windows distribution of Python based on InnoSetup,
    inspired from WinPython but more easier to tweak I hope.

    @param      folder          where to prepare the python version
    @param      module_list     list of module to install (see @see fn small_installation = default options)
    @param      fLOG            logging function
    @param      download_only   only downloads
    @param      no_setup        skip the building of the setup
    @param      verbose         print more information
    @param      notebooks       notebooks to copy to the workspace, list of ("subfolders", url)
    @param      selection       selection of tools to install
    @return                     list of completed operations

    The available tools to install must be chose among:
        * `R <http://www.r-project.org/>`_
        * `Julia <http://julialang.org/>`_

    By default, only R is included. Julia requires too much work.
    The command line does not always end. The building of the package
    is sometimes reluctant to work. And the Julia kernel is exclusive:
    it cannot be setup with others kernel. Maybe the version 0.5 will fix those issues.

    The setup will also contains `pandoc <http://pandoc.org/>`_,
    `7z <http://www.7-zip.org/>`_,
    `SQLiteSpy <http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index>`_,
    `Scite<http://www.scintilla.org/SciTE.html>`_,
    `MinGW <http://www.mingw.org/>`_.

    The function first downloads everything.
    It does not do it twice, so you can run the function again and directly go
    to where it was interrupted. If there is no notebooks,
    the setup will add some anyway.

    It uses `InnoSetup <http://www.jrsoftware.org/isinfo.php>`_ to build the setup.

    The distribution will contain the following subfolders:
        * *tools*: subfolders for R, Julia, MinGW, Scite, pandoc, 7z...
        * *python*: subfolder for python interpreter
        * *workspace*: current folder for the notebooks

    Comments and remarks:
        * 7z setup needs a last click to complete
        * pandoc needs a last click to complete
        * R must be manually installed in the right folder
        * Julia produces a file exe, for the time being it must be done manually
        * MinGW is also installed manually, the command line is different from others tools,
          once it is installed, you should run the command line::

            mingw-get install binutils gcc g++ mingw32 fortran gdb mingw32 mingw w32api g77

        * Python setups needs a last click to complete
        * Julia command line sometimes gets stuck, the setup needs to be stopped
          and restarted. It happens while installing the packages and
          also while building IJulia (the package to use Julia in a notebook).
          The Julia should be stopped instead of stopping the python script.
          That trick shows the standard output of Julia.
        * Juilia kernel cannot be used with the others: it requires a different
          configuration which prevents others kernel to be available at the same time.
          We will skip for the time being.


    With Julia, initialisation, installation or building takes time.
    The function writes a file ``log.step.<julia_step>.txt``
    to tell the step has completed once. You can remove this file
    to do it again.

    @example(Prepare a standalone distribution)
    The function downloads everything. The installation of tools
    is still manual. Package installation is automated.

    ::

        from pymyinstall import win_python_setup, installation_ensae, installation_teachings
        list_modules = installation_ensae() + installation_teachings()
        win_python_setup(module_list=list_modules,
                         verbose=False,
                         download_only=False)

    This works only for Windows.
    @endexample

    @warning The Julia installation might be stuck after the installation or the build.
             In that case, the script python should be stopped by *stopping the Julia
             process* from the Task Manager
             and started again. If it has completed, it will go to the
             next step.

    @todo Use chocolatey to process installation.

    @todo Fix Julia installation.
    """
    if notebooks is None:
        notebooks = _default_notebooks

    if not isinstance(selection, set):
        selection = set(selection)
    selection.add("pandoc")
    selection.add("7z")
    selection.add("scite")
    selection.add("sqlitespy")
    selection.add("mingw")
    selection = set(_.lower() for _ in selection)

    ######
    # next
    ######

    operations = []
    operations.append(("time", dtnow()))

    folder = os.path.abspath(folder)
    download_folder = os.path.abspath(download_folder)

    if not os.path.exists(folder):
        os.makedirs(folder)
        operations.append(("mkdir", folder))

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        operations.append(("mkdir", download_folder))

    ###################
    # definition of folders
    ###################
    operations.append(("time", dtnow()))
    folders = dict(tools=os.path.join(folder, "tools"),
                   workspace=os.path.join(folder, "workspace"),
                   python=os.path.join(folder, "python"),
                   config=os.path.join(folder, "config"),
                   logs=os.path.join(folder, "logs"),
                   )

    for k, v in folders.items():
        if not os.path.exists(v):
            os.mkdir(v)

    ###########################
    # download the documentation
    ###########################
    op = win_download_notebooks(
        notebooks, folders["workspace"], verbose=verbose, fLOG=fLOG)
    operations.extend(op)
    operations.append(("time", dtnow()))

    ######################
    # download of everything
    ######################
    operations.append(("time", dtnow()))
    op = win_download(folder=download_folder,
                      module_list=module_list,
                      verbose=verbose,
                      fLOG=fLOG,
                      selection=selection)
    operations.extend(op)
    operations.append(("time", dtnow()))

    ########
    # license
    ########
    fLOG("--- license")
    with open(os.path.join(folder, "license.txt"), "w") as f:
        f.write(license)
    operations.append(("license", "license.txt"))

    if not download_only:
        ########################
        # copy icons in tools/icons
        #######################
        fLOG("--- copy icons")
        op = copy_icons(os.path.join(os.path.dirname(__file__), "icons"),
                        os.path.join(folders["tools"], "icons"))
        operations.extend(op)
        operations.append(("time", dtnow()))

        #############
        # install setups
        #############
        fLOG("--- installation of python and tools")
        op, installed = win_install(
            folders=folders, download_folder=download_folder, verbose=verbose, fLOG=fLOG,
            selection=selection)
        operations.extend(op)
        operations.append(("time", dtnow()))
        if "pandoc" not in installed:
            raise FileNotFoundError("pandoc was not installed")

        if verbose:
            for k, v in installed.items():
                fLOG("  INSTALLED:", k, "-->", v)

        ##########
        # clean msi
        ##########
        fLOG("--- clean msi")
        op = clean_msi(folders["tools"], "*.msi", verbose=verbose, fLOG=fLOG)
        operations.extend(op)
        operations.append(("time", dtnow()))

        ################
        # create links tools
        ################
        fLOG("--- create links")
        op = create_links_tools(folder, installed, verbose=verbose, fLOG=fLOG)
        operations.extend(op)
        operations.append(("time", dtnow()))

        #########################
        # create batch command files
        #########################
        fLOG("--- create batch command file")
        op = create_win_batches(
            folders, verbose=verbose, fLOG=fLOG, selection=selection)
        operations.extend(op)

        #######################
        # modifies scite properties
        #######################
        fLOG("--- modifies Scite properties")
        modify_scite_properties(os.path.join("..", "..", "..", "pythonw"),
                                os.path.join(folders["tools"], "Scite", "wscite"))

        ###########
        # update pip
        ###########
        fLOG("--- update pip")
        op = update_pip(folders["python"])
        operations.extend(op)
        operations.append(("time", dtnow()))

        if "julia" in selection:
            ops = win_install_julia_step(folders, verbose=verbose, fLOG=fLOG)
            operations.extend(ops)

        if "R" in selection:
            ops = win_install_r_step(folders, verbose=verbose, fLOG=fLOG)
            operations.extend(ops)

        ######################
        # installation of packages
        ######################
        fLOG("--- installation of python packages")
        python_path = folders["python"]
        win_install_packages_other_python(
            python_path, download_folder, verbose=verbose, fLOG=fLOG)
        fLOG("done")
        operations.append(("time", dtnow()))

        ######################
        # create ipython profile
        ######################
        config_path = folders["config"]
        ipython_path = os.path.join(
            folders["python"], "Scripts", "ipython.exe")
        cmd = " profile create win_profile --ipython-dir={0}".format(
            folders["config"])
        cmd = ipython_path + cmd
        out, err = run_cmd(cmd, wait=True)
        profile = os.path.join(
            config_path, "profile_win_profile", "ipython_notebook_config.py")
        if not os.path.exists(profile):
            raise WinInstallException(
                "missing file, unable to execute:\nCMD:\n{0}\nOUT:\n{1}\nERR:\n{2}".format(cmd, out, err))

        ########
        # kernels
        ########
        res = install_kernels(folders["tools"], folders["python"])
        for r in res:
            fLOG("ADD: kernal", r)

    if not no_setup:
        #########################
        # build setup with InnoSetup
        #########################
        fLOG("--- building setup with InnoSetup")
        replacements = dict(__DISTPATH__=folder)
        out = run_innosetup(replacements=replacements, fLOG=fLOG,
                            temp_folder=os.path.join(folders["logs"]))
        fLOG("done")
        with open(os.path.join(folders["logs"], "out.install.innosetup.txt"), "w", encoding="utf8") as f:
            f.write(out)
        operations.append(("InnoSetup", "done"))
        operations.append(("time", dtnow()))

    ##########
    # store logs
    ##########
    with open(os.path.join(folders["logs"], "log.setup.txt"), "a", encoding="utf8") as f:
        f.write("\n")
        f.write("-------------------------------------------\n")
        f.write("NEW RUN\n")
        f.write("-------------------------------------------\n")
        for ab in operations:
            if isinstance(ab, tuple):
                if len(ab) == 2:
                    a, b = ab
                elif len(ab) == 1:
                    a, b = a, None
                else:
                    a, b = ab[0], str(ab[1:])

            if isinstance(b, str  # unicode#
                          ):
                b = b.replace(folder, "")
                b = b.replace(os.environ["USERNAME"], "---")
            f.write("{0}\t{1}\n".format(a, b))


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
        d = os.path.join(dest, file)
        if not os.path.exists(d):
            shutil.copy(os.path.join(src, file), dest)
            operations.append(("copy", file))
    return operations


def win_download(folder="build/win_python_setup",
                 module_list=None,
                 verbose=False,
                 fLOG=print,
                 download_only=False,
                 selection=None):
    """
    The function downloads everything needed to prepare a setup.

    @param      folder          where to prepare the python version
    @param      module_list     list of module to install (see @see fn small_installation = default options)
    @param      fLOG            logging function
    @param      download_only   only downloads
    @param      verbose         print more information
    @param      selection       selection of tools to install
    @return                     list of completed operations
    """
    if selection is None:
        raise ValueError("selection must be specified")

    available = os.listdir(folder)

    def is_here(program):
        return _is_package_in_list(program, available)

    operations = []

    if not is_here("scite") and "scite" in selection:
        fLOG("--- download", "scite")
        r = install_scite(dest_folder=folder, fLOG=fLOG, install=False)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("mingw") and "mingw" in selection:
        fLOG("--- download", "mingw")
        r = install_mingw(dest_folder=folder, fLOG=fLOG, install=False)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("SQLiteSpy") and "sqlitespy" in selection:
        fLOG("--- download", "sqllitespy")
        r = install_sqlitespy(temp_folder=folder, fLOG=fLOG, install=False)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("python"):
        fLOG("--- download", "python")
        r = install_python(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("R-") and "r" in selection:
        fLOG("--- download", "R")
        r = install_R(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("julia") and "julia" in selection:
        fLOG("--- download", "julia")
        r = install_julia(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("pandoc") and "pandoc" in selection:
        if verbose:
            fLOG("download", "pandoc")
        r = install_pandoc(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("7z") and "7z" in selection:
        if verbose:
            fLOG("download", "7z")
        r = install_7z(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True)
        operations.append(("download", r))
        fLOG("done")

    if module_list is None:
        module_list = small_installation()

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
                    "Julia", "Scite", "7z", "MinGW", "R", "pandoc", "Python", "SQLiteSpy"],
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
    dfunc = {".zip": extract_archive, ".exe": extract_exe, ".msi": extract_msi}

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
        exes = []
        for root, dirnames, filenames in os.walk(loc):
            for filename in fnmatch.filter(filenames, '*.exe'):
                exes.append(os.path.join(root, filename))

        name = name.lower()
        if name.lower() == "mingw":
            name = "gcc"
        exp = name + ".exe"
        found = None

        for exe in exes:
            file = os.path.split(exe)[-1].lower()
            if file == exp:
                found = exe
                break
        return found

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
            pass
        else:
            fLOG("--- install", cand, " in ", loc)
            full = os.path.join(download_folder, cand)
            ext = os.path.splitext(cand)[-1]
            func = dfunc[ext]

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
        if found is None and name == "MinGW" and cand == "mingw-get-setup.exe":
            exe = os.path.join(loc, "bin", "mingw-get.exe")
            if os.path.exists(exe):
                cmd = exe + \
                    " install binutils gcc g++ mingw32 fortran gdb mingw32 mingw w32api g77"
                if verbose:
                    fLOG("install MinGW", cmd)
                retcode = subprocess.call(cmd, shell=True, stdout=sys.stderr)
                if retcode < 0:
                    raise WinInstallException(
                        "unable to execute:\nCMD:\n{0}".format(cmd))
                found = find_exe(loc, name)

        if found is None:
            raise FileNotFoundError("unable to find executable for name={0} in {1}, found: {2}".format(
                name, loc, found))
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

    return operations
