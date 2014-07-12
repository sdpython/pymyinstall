"""
@file
@brief Various helper about shortcuts and links
"""

import os, sys

def add_shortcut_to_desktop(file, name, description = "", arguments = ""):
    """
    Add a shortcut to the desktop.
    
    @param      file        file name (without .lnk extension)
    @param      name        name of the shortcut
    @param      description description
    @param      arguments   arguments
    @return                 path to the shortcut
    """
    if not sys.platform.startswith("win"):
        raise NotImplementedError("not implemented on this platform: " + sys.platform)
        
    try:
        import winshell
    except ImportError as e :
        if "DLL load failed" in str(e):
            os.environ["PATH"] = os.environ["PATH"] + ";" + os.path.split(sys.executable)[0] + r"\lib\site-packages\pywin32_system32"
            try:
                import winshell
            except ImportError as ee :
                raise ImportError(r"you should run the following in your current folder:\ncopy C:\%s\lib\site-packages\pywin32_system32\py*.dll %s" % (os.path.split(sys.executable), os.getcwd())) from e
        else :
            raise e
    
    link_filepath = os.path.join(winshell.desktop(), name + ".lnk")
    with winshell.shortcut(link_filepath) as link:
        link.path = file
        link.description = description
        link.arguments = arguments 
    return link_filepath
