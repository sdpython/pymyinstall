"""
@file
@brief Creates batch file to set up the environment
"""
import os


def create_win_batches(folders, verbose=False, fLOG=print):
    """
    create batchs for the setup, they will be placed in
    *folders["config"]*
    
    @param      folders     dictionary with the keys *tools*, *config*, *python*, *workspace*
    @param      verbose     verbose
    @param      fLOG        logging function
    @return                 operations (list of what was done)
    """
    operations = []
    for func in [create_win_env, 
                 create_win_ipython_console,
                 create_win_ipython_qtconsole,
                 create_win_ipython_notebook,
                 create_win_rodeo,
                 create_win_scite,
                 ]:
        op = func(folders)
        if verbose: 
            for o in op:
                fLOG(" ".join(o))
        operations.extend(op)
    return operations
    

def create_win_env(folders):
    """
    create a batch file to set up the environment
    
    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    tools = folders["tools"]
    text = ["@echo off", "set CURRENT=%~dp0"]
    if os.path.exists(os.path.join(tools, "R")):
        text.append("set R_HOME=%CURRENT%\\..\\tools\\R")
    if os.path.exists(os.path.join(tools, "Julia")):
        text.append("set JULIA_HOME=%CURRENT%\\..\\tools\\Julia")
    
    text = "\n".join(text)
    name = os.path.join(folders["config"], "env.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]
        
        
def create_win_ipython_console(folders):
    """
    create a batch file to start ipython
    
    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    tools = folders["tools"]
    text = ["@echo off", 
            "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set IPYTHON=%CURRENT2%\\..\\python\\Scripts\\ipython.exe",
            "cd %CURRENT2%\\..\\workspace",
            "%IPYTHON%"]
    
    text = "\n".join(text)
    name = os.path.join(folders["config"], "ipython_console.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]
        
        
def create_win_ipython_qtconsole(folders):
    """
    create a batch file to start ipython QtConsole
    
    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    tools = folders["tools"]
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set IPYTHON=%CURRENT2%\\..\\python\\Scripts\\ipython.exe",
            "cd %CURRENT2%\\..\\workspace",
            "%IPYTHON% qtconsole"]
    
    text = "\n".join(text)
    name = os.path.join(folders["config"], "ipython_qtconsole.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]
        

def create_win_ipython_notebook(folders):
    """
    create a batch file to start ipython
    
    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    tools = folders["tools"]
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set IPYTHON=%CURRENT2%\\..\\python\\Scripts\\ipython.exe",
            "cd %CURRENT2%\\..\\workspace",
            "%IPYTHON% notebook --notebook-dir=%CURRENT2%\\..\\workspace"]
    
    text = "\n".join(text)
    name = os.path.join(folders["config"], "ipython_notebook.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]
        

def create_win_rodeo(folders):
    """
    create a batch file to start ipython
    
    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    tools = folders["tools"]
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set RODEO=%CURRENT2%\\..\\python\\Scripts\\rodeo.exe",
            "cd %CURRENT2%\\..\\workspace",
            "%RODEO% %CURRENT2%\\..\\workspace"]
    
    text = "\n".join(text)
    name = os.path.join(folders["config"], "rodeo.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]
        
        
def create_win_scite(folders):
    """
    create a batch file to start ipython
    
    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    tools = folders["tools"]
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set SCITE=%CURRENT2%\\..\\tools\\Scite\\wscite\\scite.exe",
            "cd %CURRENT2%\\..\\workspace",
            "%SCITE% %1"]
    
    text = "\n".join(text)
    name = os.path.join(folders["config"], "scite.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]
        
