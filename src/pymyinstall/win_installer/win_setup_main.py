#-*- coding: utf-8 -*-
"""
@file
@brief Functions to prepare a setup on Windows
"""
from __future__ import print_function

import os
import shutil

from ..installhelper.install_cmd_helper import update_pip, run_cmd
from ..installhelper.install_custom_scite import modify_scite_properties

from .win_exception import WinInstallException
from .win_batch import create_win_batches
from .win_ipy_kernels import install_kernels
from .win_innosetup_helper import run_innosetup, innosetup_replacements
from .win_fix_compiler_c import switch_to_VS_compiler, switch_to_mingw_compiler
from .win_patch import win_patch_paths
from .win_setup_main_helper import dtnow, copy_icons, win_download, win_install, create_links_tools
from .win_setup_main_helper import win_download_notebooks, win_install_julia_step, win_install_r_step
from .win_packages import win_install_packages_other_python, get_modules_version
from .win_extract import clean_msi


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
                     selection={"R", "mingw"},
                     documentation=True,
                     last_function=None
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
    @param      last_function   function to execute just before running InnoSetup,
                                see `win_setup_helper.py <https://github.com/sdpython/ensae_teaching_cs/blob/master/src/ensae_teaching_cs/automation/win_setup_helper.py>`_
                                for an example
    @param      documentation   add documentation
    @return                     list of completed operations

    The available tools to install must be chose among:
        * `R <http://www.r-project.org/>`_
        * `Julia <http://julialang.org/>`_
        * `MinGW <http://www.mingw.org/>`_
        * `VS <https://www.visualstudio.com/en-us/products/visual-studio-express-vs.aspx>`_

    By default, only R is included. Julia requires too much work.
    The command line does not always end. The building of the package
    is sometimes reluctant to work. And the Julia kernel is exclusive:
    it cannot be setup with others kernel. Maybe the version 0.5 will fix those issues.

    The signature of function ``last_function`` should be the following::

        def last_function(inno_script, folders, verbose=False, fLOG=print):
            # something specific to do
            # before compiling the setup
            # such adding new tools
            # or replacing icons
            # the inno setup script is located in folders["logs"]

    The parameters *folders* is a dictionary which gives access to the main folders
    of the distribution.

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
    * *build*: location of downloaded modules and tools

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
    * If the R kernel fails to start, you should manually run the script
      `R_install.r <https://github.com/sdpython/pymyinstall/blob/master/src/pymyinstall/win_installer/R_install.r>`_.

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
    selection.add("python")
    selection = set(_.lower() for _ in selection)
    fLOG("--- selection", selection)

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
                   build=download_folder,
                   )

    for k, v in folders.items():
        if not os.path.exists(v):
            os.mkdir(v)

    ###########################
    # download the documentation
    ###########################
    if documentation:
        operations.append(("documentation", "-"))
        op = win_download_notebooks(
            notebooks, folders["workspace"], verbose=verbose, fLOG=fLOG)
        operations.extend(op)
        operations.append(("time", dtnow()))

    ######################
    # download of everything
    ######################
    for mod in module_list:
        mod.fLOG = fLOG
    operations.append(("download", "-"))
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
            folders, verbose=verbose, fLOG=fLOG, selection=selection, module_list=module_list)
        operations.extend(op)

        #######################
        # modifies scite properties
        #######################
        fLOG("--- modifies Scite properties")
        modify_scite_properties(os.path.join("%PYTHON_WINHOME%", "pythonw"),
                                os.path.join(folders["tools"], "Scite", "wscite"))

        ###########
        # update pip
        ###########
        fLOG("--- update pip")
        operations.append(("python pip", "update"))
        op = update_pip(folders["python"])
        operations.extend(op)
        operations.append(("time", dtnow()))

        if "julia" in selection:
            operations.append(("julia", "-"))
            ops = win_install_julia_step(folders, verbose=verbose, fLOG=fLOG)
            operations.extend(ops)
            operations.append(("time", dtnow()))

        if "r" in selection:
            operations.append(("r", "-"))
            ops = win_install_r_step(folders, verbose=verbose, fLOG=fLOG)
            operations.extend(ops)
            operations.append(("time", dtnow()))

        ######################
        # installation of packages
        ######################
        fLOG("--- installation of python packages")
        operations.append(("python packaes", "start"))
        python_path = folders["python"]
        win_install_packages_other_python(
            python_path, download_folder, verbose=verbose, fLOG=fLOG,
            module_list=module_list)
        fLOG("done")
        operations.append(("time", dtnow()))

        ##########################
        # mingw, add file distutils.cfg
        ##########################
        if "mingw" in selection:
            fLOG("--- switch_to_mingw_compiler")
            op = switch_to_mingw_compiler(folders["python"])
            for o in op:
                operations.append(("modify", o))

        ##########################
        # Visual Studio, switch on 2013
        ##########################
        if "vs" in selection:
            fLOG("--- switch_to_VS_compiler")
            op = switch_to_VS_compiler(folders["python"])
            for o in op:
                operations.append(("modify", o))

        ######################
        # create ipython profile
        ######################
        has_ipython = False
        for mod in module_list:
            if mod.name == "ipython":
                has_ipython = True
        if has_ipython:
            fLOG("--- create ipython profile")
            operations.append(("ipython", "create profile"))
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
            operations.append(("time", dtnow()))

        ######################
        # update ipython profile
        ######################
        if has_ipython:
            fLOG("--- update ipython profile")
            operations.append(("ipython", "update profile"))
            with open(profile, "r") as f:
                content = f.read()
            content += """
                        c.ContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store', '*.so', '*.dylib', '*~', ".ipynb_checkpoints", ".kernel-*.json", ".kernel", ".RData", ".RHistory"]
                        c.FileContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store', '*.so', '*.dylib', '*~', ".ipynb_checkpoints", ".kernel-*.json", ".kernel", ".RData", ".RHistory"]
                        """.split("\n")
            content = "\n".join(_.strip() for _ in content)
            with open(profile, "w") as f:
                f.write("\n" + content + "\n")
            operations.append(("time", dtnow()))

        ######################
        # copy pywin32 dll to main folders
        ######################
        fLOG("--- pywin32 dll to main folders")
        operations.append(("pywin32", "dll"))
        fdll = os.path.join(
            python_path, "Lib", "site-packages", "pywin32_system32")
        for dll in os.listdir(fdll):
            full = os.path.join(fdll, dll)
            if os.path.isdir(full):
                continue
            try:
                shutil.copy(full, python_path)
            except KeyError as a:
                # it means it already exists
                continue
            operations.append(("pywin32", "copy " + dll))
        operations.append(("time", dtnow()))

        ########
        # kernels
        ########
        if has_ipython:
            fLOG("--- add kernels")
            operations.append(("kernel", "add"))
            res = install_kernels(folders["tools"], folders["python"])
            for r in res:
                fLOG("ADD: kernel", r)
            operations.append(("time", dtnow()))

    ################################
    # prepare setup script for InnoSetup
    ###############################
    fLOG("--- prepare setup script for InnoSetup")
    replacements = dict(__DISTPATH__=folder)
    new_script = innosetup_replacements(replacements=replacements, fLOG=fLOG,
                                        temp_folder=os.path.join(folders["logs"]))
    fLOG("done")
    operations.append(("InnoSetup", "replacement"))
    operations.append(("time", dtnow()))

    if last_function is not None:
        #################
        # run last_function
        #################
        fLOG("--- run last_function")
        operations.append(("start", "last_function"))
        last_function(new_script, folders, verbose=verbose, fLOG=fLOG)
        operations.append(("time", dtnow()))

    ##################
    # patch exe in scripts
    ##################
    fLOG(
        "--- patch paths, see http://www.clemens-sielaff.com/create-a-portable-python-with-pip-on-windows/")
    op = win_patch_paths(
        os.path.join(folders["python"], "Scripts"), folders["python"], fLOG=fLOG)
    operations.extend(op)
    operations.append(("time", dtnow()))

    #################
    # print the list of modules
    #################
    fLOG("--- pip freeze")
    mods = get_modules_version(folders["python"])
    fLOG("nb modules: {0}".format(len(mods)))
    if len(mods) == 0:
        raise ValueError(
            "unable to get module list from folder " + folders["python"])
    with open(os.path.join(folders["config"], "installed_modules.txt"), "w") as f:
        for a, b in sorted(mods.items()):
            f.write("{0}\t{1}\n".format(a, b))

    if not no_setup:
        ################################
        # prepare setup script for InnoSetup
        ###############################
        fLOG("--- building setup with InnoSetup")
        out = run_innosetup(new_script, fLOG=fLOG,
                            temp_folder=os.path.join(folders["logs"]))
        with open(os.path.join(folders["logs"], "out.install.innosetup.txt"), "w", encoding="utf8") as f:
            f.write(out)
        fLOG("done")
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
