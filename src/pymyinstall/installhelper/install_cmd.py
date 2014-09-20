# coding: latin-1
"""
@file
@brief Various function to install various python module from various location.
"""
import sys, re, platform, os, urllib, urllib.request, zipfile,time, subprocess, importlib



def python_version():
    """
    retrieve the platform and version of this python
    
    @return     tuple, example: ("win32","32bit") or ("win32","64bit")
    """
    return sys.platform, platform.architecture()[0]

def split_cmp_command(cmd, remove_quotes = True) :
    """
    
    splits a command line

    @param      cmd             command line
    @param      remove_quotes   True by default
    @return                     list
        
    """
    if isinstance (cmd, str) :
        spl = cmd.split()
        res = []
        for s in spl :
            if len(res) == 0 :
                res.append(s)
            elif res[-1].startswith('"') and not res[-1].endswith('"') :
                res[-1] += " " + s
            else : 
                res.append(s)
        if remove_quotes :
            res = [ _.strip('"') for _ in res ]
        return res
    else : 
        return cmd
    
def run_cmd (   cmd, 
                sin             = "", 
                shell           = False, 
                wait            = False, 
                log_error       = True,
                secure          = None,
                stop_waiting_if = None,
                do_not_log      = False,
                encerror        = "ignore",
                encoding        = "utf8",
                fLOG            = print) :
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
    @param      fLOG                logging function
    @return                         content of stdout, stderr  (only if wait is True)
    """
    if sin is not None and sin != "" :
        raise NotImplementedError("sin is not used")

    if secure is not None :
        if not do_not_log :
            fLOG("secure=",secure)
        with open(secure,"w") as f : f.write("")
        add = ">%s" % secure 
        if isinstance (cmd, str) : cmd += " " + add
        else : cmd.append(add)
    if not do_not_log : 
        fLOG ("execute ", cmd)
    
    if sys.platform.startswith("win") :
        
        startupinfo = subprocess.STARTUPINFO()    
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        
        proc = subprocess.Popen (cmd, 
                                 shell = shell, 
                                 stdout = subprocess.PIPE, 
                                 stderr = subprocess.PIPE,
                                 startupinfo = startupinfo)
    else :
        proc = subprocess.Popen (split_cmp_command(cmd),
                                 shell = shell, 
                                 stdout = subprocess.PIPE, 
                                 stderr = subprocess.PIPE)
    if wait : 
    
        out = [ ]
        skip_waiting = False
        
        if secure is None :
            for line in proc.stdout :
                if not do_not_log : 
                    fLOG(line.decode(encoding, errors=encerror).strip("\n"))
                try :
                    out.append(line.decode(encoding, errors=encerror).strip("\n"))
                except UnicodeDecodeError as exu :
                    raise Exception("issue with cmd:" + str(cmd) + "\n" + str(exu))
                if proc.stdout.closed: 
                    break
                if stop_waiting_if is not None and stop_waiting_if(line.decode("utf8", errors=encerror)) :
                    skip_waiting = True
                    break
        else :
            last = []
            while proc.poll() is None :
                if os.path.exists (secure) :
                    with open(secure,"r") as f :
                        lines = f.readlines()
                    if len(lines) > len(last) :
                        for line in lines[len(last):] :
                            if not do_not_log : 
                                fLOG(line.strip("\n"))
                            out.append(line.strip("\n"))
                        last = lines
                    if stop_waiting_if is not None and len(last)>0 and stop_waiting_if(last[-1]) :
                        skip_waiting = True
                        break
                time.sleep(0.1)
         
        if not skip_waiting :
            proc.wait ()
        
        out = "\n".join(out)
        err = proc.stderr.read().decode(encoding, errors=encerror)
        if not do_not_log : 
            fLOG ("end of execution ", cmd)
        if len (err) > 0 and log_error and not do_not_log :
            fLOG ("error (log)\n%s" % err)
        #return bytes.decode (out, errors="ignore"), bytes.decode(err, errors="ignore")
        return out, err
    else :
        return "",""    
        
def unzip_files(zipf, whereTo, fLOG = print):
    """
    unzip files from a zip archive
    
    @param      zipf        archive
    @param      whereTo     destination folder
    @param      fLOG        logging function
    @return                 list of unzipped files
    """
    file = zipfile.ZipFile (zipf, "r")
    files = []
    for info in file.infolist () :
        if not os.path.exists (info.filename) :
            data = file.read (info.filename)
            tos = os.path.join (whereTo, info.filename)
            if not os.path.exists (tos) :
                finalfolder = os.path.split(tos)[0]
                if not os.path.exists (finalfolder) :
                    fLOG ("    creating folder ", finalfolder)
                    os.makedirs (finalfolder)
                if not info.filename.endswith ("/") :
                    u = open (tos, "wb")
                    u.write ( data )
                    u.close()
                    files.append (tos)
                    fLOG ("    unzipped ", info.filename, " to ", tos)
            elif not tos.endswith("/") :
                files.append (tos)
        elif not info.filename.endswith ("/") :
            files.append (info.filename)
    return files        

class ModuleInstall :
    """
    defines the necessary information for a module
    
    @example(Installation from GitHub)
    @code
    ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")
    @endcode
    @endexample
    """
    
    allowedKind = ["pip", "github", "exe"]
    expKPage    = "onclick=.javascript:dl[(]([,\\[\\]0-9]+) *, *.([0-9&;@?=:A-Zgtl]+).[)]. title(.+)?.>(.+?win32-py3.3.exe)</a>"
    expKPageQt  = "onclick=.javascript:dl[(]([,\\[\\]0-9]+) *, *.([0-9&;@?=:A-Zgtl]+).[)]. title(.+)?.>(PyQt4[-0-9.]+-gpl-Py3.3-Qt[-0-9.]+x32.exe)</a>"
    exeLocation = "http://www.lfd.uci.edu/~gohlke/pythonlibs/"
    gitexe      = r"C:\Program Files (x86)\Git"
    
    def __init__(self,  name, 
                        kind    = "pip", 
                        gitrepo = None, 
                        mname   = None, 
                        fLOG    = print, 
                        version = None,
                        script  = None):
        """
        constructor
        
        @param      name            name
        @param      kind            kind of installation (pip, github, exe)
        @param      gitrepo         github repository (example: sdpython)
        @param      mname           sometimes, the module name is different from its official name
        @param      version         to install a specific version (None for the latest)
        @param      fLOG            logging function
        @param      script          some extensions are not a module but an application (such as ``spyder``),
                                    the class will check this script is available
        
        exe is only for Windows.
        """
        if kind != "pip" and version is not None :
            raise NotImplementedError("version can be only specified if kind=='pip'")
        
        self.name       = name
        self.kind       = kind
        self.gitrepo    = gitrepo
        self.version    = version
        self.mname      = mname
        self.script     = script
        
        if self.kind not in ModuleInstall.allowedKind:
            raise Exception("unable to interpret kind {0}, it should be in {1}".format(kind, ",".join(ModuleInstall.allowedKind)))
        if self.kind == "github" and self.gitrepo is None :
            raise Exception("gitrepo cannot be empty")
            
        self.fLOG = fLOG
        
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
            return "{0}:{1}:import {2}".format(self.name,self.kind, self.ImportName)
        else :
            return "{0}:{1}:{2}".format(self.name,self.kind, self.Script)
    
    @property
    def ImportName(self):
        """
        return the import name
        """
        if self.mname is not None : return self.mname
        if self.name.startswith("python-"): return self.name[len("python-"):]
        else: return self.name
        
    def IsInstalled(self):
        """
        checks if a module is installed
        """
        if self.script is None :
            try :
                importlib.find_loader(self.ImportName)
                return True
            except ImportError as e :
                txt = "import {0}".format(self.ImportName)
                try :
                    exec(txt)
                    return True
                except Exception as ee :
                    return False
        else:
            return os.path.exists(self.Script)
                
    def get_exe_url_link(self, file_save = None) :
        """
        for windows, get the url of the setup using a webpage
        
        @param      file_save   for debug purposes
        @return                 url, exe name
        """
        version = python_version()
        plat    = version[0] if version[0] == "win32" else version[1]
        if version[1] == '64bit' and version[0] == 'win32' : plat = "amd64"
        if self.name.lower() == "pyqt":
            pattern = ModuleInstall.expKPageQt.replace("Py3.3",
                                                       "Py{0}.{1}".format(sys.version_info.major,sys.version_info.minor))
            if plat == "amd64":
                pattern = pattern.replace("x32","x64")
        else :
            pattern = ModuleInstall.expKPage.replace("win32-py3.3.exe",
                                                     "{0}-py{1}.{2}.exe".format(plat,sys.version_info.major,sys.version_info.minor))
        expre = re.compile(pattern)
        
        if "cached_page" not in self.__dict__ :
            page = os.path.join(os.path.split(__file__)[0],"page.html")
            if os.path.exists(page) :
                with open(page,"r",encoding="utf8") as f : text = f.read()
            else :
                req = urllib.request.Request(ModuleInstall.exeLocation, headers= { 'User-agent': 'Mozilla/5.0' })
                u = urllib.request.urlopen(req)
                text = u.read()
                u.close()
                text = text.decode("utf8")
                
            text = text.replace("&quot;","'")
            self.cached_page = text
            
        page = self.cached_page.replace("&#8209;","-")
        alls  = expre.findall(page)
        if len(alls) == 0 :
            if file_save is not None :
                with open(file_save, "w", encoding="utf8") as f:
                    f.write(page)
            raise Exception("unable to find regex with pattern: " + pattern)

        if self.name == "PyQt":
            alls = [ _ for _ in alls if _[-1].startswith(self.name + "4") ]
        else :
            alls = [ _ for _ in alls if _[-1].startswith(self.name + "-") ]
        if len(alls) == 0 :
            if file_save is not None :
                with open(file_save, "w", encoding="utf8") as f:
                    f.write(page)
            raise Exception("unable to find a single link for " + self.name)
        link = alls[-1]
        
        def dc(ml,mi):
                ot=""
                for j in range(0,len(mi)) :
                    ot+= chr(ml[ord(mi[j])-48])
                return ot
        def dl1(ml,mi):
            ot=""
            for j in range(0,len(mi)):
                ot+=chr(ml[ord(mi[j])-48])
            return ot
        def dl(ml,mi):
            mi=mi.replace('&lt;','<')
            mi=mi.replace('&gt;','>')
            mi=mi.replace('&amp;','&')
            return dl1(ml,mi)
        
        url = dl(eval(link[0]),link[1])
        return ModuleInstall.exeLocation + url, link[-1]
        
    def unzipfiles(self, zipf, whereTo):
        """
        unzip files from a zip archive
        
        @param      zipf        archive
        @param      whereTo     destination folder
        @return                 list of unzipped files
        """
        return unzip_files(zipf, whereTo, self.fLOG)
        
    def download(self, temp_folder = ".", force = False, unzipFile = True, file_save = None):
        """
        download the module without installation
        
        @param      temp_folder     destination
        @param      force           force the installation even if already installed
        @param      unzipFile       if it can be unzipped, it will be (for github, mostly)
        @param      file_save       for debug purposes, do not change it unless you know what you are doing
        @return                     downloaded files
        """
        kind = self.kind
        
        if kind == "pip" :
            # see http://www.pip-installer.org/en/latest/usage.html
            raise Exception("this functionality is not available for packages installed using pip")
            
        elif kind == "github" :
            outfile = os.path.join(temp_folder, self.name + ".zip")
            if force or not os.path.exists(outfile) :
                zipurl = "https://github.com/{1}/{0}/archive/master.zip".format(self.name, self.gitrepo)
                self.fLOG("downloading", zipurl)
                try :
                    req = urllib.request.Request(zipurl, headers= { 'User-agent': 'Mozilla/5.0' })
                    u = urllib.request.urlopen(req)
                    text = u.read()
                    u.close()
                except urllib.error.HTTPError as e :
                    raise Exception("unable to get archive from: " + zipurl) from e
            
                if not os.path.exists(temp_folder) : 
                    os.makedirs(temp_folder)
                u = open (outfile, "wb")
                u.write ( text )
                u.close()            
            
            if unzipFile :
                self.fLOG("unzipping ", outfile)
                files = self.unzipfiles(outfile, temp_folder)
                return files
            else :
                return outfile
            
        elif kind == "exe":
            ver = python_version()
            if ver[0] != "win32":
                raise Exception("this option is not available on other systems than Windows")
                #return self.install("pip")
            else :
                url,exe = self.get_exe_url_link(file_save = file_save)

                self.fLOG("downloading", exe)
                req = urllib.request.Request(url, headers= { 'User-agent': 'Mozilla/5.0' })
                u = urllib.request.urlopen(req)
                text = u.read()
                u.close()
                
                if not os.path.exists(temp_folder) : 
                    os.makedirs(temp_folder)
                
                exename = os.path.join(temp_folder,exe)
                self.fLOG("writing", exe)
                with open(exename,"wb") as f : f.write(text)
                return exename
        
    def install(self,   force_kind = None, 
                        force = False, 
                        temp_folder = ".", 
                        log = False,
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
        
        if not force and self.IsInstalled() :
            return True
            
        self.fLOG("installation of ", self)        
        kind = force_kind if force_kind != None else self.kind
        
        if kind == "pip" :
            pip = os.path.join(os.path.split(sys.executable)[0],"Scripts","pip.exe")
            cmd = pip + " install {0}".format(self.name)
            if self.version is not None : cmd += "=={0}".format(self.version)
            if len(options) > 0 :
                cmd += " " + " ".join(*options)
            out, err = run_cmd(cmd, wait = True, do_not_log = not log, fLOG = self.fLOG)
            if "Successfully installed" not in out :
                if "Requirement already satisfied" not in out :
                    raise Exception("unable to install " + str(self) + "\n" + out + "\n" + err)
            ret = True
            
        elif kind == "github" :
            # the following code requires admin rights
            #if python_version()[0].startswith("win") and kind == "git" and not os.path.exists(ModuleInstall.gitexe) :
            #    raise FileNotFoundError("you need to install github first: see http://windows.github.com/")
            #if python_version()[0].startswith("win"):
            #    os.chdir(os.path.join(ModuleInstall.gitexe,"bin"))
            #cmd = pip + " install -e git://github.com/{0}/{1}-python.git#egg={1}".format(self.gitrepo, self.name)
            
            files = self.download(temp_folder=temp_folder, force = force, unzipFile = True)
            setu = [ _ for _ in files if _.endswith("setup.py") ]
            if len(setu) == 0 :
                raise Exception("unable to find setup.py for module " + self.name)
            elif len(setu) > 1 :
                setu = [ (len(_),_) for _ in setu ]
                setu.sort()
                if setu[0][0] == setu[1][0]:
                    raise Exception("more than one setup.py for module " + self.name + "\n" + "\n".join(setu))
                else :
                    self.fLOG("warning: more than one setup: " + "; ".join(setu))
                    setu = [setu[0][1]]
            setu = os.path.abspath(setu[0])
            
            self.fLOG("install ", setu[0])
            cwd = os.getcwd()
            os.chdir(os.path.split(setu)[0])
            cmd = "{0} setup.py install".format(sys.executable.replace("pythonw.ewe","python.exe"))
            if len(options) > 0 :
                cmd += " " + " ".join(*options)
            out, err = run_cmd(cmd, wait = True, do_not_log = not log, fLOG = self.fLOG)
            os.chdir(cwd)
            if "Successfully installed" not in out and "install  C" not in out :
                if "Finished processing dependencies" not in out :
                    raise Exception("unable to install " + str(self) + "\n" + out + "\n" + err)
                else :
                    self.fLOG("warning: ``Successfully installed`` or ``install  C`` not found")
            ret = True
            
        elif kind == "exe":
            ver = python_version()
            if ver[0] != "win32":
                ret = self.install("pip")
            else :
                exename = self.download(temp_folder=temp_folder, force = force, unzipFile = True)
                self.fLOG("executing", os.path.split(exename)[-1])
                out,err = run_cmd(exename + " /s /qn", wait=True, do_not_log = not log, fLOG = self.fLOG)
                ret = len(err) == 0
        else :
            raise Exception("unknown kind: {0} for module {1}".format(kind, self.name))
        
        # at this stage, there is a bug, for some executable, the execution
        # takes longer than expected
        # if not self.IsInstalled() :
        #    raise Exception("unable to install module: {0}, str:{1}".format(self.name, self))
                
        if ret and self.script is not None:
            if sys.platform.startswith("win"):
                # here, we have to wait until the script is installed
                ti = 0
                while not self.IsInstalled():
                    time.sleep(0.5)
                    ti += 0.5
                    if ti > 60 :
                        self.fLOG("wait for the end of execution of ", self.name)
                    ti = 0
                
                # we add set path=%path%;PYTHONPATH
                with open(self.Script,"r") as f :
                    full = f.read()
                
                exe = os.path.split(sys.executable)[0]
                cmd = "set path=%path%;{0}".format(exe)
                if cmd not in full :
                    self.fLOG("add {0} to {1}".format(cmd,self.Script))
                    with open(self.Script,"w") as f :
                        if full.startswith("@echo off"):
                            f.write(full.replace("@echo off", "@echo off\n{0}".format(cmd)))
                        else :
                            f.write(cmd)
                            f.write("\n")
                            f.write(full)
                    
        return ret
            
            
def add_shortcut_to_desktop_for_module(name):
    """
    add a shortcut on a module which includes a script
    
    @param      name        name of the module
    @return                 shortcut was added or not
    """
    if name == "spyder":
        from .link_shortcuts import add_shortcut_to_desktop, suffix
        md = ModuleInstall("spyder", "exe", script="spyder.bat")
        sc = md.Script
        if os.path.exists(sc):
            ver = suffix()
            r = add_shortcut_to_desktop(sc, name + "." + ver,name + "." + ver)
            return os.path.exists(r)
        else :
            return False
    else :
        raise NotImplementedError("nothing implemented for module: {0}".format(name))
                
