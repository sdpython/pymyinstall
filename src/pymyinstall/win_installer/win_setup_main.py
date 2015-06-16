#-*- coding: utf-8 -*-
"""
@file
@brief Functions to prepare a setup on Windows
"""
from __future__ import print_function

import os
import fnmatch
import shutil
import datetime

from ..installhelper.install_custom_pandoc import install_pandoc
from ..installhelper.install_custom_R import install_R
from ..installhelper.install_custom_julia import install_julia
from ..installhelper.install_custom_scite import install_scite
from ..installhelper.install_custom_sqlitespy import install_sqlitespy
from ..installhelper.install_custom_python import install_python
from ..installhelper.install_custom_mingw import install_mingw
from ..installhelper.install_custom_7z import install_7z
from ..installhelper.install_custom import download_page
from ..installhelper.install_custom_scite import modify_scite_properties
from ..packaged.packaged_config import small_installation
from .import_pywin32 import import_pywin32
from .win_extract import extract_msi, extract_exe, extract_archive, clean_msi
from .win_packages import _is_package_in_list, win_install_packages_other_python
from .win_batch import create_win_batches
from .win_setup_r import r_run_script, _script as _script_r
from .win_setup_julia import julia_run_script, _script as _script_julia

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


def win_python_setup(folder="dist/win_python_setup",
                     download_folder="build/win_python_setup",
                     module_list=None,
                     verbose=False,
                     fLOG=print,
                     download_only=False,
                     no_setup=False,
                     notebooks=None,
                     **options
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
    @param      options         list of available options (will expand later)
    @param      notebooks       notebooks to copy to the workspace, list of ("subfolders", url)
    @return                     list of completed operations

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

    @todo Use chocolatey to process installation.

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
    """
    if notebooks is None:
        notebooks = _default_notebooks

    def now():
        return datetime.datetime.now()

    operations = []
    operations.append(("time", now()))

    folder = os.path.abspath(folder)
    download_folder = os.path.abspath(download_folder)

    if not os.path.exists(folder):
        os.makedirs(folder)
        operations.append(("mkdir", folder))

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        operations.append(("mkdir", download_folder))

    # definition of folders
    operations.append(("time", now()))
    folders = dict(tools=os.path.join(folder, "tools"),
                   workspace=os.path.join(folder, "workspace"),
                   python=os.path.join(folder, "python"),
                   config=os.path.join(folder, "config"),
                   logs=os.path.join(folder, "logs"),
                   )

    for k, v in folders.items():
        if not os.path.exists(v):
            os.mkdir(v)

    # download the documentation
    op = win_download_notebooks(
        notebooks, folders["workspace"], verbose=verbose, fLOG=fLOG)
    operations.extend(op)
    operations.append(("time", now()))

    # download of everything
    operations.append(("time", now()))
    op = win_download(folder=download_folder,
                      module_list=module_list,
                      verbose=verbose,
                      fLOG=fLOG,
                      **options)
    operations.extend(op)
    operations.append(("time", now()))

    # license
    fLOG("--- license")
    with open(os.path.join(folder, "license.txt"), "w") as f:
        f.write(license)
    operations.append(("license", "license.txt"))

    if not download_only:
        # copy icons in tools/icons
        fLOG("--- copy icons")
        op = copy_icons(os.path.join(os.path.dirname(__file__), "icons"),
                        os.path.join(folders["tools"], "icons"))
        operations.extend(op)
        operations.append(("time", now()))

        # install setups
        fLOG("--- installation of python and tools")
        op, installed = win_install(folders=folders, download_folder=download_folder, verbose=verbose, fLOG=fLOG,
                                    **options)
        operations.extend(op)
        operations.append(("time", now()))
        if "pandoc" not in installed:
            raise FileNotFoundError("pandoc was not installed")

        if verbose:
            for k, v in installed.items():
                fLOG("  INSTALLED:", k, "-->", v)

        # clean msi
        op = clean_msi(folders["tools"], "*.msi", verbose=verbose, fLOG=fLOG)
        operations.extend(op)
        operations.append(("time", now()))

        # create links tools
        fLOG("--- create links")
        op = create_links_tools(folder, installed, verbose=verbose, fLOG=fLOG)
        operations.extend(op)
        operations.append(("time", now()))

        # create batch command files
        fLOG("--- create batch command file")
        op = create_win_batches(folders, verbose=verbose, fLOG=fLOG)
        operations.extend(op)

        # modifies scite properties
        fLOG("--- modifies Scite properties")
        modify_scite_properties(os.path.join("..", "..", "..", "pythonw"),
                                os.path.join(folders["tools"], "Scite", "wscite"))

        # update pip
        fLOG("--- update pip")
        op = update_pip(folders["python"])
        operations.extend(op)
        operations.append(("time", now()))

        ##
        # packages for R, Julia, Python
        ##

        # install Julia packages
        jl = os.path.join(folders["tools"], "Julia")
        output = os.path.join(folders["logs"], "out.install.julia.txt")
        out = julia_run_script(jl, _script_julia)
        with open(os.path.join(folders["logs"], "out.install.julia.txt"), "w", encoding="utf8") as f:
            f.write(out)
        operations.append(("Julia", _script_julia))
        operations.append(("time", now()))

        # install R packages
        r = os.path.join(folders["tools"], "R")
        output = os.path.join(folders["logs"], "out.install.r.txt")
        out = r_run_script(r, _script_r, output)
        operations.append(("R", _script_r))
        operations.append(("time", now()))

        # installation of packages
        fLOG("--- installation of python packages")
        python_path = folders["python"]
        win_install_packages_other_python(
            python_path, download_folder, verbose=verbose, fLOG=fLOG)
        fLOG("done")
        operations.append(("time", now()))

    if not no_setup:
        # build setup with InnoSetup
        fLOG("--- building setup with InnoSetup")
        replacements = dict(__DISTPATH__=folder)
        out = run_innosetup(replacements=replacements, fLOG=fLOG,
                            temp_folder=os.path.join(folders["logs"]))
        fLOG("done")
        with open(os.path.join(folders["logs"], "out.install.innosetup.txt"), "w", encoding="utf8") as f:
            f.write(out)
        operations.append(("InnoSetup", "done"))
        operations.append(("time", now()))

    # store logs
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
                 **options
                 ):
    """
    The function downloads everything needed to prepare a setup.

    @param      folder          where to prepare the python version
    @param      module_list     list of module to install (see @see fn small_installation = default options)
    @param      fLOG            logging function
    @param      download_only   only downloads
    @param      options         list of available options (will expand later)
    @param      verbose         print more information
    @return                     list of completed operations
    """
    available = os.listdir(folder)

    def is_here(program):
        return _is_package_in_list(program, available)

    operations = []

    if not is_here("scite"):
        fLOG("--- download", "scite")
        r = install_scite(dest_folder=folder, fLOG=fLOG, install=False)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("mingw"):
        fLOG("--- download", "mingw")
        r = install_mingw(dest_folder=folder, fLOG=fLOG, install=False)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("SQLiteSpy"):
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

    if not is_here("R-"):
        fLOG("--- download", "R")
        r = install_R(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("julia"):
        fLOG("--- download", "julia")
        r = install_julia(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("pandoc"):
        if verbose:
            fLOG("download", "pandoc")
        r = install_pandoc(
            temp_folder=folder, fLOG=fLOG, install=False, force_download=True)
        operations.append(("download", r))
        fLOG("done")

    if not is_here("7z"):
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
                **options):
    """
    Install setups

    @param      folders         dictionary of folders, must contain key tools, python
    @param      download_folder where the setup are
    @param      fLOG            logging function
    @param      verbose         print more information
    @param      names           name of subfolders to be created
    @param      options         list of available options (will expand later)
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
            if lf.startswith(name.lower()):
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
