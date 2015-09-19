"""
@file
@brief Custom versions of some modules
"""
import sys
import platform


class UnavailableCustomBuildError(Exception):
    """
    raise when a module does not have a custom build
    """
    pass


def get_exewheel_url_link_xd(name, file_save=None, wheel=False, exeLocationXd=None):
    """
    for windows, get the url of the setup using a webpage

    @param      name        module name
    @param      file_save   for debug purposes
    @param      wheel       returns the wheel file or the exe file
    @return                 url, exe name
    """
    sver = "%d%d" % sys.version_info[:2]
    sverp = "%d.%d" % sys.version_info[:2]
    ext = "exe" if not wheel else "whl"

    if name == "pywin32":
        if ext == "whl":
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        else:
            if platform.architecture()[0] == "64bit":
                exe = "pywin32-219.win-amd64-py%s.exe" % sverp
            else:
                exe = "pywin32-219.win32-py%s.exe" % sverp
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "pycrypto":
        p = platform.architecture()[0]
        vers = "{0}.{1}".format(*(sys.version_info[:2]))
        if p == "64bit":
            p = "win-amd64"
        else:
            p = "win32"
        if ext == "exe":
            exe = "pycrypto-2.6.1.{0}-py{1}.{2}".format(p, vers, ext)
        elif ext == "whl":
            exe = "pycrypto-2.6.1-cp%s-none-win_amd64.whl" % sver
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "CVXcanon":
        if ext == "whl":
            if platform.architecture()[0] == "64bit":
                exe = "CVXcanon-0.0.18-py3-none-any.whl"
            else:
                raise UnavailableCustomBuildError(
                    "CVXcanon is unavailable for 32bit")
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "gevent":
        if ext == "whl":
            if platform.architecture()[0] == "64bit":
                exe = "gevent-1.1b3-cp%s-none-win_amd64.whl" % sver
            else:
                exe = "gevent-1.1b3-cp%s-none-win32.whl" % sver
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "dpark":
        if ext == "whl":
            if platform.architecture()[0] == "64bit":
                exe = "DPark-0.1-cp%s-none-win_amd64.whl" % sver
            else:
                exe = "DPark-0.1-cp%s-none-win32.whl" % sver
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "tifffile":
        if ext == "whl":
            if platform.architecture()[0] == "64bit":
                exe = "tifffile-0.7.0-cp%s-none-win_amd64.whl" % sver
            else:
                exe = "tifffile-0.7.0-cp%s-none-win32.whl" % sver
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "xgboost":
        if ext == "whl":
            exe = "xgboost-0.4-py3-none-any.whl"
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "skdata":
        if ext == "whl":
            exe = "skdata-0.0.4-py3-none-any.whl"
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "JSAnimation":
        if ext == "whl":
            exe = "JSAnimation-0.1.tar.gz"
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "cchardet":
        if ext == "whl":
            if platform.architecture()[0] == "64bit":
                exe = "cchardet-1.0.0-cp%s-none-win_amd64.whl" % sver
            else:
                exe = "cchardet-1.0.0-cp%s-none-win32.whl" % sver
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    elif name == "aiohttp":
        if ext == "whl":
            if platform.architecture()[0] == "64bit":
                exe = "aiohttp-0.18.0a0-cp%s-none-win_amd64.whl" % sver
            else:
                exe = "aiohttp-0.18.0a0-cp%s-none-win32.whl" % sver
        else:
            raise UnavailableCustomBuildError("unexpected extension: " +
                                              ext + " for module " + file_save)
        url = "{0}/{1}".format(exeLocationXd, exe)
        return url, exe

    else:
        raise ImportError(
            "unable to get this module {0} from this location {1}".format(
                name,
                "exe_xd or wheel_xd"))
