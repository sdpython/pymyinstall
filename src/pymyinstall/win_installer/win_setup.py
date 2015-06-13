"""
@file
@brief Functions to prepare a setup on Windows
"""
import os
import fnmatch
import shutil

from ..installhelper import install_pandoc, install_sqlitespy, install_R, install_scite, install_julia, install_python, install_mingw, install_7z
from ..installhelper.install_custom_scite import modify_scite_properties
from ..packaged.packaged_config import small_installation
from .win_extract import extract_msi, extract_exe, extract_archive, clean_msi
from .win_packages import _is_package_in_list, win_install_packages_other_python
#from .win_helper import create_shortcut
from ..installhelper.link_shortcuts import add_shortcut
from ..installhelper.install_cmd_helper import update_pip
from .import_pywin32 import import_pywin32


def win_python_setup(folder="dist/win_python_setup",
                     download_folder="build/win_python_setup",
                     module_list=None,
                     verbose=False,
                     fLOG=print,
                     download_only=False,
                     **options
                     ):
    """
    Prepares a Windows distribution of Python based on InnoSetup,
    inspired from WinPython but more easier to tweak I hope.

    @param      folder          where to prepare the python version
    @param      module_list     list of module to install (see @see fn small_installation = default options)
    @param      fLOG            logging function
    @param      download_only   only downloads
    @param      verbose         print more information
    @param      options         list of available options (will expand later)
    @return                     list of completed operations

    The function first downloads everything.
    It does not do it twice, so you can run the function again and directly go
    to where it was interrupted.

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
    operations = []

    folder = os.path.abspath(folder)
    download_folder = os.path.abspath(download_folder)

    if not os.path.exists(folder):
        os.makedirs(folder)
        operations.append(("mkdir", folder))

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        operations.append(("mkdir", download_folder))

    # definition of folders
    folders = dict(tools=os.path.join(folder, "tools"),
                   workspace=os.path.join(folder, "workspace"),
                   python=os.path.join(folder, "python"))

    for k, v in folders.items():
        if not os.path.exists(v):
            os.mkdir(v)

    # download of everything
    op = win_download(folder=download_folder,
                      module_list=module_list,
                      verbose=verbose,
                      fLOG=fLOG,
                      **options)
    operations.extend(op)

    if not download_only:
        # copy icons in tools/icons
        fLOG("--- copy icons")
        op = copy_icons(os.path.join(os.path.dirname(__file__), "icons"),
                   os.path.join(folders["tools"], "icons"))
        operations.extend(op)
        
        # install setups
        fLOG("--- installation of python and tools")
        op, installed = win_install(folders=folders, download_folder=download_folder, verbose=verbose, fLOG=fLOG,
                                    **options)
        operations.extend(op)
        if "pandoc" not in installed:
            raise FileNotFoundError("pandoc was not installed")

        if verbose:
            for k, v in installed.items():
                fLOG("  INSTALLED:", k, "-->", v)
                
        # create links tools
        op = create_links_tools(folder, installed, verbose=verbose, fLOG=fLOG)
        operations.extend(op)
                
        # clean msi
        op = clean_msi(folders["tools"], "*.msi", verbose=verbose, fLOG=fLOG)
        operations.extend(op)
        
        # modifies scite properties
        fLOG("--- modifies Scite properties")
        modify_scite_properties(os.path.join("..", "..", "..", "pythonw"), 
                                os.path.join(folders["tools"], "Scite", "wscite"))

        # update pip
        fLOG("--- update pip")
        update_pip(folder["python"])
        
        # installation of packages
        fLOG("--- installation of python packages")
        python_path = folders["python"]
        win_install_packages_other_python(
            python_path, download_folder, verbose=verbose, fLOG=fLOG)
        fLOG("done")

        # setup


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
                names=["Julia", "Scite", "7z", "MinGW", "R", "pandoc", "Python"],
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
    icon_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "icon")
    
    for k,v in installed.items():
        print(k,v)
        if k == "R":
            link_name = "R Gui.lnk"
            dest = os.path.join(folder, link_name)
            if not os.path.exists(dest):
                add_shortcut(file="tools\\R\\bin\\Rgui.exe", 
                    name="R Gui", description=None,
                    arguments="", workdir="workspace", 
                    icon=os.path.join(icon_path, "r.ico"),
                    folder=folder)
                if verbose:
                    fLOG("create link", dest)
                operations.append(("link", link_name))
    return operations
                        