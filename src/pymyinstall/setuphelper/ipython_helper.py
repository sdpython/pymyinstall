# coding: latin-1
"""
@file
@brief Change ipython configuration
"""
import sys, os, re

from ..installhelper.link_shortcuts import add_shortcut_to_desktop, suffix


def noLOG(*l, **p) :
    pass

def setup_ipython(  current_path        = None,
                    additional_path     = None,
                    apply_modification  = True,
                    shortcut            = True,
                    browser             = None
                ) :
    """
    The function applies the modification suggested in this blog post:
    `Travailler avec IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_ (written in French).
    
    @param      additional_path     additional paths to add to ipython (a list)
    @param      current_path        change the current path when running a notebook
    @param      apply_modification  apply the modification, otherwise, just create the profile
    @param      shortcut            add short cut the desktop
    @param      browser             if not None, tries to change if it finds it (IE, Chrome, Firefox, on Windows)
    @return                         path the config file
    
    If you need to create a shortcut with the appropriate paths, you can use the following instructions
    to open IPython notebook on a specific folder:
    
    @code
    set path=%path%;c:\Python34;c:\\Python34\\Scripts
    ipython3 notebook --notebook-dir=_doc\\notebooks
    @endcode
    
    """
    if sys.platform.startswith("win"):
        user_profile = os.environ['USERPROFILE']
        profile = os.path.join(user_profile, ".ipython", "profile_default")
        ipython_config = os.path.join(profile, "ipython_config.py")
        ipython_notebook_config = os.path.join(profile, "ipython_notebook_config.py")
        
        checkpath = os.path.join(profile, "checkspoints")
        if not os.path.exists(checkpath) : os.mkdir(checkpath)
        
        if not os.path.exists(ipython_config):
            from ..installhelper.install_cmd import run_cmd
            exe = os.path.join(os.path.split(sys.executable)[0], "Scripts", "ipython3.exe")
            cmd = exe + " profile create"
            out,err = run_cmd(cmd, wait=True, fLOG = noLOG)
            
            if not os.path.exists(ipython_config):
                raise Exception("unable to create ipython configuration because of:\n{0}\nERR:\n{1}\ncmd={2}".format(out,err,cmd))


        with open(ipython_notebook_config,"r") as f : text = f.read()
        
        # change current path and pylab configuration
        for var in ["IPKernelApp.file_to_run", 
                    "ProfileDir.location", 
                    "FileNotebookManager.checkpoint_dir",
                    "NotebookManager.notebook_dir",
                    "NotebookApp.ipython_dir",
                    "IPKernelApp.pylab"] :
            reg = re.compile("(#? *c.{0} =.*)".format(var))
            alls = reg.findall(text)
            if len(alls) == 1 and current_path is not None :
                if "pylab" in var :
                    text = text.replace(alls[0], "c.{0} = 'inline'".format(var))
                elif "checkpoint_dir" in var :
                    text = text.replace(alls[0], "c.{0} = r'{1}'".format(var,checkpath))
                elif "file_to_run" not in var :
                    text = text.replace(alls[0], "c.{1} = r'{0}'".format(current_path, var))
                else :
                    text = text.replace(alls[0], "c.{1} = r'{0}\ipython_startup.py'".format(current_path, var))
                    
        # browser
        if browser is not None :
            if sys.platform.startswith("win"):
                paths = {  "firefox":r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
                            "ie":r"C:\Program Files\Internet Explorer\iexplore.exe",
                            "chrome":r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                            }
                browser = browser.lower()
                if browser not in paths :
                    raise KeyError("unable to find browser {0} in [{1}]".format(browser, ",".join(paths.keys())))
                subtext = """
                    import webbrowser
                    webbrowser.register('{0}', None, webbrowser.GenericBrowser(r'{1}'))
                    c.NotebookApp.browser = '{0}'
                    """.format(browser, paths[browser]).replace("                    ","")
                text += subtext
                
            else:
                raise NotImplementedError("implemented only on Windows")
        
        if apply_modification:
            # write modification
            with open(ipython_notebook_config,"w") as f : 
                f.write(text)
        
        # write ipython_startup.py
        rows= ["import sys"]
        if additional_path is not None :
            for p in additional_path :
                if not os.path.exists(p): raise FileNotFoundError(p)
                rows.append ( "sys.path.append(r'{0}')".format(p) )
        s = "\n".join(rows)
        
        if apply_modification :
            with open(os.path.join(current_path, "ipython_startup.py"),"w") as f : 
                f.write(s)
                
        return [ ipython_notebook_config, ipython_config]
        
    else :
        raise NotImplementedError("implemented only for Windows")
        
def add_shortcut_to_desktop_for_ipython(folder):
    """
    create a shortcut on your desktop
    
    @param      folder      notebook dir
    @return                 filename
    """
    file = os.path.join(os.path.split(sys.executable)[0], "Scripts", "ipython3")
    arguments = " notebook --notebook-dir=" + folder
    ver = suffix()
    return add_shortcut_to_desktop(file, "notebook." + ver, "IPython Notebook {1} ({0})".format(folder, ver), arguments)
                    
if __name__ == "__main__" :
    setup_ipython(r"C:\temp", [], apply_modification = False)
