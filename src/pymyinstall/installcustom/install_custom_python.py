"""
@file
@brief Various functions to install `python <http://www.python.org/>`_.
"""
from __future__ import print_function
import sys
import re
import os

from ..installhelper.install_cmd_helper import run_cmd, python_version, unzip_files
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


def install_python(
        temp_folder=".", fLOG=print, install=True, force_download=False, version=None, modules=None):
    """
    Install `python <http://www.python.org/>`_.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of python
    @param      version         version to download (by default the current version of Python)
    @param      modules         modules to install
    @return                     temporary file

    The version is fixed to the current version of Python and amd64.
    """
    if version is None:
        version = "%s.%s.%s" % sys.version_info[:3]
    versioni = tuple([int(_) for _ in version.split(".")])
    link = "https://www.python.org/downloads/release/python-%s/" % version.replace(
        ".", "")
    page = download_page(link)
    if sys.platform.startswith("win"):
        if versioni[:2] <= (3, 4):
            o, b = python_version()
            if "32" in b:
                reg = re.compile("href=\\\"(.*?[.]((msi)|(exe)|(zip)))\\\"")
                alls = reg.findall(page)
                alls = [_ for _ in alls if "amd64" not in _]
            else:
                reg = re.compile(
                    "href=\\\"(.*?amd64[.]((msi)|(exe)|(zip)))\\\"")
                alls = reg.findall(page)

            if len(alls) == 0:
                raise Exception(
                    "(1) unable to find a link on page: " + link + "\n" +
                    page)

            alls0 = alls
            alls = [_ for _ in alls if not _[0].endswith("zip")]

            if len(alls) == 0:
                raise Exception(
                    "(2) unable to find a link on page: " + link + "\n" +
                    "\n".join(str(_) for _ in alls0))

            url = alls[0][0]
            full = url.split("/")[-1]
            outfile = os.path.join(temp_folder, full)
            local = download_file(url, outfile, fLOG=fLOG)
            if install:
                if local.endswith("msi"):
                    run_cmd("msiexec /i " + local, fLOG=fLOG, wait=True)
                else:
                    unzip_files(local, temp_folder, fLOG=fLOG)
                    p35 = os.path.join(temp_folder, "python35.zip")
                    if os.path.exists(p35):
                        lib = os.path.join(temp_folder, "Lib")
                        if not os.path.exists(lib):
                            os.mkdir(lib)
                        unzip_files(p35, lib, fLOG=fLOG)
                        os.remove(p35)
            return local
        else:
            # the setup for Python 3.5 does not accept multiple version
            # it was installed on one machine and then compressed into a 7z
            # file
            if versioni >= (3, 6, 0):
                url = "https://www.python.org/ftp/python/3.6.0/python-3.6.0-embed-amd64.zip"
            elif versioni >= (3, 5, 0):
                url = "https://www.python.org/ftp/python/3.5.3/python-3.5.3-embed-amd64.zip"
            else:
                raise Exception(
                    "unable to find a proper version for version {0}".format(version))
            full = url.split("/")[-1]
            outfile = os.path.join(temp_folder, full)
            local = download_file(url, outfile, fLOG=fLOG)
            if install:
                # unzip files
                unzip_files(local, temp_folder, fLOG=fLOG)

                # get-pip
                get_pip = "https://bootstrap.pypa.io/get-pip.py"
                outfile_pip = os.path.join(temp_folder, "get-pip.py")
                download_file(get_pip, outfile_pip, fLOG=fLOG)

                # following issue https://github.com/pypa/get-pip/issues/7
                pth = os.path.join(temp_folder, "python36._pth")
                with open(pth, "r") as f:
                    content = f.read()
                content = content.replace("#import site", "import site")
                with open(pth, "w") as f:
                    f.write(content)

                # run get-pip.py
                pyexe = os.path.join(temp_folder, "python.exe")
                if not os.path.exists(pyexe):
                    raise FileNotFoundError(pyexe)
                cmd = '"{0}" -u "{1}"'.format(pyexe, outfile_pip)
                out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
                if len(err) > 0:
                    raise Exception(
                        "Something went wrong:\nCMD\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))

                # modules
                if modules is not None:
                    if isinstance(modules, list):
                        raise NotImplementedError(
                            "Not implemented for a list of modules.")

                    # cmd = '"{0}" -u -c "import pip;pip.main([\'install\', \'https://github.com/sdpython/pymyinstall/archive/master.zip\'])"'.format(pyexe)
                    cmd = '"{0}" -u -c "import pip;pip.main([\'install\', \'pymyinstall\'])"'.format(
                        pyexe)
                    out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
                    exp = ".zip/lib2to3/Grammar.txt"
                    if len(err) > 0 and exp not in out.replace("\\", "/").replace("//", "/"):
                        raise Exception(
                            "Something went wrong:\nCMD\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))
                    fLOG(out)

                    cmd = '"{0}" -u -c "import sys;from pymyinstall.packaged import install_all;install_all(temp_folder=\'download\', verbose=True, source=\'2\', list_module=\'{1}\')"'.format(
                        pyexe, modules)
                    out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
                    if len(err) > 0:
                        raise Exception(
                            "Something went wrong:\nCMD\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))
                    fLOG(out)

            return local
    else:
        raise NotImplementedError("not available on platform " + sys.platform)
