# -*- coding: utf-8 -*-
"""
@file
@brief Various functions to install `python <http://www.python.org/>`_.
"""
from __future__ import print_function
import sys
import os
import datetime

from ..installhelper.install_cmd_helper import run_cmd, unzip_files
from .install_custom import download_page, download_file

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def unzip7_files(filename_7z, fLOG=print, dest="."):
    """
    If `7z <http://www.7-zip.org/>`_ is installed, the function uses it
    to uncompress file into *7z* format. The file *filename_7z* must not exist.

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
        raise Exception("OUT:\n{0}\nERR-A:\n{1}".format(out, err))

    return out


def fix_fcntl_windows(path):
    """
    Adds a file `fnctl.py` on :epkg:`Windows`
    (only available on :epkg:`Linux`).

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
    Adds a file `termios.py` on :epkg:`Windows`
    (only available on :epkg:`Linux`).

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


def fix_resource_windows(path):
    """
    Adds a file `resource.py` on :epkg:`Windows`
    (only available on :epkg:`Linux`).

    @param   path       path to the python installation
    """
    if not sys.platform.startswith("win"):
        raise Exception("fcntl should only be added on Windows.")
    dest = os.path.join(path, "Lib", "resource.py")
    if os.path.exists(dest):
        # already done
        return
    module = """
        """.replace("                ", "")
    with open(dest, "w") as f:
        f.write(module)


def install_python(temp_folder=".", fLOG=print, install=True, force_download=False,  # pylint: disable=R0914
                   version=None, modules=None, custom=False, latest=False,
                   download_folder="download", verbose=False):
    """
    Installs :epkg:`python`.
    It does not do it a second time if it is already installed.

    @param      temp_folder     where to download the setup
    @param      fLOG            logging function
    @param      install         install (otherwise only download)
    @param      force_download  force the downloading of python
    @param      version         version to download (by default the current version of Python)
    @param      modules         modules to install
    @param      custom          the standalone distribution has issue when installing new packages,
                                custom is True means switching to a zip of the standard distribution,
                                see below
    @param      latest          install this version of pymyinstall and not the pypi version
    @param      download_folder download folder for packages
    @param      verbose         more display
    @return                     temporary file

    The version is fixed to the current version of Python and amd64.
    The standalone distribution has an issue and raises an error for some
    packages such as `smart_open <https://pypi.python.org/pypi/smart_open>`_:

    ::

        error: [Errno 2] No such file or directory: '<python>\\python36.zip\\lib2to3\\Grammar.txt'

    In that case, you should consider using ``custom=True``.

    .. versionchanged:: 1.1
        Add parameters *custom*, *latest*, *verbose*.

    .. versionchanged:: 1.2
        Implements the version for :epkg:`Linux`.
    """
    def clean_err(err):
        # remove a couple of warnings.
        lines = err.split("\n")
        lines2 = [
            _ for _ in lines if "UserWarning: Module pymyinstall was already imported" not in _]
        if len(lines2) < len(lines):
            lines2 = [
                _ for _ in lines2 if "from pip._vendor import pkg_resources" not in _]
        return "\n".join(lines2)

    if version is None:
        version = "%s.%s.%s" % sys.version_info[:3]
    versioni = tuple([int(_) for _ in version.split(".")])
    link = "https://www.python.org/downloads/release/python-%s/" % version.replace(
        ".", "")
    page = download_page(link)
    if page is None:
        raise ValueError("page is None for link '{0}'".format(link))

    if sys.platform.startswith("win"):
        if versioni[:2] <= (3, 4):
            raise NotImplementedError(
                "Python <= 3.4 is not supported anymore.")
        # The setup for Python 3.5 does not accept multiple versions,
        # it was installed on one machine and then compressed into a 7z
        # file
        if versioni >= (3, 7, 0):
            if custom:
                if versioni > (3, 7, 0):
                    raise ValueError(
                        "Not custom zip available for Python {0}".format(versioni))
                url = "http://www.xavierdupre.fr/enseignement/setup/Python{0}{1}-{0}.{1}.{2}-amd64.zip".format(
                    *sys.version_info[:3])
            else:
                url = "https://www.python.org/ftp/python/{0}.{1}.{2}/python-{0}.{1}.{2}-embed-amd64.zip".format(
                    *sys.version_info[:3])
        elif versioni >= (3, 6, 0):
            if custom:
                if versioni > (3, 6, 5):
                    raise ValueError(
                        "Not custom zip available for Python {0}".format(versioni))
                url = "http://www.xavierdupre.fr/enseignement/setup/Python{0}{1}-{0}.{1}.{2}-amd64.zip".format(
                    *sys.version_info[:3])
            else:
                url = "https://www.python.org/ftp/python/{0}.{1}.{2}/python-{0}.{1}.{2}-embed-amd64.zip".format(
                    *sys.version_info[:3])
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
                "Unable to find a proper version for version {0}".format(version))
    else:
        url = "https://www.python.org/ftp/python/{0}.{1}.{2}/Python-{0}.{1}.{2}.tgz".format(
            *versioni)

    full = url.split("/")[-1]
    outfile = os.path.join(temp_folder, full)
    fLOG("[install_python] download", url)
    local = download_file(url, outfile, fLOG=fLOG)

    # Install
    if install:
        # unzip files
        if sys.platform.startswith("win"):
            unzip_files(local, temp_folder, fLOG=fLOG)
        else:
            cmd = "tar xzf {0}".format(outfile)
            out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                               change_path=temp_folder)
            if err:
                raise RuntimeError(
                    "Issue with running '{0}'\n--OUT--\n{1}\n--ERR--\n{2}\n--IN--\n{3}".format(cmd, out, err, temp_folder))
            pyinstall = os.path.join(
                temp_folder, "Python-{0}.{1}.{2}".format(*versioni))

            cmd = "./configure --enable-optimizations --with-ensurepip=install --prefix={0}/inst --exec-prefix={0}/bin --datadir={0}/data"
            cmd = cmd.format(temp_folder)
            out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                               change_path=pyinstall)
            if err:
                lines = []
                for line in err.split("\n"):
                    if "[libinstall] Error 1 (ignored)" in line:
                        continue
                    lines.append(line)
                err = "\n".join(lines).strip() if lines else None
            if err:
                raise RuntimeError(
                    "Issue with running '{0}'\n--OUT--\n{1}\n--ERR--\n{2}".format(cmd, out, err))

            # See https://stackoverflow.com/questions/44708262/make-install-from-source-python-without-running-tests.
            os.environ["EXTRATESTOPTS"] = "--list-tests"
            cmd = "make"
            out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                               change_path=pyinstall)
            if err:
                lines = []
                for line in err.split("\n"):
                    if "find: ‘build’: No such file or directory" in line:
                        continue
                    if "(ignored)" in line:
                        continue
                    if "Task was destroyed but it is pending!" in line:
                        continue
                    if "[libinstall] Error 1 (ignored)" in line:
                        continue
                    if "task: <Task finished coro=<<async_generator_athrow without __name__>()" in line:
                        continue
                    if "stty: 'standard input': Inappropriate ioctl for device" in line:
                        continue
                    if "task: <Task pending coro=<<async_generator_athrow without __name__>()>>" in line:
                        continue
                    if "unhandled exception during asyncio.run() shutdown" in line:
                        continue
                    if "RuntimeError: can't send non-None value to a just-started coroutine" in line:
                        continue
                    lines.append(line)
                err = "\n".join(lines).strip() if lines else None
            if err:
                raise RuntimeError(
                    "Issue with running '{0}'\n---OUT---\n{1}\n---ERR---\n{2}\n---IN---\n{3}".format(cmd, out, err, pyinstall))

            cmd = "make altinstall"
            out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                               change_path=pyinstall)
            if err:
                raise RuntimeError(
                    "Issue with running '{0}'\n--OUT--\n{1}\n--ERR--\n{2}\n--IN--\n{3}".format(cmd, out, err, pyinstall))

        # has pip?
        if sys.platform.startswith("win"):
            pyexe = os.path.join(temp_folder, "python.exe")
        else:
            pyexe = os.path.join(temp_folder, "bin", "python")
        cmd = "{0} -m pip --help"
        try:
            _, err = run_cmd(cmd, wait=True)
            has_pip = not err
        except Exception:
            has_pip = False

        # get-pip
        if not has_pip:
            get_pip = "https://bootstrap.pypa.io/get-pip.py"
            outfile_pip = os.path.join(temp_folder, "get-pip.py")
            download_file(get_pip, outfile_pip, fLOG=fLOG)

            # following issue https://github.com/pypa/get-pip/issues/7
            if sys.platform.startswith("win"):
                vers = "%d%d" % sys.version_info[:2]
                if vers in ("36", "37"):
                    pth = os.path.join(temp_folder, "python%s._pth" % vers)
                    with open(pth, "r") as f:
                        content = f.read()
                    content = content.replace("#import site", "import site")
                    with open(pth, "w") as f:
                        f.write(content)

        # run get-pip.py
        if sys.platform.startswith("win"):
            pyexe = os.path.join(temp_folder, "python.exe")
        else:
            versioni3 = versioni[:3]
            pyexe = os.path.join(
                temp_folder, "Python-{}.{}.{}".format(*versioni3), "python")
        if not os.path.exists(pyexe):
            raise FileNotFoundError(pyexe)

    # Patches for windows.
    if install and sys.platform.startswith("win"):
        if not custom:
            cmd = '"{0}" -u "{1}"'.format(pyexe, outfile_pip)
            out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
            if len(err) > 0:
                skip = ['Consider adding this directory to PATH',
                        'which is not on PATH.']
                lines = err.split('\n')
                errs = []
                for line in lines:
                    zoo = True
                    for sk in skip:
                        if sk in line:
                            zoo = False
                            break
                    if zoo:
                        errs.append(line)
                err = "\n".join(errs).strip(' \n\r')
            if len(err) > 0:
                raise Exception(
                    "Something went wrong:\nCMD\n{0}\nOUT\n{1}\nERR-B\n{2}".format(cmd, out, err))
        else:
            from ..win_installer.win_patch import win_patch_paths
            fLOG("[install_python] Patch scripts .exe")
            patched = win_patch_paths(temp_folder, pyexe, fLOG=fLOG)
            for pat in patched:
                fLOG("  - ", pat)

        # fix fcntl
        fix_fcntl_windows(temp_folder)
        fix_termios_windows(temp_folder)
        fix_resource_windows(temp_folder)

    # modules
    if install and modules is not None:
        if isinstance(modules, list):
            raise NotImplementedError(
                "Not implemented for a list of modules.")

        # cmd = '"{0}" -u -c "import pip;pip.main([\'install\',
        #        \'https://github.com/sdpython/pymyinstall/archive/master.zip\'])"'.format(pyexe)
        if latest:
            folder = os.path.normpath(os.path.join(os.path.abspath(
                os.path.dirname(__file__)), "..", "..", ".."))
            setup = os.path.join(folder, "setup.py")
            if not os.path.exists(setup):
                raise FileNotFoundError(setup)
            sep = "\\" if sys.platform.startswith("win") else "/"
            cmd = '"{0}" -u "{1}{2}setup.py" install'.format(
                pyexe, folder, sep)
            change_path = folder
        else:
            cmd = '"{0}" -u -c "import pip._internal;pip._internal.main([\'install\', \'pymyinstall\'])"'.format(
                pyexe)
            change_path = None
        fLOG("[install_python] " + cmd)
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG, change_path=change_path)
        err_keep = err
        err = [_ for _ in err.split("\n") if not _.startswith("pymyinstall.") and not _.startswith(
            "zip_safe flag not set; analyzing archive contents...") and not _.startswith("error removing build")]
        err = "\n".join(_ for _ in err if _)

        exp = ".zip/lib2to3/Grammar.txt"
        if len(err) > 0 and exp not in out.replace("\\", "/").replace("//", "/"):
            raise Exception(
                "Something went wrong:\nCMD\n{0}\nOUT\n{1}\nERR-C\n{2}".format(cmd, out, err_keep))
        fLOG(out)

        dirpyexe = os.path.dirname(pyexe)
        fLOG(
            "[install_python] add python to PATH='{0}'".format(dirpyexe))
        path = os.environ['PATH']
        path = ";".join([dirpyexe, path])
        os.environ['PATH'] = path

        fLOG("[install_python] install modules")
        pattern = '"{0}" -u -c "import sys;from pymyinstall.packaged import install_all;install_all(fLOG=print, temp_folder=\'{2}\',' + \
                  'verbose=True, source=\'2\', list_module=\'{1}\')"'
        cmd = pattern.format(
            pyexe, modules, download_folder.replace("\\", "/"))
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                           communicate=False, catch_exit=True)
        fLOG("[install_python] end installed modules.")
        if len(err) > 0:
            # We try a second time to make sure a second pass does not help.
            fLOG("[install_python2] install modules")
            out_, err_ = run_cmd(
                cmd, wait=True, fLOG=fLOG, communicate=False, catch_exit=False)
            err__ = clean_err(err_)
            if len(err__) > 0:
                mes = "[install_python2] end installed modules. Something went wrong:\n"
                raise Exception(
                    mes + "ERR-D-CMD\n{0}\nOUT\n{1}\nOUT2\n{3}\nERR-D\n{2}\nERR2-D\n{4}\nERR2-Dc\n{5}\n**CMD**\n{0}".format(
                        cmd, out, err, out_, err_, err__))
            else:
                out += ("\n-------------" * 5) + "\n" + out_
            fLOG("[install_python2] end installed modules.")
        fLOG(out)

    return local


def folder_older_than(folder, delay=datetime.timedelta(30)):
    """
    Tells if a folder is older than a given timespan.

    @param      folder      folder name
    @param      delay       delay
    @return                 boolean
    """
    folder = os.path.abspath(folder)
    if not os.path.exists(folder):
        return False
    cre = os.stat(folder).st_ctime
    dt = datetime.datetime.fromtimestamp(cre)
    now = datetime.datetime.now()
    delta = now - dt
    return delta > delay
