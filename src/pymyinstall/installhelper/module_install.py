"""
@file
@brief Various function to install various python module from various location.
"""
from __future__ import print_function
from .install_cmd_helper import python_version, run_cmd, unzip_files, get_pip_program
from .install_cmd_helper import get_python_program, get_file_modification_date, get_conda_program, is_conda_distribution
from .module_install_exceptions import MissingPackageOnPyPiException, MissingInstalledPackageException, InstallError
from .module_install_exceptions import DownloadError, MissingVersionWheelException, WrongWheelException, MissingWheelException
from .module_install_version import get_pypi_version, get_module_version, annoying_modules, get_module_metadata
from .module_install_version import numeric_version, compare_version, choose_most_recent, get_wheel_version
from .module_install_page_wheel import get_page_wheel, read_page_wheel, save_page_wheel, enumerate_links_module, extract_all_links
from .missing_license import missing_module_licenses
from .internet_settings import default_user_agent
from .install_cmd_regex import regex_wheel_version, regex_wheel_version2, regex_wheel_version5

import sys
import re
import os
import time
import importlib
import datetime
import warnings

if sys.version_info[0] == 2:
    from urlparse import urlsplit
    import urllib2 as urllib_request
    import urllib2 as urllib_error
    import xmlrpclib as xmlrpc_client
    from codecs import open
    FileNotFoundError = Exception
    PermissionError = Exception
else:
    from urllib.parse import urlsplit
    import urllib.request as urllib_request
    import urllib.error as urllib_error
    import importlib.util
    import xmlrpc.client as xmlrpc_client


class ModuleInstall:

    """
    defines the necessary information for a module

    .. exref::
        :title: Installation from GitHub

        ::

            ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")
    """

    allowedKind = ["pip", "github", "exe", "exe2", "wheel", "wheel2"]
    exeLocation = "http://www.lfd.uci.edu/~gohlke/pythonlibs/"
    exeLocationXd_Default = "http://www.xavierdupre.fr/enseignement/setup/"
    gitexe = r"C:\Program Files (x86)\Git"

    @staticmethod
    def is_annoying(module_name):
        """
        some modules are not available on pipy
        """
        return module_name in annoying_modules

    def __init__(self, name, kind="pip", gitrepo=None, mname=None, fLOG=print,
                 version=None, script=None, index_url=None, deps=None,
                 purpose=None, usage=None, web=None, source=None, custom=None,
                 branch="master", pip_options=None, overwrite=None, post=None):
        """
        constructor

        @param      name            name
        @param      kind            kind of installation (*pip*, *github*, *wheel*)
        @param      gitrepo         github repository (example: sdpython)
        @param      mname           sometimes, the module name is different from its official name
        @param      version         to install a specific version (None for the latest)
        @param      fLOG            logging function
        @param      script          some extensions are not a module but an application (such as ``spyder``),
                                    the class will check this script is available
        @param      deps            overwrite deps parameters when installing the module
        @param      index_url       to get the package from a custom pypi server
        @param      purpose         purpose of the module
        @param      usage           main usage for the module
        @param      web             website for the module, if None, default to pipy
        @param      source          to overwrite parameter *source* of methods
                                    @see me download, @see me install or @see me update.
        @param      custom          custom instructions to install, usually
                                    ``['build', 'install']`` to run
                                    ``setup.py build`` and ``setup.py install``
        @param      branch          only necessary for install process with github
        @param      pip_options     additional options for pip (list)
        @param      overwrite       overwrite the location of the wheel
        @param      post            instructions post installation (look for this parameter
                                    in the code to see what is supported)

        .. versionchanged:: 1.1
            Parameters *source*, *custom*, *branch*, *pip_options*, *overwrite*, *post* were added.
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
        self.index_url = index_url
        self.deps = deps
        self.purpose = purpose
        self.usage = usage
        self.existing_version = None
        self.source = source
        self.custom = custom
        self.branch = branch
        self.pip_options = pip_options
        self.overwrite = overwrite
        self.post_installation = post
        self.web = web if web is not None else (
            "https://pypi.python.org/pypi/" + self.name)

        if self.kind not in ModuleInstall.allowedKind:
            raise Exception(
                "unable to interpret kind {0}, it should be in {1}".format(
                    kind, ",".join(
                        ModuleInstall.allowedKind)))
        if self.kind == "github" and self.gitrepo is None:
            raise Exception("gitrepo cannot be empty")

        self.fLOG = fLOG

    def copy(self, version=None):
        """
        copy the module, if version is not None, change the version number

        @param      version     version number or None for unchanged
        @return                 @see cl ModuleInstall

        .. versionadded:: 1.0
        """
        mod = ModuleInstall(**self.as_dict())
        if version is not None:
            mod.version = version
        return mod

    def as_dict(self, rst_link=False):
        """
        returns the members in a dictionary

        @param      rst_link    if True, add rst_link, license, classifier
        @return                 dictionary
        """
        r = dict(name=self.name, kind=self.kind, gitrepo=self.gitrepo, version=self.version,
                 mname=self.mname, script=self.script, deps=self.deps, index_url=self.index_url,
                 purpose=self.purpose, usage=self.usage, web=self.web,
                 post=None if self.post_installation is None else self.post_installation.copy())
        if rst_link:
            r["rst_link"] = "`{0} <{1}>`_".format(self.name, self.web)
            r["license"] = self.get_installed_license()
            r["installed"] = self.get_installed_version()
            r["classifier"] = self.get_installed_classifier()
        return r

    def __cmp__(self, o):
        """
        to sort modules

        @param      o       other module
        @return             -1, 0, 1
        """
        def compare(v1, v2):
            if v1 is None:
                if v2 is None:
                    return 0
                else:
                    return 1
            else:
                if v2 is None:
                    return -1
                else:
                    if v1 < v2:
                        return -1
                    elif v1 > v2:
                        return 1
                    else:
                        return 0

        r = compare(self.usage, o.usage)
        if r != 0:
            return r
        r = compare(self.name.lower(), o.name.lower())
        return r

    def __lt__(self, o):
        """
        overload operator ``<``

        @param      o       other module
        @return             boolean
        """
        return self.__cmp__(o) < 0

    @staticmethod
    def clear_cache():
        """
        clear the local cache to get wheel link
        """
        if os.path.exists(ModuleInstall._page_cache_html):
            os.remove(ModuleInstall._page_cache_html)
        if os.path.exists(ModuleInstall._page_cache_html2):
            os.remove(ModuleInstall._page_cache_html2)

    @property
    def Purpose(self):
        """
        returns the comment
        """
        return "-" if self.purpose is None else self.purpose

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

    def is_installed_local(self):
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

    def is_installed_local_cmd(self):
        """
        Test the module by running a command line.
        Does some others verifications for a specific modules such as scipy.

        .. versionadded:: 1.1
        """
        exe = get_python_program()
        cmd = exe + ' -u -c "import {0}"'.format(self.ImportName)
        out, err = run_cmd(cmd, fLOG=self.fLOG)
        if err:
            raise InstallError("cannot import module {0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
                self.ImportName, cmd, out, err))
        if self.name == "scipy":
            cmd = exe + '-u -c "import scipy.sparse"'
            out, err = run_cmd(cmd, fLOG=self.fLOG)
            if err:
                if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 5) and "DLL" in err:
                    mes = "scipy.sparse is failing, you should check that Visual Studio 2015 is installed\n{0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}"
                    raise InstallError(mes.format(
                        self.ImportName, cmd, out, err))
                else:
                    raise InstallError("scipy.sparse is failing\n{0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
                        self.ImportName, cmd, out, err))
        return True

    _page_cache_html2 = os.path.join(
        os.path.abspath(os.path.split(__file__)[0]), "page2.html")

    def get_exewheel_url_link2(self, file_save=None, wheel=False, source=None):
        """
        for windows, get the url of the setup using a webpage

        @param      file_save   for debug purposes
        @param      wheel       returns the wheel file or the exe file
        @param      source      source of the wheels (ex: ``2`` or ``http://...``)
        @return                 url, exe name

        .. versionchanged:: 1.1
            Parameter *source* was added.
        """
        if source is None or source == "2":
            source = ModuleInstall.exeLocationXd_Default
        source_page = source.rstrip("/") + "/index_modules_list.html"

        if "cached_page2" not in self.__dict__:
            page = ModuleInstall._page_cache_html2

            exi = os.path.exists(page)
            if exi:
                dt = get_file_modification_date(page)
                now = datetime.datetime.now()
                df = now - dt
                if df > datetime.timedelta(1):
                    exi = False

            if exi:
                text = read_page_wheel(page)
                self.cached_page2 = text
            else:
                text = get_page_wheel(source_page)
                save_page_wheel(page, text)
                self.cached_page2 = text

        page = self.cached_page2
        reg = re.compile('href=\\"(.*?)\\"')
        alls = reg.findall(page)
        if len(alls) == 0:
            keep = []
            for line in page.split("\n"):
                lline = line.lower()
                if self.name in lline or (self.mname and self.mname in lline):
                    keep.append(line)
            raise Exception(
                "module " +
                self.name + "\nexample:\n" + "\n".join(keep))

        version = python_version()
        plat = version[0] if version[0] == "win32" else version[1]
        if version[1] == '64bit' and version[0] == 'win32':
            plat = "amd64"
        cp = "-cp%d%d-" % sys.version_info[:2]
        py = "-py%d%d-" % sys.version_info[:2]
        pyn = "-py%d-" % sys.version_info[0]
        links = [_ for _ in alls if "/" +
                 self.name in _ and (pyn in _ or py in _ or cp in _) and (plat in _ or "-any" in _)]
        if len(links) == 0 and "-" in self.name:
            name_ = self.name.replace("-", "_")
            links = [_ for _ in alls if "/" +
                     name_ in _ and (pyn in _ or py in _ or cp in _) and (plat in _ or "-any" in _)]
        if len(links) == 0:
            if file_save is not None:
                with open(file_save, "w", encoding="utf8") as f:
                    f.write(page)
            short_list = [_ for _ in alls if self.name in _]
            raise MissingWheelException("unable to find a single link for " +
                                        self.name + "\n" + "\n".join(short_list))

        links = [(l.split("/")[-1], l) for l in links]
        links0 = links

        if self.name == "PyQt":
            links = [l for l in links if l[0].lower().startswith("pyqt4")]
        elif self.name == "numpy":
            links = [l for l in links if "unoptimized" not in l[
                0].lower() and "vanilla" not in l[0].lower()]

        if len(links) == 0:
            raise Exception("unable to find a single link for " +
                            self.name +
                            "\nEX:\n" +
                            "\n".join(str(_) for _ in links0))

        link = choose_most_recent(links)
        self.existing_version = self.extract_version(link[0])
        url, whl = link[1], link[0]
        if not whl.endswith(".whl"):
            whl += ".whl"
        return url, whl

    _page_cache_html = os.path.join(
        os.path.abspath(os.path.split(__file__)[0]), "page.html")

    def get_exewheel_url_link(self, file_save=None, wheel=False):
        """
        for windows, get the url of the setup using a webpage

        @param      file_save   for debug purposes
        @param      wheel       returns the wheel file or the exe file
        @return                 url, exe name
        """
        if "cached_page" not in self.__dict__:
            page = ModuleInstall._page_cache_html

            exi = os.path.exists(page)
            if exi:
                dt = get_file_modification_date(page)
                now = datetime.datetime.now()
                df = now - dt
                if df > datetime.timedelta(1):
                    exi = False

            if exi:
                text = read_page_wheel(page)
                self.cached_page = text
            else:
                text = get_page_wheel(ModuleInstall.exeLocation)
                save_page_wheel(page, text)
                self.cached_page = text

        page = self.cached_page
        alls = extract_all_links(page)
        if len(alls) == 0:
            keep = []
            for line in page.split("\n"):
                lline = line.lower()
                if self.name in lline or (self.mname and self.mname in lline):
                    keep.append(line)
            raise Exception(
                "module " +
                self.name + "\nexample:\n" + "\n".join(keep))

        version = python_version()
        plat = version[0] if version[0] == "win32" else version[1]
        if version[1] == '64bit' and version[0] == 'win32':
            plat = "amd64"
        links = list(enumerate_links_module(
            self.name, alls, sys.version_info, plat))
        if len(links) == 0:
            if file_save is not None:
                with open(file_save, "w", encoding="utf8") as f:
                    f.write(page)
            raise MissingWheelException(
                "unable to find a single link for " + self.name)
        links0 = links

        if self.name == "PyQt":
            links = [l for l in links if l[0].lower().startswith("pyqt4")]
        elif self.name == "numpy":
            links = [l for l in links if "unoptimized" not in l[
                0].lower() and "vanilla" not in l[0].lower()]

        if len(links) == 0:
            raise Exception("unable to find a single link for " +
                            self.name +
                            "\nEX:\n" +
                            "\n".join(str(_) for _ in links0))

        link = choose_most_recent(links)
        self.existing_version = self.extract_version(link[0])
        url, whl = ModuleInstall.exeLocation + link[2], link[0]
        if not whl.endswith(".whl"):
            whl += ".whl"
        return url, whl

    def unzipfiles(self, zipf, whereTo):
        """
        unzip files from a zip archive

        @param      zipf        archive
        @param      whereTo     destination folder
        @return                 list of unzipped files
        """
        return unzip_files(zipf, whereTo, self.fLOG)

    def extract_version(self, name):
        """
        extract the version from a filename

        @param      name        filename
        @return                 verions (str)
        """
        reg = re.compile(regex_wheel_version)
        res = reg.search(name)
        if res:
            return res.groups()[0]
        else:
            reg = re.compile(regex_wheel_version2)
            res = reg.search(name)
            if res:
                return res.groups()[0]
            else:
                reg = re.compile(regex_wheel_version5)
                res = reg.search(name)
                if res:
                    return res.groups()[0]
                else:
                    raise MissingVersionWheelException(
                        "unable to extract version number from {0}".format(name))

    def download(self, temp_folder=".", force=False, unzipFile=True,
                 file_save=None, deps=False, source=None):
        """
        download the module without installation

        @param      temp_folder     destination
        @param      force           force the installation even if already installed
        @param      unzipFile       if it can be unzipped, it will be (for github, mostly)
        @param      file_save       for debug purposes, do not change it unless you know what you are doing
        @param      deps            download the dependencies too (only available for pip)
        @param      source          overwrite source of the download, only for wheel packages,
                                    see @see me get_exewheel_url_link2
        @return                     downloaded files

        .. versionchanged:: 0.9
            Parameter *deps* was added, the function now downloads a module using pip.

        .. versionchanged:: 1.0
            *deps* is overwritten by *self.deps* if not None

        .. versionchanged:: 1.1
            Parameter *source* was added, if None, it is overwritten by *self.source*.
        """
        if source is None:
            source = self.source
        kind = self.kind

        deps = deps if self.deps is None else self.deps

        if kind == "pip":
            # see https://pip.pypa.io/en/latest/reference/pip_install.html
            # we use pip install <package> --download=temp_folder
            pp = get_pip_program()
            cmd = pp + ' download {0}'.format(self.name)
            if self.version is not None:
                cmd += "=={0}".format(self.version)
            if " " in temp_folder:
                raise FileNotFoundError(
                    "no space allowed in folders: [" + temp_folder + "]")
            if deps:
                cmd += ' --dest={0}'.format(temp_folder)
            else:
                cmd += ' --dest={0} --no-deps'.format(temp_folder)
            if self.index_url is not None:
                slash = '' if self.index_url.endswith('/') else '/'
                cmd += ' --no-cache-dir --index={0}{1}simple/'.format(
                    self.index_url, slash)
                parsed_uri = urlsplit(self.index_url)
                cmd += " --trusted-host " + parsed_uri.hostname
            if self.pip_options is not None:
                cmd += " " + " ".join(self.pip_options)

            out, err = run_cmd(
                cmd, wait=True, fLOG=self.fLOG)
            if "Successfully downloaded" not in out:
                raise DownloadError(
                    "unable to download with pip " +
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
                raise FileNotFoundError(
                    "unable to find downloaded file " +
                    str(self) +
                    "\nCMD:\n" +
                    cmd +
                    "\nOUT:\n" +
                    out +
                    "\nERR:\n" +
                    err)

        elif kind in ("wheel", "wheel2"):
            if source is not None:
                kind = "wheel2"
            ver = python_version()
            if ver[0] != "win32":
                # nothing to download, you should use pip
                return None
            else:
                if hasattr(self, "overwrite") and self.overwrite is not None:
                    over = self.overwrite.format(*sys.version_info[0:2])
                    url, whl = over, over.split("/")[-1]
                    self.existing_version = "{0}{1}".format(
                        *sys.version_info[0:2])
                elif kind == "wheel":
                    url, whl = self.get_exewheel_url_link(
                        file_save=file_save, wheel=True)
                else:
                    url, whl = self.get_exewheel_url_link2(
                        file_save=file_save, wheel=True, source=source)
                whlname = os.path.join(temp_folder, whl)

                exi = os.path.exists(whlname)
                if force or not exi:

                    self.fLOG("downloading", whl)
                    # self.fLOG("url", url)
                    if self.existing_version is None:
                        self.existing_version = self.extract_version(whl)
                    req = urllib_request.Request(
                        url, headers={
                            'User-agent': default_user_agent})
                    try:
                        u = urllib_request.urlopen(req)
                        text = u.read()
                        u.close()
                    except urllib_error.HTTPError as e:
                        raise DownloadError("unable to download {} from {}".format(
                            os.path.split(whlname)[-1], url)) from e

                    if not os.path.exists(temp_folder):
                        os.makedirs(temp_folder)

                    if len(text) <= 1000:
                        raise WrongWheelException("Size of downloaded wheel is too small: {0}\nurl={1}\nagent={2}".format(
                            len(text), url, default_user_agent))

                    self.fLOG("writing", whl)
                    with open(whlname, "wb") as f:
                        f.write(text)

                return whlname

        elif kind == "github":
            outfile = os.path.join(temp_folder, self.name + ".zip")
            if force or not os.path.exists(outfile):
                zipurl = "https://github.com/{1}/{0}/archive/{2}.zip".format(
                    self.name, self.gitrepo, self.branch)
                self.fLOG("downloading", zipurl)
                try:
                    req = urllib_request.Request(
                        zipurl, headers={
                            'User-agent': default_user_agent})
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

        elif kind in ("exe", "exe2"):
            if source is not None:
                kind = "exe2"
            ver = python_version()
            if ver[0] != "win32":
                raise Exception(
                    "this option is not available on other systems than Windows, version={0}".format(ver))
            else:
                url, exe = self.get_exewheel_url_link(
                    file_save=file_save) if kind == "exe" else self.get_exewheel_url_link2(
                    file_save=file_save, source=source)

                self.fLOG("downloading", exe)
                req = urllib_request.Request(
                    url, headers={
                        'User-agent': default_user_agent})
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

    def get_pypi_version(self, url='https://pypi.python.org/pypi'):
        """
        returns the version of a package on pypi

        @param      url     pipy server
        @return             version

        See also `installing_python_packages_programatically.py <https://gist.github.com/rwilcox/755524>`_,
        `pkgtools.pypi: PyPI interface <http://pkgtools.readthedocs.org/en/latest/pypi.html>`_.
        """
        if url == 'https://pypi.python.org/pypi':
            # we use a function which caches the result
            return get_pypi_version(self.name)
        else:
            pypi = xmlrpc_client.ServerProxy(url)
            available = pypi.package_releases(self.name)
            if available is None or len(available) == 0:
                available = pypi.package_releases(self.name.capitalize())
            if (available is None or len(available) == 0) and self.mnane is not None:
                available = pypi.package_releases(self.mname)

            if available is None:
                raise MissingPackageOnPyPiException(
                    "; ".join([self.name, self.name.capitalize(), self.mname]))

            return available[0]

    def get_pypi_numeric_version(self):
        """
        returns the version of a package in pypi

        @return     tuple
        """
        vers = self.get_pypi_version()
        if vers is None:
            return None
        if isinstance(vers, list):
            v = self.get_pypi_version()
            raise TypeError("unexpected type: {0} -- {1}".format(vers, v))
        return numeric_version(vers)

    def get_installed_version(self):
        """
        return the version of the installed package

        @return         version
        """
        vers = get_module_version(None)
        if self.name in vers:
            return vers[self.name]
        cap = self.name.capitalize()
        if cap in vers:
            return vers[cap]
        cap = self.name.lower()
        if cap in vers:
            return vers[cap]
        cap = self.name.replace("-", "_")
        if cap in vers:
            return vers[cap]
        cap = self.name.replace("_", "-")
        if cap in vers:
            return vers[cap]
        cap = self.name.lower().replace("_", "-")
        if cap in vers:
            return vers[cap]
        if self.mname is not None:
            if self.mname in vers:
                return vers[self.mname]
            cap = self.mname.lower()
            if cap in vers:
                return vers[cap]
        return None

    def get_installed_metadata(self):
        """
        return the metadata of the installed package

        @return         dictionary
        """
        r = get_module_metadata(self.name)
        if r is None:
            return get_module_metadata(self.mname)
        else:
            return r

    def get_installed_license(self):
        """
        return the license of the installed package

        @return         string
        """
        meta = self.get_installed_metadata()
        if meta is None or len(meta) == 0:
            res = None
        else:
            res = None
            for k, v in meta.items():
                if k.lower() == "license":
                    res = v
                    break
        adm = {None, "", "UNKNOWN"}
        if res is not None:
            if isinstance(res, list):
                res = [_ for _ in res if _ and _ not in adm]
                if len(res) > 0:
                    res = res[0]
                else:
                    res = None
        if res in adm:
            res = missing_module_licenses.get(self.name, None)
        return res

    def get_installed_classifier(self):
        """
        return the classifier of the installed package

        @return         string
        """
        meta = self.get_installed_metadata()
        if meta is None:
            return None
        for k, v in meta.items():
            if k.lower() == "classifier":
                return v
        return None

    def is_installed_version(self):
        """
        tells if a module is installed

        @return boolean
        """
        return self.get_installed_version() is not None

    def get_installed_numeric_version(self):
        """
        returns the version as number (not string)

        @return     tuple
        """
        vers = self.get_installed_version()
        if vers is None:
            return None
        return numeric_version(vers)

    def has_update(self):
        """
        tells if the package has a newer version on pipy

        @return boolean
        """
        if ModuleInstall.is_annoying(self.name):
            return False
        vers = self.get_installed_numeric_version()
        if self.version is None:
            pypi = self.get_pypi_numeric_version()
            return compare_version(pypi, vers) > 0
        else:
            num = numeric_version(self.version)
            return compare_version(num, vers) > 0

    def _check_installation(self):
        """
        some modules uninstall and install modules with another version number,
        we try to track that
        """
        try:
            import numpy
            if compare_version(numpy.__version__, "1.10") < 0:
                raise InstallError(
                    "numpy does not have a goof version number, it should be >= 1.10 not {0}".format(numpy.__version__))
        except ImportError:
            # not installed
            pass
        return True

    def install(self, force_kind=None, force=False, temp_folder=".",
                log=False, options=None, deps=False, source=None,
                custom=None, post=None):
        """
        install the package

        @param      force_kind      overwrite self.kind
        @param      force           force the installation even if already installed
        @param      temp_folder     folder where to download the setup
        @param      log             display logs or not
        @param      options         other options to add to the command line (see below) in a list
        @param      deps            install the dependencies too (only available for pip)
        @param      source          overwrite the source of the wheels,
                                    see @see me get_exewheel_url_link2
        @param      custom          overwrite parameters in ``self.custom``
        @param      post            instructions post installation (see the cnostructor for more help)
        @return                     boolean

        The options mentioned in parameter ``options``
        are described here: `pip install <http://www.pip-installer.org/en/latest/usage.html>`_
        or `setup.py options <http://docs.python.org/3.4/install/>`_ if you
        installing a module from github.

        .. versionchanged:: 1.0
            *deps* is overwritten by *self.deps* if not None

        .. versionchanged:: 1.1
            On Anaconda (based on function @see fn is_conda_distribution), we try *conda* first
            before switching to the regular way if it did not work.
            Exception were changed from ``Exception`` to ``InstallError``.
            Parameter *source* was added, if None, it is overwritten by *self.source*.
            Parameter *custom* was added, it works the same as *source*.
            Parameter *post* was added.
        """
        if source is None:
            source = self.source
        if post is None:
            post = self.post_installation
        if not force and force_kind is None and is_conda_distribution():
            try:
                return self.install(force_kind="conda", force=True, temp_folder=temp_folder,
                                    log=log, options=options, deps=deps)
            except InstallError as e:
                warnings.warn(str(e))
                # we try the regular way now

        if not force and self.is_installed_version():
            return True

        deps = deps if self.deps is None else self.deps

        if options is None:
            options = self.pip_options
        if options is None:
            options = []

        kind = force_kind if force_kind is not None else self.kind
        add = (" with " + kind) if kind != self.kind else ""
        self.fLOG("installation of " + str(self) + add)
        ret = None
        custom = custom or self.custom

        if kind == "pip":
            if custom is not None:
                raise NotImplementedError(
                    "custom must be None not '{0}' when kind is '{1}'".format(custom, kind))
            pp = get_pip_program()
            cmd = pp + " install {0}".format(self.name)
            if self.version is not None:
                cmd += "=={0}".format(self.version)
            if len(options) > 0:
                cmd += " " + " ".join(options)

            if not deps:
                cmd += ' --no-deps'

            if self.index_url is not None:
                slash = '' if self.index_url.endswith('/') else '/'
                cmd += ' --no-cache-dir --index={0}{1}simple/'.format(
                    self.index_url, slash)
            else:
                cmd += " --cache-dir={0}".format(temp_folder)

            if self.name == "kivy-garden":
                memo = sys.argv
                sys.argv = []
            out, err = run_cmd(
                cmd, wait=True, fLOG=self.fLOG)
            if self.name == "kivy-garden":
                sys.argv = memo

            success2 = "Requirement already up-to-date: " + self.name
            uptodate = success2.replace("-", "_") in out.replace("-", "_")

            if "No distributions matching the version" in out:
                mes = "(1) unable to install with pip {0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
                    str(self), cmd, out, err)
                raise InstallError(mes)
            elif "Testing of typecheck-decorator passed without failure." in out:
                ret = True
            elif "Successfully installed" not in out and not uptodate:
                if "error: Unable to find vcvarsall.bat" in out:
                    url = "http://www.xavierdupre.fr/blog/2013-07-07_nojs.html"
                    mes = "(2) unable to install with pip {0}\nread:\n{1}\nCMD:\n{2}\nOUT:\n{3}\nERR:\n{4}".format(
                        str(self), url, cmd, out, err)
                    raise InstallError(mes)
                if "Requirement already satisfied" not in out and not uptodate:
                    mes = "(3) unable to install with pip {0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
                        str(self), cmd, out, err)
                    raise InstallError(mes)
            else:
                ret = not uptodate

        elif kind == "conda":
            if custom is not None:
                raise NotImplementedError(
                    "custom must be None not '{0}' when kind is '{1}'".format(custom, kind))
            if "--upgrade" in options:
                options = [_ for _ in options if _ != "--upgrade"]
                command = "update"
            else:
                command = "install"
            pp = get_conda_program()
            cmd = pp + " {1} {0}".format(self.name, command)
            if self.version is not None:
                cmd += "=={0}".format(self.version)
            if len(options) > 0:
                cmd += " " + " ".join(options)

            cmd += " --no-pin --yes --quiet"
            if not deps:
                cmd += ' --no-deps'

            out, err = run_cmd(
                cmd, wait=True, fLOG=self.fLOG)
            if "No distributions matching the version" in out or \
               "No packages found in current linux" in out:
                mes = "(4) unable to install with conda {0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
                    str(self), cmd, out, err)
                raise InstallError(mes)
            elif "Testing of typecheck-decorator passed without failure." in out:
                ret = True
            elif "Successfully installed" not in out:
                if "error: Unable to find vcvarsall.bat" in out:
                    url = "http://www.xavierdupre.fr/blog/2013-07-07_nojs.html"
                    mes = "(5) unable to install with conda {0}\nread:\n{1}\nCMD:\n{2}\nOUT:\n{3}\nERR:\n{4}".format(
                        str(self), url, cmd, out, err)
                    raise InstallError(mes)
                if "Requirement already satisfied" not in out:
                    mes = "(6) unable to install with conda {0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
                        str(self), cmd, out, err)
                    raise InstallError(mes)
            else:
                ret = True

        elif kind in ("wheel", "wheel2"):
            if custom is not None:
                raise NotImplementedError(
                    "custom must be None not '{0}' when kind is '{1}'".format(custom, kind))
            ver = python_version()
            if ver[0] != "win32":
                ret = self.install("pip")
                whlname = self.name
                ret = True
            else:
                whlname = self.download(
                    temp_folder=temp_folder,
                    force=force,
                    unzipFile=True,
                    source=source)
                vers = self.get_installed_numeric_version()
                ret = True
                if vers is not None:
                    whlvers = numeric_version(get_wheel_version(whlname))
                    if compare_version(vers, whlvers) >= 0:
                        self.fLOG("skipping, no newer version {0} <= {1}: whl= {2}".format(
                            whlvers, vers, whlname))
                        ret = False
            if ret:
                self.fLOG("installing", os.path.split(whlname)[-1])

                pip = get_pip_program()
                cmd = pip + " install {0}".format(whlname)
                if self.version is not None:
                    cmd += "=={0}".format(self.version)
                if len(options) > 0:
                    opts = [_ for _ in options]
                    if len(opts):
                        cmd += " " + " ".join(opts)
                if not deps:
                    cmd += ' --no-deps'
                out, err = run_cmd(
                    cmd, wait=True, fLOG=self.fLOG)
                if "No distributions matching the version" in out:
                    mes = "(7) unable to install with wheel {0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
                        str(self), cmd, out, err)
                    raise InstallError(mes)
                elif "Testing of typecheck-decorator passed without failure." in out:
                    ret = True
                elif "Successfully installed" not in out:
                    if "error: Unable to find vcvarsall.bat" in out:
                        url = "http://www.xavierdupre.fr/blog/2013-07-07_nojs.html"
                        mes = "(8) unable to install with wheel {0}\nread:\n{1}\nCMD:\n{2}\nOUT:\n{3}\nERR:\n{4}".format(
                            str(self), url, cmd, out, err)
                        raise InstallError(mes)
                    if "Requirement already satisfied" not in out:
                        mes = "(9) unable to install with wheel {0}\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
                            str(self), cmd, out, err)
                        raise InstallError(mes)
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

            files = self.download(temp_folder=temp_folder,
                                  force=force, unzipFile=True)
            setu = [_ for _ in files if _.endswith("setup.py")]
            if len(setu) == 0:
                raise Exception(
                    "unable to find setup.py for module " +
                    self.name)
            elif len(setu) > 1:
                setu = [(len(_), _) for _ in setu]
                setu.sort()
                if setu[0][0] == setu[1][0]:
                    raise InstallError(
                        "(10) more than one setup.py for module " +
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
            if custom is None:
                custom = ["install"]
            cmds = []
            for command in custom:
                cmd1 = "{0} setup.py {1}".format(
                    sys.executable.replace("pythonw.exe", "python.exe"),
                    command)
                cmds.append(cmd1)

            def enumerate_filtered_option(options):
                for o in options:
                    if o not in ('--no-deps', '--upgrade'):
                        yield o

            filter_options = list(enumerate_filtered_option(options))
            if len(filter_options) > 0:
                cmds[-1] += " " + " ".join(filter_options)

            if deps:
                # it will not work
                # cmd += ' --no-deps'
                pass

            outs = ""
            errs = ""
            for cmd in cmds:
                out, err = run_cmd(
                    cmd, wait=True, fLOG=self.fLOG)
                if len(outs) > 0:
                    outs += "\n"
                if len(errs) > 0:
                    errs += "\n"
                outs += out
                errs += err
            os.chdir(cwd)

            out, err = outs, errs
            if "Successfully installed" not in out and "install  C" not in out:
                if "Finished processing dependencies" not in out:
                    raise InstallError(
                        "(11) unable to install with github " +
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
                        "(12) unable to install with github " +
                        str(self) +
                        "\nCMD:\n" +
                        cmd +
                        "\nOUT:\n" +
                        out +
                        "\nERR:\n" +
                        err)
            ret = True

        elif kind == "exe":
            if custom is not None:
                raise NotImplementedError(
                    "custom must be None not '{0}' when kind is '{1}'".format(custom, kind))
            ver = python_version()
            if ver[0] != "win32":
                ret = self.install("pip")
            else:
                exename = self.download(
                    temp_folder=temp_folder,
                    force=force,
                    unzipFile=True,
                    source=source)
                self.fLOG("executing", os.path.split(exename)[-1])
                out, err = run_cmd(
                    exename + " /s /qn /SILENT", wait=True, fLOG=self.fLOG)
                ret = len(err) == 0

        elif kind == "exe2":
            if custom is not None:
                raise NotImplementedError(
                    "custom must be None not '{0}' when kind is '{1}'".format(custom, kind))
            ver = python_version()
            if ver[0] != "win32":
                ret = self.install("pip")
            else:
                exename = self.download(
                    temp_folder=temp_folder,
                    force=force,
                    unzipFile=True,
                    source=source)
                self.fLOG("executing", os.path.split(exename)[-1])
                out, err = run_cmd(
                    exename + " /s /qn", wait=True, fLOG=self.fLOG)
                ret = len(err) == 0
        else:
            raise ImportError(
                "unknown kind: {0} for module {1}".format(
                    kind,
                    self.name))

        if ret is not None and ret:
            self._check_installation()

        # at this stage, there is a bug, for some executable, the execution
        # takes longer than expected
        # if not self.is_installed_version() :
        #    raise Exception("unable to install module: {0}, str:{1}".format(self.name, self))

        if ret is not None and ret and self.script is not None:
            if sys.platform.startswith("win"):
                # here, we have to wait until the script is installed
                ti = 0
                while not self.is_installed_local():
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

        if ret is not None and post is not None:
            self.fLOG("run_post_installation [begin]", post)
            ret = self.run_post_installation(post)
            self.fLOG("run_post_installation [end]")

        if ret is not None and ret:
            # we check the module was properly installed
            if not self.is_installed_local_cmd():
                raise InstallError(
                    "** unable to install module {0}, unable to import it".format(self.name))

        return ret

    def run_post_installation(self, post):
        """
        Run instructions post installation

        @param      post        dictionary, instructions post installation
        @return                 boolean

        Example:

        ::

            post = dict(cmd_python="Scripts\\\\pywin32_postinstall.py -install")

        .. versionadded:: 1.1
        """
        if not isinstance(post, dict):
            raise TypeError("expecting a dictionary")
        for k, v in post.items():
            if k == "cmd_python":
                exe = os.path.abspath(sys.executable)
                cmd = '"{0}" {1}'.format(exe, v.format(os.path.dirname(exe)))
                out, err = run_cmd(cmd, wait=True, fLOG=self.fLOG)
                if err is not None and len(err) > 0:
                    raise InstallError(
                        "Post installation script failed.\nCMD\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))
                self.fLOG("OUT:\n{0}".format(out))
            else:
                raise KeyError("Unable to interpret command '{0}'".format(k))
        return True

    def update(self, force_kind=None, force=False, temp_folder=".",
               log=False, options=None, deps=False, source=None):
        """
        update the package if necessary, we use ``pip install <module_name> --upgrade --no-deps``,

        @param      force_kind      overwrite self.kind
        @param      force           force the installation even if not need to update
        @param      temp_folder     folder where to download the setup
        @param      log             display logs or not
        @param      options         others options to add to the command line (see below) an a list
        @param      deps            download the dependencies too (only available for pip)
        @param      source          overwrite the source of the wheel, see @see me get_exewheel_url_link2
        @return                     boolean

        The options mentioned in parameter ``options``
        are described here: `pip install <http://www.pip-installer.org/en/latest/usage.html>`_
        or `setup.py options <http://docs.python.org/3.4/install/>`_ if you
        installing a module from github.

        .. versionchanged:: 1.1
            Parameter *source* was added, if None, it is overwritten by *self.source*.
        """
        if source is None:
            source = self.source
        if ModuleInstall.is_annoying(self.name):
            return False

        if not self.is_installed_version():
            raise MissingInstalledPackageException(self.name)

        if not force and not self.has_update():
            return True

        self.fLOG("update of ", self)

        options = [] if options is None else list(options)
        for opt in ["--upgrade", "--no-deps"]:
            if opt not in options:
                if not deps or opt == "--no-deps":
                    options.append(opt)

        res = self.install(force_kind=force_kind, force=True,
                           temp_folder=temp_folder, log=log, options=options, source=source)
        return res
