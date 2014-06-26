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
        
    import winshell
    
    link_filepath = os.path.join(winshell.desktop(), name + ".lnk")
    with winshell.shortcut(link_filepath) as link:
        link.path = file
        link.description = description
        link.arguments = argument  
    return link_filepath
