"""
@file
@brief Various function to install various python module from various location.
"""
from __future__ import print_function

import sys
import platform
import os
import zipfile
import datetime
from .module_install_exceptions import UpdatePipError
from .run_cmd import run_cmd_private, run_cmd_old

if sys.version_info[0] == 2:
    FileNotFoundError = Exception


def python_version():
    """
    Retrieves the platform and version of this :epkg:`python`.

    @return     tuple, example: ("win32","32bit") or ("win32","64bit")
    """
    return sys.platform, platform.architecture()[0]


def unzip_files(zipf, whereTo, fLOG=print):
    """
    Unzip files from a :epkg:`zip` archive.

    @param      zipf        archive
    @param      whereTo     destination folder
    @param      fLOG        logging function
    @return                 list of unzipped files
    """
    files = []
    with zipfile.ZipFile(zipf, "r") as file:
        for info in file.infolist():
            if not os.path.exists(info.filename):
                data = file.read(info.filename)
                tos = os.path.join(whereTo, info.filename)
                if not os.path.exists(tos):
                    finalfolder = os.path.split(tos)[0]
                    if not os.path.exists(finalfolder):
                        fLOG("    creating folder ", finalfolder)
                        os.makedirs(finalfolder)
                    if not info.filename.endswith("/"):
                        u = open(tos, "wb")
                        u.write(data)
                        u.close()
                        files.append(tos)
                        if fLOG:
                            fLOG("    unzipped ", info.filename, " to ", tos)
                elif not tos.endswith("/"):
                    files.append(tos)
            elif not info.filename.endswith("/"):
                files.append(info.filename)
    return files


def add_shortcut_to_desktop_for_module(name):
    """
    Adds a shortcut on a module which includes a script.

    @param      name        name of the module
    @return                 shortcut was added or not
    """
    if name == "spyder":
        from .link_shortcuts import add_shortcut_to_desktop, suffix
        from .module_install import ModuleInstall
        md = ModuleInstall("spyder", "exe", script="spyder.bat")
        sc = md.Script
        if os.path.exists(sc):
            ver = suffix()
            r = add_shortcut_to_desktop(sc, name + "." + ver, name + "." + ver)
            return os.path.exists(r)
        else:
            return False
    else:
        raise NotImplementedError(
            "nothing implemented for module: {0}".format(name))


def get_pip_program(exe=None):
    """
    Gets :epkg:`pip` executable and
    fixes an issue with :epkg:`Pandoc`.

    @param      exe             path to python executable
    @return                     pip executable

    .. faqref::
        :title: How can I check the dependencies?

        The module `pipdeptree <https://github.com/naiquevin/pipdeptree>`_ gives
        you something like::

            d3py==0.2.3
            - ipython [installed: 3.1.0]
            - networkx [installed: 1.9.1]
                - decorator [required: >=3.4.0, installed: 3.4.2]
            - numpy [installed: 1.9.2]
            - pandas [installed: 0.16.0]
                - pytz [required: >=2011k, installed: 2015.4]
                - python-dateutil [required: >=2, installed: 2.4.2]
                - six [required: >=1.5, installed: 1.9.0]
                - numpy [required: >=1.7.0, installed: 1.9.2]
            autopep8==1.1.1
            - pep8 [required: >=1.5.7, installed: 1.5.7]
            sphinxjp.themes.basicstrap==0.4.2
            - setuptools
            - Sphinx [installed: 1.3.1]
                - alabaster [required: >=0.7, installed: 0.7.4]
                - six [required: >=1.4, installed: 1.9.0]
                - colorama [installed: 0.3.3]
                - Pygments [required: >=2.0, installed: 2.0.2]
                - Babel [required: >=1.3, installed: 1.3]
                - pytz [required: >=0a, installed: 2015.4]
                - snowballstemmer [required: >=1.1, installed: 1.2.0]
                - docutils [required: >=0.11, installed: 0.12]
                - sphinx-rtd-theme [required: >=0.1, installed: 0.1.8]
                - Sphinx [required: >=1.3, installed: 1.3.1]
                    - alabaster [required: >=0.7, installed: 0.7.4]
                    - six [required: >=1.4, installed: 1.9.0]
                    - colorama [installed: 0.3.3]
                    - Pygments [required: >=2.0, installed: 2.0.2]
                    - Babel [required: >=1.3, installed: 1.3]
                    - pytz [required: >=0a, installed: 2015.4]
                    - snowballstemmer [required: >=1.1, installed: 1.2.0]
                    - docutils [required: >=0.11, installed: 0.12]
                    - Jinja2 [required: >=2.3, installed: 2.7.3]
                    - MarkupSafe [installed: 0.23]
                - Jinja2 [required: >=2.3, installed: 2.7.3]
                - MarkupSafe [installed: 0.23]

            ...
    """
    tried = []
    if exe is None:
        exe = os.path.dirname(sys.executable)
    major, minor = sys.version_info[0:2]
    if sys.platform.startswith("win"):
        if not exe.lower().endswith("scripts"):
            pi = os.path.join(exe, "Scripts", "pip.exe")
            tried.append(pi)
            if not os.path.exists(pi):
                pi = os.path.join(exe, "Scripts", "pip%d.exe" % major)
                tried.append(pi)
                if not os.path.exists(pi):
                    # Anaconda is different
                    pi = os.path.join(exe, "Scripts", "pip.exe")
                    tried.append(pi)
                    if not os.path.exists(pi):
                        pi = os.path.join(exe, "Scripts", "pip%d.exe" % major)
                        tried.append(pi)
                        if not os.path.exists(pi):
                            pi = os.path.join(
                                exe, "Scripts", "pip%d.%d.exe" % (major, minor))
                            tried.append(pi)
                            raise FileNotFoundError(
                                "tried (1):\n" + "\n".join(tried) + "\n---- try ---\npython -m pip install -U pip --force")
        else:
            pi = os.path.join(exe, "pip.exe")
            tried.append(pi)
            if not os.path.exists(pi):
                # Anaconda is different
                pi = os.path.join(exe, "pip.exe")
                tried.append(pi)
                if not os.path.exists(pi):
                    pi = os.path.join(exe, "pip%d.exe" % major)
                    tried.append(pi)
                    if not os.path.exists(pi):
                        pi = os.path.join(exe, "pip%d.%d.exe" % (major, minor))
                        tried.append(pi)
                        if not os.path.exists(pi):
                            raise FileNotFoundError(
                                "tried (2):\n" + "\n".join(tried) + "\n---- try ---\npython -m pip install -U pip --force")
    else:
        if sys.version_info[0] == 2:
            if exe is None:
                return "pip"
            else:
                pi = os.path.join(exe, "pip")
        else:
            major = sys.version_info[0]
            minor = sys.version_info[1]
            if exe is None:
                return "pip%d.%d" % (major, minor)
            else:
                # this does not work because on Linux, the binary is installed on the local path
                # pip3.4 are not in the same place
                # pi = os.path.join(exe, "pip%d.%d" % (major, minor))
                import pip
                exe = os.path.normpath(os.path.join(os.path.dirname(
                    pip.__file__), "..", "..", "..", "..", "bin"))
                pi = os.path.join(exe, "pip%d.%d" % (major, minor))
                if not os.path.exists(pi):
                    pi = os.path.join(exe, "pip")
                    if not os.path.exists(pi):
                        raise FileNotFoundError(
                            "unable to find pip: {0}\n__file__={1}\nexe={2}".format(pi, pip.__file__, exe))
    return pi


def get_python_program():
    """
    Returns the executable for :epkg:`python`.

    .. versionadded:: 1.1
    """
    pip = get_pip_program()
    dirname = os.path.dirname(pip)
    exe = os.path.join(
        dirname, "python.exe" if sys.platform.startswith("win") else "python")
    if os.path.exists(exe):
        return exe
    exe = os.path.normpath(os.path.join(
        dirname, "..", "python.exe" if sys.platform.startswith("win") else "python"))
    if os.path.exists(exe):
        return exe
    raise FileNotFoundError(exe)


def get_conda_program(exe=None):
    """
    Gets :epkg:`conda` executable and
    fixes an issue with :epkg:`Pandoc`.

    @param      exe             path to python executable
    @return                     conda executable
    """
    tried = []
    if exe is None:
        exe = os.path.dirname(sys.executable)
    if sys.platform.startswith("win"):
        if not exe.lower().endswith("scripts"):
            pi = os.path.join(exe, "Scripts", "conda.exe")
            tried.append(pi)
            if not os.path.exists(pi):
                # Anaconda is different
                pi = os.path.join(exe, "Scripts", "conda.exe")
                tried.append(pi)
                if not os.path.exists(pi):
                    raise FileNotFoundError(
                        "tried (1):\n" + "\n".join(tried))
        else:
            pi = os.path.join(exe, "conda.exe")
            tried.append(pi)
            if not os.path.exists(pi):
                # Anaconda is different
                pi = os.path.join(exe, "conda.exe")
                tried.append(pi)
                if not os.path.exists(pi):
                    raise FileNotFoundError(
                        "tried (2):\n" + "\n".join(tried))
    else:
        if exe is None:
            return "conda"
        else:
            pi = os.path.join(exe, "conda")

    return pi


def get_file_modification_date(filename):
    """
    Gets the date modification for a filename.

    @param      filename        filename
    @return                     datetime
    """
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def update_pip(python_path=None, fLOG=print):
    """
    Updates :epkg:`pip` for a specific distribution.

    @param      python_path     python path (or sys.executable if None)
    @param      fLOG            logging function
    @return                     output

    The command ``python -m pip install -U pip`` or
    ``pip install --upgrade pip`` might fail on Windows due to very long paths
    (see `Upgrading pip fails on Windows when install path is too long <https://github.com/pypa/pip/issues/3055>`_).
    If that happens,
    assuming the module *pymyinstall* was installed with pip, we can now remove
    *pip* and use *get_pip.py* instead. This part requires *pyquickhelper*.

    We try the url `bootstrap.pypa.io/get-pip.py <https://bootstrap.pypa.io/get-pip.py>`_ first
    then a local copy.
    """
    if python_path is None:
        python_path = sys.executable
    else:
        python_path = os.path.join(python_path, "python")
    cmd = python_path + " -m pip install -U pip"
    out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
    if err and len(err) > 0:
        if ("FileNotFoundError" in err or "No module named pip.__main__" in err) \
           and sys.platform.startswith("win"):
            from pyquickhelper.filehelper import remove_folder
            # we try to remove pip and to install it again
            # it might be due to long path on Windows
            pack = os.path.join(os.path.dirname(
                python_path), "Lib", "site-packages")
            if not os.path.exists(pack):
                raise FileNotFoundError(pack)
            fpip = os.path.join(pack, "pip")
            if os.path.exists(fpip):
                # remove the folder
                fLOG("  remove folder", fpip)
                remove_folder(fpip)

            pip_ = [_ for _ in os.listdir(pack) if _.startswith("pip-")]
            if len(pip_) > 0:
                for _ in pip_:
                    fp = os.path.join(pack, _)
                    fLOG("  remove folder", fp)
                    remove_folder(fpip)

            url = "https://bootstrap.pypa.io/get-pip.py"
            cmd = python_path + " " + url
            out, err = run_cmd(cmd, wait=True)
            if err and len(err) > 0:
                get_pip = os.path.abspath(os.path.join(
                    os.path.dirname(__file__), "get_pip.py"))
                if not os.path.exists(get_pip):
                    raise FileNotFoundError(get_pip)
                cmd = python_path + " " + get_pip
                out, err = run_cmd(cmd, wait=True)
                if err and len(err) > 0:
                    raise UpdatePipError(
                        "unable to update pip with get_pip.\nCMD:\n{0}\nOUT:\n{1}\nERR-E:\n{2}".format(cmd, out, err))
        else:
            lines = err.split("\n")
            keep = []
            for line in lines:
                if len(line.strip("\n\r\t ")) == 0:
                    continue
                if "Prompt dismissed.." in line:
                    continue
                if not line.startswith(" ") and "RuntimeWarning: Config variable" not in line and \
                    not(" which is incompatible." in line and " has requirement " in line) and \
                        not(" requires " in line and " which is not installed." in line) and \
                        not("Cache entry deserialization failed, entry ignored" in line) and \
                        len(line.strip()) > 3:
                    keep.append(line)
            if len(keep) > 0 and "Requirement already up-to-date" not in out:
                for _ in keep:
                    print("++", _)
                raise UpdatePipError(
                    "Unable to update pip.\nCMD:\n{0}\nOUT:\n{1}\nERR-F:"
                    "\n{2}\n---KEPT---\n{3}".format(cmd, out, err, "\n".join(keep)))
    return out


def has_pip():
    """
    Tells if :epkg:`pip` is installed.

    @return     boolean
    """
    try:
        import pip
        return pip is not None
    except ImportError:
        return False


def is_conda_distribution():
    """
    Tells if it is a :epkg:`conda` distribution or not,
    check the presence of ``Continuum Analytics``
    or ``|Anaconda`` in ``sys.version``.

    @return         boolean

    .. versionadded:: 1.1
    """
    return "Continuum Analytics" in sys.version or "|Anaconda" in sys.version


def run_cmd(cmd, sin="", shell=sys.platform.startswith("win"), wait=False, log_error=True,
            stop_running_if=None, encerror="ignore",
            encoding="utf8", change_path=None, communicate=True,
            preprocess=True, timeout=None, catch_exit=False, fLOG=None,
            tell_if_no_output=None, old_behavior=False):
    """
    Runs a command line and waits for the results,
    @see fn run_cmd_private.
    """
    if old_behavior or not sys.platform.startswith("win"):
        return run_cmd_old(
            cmd=cmd, sin=sin, shell=shell, wait=wait, log_error=log_error,
            secure=None, stop_waiting_if=stop_running_if, do_not_log=False,
            encerror=encerror, encoding=encoding, cwd=change_path, fLOG=fLOG)
    return run_cmd_private(
        cmd=cmd, sin=sin, shell=shell, wait=wait, log_error=log_error,
        stop_running_if=stop_running_if, encerror=encerror,
        encoding=encoding, change_path=change_path, communicate=communicate,
        preprocess=preprocess, timeout=timeout, catch_exit=catch_exit, fLOG=fLOG,
        tell_if_no_output=tell_if_no_output)
