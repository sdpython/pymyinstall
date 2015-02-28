# coding: latin-1
"""
@file
@brief Various function to install various python module from various location.
"""
import sys
import re
import platform
import os
import urllib
import urllib.request
import urllib.error
import zipfile
import time
import subprocess
import importlib
import importlib.util


def python_version():
    """
    retrieve the platform and version of this python

    @return     tuple, example: ("win32","32bit") or ("win32","64bit")
    """
    return sys.platform, platform.architecture()[0]


def split_cmp_command(cmd, remove_quotes=True):
    """

    splits a command line

    @param      cmd             command line
    @param      remove_quotes   True by default
    @return                     list

    """
    if isinstance(cmd, str):
        spl = cmd.split()
        res = []
        for s in spl:
            if len(res) == 0:
                res.append(s)
            elif res[-1].startswith('"') and not res[-1].endswith('"'):
                res[-1] += " " + s
            else:
                res.append(s)
        if remove_quotes:
            res = [_.strip('"') for _ in res]
        return res
    else:
        return cmd


def run_cmd(cmd,
            sin="",
            shell=False,
            wait=False,
            log_error=True,
            secure=None,
            stop_waiting_if=None,
            do_not_log=False,
            encerror="ignore",
            encoding="utf8",
            fLOG=print):
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
    if sin is not None and sin != "":
        raise NotImplementedError("sin is not used")

    if secure is not None:
        if not do_not_log:
            fLOG("secure=", secure)
        with open(secure, "w") as f:
            f.write("")
        add = ">%s" % secure
        if isinstance(cmd, str):
            cmd += " " + add
        else:
            cmd.append(add)
    if not do_not_log:
        fLOG("execute ", cmd)

    if sys.platform.startswith("win"):

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        proc = subprocess.Popen(cmd,
                                shell=shell,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                startupinfo=startupinfo)
    else:
        proc = subprocess.Popen(split_cmp_command(cmd),
                                shell=shell,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    if wait:

        out = []
        skip_waiting = False

        if secure is None:
            for line in proc.stdout:
                if not do_not_log:
                    fLOG(line.decode(encoding, errors=encerror).strip("\n"))
                try:
                    out.append(
                        line.decode(
                            encoding,
                            errors=encerror).strip("\n"))
                except UnicodeDecodeError as exu:
                    raise Exception(
                        "issue with cmd:" +
                        str(cmd) +
                        "\n" +
                        str(exu))
                if proc.stdout.closed:
                    break
                if stop_waiting_if is not None and stop_waiting_if(
                        line.decode("utf8", errors=encerror)):
                    skip_waiting = True
                    break
        else:
            last = []
            while proc.poll() is None:
                if os.path.exists(secure):
                    with open(secure, "r") as f:
                        lines = f.readlines()
                    if len(lines) > len(last):
                        for line in lines[len(last):]:
                            if not do_not_log:
                                fLOG(line.strip("\n"))
                            out.append(line.strip("\n"))
                        last = lines
                    if stop_waiting_if is not None and len(
                            last) > 0 and stop_waiting_if(last[-1]):
                        skip_waiting = True
                        break
                time.sleep(0.1)

        if not skip_waiting:
            proc.wait()

        out = "\n".join(out)
        err = proc.stderr.read().decode(encoding, errors=encerror)
        if not do_not_log:
            fLOG("end of execution ", cmd)
        if len(err) > 0 and log_error and not do_not_log:
            fLOG("error (log)\n%s" % err)
        # return bytes.decode (out, errors="ignore"), bytes.decode(err,
        # errors="ignore")
        return out, err
    else:
        return "", ""


def unzip_files(zipf, whereTo, fLOG=print):
    """
    unzip files from a zip archive

    @param      zipf        archive
    @param      whereTo     destination folder
    @param      fLOG        logging function
    @return                 list of unzipped files
    """
    file = zipfile.ZipFile(zipf, "r")
    files = []
    for info in file.infolist():
        if not os.path.exists(info.filename):
            data = file.read(info.filename)
            tos = os.path.join(whereTo, info.filename)
            if not os.path.exists(tos):
                finalfolder = os.path.split(tos)[0]
                if not os.path.exists(finalfolder):
                    fLOG("    creating folder ", finalfolder)
                    os.makedirs(finalfolder)
                if not info.filename.endswith("/"):
                    u = open(tos, "wb")
                    u.write(data)
                    u.close()
                    files.append(tos)
                    fLOG("    unzipped ", info.filename, " to ", tos)
            elif not tos.endswith("/"):
                files.append(tos)
        elif not info.filename.endswith("/"):
            files.append(info.filename)
    return files


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
            r = add_shortcut_to_desktop(sc, name + "." + ver, name + "." + ver)
            return os.path.exists(r)
        else:
            return False
    else:
        raise NotImplementedError(
            "nothing implemented for module: {0}".format(name))
