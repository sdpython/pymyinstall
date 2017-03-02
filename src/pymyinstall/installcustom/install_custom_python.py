"""
@file
@brief Various functions to install `python <http://www.python.org/>`_.
"""
from __future__ import print_function
import sys
import os

from ..installhelper.install_cmd_helper import run_cmd, unzip_files
from .install_custom import download_page, download_file

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def unzip7_files(filename_7z, fLOG=print, dest="."):
    """
    If `7z <http://www.7-zip.org/>`_ is installed, the function uses it
    to uncompress file into 7z format. The file *filename_7z* must not exist.

    .. index:: 7zip, 7z

    :param      filename_7z:     final destination
    :param      fLOG:            logging function
    :param      dest:            destination folder

    :return:                     output of 7z

    .. versionadded:: 1.1
    """
    if sys.platform.startswith("win"):
        exe = r"C:\Program Files\7-Zip\7z.exe"
        if not os.path.exists(exe):
            raise FileNotFoundError("unable to find: {0}".format(exe))
    else:
        exe = "7z"

    if not os.path.exists(filename_7z):
        raise FileNotFoundError(filename_7z)

    cmd = '"{0}"-y -o"{2}" x "{1}"'.format(exe, filename_7z, dest)
    out, err = run_cmd(cmd, wait=True)

    if err is not None and len(err) > 0:
        raise Exception("OUT:\n{0}\nERR:\n{1}".format(out, err))

    return out


def fix_fcntl_windows(path):
    """
    Add a file fnctl.py on Windows (only available on Linux)

    @param   path       path to the python installation
    """
    if not sys.platform.startswith("win"):
        raise Exception("fcntl should only be added on Windows.")
    dest = os.path.join(path, "Lib", "fcntl.py")
    if os.path.exists(dest):
        # already done
        return
    module = """
                def fcntl(fd, op, arg=0):
                    return 0
                def ioctl(fd, op, arg=0, mutable_flag=True):
                    if mutable_flag:
                        return 0
                    else:
                        return ""
                def flock(fd, op):
                    return
                def lockf(fd, operation, length=0, start=0, whence=0):
                    return
        """.replace("                ", "")
    with open(dest, "w") as f:
        f.write(module)


def fix_termios_windows(path):
    """
    Add a file termios.py on Windows (only available on Linux)

    @param   path       path to the python installation
    """
    if not sys.platform.startswith("win"):
        raise Exception("fcntl should only be added on Windows.")
    dest = os.path.join(path, "Lib", "termios.py")
    if os.path.exists(dest):
        # already done
        return
    module = """
                TCSAFLUSH = 1
        """.replace("                ", "")
    with open(dest, "w") as f:
        f.write(module)


def install_python(temp_folder=".", fLOG=print, install=True, force_download=False,
                   version=None, modules=None, custom=False, latest=False):
    """
    Install `python <http://www.python.org/>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of python
    @param      version         version to download (by default the current version of Python)
    @param      modules         modules to install
    @param      custom          the standalone distribution has issue when installing new packages,
                                custom is True means switching to a zip of the standard distribution
    @param      latest          install this version of pymyinstall and not the pypi version
    @return                     temporary file

    The version is fixed to the current version of Python and amd64.

    .. versionmodified:: 1.1
        Add parameters *custom*, *latest*.
    """
    if version is None:
        version = "%s.%s.%s" % sys.version_info[:3]
    versioni = tuple([int(_) for _ in version.split(".")])
    link = "https://www.python.org/downloads/release/python-%s/" % version.replace(
        ".", "")
    page = download_page(link)
    if page is None:
        raise ValueError("page is None fir link '{0}'".format(link))
    if sys.platform.startswith("win"):
        if versioni[:2] <= (3, 4):
            raise NotImplementedError(
                "Python <= 3.4 is not supported anymore.")
        # the setup for Python 3.5 does not accept multiple version
        # it was installed on one machine and then compressed into a 7z
        # file
        if versioni >= (3, 6, 0):
            if custom:
                if versioni != (3, 6, 0):
                    raise ValueError(
                        "Not custom zip available for Python {0}".format(versioni))
                url = "http://www.xavierdupre.fr/enseignement/setup/Python36-3.6.0-amd64.zip"
            else:
                url = "https://www.python.org/ftp/python/3.6.0/python-3.6.0-embed-amd64.zip"
        elif versioni >= (3, 5, 0):
            if custom:
                if versioni not in [(3, 5, 3), (3, 5, 2)]:
                    raise ValueError(
                        "Not custom zip available for Python {0}".format(versioni))
                url = "http://www.xavierdupre.fr/enseignement/setup/Python35-3.5.3-amd64.zip"
            else:
                url = "https://www.python.org/ftp/python/3.5.3/python-3.5.3-embed-amd64.zip"
        else:
            raise Exception(
                "unable to find a proper version for version {0}".format(version))
        full = url.split("/")[-1]
        outfile = os.path.join(temp_folder, full)
        fLOG("[install_python] download", url)
        local = download_file(url, outfile, fLOG=fLOG)
        if install:
            # unzip files
            unzip_files(local, temp_folder, fLOG=fLOG)

            # get-pip
            if not custom:
                get_pip = "https://bootstrap.pypa.io/get-pip.py"
                outfile_pip = os.path.join(temp_folder, "get-pip.py")
                download_file(get_pip, outfile_pip, fLOG=fLOG)

                # following issue https://github.com/pypa/get-pip/issues/7
                vers = "%d%d" % sys.version_info[:2]
                if vers == "36":
                    pth = os.path.join(temp_folder, "python%s._pth" % vers)
                    with open(pth, "r") as f:
                        content = f.read()
                    content = content.replace("#import site", "import site")
                    with open(pth, "w") as f:
                        f.write(content)

            # run get-pip.py
            pyexe = os.path.join(temp_folder, "python.exe")
            if not os.path.exists(pyexe):
                raise FileNotFoundError(pyexe)

            if not custom:
                cmd = '"{0}" -u "{1}"'.format(pyexe, outfile_pip)
                out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
                if len(err) > 0:
                    raise Exception(
                        "Something went wrong:\nCMD\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))
            else:
                from ..win_installer.win_patch import win_patch_paths
                fLOG("[install_python] Patch scripts .exe")
                patched = win_patch_paths(temp_folder, pyexe, fLOG=fLOG)
                for pat in patched:
                    fLOG("  - ", pat)

            # fix fcntl
            fix_fcntl_windows(temp_folder)
            fix_termios_windows(temp_folder)

            # modules
            if modules is not None:
                if isinstance(modules, list):
                    raise NotImplementedError(
                        "Not implemented for a list of modules.")

                # cmd = '"{0}" -u -c "import pip;pip.main([\'install\', \'https://github.com/sdpython/pymyinstall/archive/master.zip\'])"'.format(pyexe)
                if latest:
                    folder = os.path.normpath(os.path.join(os.path.abspath(
                        os.path.dirname(__file__)), "..", "..", ".."))
                    setup = os.path.join(folder, "setup.py")
                    if not os.path.exists(setup):
                        raise FileNotFoundError(setup)
                    cmd = '"{0}" -u "{1}\\setup.py" install'.format(
                        pyexe, folder)
                    change_path = folder
                else:
                    cmd = '"{0}" -u -c "import pip;pip.main([\'install\', \'pymyinstall\'])"'.format(
                        pyexe)
                    change_path = None
                out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                                   change_path=change_path)
                err = [_ for _ in err.split("\n") if not _.startswith("pymyinstall.") and not _.startswith(
                    "zip_safe flag not set; analyzing archive contents...")]
                err = "\n".join(_ for _ in err if _)

                exp = ".zip/lib2to3/Grammar.txt"
                if len(err) > 0 and exp not in out.replace("\\", "/").replace("//", "/"):
                    raise Exception(
                        "Something went wrong:\nCMD\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))
                fLOG(out)

                fLOG("[install_python] modules")
                cmd = ('"{0}" -u -c "import sys;from pymyinstall.packaged import install_all;install_all(fLOG=print, temp_folder=\'download\', ' +
                       'verbose=True, source=\'2\', list_module=\'{1}\')"').format(pyexe, modules)
                out, err = run_cmd(
                    cmd, wait=True, fLOG=fLOG, communicate=False)
                if len(err) > 0:
                    raise Exception(
                        "Something went wrong:\nCMD\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))
                fLOG(out)

        return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
