"""
@file
@brief Various function to install various python module from various location.
"""
from __future__ import print_function

import sys
import re
import platform
import os
import time
import importlib
import datetime
from .install_cmd_helper import python_version, run_cmd, unzip_files, get_pip_program, get_file_modification_date
from .install_memoize import install_memoize

if sys.version_info[0] == 2:
    import urllib2 as urllib_request
    import urllib2 as urllib_error
else:
    import urllib.request as urllib_request
    import urllib.error as urllib_error
    import importlib.util


@install_memoize
def get_page_wheel(page):
    """
    get the page

    @param      page        location
    @return                 page content
    """
    req = urllib_request.Request(
        page,
        headers={
            'User-agent': 'Mozilla/5.0'})
    u = urllib_request.urlopen(req)
    text = u.read()
    u.close()
    text = text.decode("utf8")
    text = text.replace("&quot;", "'")
    text = text.replace("&#8209;", "-")
    return text


class ModuleInstall:

    """
    defines the necessary information for a module

    @example(Installation from GitHub)
    @code
    ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")
    @endcode
    @endexample
    """

    allowedKind = ["pip", "github", "exe", "exe_xd", "wheel"]
    expKPage = "onclick=.javascript:dl[(]([,\\[\\]0-9]+) *, *.([0-9&;@?=:A-Zgtl]+).[)]. title(.+)?.>(.+?win32-py3.3.exe)</a>"
    expKPageWhl = "onclick=.javascript:dl[(]([,\\[\\]0-9]+) *, *.([0-9&;@?=:A-Zgtl]+).[)]. title(.+)?.>(.+?-cp33-none-win32.whl)</a>"
    exeLocation = "http://www.lfd.uci.edu/~gohlke/pythonlibs/"
    exeLocationXd = "http://www.xavierdupre.fr/enseignement/setup/"
    gitexe = r"C:\Program Files (x86)\Git"

    def __init__(self, name,
                 kind="pip",
                 gitrepo=None,
                 mname=None,
                 fLOG=print,
                 version=None,
                 script=None):
        """
        constructor

        @param      name            name
        @param      kind            kind of installation (*pip*, *github*, *exe*, *wheel*)
        @param      gitrepo         github repository (example: sdpython)
        @param      mname           sometimes, the module name is different from its official name
        @param      version         to install a specific version (None for the latest)
        @param      fLOG            logging function
        @param      script          some extensions are not a module but an application (such as ``spyder``),
                                    the class will check this script is available

        exe is only for Windows.
        """
        if kind != "pip" and version is not None:
            raise NotImplementedError(
                "version can be only specified if kind=='pip'")

        self.name = name
        self.kind = kind
        self.gitrepo = gitrepo
        self.version = version
        self.mname = mname
        self.script = script

        if self.kind not in ModuleInstall.allowedKind:
            raise Exception(
                "unable to interpret kind {0}, it should be in {1}".format(
                    kind, ",".join(
                        ModuleInstall.allowedKind)))
        if self.kind == "github" and self.gitrepo is None:
            raise Exception("gitrepo cannot be empty")

        self.fLOG = fLOG

    @staticmethod
    def clear_cache():
        """
        clear the local cache to get wheel link
        """
        if os.path.exists(ModuleInstall._page_cache_html):
            os.remove(ModuleInstall._page_cache_html)

    @property
    def Script(self):
        """
        returns the script to run if the extension is an application and not a module
        """
        exe = os.path.split(sys.executable)[0]
        if sys.platform.startswith("win"):
            sc = os.path.join(exe, "Scripts", self.script)
        else:
            sc = os.path.join(exe, "Scripts", os.path.splitext(self.script)[0])
        return sc

    def __str__(self):
        """
        usual
        """
        if self.script is None:
            return "{0}:{1}:import {2}:v{3}".format(
                self.name, self.kind, self.ImportName, self.version)
        else:
            return "{0}:{1}:{2}:v{3}".format(self.name, self.kind, self.Script, self.version)

    @property
    def ImportName(self):
        """
        return the import name
        """
        if self.mname is not None:
            return self.mname
        if self.name.startswith("python-"):
            return self.name[len("python-"):]
        else:
            return self.name

    def IsInstalled(self):
        """
        checks if a module is installed
        """
        if self.script is None:
            try:
                if "." in self.ImportName:
                    raise ImportError(self.ImportName)
                if sys.version_info[0] == 2:
                    r = importlib.import_module(self.ImportName)
                    return r
                else:
                    r = importlib.util.find_spec(self.ImportName)
                    return r is not None
                return r is not None
            except ImportError:
                txt = "import {0}".format(self.ImportName)
                try:
                    exec(txt)
                    return True
                except Exception:
                    return False
        else:
            return os.path.exists(self.Script)

    def get_exewheel_url_link_xd(self, file_save=None, wheel=False):
        """
        for windows, get the url of the setup using a webpage

        @param      file_save   for debug purposes
        @param      wheel       returns the wheel file or the exe file
        @return                 url, exe name
        """
        ext = "exe" if not wheel else "whl"
        if self.name == "pycrypto":
            p = platform.architecture()[0]
            vers = "{0}.{1}".format(*(sys.version_info[:2]))
            if p == "64bit":
                p = "win-amd64"
            else:
                p = "win32"
            exe = "pycrypto-2.6.1.{0}-py{1}.{2}".format(p, vers, ext)
            url = "{0}/{1}".format(ModuleInstall.exeLocationXd, exe)
            return url, exe
        else:
            raise ImportError(
                "unable to get this module {0} from this location {1}".format(
                    self.name,
                    "exe_xd or wheel_xd"))

    _page_cache_html = os.path.join(
        os.path.abspath(os.path.split(__file__)[0]), "page.html")

    def get_exewheel_url_link(self, file_save=None, wheel=False):
        """
        for windows, get the url of the setup using a webpage

        @param      file_save   for debug purposes
        @param      wheel       returns the wheel file or the exe file
        @return                 url, exe name
        """
        version = python_version()
        plat = version[0] if version[0] == "win32" else version[1]
        if version[1] == '64bit' and version[0] == 'win32':
            plat = "amd64"

        if wheel:
            plat = "32" if plat == "win32" else "_amd64"
            pattern = ModuleInstall.expKPageWhl.replace("-cp33-none-win32.whl",
                                                        "-((cp{1}{2})|(py3)|(py2[.]py3)|(py33[.]py34))-none-((win{0})|(any)).whl".format(plat, sys.version_info.major, sys.version_info.minor))
            ind = 3
        else:
            pattern = ModuleInstall.expKPage.replace("win32-py3.3.exe",
                                                     "{0}-py{1}.{2}.exe".format(plat, sys.version_info.major, sys.version_info.minor))
            ind = -1
        expre = re.compile(pattern)

        if "cached_page" not in self.__dict__:
            page = ModuleInstall._page_cache_html

            exi = os.path.exists(page)
            if exi:
                dt = get_file_modification_date(page)
                now = datetime.datetime.now()
                df = now - dt
                if df > datetime.timedelta(7):
                    exi = False

            if exi:
                with open(page, "r", encoding="utf8") as f:
                    text = f.read()
                self.cached_page = text
            else:
                text = get_page_wheel(ModuleInstall.exeLocation)
                with open(page, "w", encoding="utf8") as f:
                    f.write(text)
                self.cached_page = text

        page = self.cached_page
        alls = expre.findall(page)
        if len(alls) == 0:
            keep = []
            for line in page.split("\n"):
                if "networkx" in line:
                    keep.append(line)
            raise Exception(
                "module " +
                self.name +
                ", unable to find regex with pattern: " +
                pattern + "\nexample:\n" + "\n".join(keep))

        if ind == -1:
            ind = len(alls[0]) - 1
        end = ind + 1
        memoalls = alls

        if self.name == "PyQt":
            alls = [_[:end]
                    for _ in alls if _[ind].startswith(self.name + "4")]
        elif self.name == "numpy":
            white = self.name.replace("-", "_")
            alls = [_[:end] for _ in alls if "unoptimized" not in _[ind] and
                    (_[ind].startswith(self.name + "-") or _[ind].startswith(white + "-"))]
        else:
            white = self.name.replace("-", "_")
            alls = [_[:end] for _ in alls if _[ind].startswith(
                self.name + "-") or _[ind].startswith(white + "-")]

        if len(alls) == 0:
            if file_save is not None:
                with open(file_save, "w", encoding="utf8") as f:
                    f.write(page)
            raise Exception("unable to find a single link for " +
                            self.name +
                            "\npattern:" +
                            pattern +
                            "\nEX:\n" +
                            str(memoalls[0]))
        link = alls[-1]

        # def dc(ml,mi):
        #        ot=""
        #        for j in range(0,len(mi)) :
        #            ot+= chr(ml[ord(mi[j])-48])
        #        return ot
        def dl1(ml, mi):
            ot = ""
            for j in range(0, len(mi)):
                ot += chr(ml[ord(mi[j]) - 48])
            return ot

        def dl(ml, mi):
            mi = mi.replace('&lt;', '<')
            mi = mi.replace('&gt;', '>')
            mi = mi.replace('&amp;', '&')
            return dl1(ml, mi)

        url = dl(eval(link[0]), link[1])
        return ModuleInstall.exeLocation + url, link[-1]

    def unzipfiles(self, zipf, whereTo):
        """
        unzip files from a zip archive

        @param      zipf        archive
        @param      whereTo     destination folder
        @return                 list of unzipped files
        """
        return unzip_files(zipf, whereTo, self.fLOG)

    def download(
            self, temp_folder=".", force=False, unzipFile=True, file_save=None, deps=False):
        """
        download the module without installation

        @param      temp_folder     destination
        @param      force           force the installation even if already installed
        @param      unzipFile       if it can be unzipped, it will be (for github, mostly)
        @param      file_save       for debug purposes, do not change it unless you know what you are doing
        @param      deps            download the dependencies too (only available for pip)
        @return                     downloaded files

        .. versionchanged:: 0.9
            Parameter *deps* was added, the function now downloads a module using pip.
        """
        kind = self.kind

        if kind == "pip":
            # see https://pip.pypa.io/en/latest/reference/pip_install.html
            # we use pip install <package> --download=temp_folder
            pip = get_pip_program()
            cmd = pip + ' install {0}'.format(self.name)
            if self.version is not None:
                cmd += "=={0}".format(self.version)
            if " " in temp_folder:
                raise FileNotFoundError(
                    "no space allowed in folders: [" + temp_folder + "]")
            if deps:
                cmd += ' --download={0}'.format(temp_folder)
            else:
                cmd += ' --download={0} --no-deps'.format(temp_folder)

            out, err = run_cmd(
                cmd, wait=True, do_not_log=True, fLOG=self.fLOG)
            if "Successfully downloaded" not in out:
                raise Exception(
                    "unable to download " +
                    str(self) +
                    "\nCMD:\n" +
                    cmd +
                    "\nOUT:\n" +
                    out +
                    "\nERR:\n" +
                    err)
            else:
                lines = out.split("\n")
                for line in lines:
                    if line.strip().startswith("Saved "):
                        return line.split("Saved")[-1].strip()
                    elif line.strip().startswith("File was already downloaded"):
                        return line.split("File was already downloaded")[-1].strip()
                raise Exception(
                    "unable to find downloaded file " +
                    str(self) +
                    "\nCMD:\n" +
                    cmd +
                    "\nOUT:\n" +
                    out +
                    "\nERR:\n" +
                    err)

        elif kind == "wheel":
            ver = python_version()
            if ver[0] != "win32":
                # nothing to download, you should use pip
                return None
            else:
                url, whl = self.get_exewheel_url_link(
                    file_save=file_save, wheel=True)
                whlname = os.path.join(temp_folder, whl)

                exi = os.path.exists(whlname)
                if force or not exi:

                    self.fLOG("downloading", whl)
                    req = urllib_request.Request(
                        url, headers={
                            'User-agent': 'Mozilla/5.0'})
                    u = urllib_request.urlopen(req)
                    text = u.read()
                    u.close()

                    if not os.path.exists(temp_folder):
                        os.makedirs(temp_folder)

                    self.fLOG("writing", whl)
                    with open(whlname, "wb") as f:
                        f.write(text)

                return whlname

        elif kind == "github":
            outfile = os.path.join(temp_folder, self.name + ".zip")
            if force or not os.path.exists(outfile):
                zipurl = "https://github.com/{1}/{0}/archive/master.zip".format(
                    self.name,
                    self.gitrepo)
                self.fLOG("downloading", zipurl)
                try:
                    req = urllib_request.Request(
                        zipurl, headers={
                            'User-agent': 'Mozilla/5.0'})
                    u = urllib_request.urlopen(req)
                    text = u.read()
                    u.close()
                except urllib_error.HTTPError as e:
                    raise Exception(
                        "unable to get archive from: " +
                        zipurl) from e

                if not os.path.exists(temp_folder):
                    os.makedirs(temp_folder)
                u = open(outfile, "wb")
                u.write(text)
                u.close()

            if unzipFile:
                self.fLOG("unzipping ", outfile)
                files = self.unzipfiles(outfile, temp_folder)
                return files
            else:
                return outfile

        elif kind in ["exe", "exe_xd"]:
            ver = python_version()
            if ver[0] != "win32":
                raise Exception(
                    "this option is not available on other systems than Windows, version={0}".format(ver))
            else:
                url, exe = self.get_exewheel_url_link(
                    file_save=file_save) if kind == "exe" else self.get_exewheel_url_link_xd(
                    file_save=file_save)

                self.fLOG("downloading", exe)
                req = urllib_request.Request(
                    url, headers={
                        'User-agent': 'Mozilla/5.0'})
                u = urllib_request.urlopen(req)
                text = u.read()
                u.close()

                if not os.path.exists(temp_folder):
                    os.makedirs(temp_folder)

                exename = os.path.join(temp_folder, exe)
                self.fLOG("writing", exe)
                with open(exename, "wb") as f:
                    f.write(text)
                return exename

        else:
            raise ImportError(
                "unknown kind: {0} for module {1}".format(
                    kind,
                    self.name))

    def Install(self, *l, **p):
        """
        @see me install
        """
        self.install(*l, **p)

    def install(self,
                force_kind=None,
                force=False,
                temp_folder=".",
                log=False,
                *options):
        """
        install the package

        @param      force_kind      overwrite self.kind
        @param      force           force the installation even if already installed
        @param      temp_folder     folder where to download the setup
        @param      log             display logs or not
        @param      options         other options to add to the command line (see below)
        @return                     boolean

        The options mentioned in parameter ``options``
        are described here: `pip install <http://www.pip-installer.org/en/latest/usage.html>`_
        or `setup.py options <http://docs.python.org/3.4/install/>`_ if you
        installing a module from github.
        """

        if not force and self.IsInstalled():
            return True

        self.fLOG("installation of ", self)
        kind = force_kind if force_kind is not None else self.kind
        ret = None

        if kind == "pip":
            if sys.platform.startswith("win"):
                pip = os.path.join(
                    os.path.split(
                        sys.executable)[0],
                    "Scripts",
                    "pip.exe")
            else:
                pip = os.path.join(
                    os.path.split(
                        sys.executable)[0],
                    "pip")
            cmd = pip + " install {0}".format(self.name)
            if self.version is not None:
                cmd += "=={0}".format(self.version)
            if len(options) > 0:
                cmd += " " + " ".join(*options)
            out, err = run_cmd(
                cmd, wait=True, do_not_log=not log, fLOG=self.fLOG)
            if "No distributions matching the version" in out:
                raise Exception(
                    "unable to install " +
                    str(self) +
                    "\nOUT:\n" +
                    out +
                    "\nERR:\n" +
                    err)
            elif "Testing of typecheck-decorator passed without failure." in out:
                ret = True
            elif "Successfully installed" not in out:
                if "error: Unable to find vcvarsall.bat" in out:
                    url = "http://www.xavierdupre.fr/blog/2013-07-07_nojs.html"
                    raise Exception(
                        "unable to install " +
                        str(self) +
                        "\nread:\n" +
                        url +
                        "OUT:\n" +
                        out +
                        "\nERR:\n" +
                        err)
                if "Requirement already satisfied" not in out:
                    raise Exception(
                        "unable to install " +
                        str(self) +
                        "\nOUT:\n" +
                        out +
                        "\nERR:\n" +
                        err)
            else:
                ret = True

        elif kind == "wheel":
            ver = python_version()
            if ver[0] != "win32":
                ret = self.install("wheel")
                whlname = self.name
            else:
                whlname = self.download(
                    temp_folder=temp_folder,
                    force=force,
                    unzipFile=True)
                self.fLOG("installing", os.path.split(whlname)[-1])

            if sys.platform.startswith("win"):
                pip = os.path.join(
                    os.path.split(
                        sys.executable)[0],
                    "Scripts",
                    "pip.exe")
            else:
                pip = os.path.join(
                    os.path.split(
                        sys.executable)[0],
                    "pip")
            cmd = pip + " install {0}".format(whlname)
            if self.version is not None:
                cmd += "=={0}".format(self.version)
            if len(options) > 0:
                cmd += " " + " ".join(*options)
            out, err = run_cmd(
                cmd, wait=True, do_not_log=not log, fLOG=self.fLOG)
            if "No distributions matching the version" in out:
                raise Exception(
                    "unable to install " +
                    str(self) +
                    "\nOUT:\n" +
                    out +
                    "\nERR:\n" +
                    err)
            elif "Testing of typecheck-decorator passed without failure." in out:
                ret = True
            elif "Successfully installed" not in out:
                if "error: Unable to find vcvarsall.bat" in out:
                    url = "http://www.xavierdupre.fr/blog/2013-07-07_nojs.html"
                    raise Exception(
                        "unable to install " +
                        str(self) +
                        "\nread:\n" +
                        url +
                        "OUT:\n" +
                        out +
                        "\nERR:\n" +
                        err)
                if "Requirement already satisfied" not in out:
                    raise Exception(
                        "unable to install " +
                        str(self) +
                        "\nOUT:\n" +
                        out +
                        "\nERR:\n" +
                        err)
            else:
                ret = True

        elif kind == "github":
            # the following code requires admin rights
            # if python_version()[0].startswith("win") and kind == "git" and not os.path.exists(ModuleInstall.gitexe) :
            #    raise FileNotFoundError("you need to install github first: see http://windows.github.com/")
            # if python_version()[0].startswith("win"):
            #    os.chdir(os.path.join(ModuleInstall.gitexe,"bin"))
            # cmd = pip + " install -e
            # git://github.com/{0}/{1}-python.git#egg={1}".format(self.gitrepo,
            # self.name)

            files = self.download(
                temp_folder=temp_folder,
                force=force,
                unzipFile=True)
            setu = [_ for _ in files if _.endswith("setup.py")]
            if len(setu) == 0:
                raise Exception(
                    "unable to find setup.py for module " +
                    self.name)
            elif len(setu) > 1:
                setu = [(len(_), _) for _ in setu]
                setu.sort()
                if setu[0][0] == setu[1][0]:
                    raise Exception(
                        "more than one setup.py for module " +
                        self.name +
                        "\n" +
                        "\n".join(
                            str(_) for _ in setu))
                else:
                    self.fLOG("warning: more than one setup: " + str(setu))
                    setu = [setu[0][1]]
            setu = os.path.abspath(setu[0])

            self.fLOG("install ", setu[0])
            cwd = os.getcwd()
            os.chdir(os.path.split(setu)[0])
            cmd = "{0} setup.py install".format(
                sys.executable.replace(
                    "pythonw.exe",
                    "python.exe"))
            if len(options) > 0:
                cmd += " " + " ".join(*options)
            out, err = run_cmd(
                cmd, wait=True, do_not_log=not log, fLOG=self.fLOG)
            os.chdir(cwd)
            if "Successfully installed" not in out and "install  C" not in out:
                if "Finished processing dependencies" not in out:
                    raise Exception(
                        "unable to install " +
                        str(self) +
                        "\nOUT:\n" +
                        out +
                        "\nERR:\n" +
                        err)
                else:
                    self.fLOG(
                        "warning: ``Successfully installed`` or ``install  C`` not found")
                if "Permission denied" in out:
                    raise PermissionError(
                        "unable to install " +
                        str(self) +
                        "\nOUT:\n" +
                        out +
                        "\nERR:\n" +
                        err)
            ret = True

        elif kind == "exe":
            ver = python_version()
            if ver[0] != "win32":
                ret = self.install("pip")
            else:
                exename = self.download(
                    temp_folder=temp_folder,
                    force=force,
                    unzipFile=True)
                self.fLOG("executing", os.path.split(exename)[-1])
                out, err = run_cmd(
                    exename + " /s /qn /SILENT", wait=True, do_not_log=not log, fLOG=self.fLOG)
                ret = len(err) == 0

        elif kind == "exe_xd":
            ver = python_version()
            if ver[0] != "win32":
                ret = self.install("pip")
            else:
                exename = self.download(
                    temp_folder=temp_folder,
                    force=force,
                    unzipFile=True)
                self.fLOG("executing", os.path.split(exename)[-1])
                out, err = run_cmd(
                    exename + " /s /qn", wait=True, do_not_log=not log, fLOG=self.fLOG)
                ret = len(err) == 0
        else:
            raise ImportError(
                "unknown kind: {0} for module {1}".format(
                    kind,
                    self.name))

        # at this stage, there is a bug, for some executable, the execution
        # takes longer than expected
        # if not self.IsInstalled() :
        #    raise Exception("unable to install module: {0}, str:{1}".format(self.name, self))

        if ret is not None and ret and self.script is not None:
            if sys.platform.startswith("win"):
                # here, we have to wait until the script is installed
                ti = 0
                while not self.IsInstalled():
                    time.sleep(0.5)
                    ti += 0.5
                    if ti > 60:
                        self.fLOG(
                            "wait for the end of execution of ",
                            self.name)
                    ti = 0

                # we add set path=%path%;PYTHONPATH
                with open(self.Script, "r") as f:
                    full = f.read()

                exe = os.path.split(sys.executable)[0]
                cmd = "set path=%path%;{0}".format(exe)
                if cmd not in full:
                    self.fLOG("add {0} to {1}".format(cmd, self.Script))
                    with open(self.Script, "w") as f:
                        if full.startswith("@echo off"):
                            f.write(
                                full.replace(
                                    "@echo off",
                                    "@echo off\n{0}".format(cmd)))
                        else:
                            f.write(cmd)
                            f.write("\n")
                            f.write(full)

        return ret
