"""
@file
@brief Various helper about shortcuts and links
"""

import os
import sys
import platform


def add_shortcut_to_desktop(file, name, description="", arguments="", icon=None, workdir=None):
    """
    @see fn add_shortcut
    """
    return add_shortcut(file, name, description, arguments, icon, workdir)


def add_shortcut(target,
                 name,
                 description="",
                 arguments="",
                 icon=None,
                 workdir=None,
                 folder=None):
    """
    Add a shortcut to the desktop.

    @param      target      target
    @param      name        name of the shortcut
    @param      description description
    @param      arguments   arguments
    @param      icon        icon
    @param      workdir     working directory
    @param      folder      where to save the shortcut (None for the desktop)
    @return                 path to the shortcut
    """
    if not sys.platform.startswith("win"):
        raise NotImplementedError(
            "not implemented on this platform: " +
            sys.platform)

    try:
        import winshell
    except ImportError as e:
        if "DLL load failed" in str(e):
            os.environ["PATH"] = os.environ[
                "PATH"] + ";" + os.path.split(sys.executable)[0] + r"\lib\site-packages\pywin32_system32"
            try:
                import winshell
            except ImportError:
                raise ImportError(
                    r"you should run the following in your current folder:\ncopy C:\%s\lib\site-packages\pywin32_system32\py*.dll %s" %
                    (os.path.split(
                        sys.executable),
                        os.getcwd())) from e
        else:
            raise e

    if folder is None:
        folder = winshell.desktop()
    link_filepath = os.path.join(folder, name + ".lnk")

    args = ["/c", "start", target, arguments]

    with winshell.shortcut(link_filepath) as link:
        link.path = r"%windir%\system32\cmd.exe"
        link.description = description if description is not None else name
        link.arguments = " ".join(args)
        if icon is not None:
            link.icon_location = (icon, 0)
        if workdir is not None:
            link.working_directory = workdir

    if not os.path.exists(link_filepath):
        raise FileNotFoundError(link_filepath)
    return link_filepath


def suffix():
    """
    add a suffix to a shortcut name = python version + architecture

    @return     string
    """
    ver = ".".join(str(_) for _ in sys.version_info[:2])
    arc = platform.architecture()[0]
    return "{0}.{1}".format(arc, ver)


if __name__ == "__main__":
    path = r"C:\github\pymyinstall\dist\win_python_setup"
    target = r"tools\R\bin\R.exe"
    name = "R Console"
    icon = r"tools\icons\r.ico"
    add_shortcut(target=target, folder=path, icon=icon, name=name)

    path = r"C:\github\pymyinstall\dist\win_python_setup"
    target = r"python\python.exe"
    name = "Python Console"
    icon = r"tools\icons\python.ico"
    add_shortcut(target=target, folder=path, icon=icon, name=name)
