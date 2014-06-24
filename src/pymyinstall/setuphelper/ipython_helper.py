# coding: latin-1
"""
@file
@brief Change ipython configuration
"""
import sys, os, re

def noLOG(*l, **p) :
    pass

def setup_ipython(  current_path = None,
                    additional_path = [ ],
                    apply_modification = True
                ) :
    """
    the function applies the modification suggested in this blog post:
    `Travailler avec IPython notebook <http://www.xavierdupre.fr/blog/2014-02-24_nojs.html>`_ (written in French).
    
    @param      additional_path     additional path to add to ipython
    @param      current_path        change the current path when running a notebook
    @param      apply_modification  apply the modification, otherwise, just create the profile
    @return                         path the config file
    """
    if sys.platform.startswith("win32"):
        user_profile = os.environ['USERPROFILE']
        profile = os.path.join(user_profile, ".ipython", "profile_default")
        ipython_config = os.path.join(profile, "ipython_config.py")
        ipython_notebook_config = os.path.join(profile, "ipython_notebook_config.py")
        
        if not os.path.exists(ipython_config):
            from ..installhelper.install_cmd import run_cmd
            exe = os.path.join(sys.executable, "Scripts", "ipython3.exe")
            cmd = exe + " create"
            out,err = run_cmd(cmd, wait=True, fLOG = noLOG)
            
            if not os.path.exists(ipython_config):
                raise Exception("unable to create ipython configuration because of:\n{0}\nERR:\n{1}".format(out,err))


        with open(ipython_notebook_config,"r") as f : text = f.read()
        
        # change current path and pylab configuration
        for var in ["IPKernelApp.file_to_run", 
                    "ProfileDir.location", 
                    "FileNotebookManager.checkpoint_dir",
                    "NotebookManager.notebook_dir",
                    "NotebookApp.ipython_dir",
                    "IPKernelApp.pylab"] :
            reg = re.compile("(#? *c.{0} =.*)".format(var))
            all = reg.findall(text)
            if len(all) == 1 and current_path != None :
                if "pylab" in var :
                    text = text.replace(all[0], "c.{0} = 'inline'".format(var))
                elif "file_to_run" not in var :
                    text = text.replace(all[0], "c.{1} = r'{0}'".format(current_path, var))
                else :
                    text = text.replace(all[0], "c.{1} = r'{0}\\ipython_startup.py'".format(current_path, var))
                    
        if apply_modification:
            # write modification
            with open(ipython_notebook_config,"w") as f : 
                f.write(text)
        
        # write ipython_startup.py
        rows= ["import sys"]
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
        
                    
if __name__ == "__main__" :
    setup_ipython(r"C:\temp", [], apply_modification = False)
