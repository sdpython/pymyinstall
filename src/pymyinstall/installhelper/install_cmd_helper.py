"""
@file
@brief Various function to install various python module from various location.
"""
from __future__ import print_function

import sys
import platform
import os
import zipfile
import time
import subprocess
import datetime
import re
from .module_install_exceptions import UpdatePipError, RunCmdError

regex_wheel_version = "[-]([0-9]+[.][abc0-9]+([.][0-9abdevcr]+)?)([+]mkl)?([+]post[0-9]{1,2})?[-]"


def python_version():
    """
    retrieve the platform and version of this python

    @return     tuple, example: ("win32","32bit") or ("win32","64bit")
    """
    return sys.platform, platform.architecture()[0]


def split_cmp_command(cmd, remove_quotes=True):
    """

    splits a command line

    @param      cmd             command line
    @param      remove_quotes   True by default
    @return                     list

    """
    if isinstance(cmd, str):
        spl = cmd.split()
        res = []
        for s in spl:
            if len(res) == 0:
                res.append(s)
            elif res[-1].startswith('"') and not res[-1].endswith('"'):
                res[-1] += " " + s
            else:
                res.append(s)
        if remove_quotes:
            res = [_.strip('"') for _ in res]
        return res
    else:
        return cmd


def run_cmd(cmd,
            sin="",
            shell=False,
            wait=False,
            log_error=True,
            secure=None,
            stop_waiting_if=None,
            do_not_log=False,
            encerror="ignore",
            encoding="utf8",
            cwd=None,
            fLOG=print):
    """
    run a command line and wait for the result
    @param      cmd                 command line
    @param      sin                 sin, what must be written on the standard input
    @param      shell               if True, cmd is a shell command (and no command window is opened)
    @param      wait                call proc.wait
    @param      log_error           if log_error, call fLOG (error)
    @param      secure              if secure is a string (a valid filename), the function stores the output in a file
                                    and reads it continuously
    @param      stop_waiting_if     the function stops waiting if some condition is fulfilled.
                                    The function received the last line from the logs.
    @param      do_not_log          do not log the output
    @param      encerror            encoding errors (ignore by default) while converting the output into a string
    @param      encoding            encoding of the output
    @param      cwd                 current folder
    @param      fLOG                logging function
    @return                         content of stdout, stderr  (only if wait is True)


    @FAQ(Exception when installing a module)

    This error can occur when a module is installed on a virtual environment
    created before *pip* was updated on the main distribution.
    The solution consists in removing the virtual environment and create it again.

    ::

        c:\\Python34_x64vir\\install\\Scripts\\python -u setup.py install
        running install
        running bdist_egg
        running egg_info
        Traceback (most recent call last):
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2785, in _dep_map
            return self.__dep_map
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2642, in __getattr__
            raise AttributeError(attr)
        AttributeError: _DistInfoDistribution__dep_map

        During handling of the above exception, another exception occurred:

        Traceback (most recent call last):
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2776, in _parsed_pkg_info
            return self._pkg_info
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2642, in __getattr__
            raise AttributeError(attr)
        AttributeError: _pkg_info

        During handling of the above exception, another exception occurred:

        Traceback (most recent call last):
          File "setup.py", line 169, in <module>
            package_data=package_data,
          File "C:\\Python34_x64\\Lib\\distutils\\core.py", line 148, in setup
            dist.run_commands()
          File "C:\\Python34_x64\\Lib\\distutils\\dist.py", line 955, in run_commands
            self.run_command(cmd)
          File "C:\\Python34_x64\\Lib\\distutils\\dist.py", line 974, in run_command
            cmd_obj.run()
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\setuptools\\command\\install.py", line 67, in run
            self.do_egg_install()
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\setuptools\\command\\install.py", line 109, in do_egg_install
            self.run_command('bdist_egg')
          File "C:\\Python34_x64\\Lib\\distutils\\cmd.py", line 313, in run_command
            self.distribution.run_command(command)
          File "C:\\Python34_x64\\Lib\\distutils\\dist.py", line 974, in run_command
            cmd_obj.run()
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\setuptools\\command\\bdist_egg.py", line 151, in run
            self.run_command("egg_info")
          File "C:\\Python34_x64\\Lib\\distutils\\cmd.py", line 313, in run_command
            self.distribution.run_command(command)
          File "C:\\Python34_x64\\Lib\\distutils\\dist.py", line 974, in run_command
            cmd_obj.run()
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\setuptools\\command\\egg_info.py", line 171, in run
            ep.require(installer=installer)
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2355, in require
            items = working_set.resolve(reqs, env, installer)
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 835, in resolve
            new_requirements = dist.requires(req.extras)[::-1]
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2586, in requires
            dm = self._dep_map
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2787, in _dep_map
            self.__dep_map = self._compute_dependencies()
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2809, in _compute_dependencies
            for req in self._parsed_pkg_info.get_all('Requires-Dist') or []:
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2778, in _parsed_pkg_info
            metadata = self.get_metadata(self.PKG_INFO)
          File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 1993, in get_metadata
            raise KeyError("No metadata except PKG-INFO is available")
        KeyError: 'No metadata except PKG-INFO is available'

    @endFAQ
    """
    if sin is not None and sin != "":
        raise NotImplementedError("sin is not used")

    if secure is not None:
        if not do_not_log:
            fLOG("secure=", secure)
        with open(secure, "w") as f:
            f.write("")
        add = ">%s" % secure
        if isinstance(cmd, str):
            cmd += " " + add
        else:
            cmd.append(add)
    if not do_not_log:
        fLOG("execute ", cmd)

    if sys.platform.startswith("win"):

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        try:
            proc = subprocess.Popen(cmd,
                                    shell=shell,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    startupinfo=startupinfo,
                                    cwd=cwd)
        except FileNotFoundError as e:
            raise RunCmdError("unable to run CMD:\n{0}".format(cmd)) from e
    else:
        try:
            proc = subprocess.Popen(split_cmp_command(cmd),
                                    shell=shell,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    cwd=cwd)
        except FileNotFoundError as e:
            raise RunCmdError("unable to run CMD:\n{0}".format(cmd)) from e
    if wait:

        out = []
        skip_waiting = False

        if secure is None:
            for line in proc.stdout:
                if not do_not_log:
                    fLOG(line.decode(encoding, errors=encerror).strip("\n"))
                try:
                    out.append(
                        line.decode(
                            encoding,
                            errors=encerror).strip("\n"))
                except UnicodeDecodeError as exu:
                    raise RunCmdError(
                        "issue with cmd:" +
                        str(cmd) +
                        "\n" +
                        str(exu))
                if proc.stdout.closed:
                    break
                if stop_waiting_if is not None and stop_waiting_if(
                        line.decode("utf8", errors=encerror)):
                    skip_waiting = True
                    break
        else:
            last = []
            while proc.poll() is None:
                if os.path.exists(secure):
                    with open(secure, "r") as f:
                        lines = f.readlines()
                    if len(lines) > len(last):
                        for line in lines[len(last):]:
                            if not do_not_log:
                                fLOG(line.strip("\n"))
                            out.append(line.strip("\n"))
                        last = lines
                    if stop_waiting_if is not None and len(
                            last) > 0 and stop_waiting_if(last[-1]):
                        skip_waiting = True
                        break
                time.sleep(0.1)

        if not skip_waiting:
            proc.wait()

        out = "\n".join(out)
        err = proc.stderr.read().decode(encoding, errors=encerror)
        if not do_not_log:
            fLOG("end of execution ", cmd)
        if len(err) > 0 and log_error and not do_not_log:
            fLOG("error (log)\n%s" % err)
        # return bytes.decode (out, errors="ignore"), bytes.decode(err,
        # errors="ignore")
        proc.stdout.close()
        proc.stderr.close()

        return out, err
    else:
        return "", ""


def unzip_files(zipf, whereTo, fLOG=print):
    """
    unzip files from a zip archive

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
                        fLOG("    unzipped ", info.filename, " to ", tos)
                elif not tos.endswith("/"):
                    files.append(tos)
            elif not info.filename.endswith("/"):
                files.append(info.filename)
    return files


def add_shortcut_to_desktop_for_module(name):
    """
    add a shortcut on a module which includes a script

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
    get pip executable + fix an issue with PANDOC

    @param      exe             path to python executable
    @param      pandoc_path     if None, call @see fn find_pandoc_path
    @return                     pip executable

    @FAQ(How can I check the dependencies?)

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
        dateutils==0.6.6
          - argparse
          - python-dateutil [installed: 2.4.2]
            - six [required: >=1.5, installed: 1.9.0]
          - pytz [installed: 2015.4]
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

    @endFAQ
    """
    tried = []
    if exe is None:
        exe = os.path.dirname(sys.executable)
    if sys.platform.startswith("win"):
        if not exe.endswith("Scripts"):
            pi = os.path.join(exe, "Scripts", "pip.exe")
            tried.append(pi)
            if not os.path.exists(pi):
                pi = os.path.join(exe, "Scripts", "pip3.exe")
                tried.append(pi)
                if not os.path.exists(pi):
                    # Anaconda is different
                    pi = os.path.join(exe, "Scripts", "pip.exe")
                    tried.append(pi)
                    if not os.path.exists(pi):
                        pi = os.path.join(exe, "Scripts", "pip3.exe")
                        tried.append(pi)
                        if not os.path.exists(pi):
                            pi = os.path.join(exe, "Scripts", "pip3.4.exe")
                            tried.append(pi)
                            if not os.path.exists(pi):
                                raise FileNotFoundError(
                                    "tried (1):\n" + "\n".join(tried))
        else:
            pi = os.path.join(exe, "pip.exe")
            tried.append(pi)
            if not os.path.exists(pi):
                # Anaconda is different
                pi = os.path.join(exe, "pip.exe")
                tried.append(pi)
                if not os.path.exists(pi):
                    pi = os.path.join(exe, "pip3.exe")
                    tried.append(pi)
                    if not os.path.exists(pi):
                        pi = os.path.join(exe, "pip3.4.exe")
                        tried.append(pi)
                        if not os.path.exists(pi):
                            raise FileNotFoundError(
                                "tried (2):\n" + "\n".join(tried))
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

    return pi


def get_conda_program(exe=None):
    """
    get conda executable + fix an issue with PANDOC

    @param      exe             path to python executable
    @param      pandoc_path     if None, call @see fn find_pandoc_path
    @return                     conda executable
    """
    tried = []
    if exe is None:
        exe = os.path.dirname(sys.executable)
    if sys.platform.startswith("win"):
        if not exe.endswith("Scripts"):
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
    get the date modification for a time

    @param      filename        filename
    @return                     datetime
    """
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def update_pip(python_path=None, fLOG=print):
    """
    update pip for a specific distribution

    @param      python_path     python path (or sys.executable if None)
    @param      fLOG            logging function
    @return                     output

    The command ``python -m pip install -U pip`` or
    ``pip install --upgrade pip`` might fails on Windows due to very long paths
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
                        "unable to update pip with get_pip.\nCMD:\n{0}\nOUT:\n{1}\nERR:\n{2}".format(cmd, out, err))
        else:
            raise UpdatePipError(
                "unable to update pip.\nCMD:\n{0}\nOUT:\n{1}\nERR:\n{2}".format(cmd, out, err))
    return out


def has_pip():
    """
    tells if pip is installed

    @return     boolean
    """
    try:
        import pip
        return pip is not None
    except ImportError:
        return False


def get_wheel_version(whlname):
    """
    extract the version from a wheel file,
    return ``2.6.0`` for ``rpy2-2.6.0-cp34-none-win_amd64.whl``

    @param      whlname     file name
    @return                 string
    """
    exp = re.compile(regex_wheel_version)
    find = exp.findall(whlname)
    if len(find) == 0:
        raise ValueError(
            "[get_wheel_version] unable to extract version of {0} (pattern: {1})".format(whlname, exp.pattern))
    if len(find) > 1:
        raise ValueError(
            "[get_wheel_version] unable to extract version of {0} (multiple version) (pattern: {1})".format(whlname, exp.pattern))
    return find[0][0]
