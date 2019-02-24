# -*- coding: utf-8 -*-
"""
@file
@brief Implements function @see fn run_cmd.

.. versionadded:: 1.1
"""
from __future__ import print_function
import sys
import os
import time
import subprocess
import threading
import warnings
import shlex
if sys.version_info[0] == 2:
    import Queue as queue
else:
    import queue


class RunCmdException(Exception):
    """
    raised by function @see fn run_cmd
    """
    pass


def get_interpreter_path():
    """
    return the interpreter path
    """
    if sys.platform.startswith("win"):
        return sys.executable.replace("pythonw.exe", "python.exe")
    else:
        return sys.executable


def split_cmp_command(cmd, remove_quotes=True):
    """
    splits a command line
    @param      cmd             command line
    @param      remove_quotes   True by default
    @return                     list
    """
    if isinstance(cmd, str  # unicode#
                  ):
        return shlex.split(cmd)
    else:
        return cmd


def decode_outerr(outerr, encoding, encerror, msg):
    """
    decode the output or the error after running a command line instructions

    @param      outerr      output or error
    @param      encoding    encoding (if None, it is replaced by ascii)
    @param      encerror    how to handle errors
    @param      msg         to add to the exception message
    @return                 converted string

    .. versionchanged:: 1.4
        If *encoding* is None, it is replaced by ``'ascii'``.
    """
    if encoding is None:
        encoding = "ascii"
    typstr = str  # unicode#
    if not isinstance(outerr, bytes):
        raise TypeError(
            "only able to decode bytes, not " + typstr(type(outerr)))
    try:
        out = outerr.decode(encoding, errors=encerror)
        return out
    except UnicodeDecodeError as exu:
        try:
            out = outerr.decode(
                "utf8" if encoding != "utf8" else "latin-1", errors=encerror)
            return out
        except Exception as e:
            out = outerr.decode(encoding, errors='ignore')
            raise Exception("issue with cmd (" + encoding + "):" +
                            typstr(msg) + "\n" + typstr(exu) + "\n-----\n" + out) from e
    raise Exception("complete issue with cmd:" + typstr(msg))


def skip_run_cmd(cmd, sin="", shell=True, wait=False, log_error=True,
                 stop_running_if=None, encerror="ignore",
                 encoding="utf8", change_path=None, communicate=True,
                 preprocess=True, timeout=None, catch_exit=False, fLOG=None,
                 timeout_listen=None, tell_if_no_output=None):
    """
    has the same signature as @see fn run_cmd but does nothing

    .. versionadded:: 1.0
    """
    return "", ""


def run_cmd_private(cmd, sin="", shell=True, wait=False, log_error=True,
                    stop_running_if=None, encerror="ignore", encoding="utf8",
                    change_path=None, communicate=True, preprocess=True, timeout=None,
                    catch_exit=False, fLOG=None, tell_if_no_output=None):
    """
    run a command line and wait for the result
    @param      cmd                 command line
    @param      sin                 sin: what must be written on the standard input
    @param      shell               if True, cmd is a shell command (and no command window is opened)
    @param      wait                call ``proc.wait``
    @param      log_error           if log_error, call fLOG (error)
    @param      stop_running_if     the function stops waiting if some condition is fulfilled.
                                    The function received the last line from the logs.
                                    Signature: ``stop_waiting_if(last_out, last_err) -> bool``.
                                    The function must return True to stop waiting.
                                    This function can also be used to intercept the standard output
                                    and the standard error while running.
    @param      encerror            encoding errors (ignore by default) while converting the output into a string
    @param      encoding            encoding of the output
    @param      change_path         change the current path if not None (put it back after the execution)
    @param      communicate         use method `communicate <https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate>`_
                                    which is supposed to be safer,
                                    parameter ``wait`` must be True
    @param      preprocess          preprocess the command line if necessary (not available on Windows) (False to disable that option)
    @param      timeout             when data is sent to stdin (``sin``), a timeout is needed to avoid
                                    waiting for ever (*timeout* is in seconds)
    @param      catch_exit          catch *SystemExit* exception
    @param      fLOG                logging function (if not None, bypass others parameters)
    @param      tell_if_no_output   tells if there is no output every *tell_if_no_output* seconds
    @return                         content of stdout, stdres  (only if wait is True)

    .. exref::
        :title: Run a program using the command line

        ::

            from pyquickhelper.loghelper import run_cmd
            out,err = run_cmd( "python setup.py install", wait=True)

    If you are using this function to run git function, parameter ``shell`` must be True.

    .. versionadded:: 1.1
    """
    if fLOG is not None:
        fLOG("execute", cmd)

    if sys.platform.startswith("win"):
        cmdl = cmd
    else:
        cmdl = split_cmp_command(cmd) if preprocess else cmd

    if catch_exit:
        try:
            pproc = subprocess.Popen(cmdl,
                                     shell=shell,
                                     stdin=subprocess.PIPE if (
                                         sin and len(sin) > 0) else None,
                                     stdout=subprocess.PIPE if wait else None,
                                     stderr=subprocess.PIPE if wait else None,
                                     cwd=change_path)
        except SystemExit as e:
            raise RunCmdException("SystemExit raised (1)") from e

    else:
        pproc = subprocess.Popen(cmdl,
                                 shell=shell,
                                 stdin=subprocess.PIPE if (
                                     sin and len(sin) > 0) else None,
                                 stdout=subprocess.PIPE if wait else None,
                                 stderr=subprocess.PIPE if wait else None,
                                 cwd=change_path)

    if isinstance(cmd, list):
        cmd = " ".join(cmd)

    if wait:
        skip_out_err = False
        out = []
        err = []
        err_read = False
        skip_waiting = False

        if communicate:
            # communicate is True
            if tell_if_no_output is not None:
                raise NotImplementedError(
                    "tell_if_no_output is not implemented when communicate is True")
            if stop_running_if is not None:
                raise NotImplementedError(
                    "stop_running_if is not implemented when communicate is True")
            input = None if (sin is None or len(sin) > 0) else sin.encode()
            if input is not None and len(input) > 0:
                if fLOG is not None:
                    fLOG("input", [input])

            if catch_exit:
                try:
                    if sys.version_info[0] == 2:
                        if timeout is not None:
                            raise NotImplementedError(
                                "timeout is only available with Python 3")
                        stdoutdata, stderrdata = pproc.communicate(input=input)
                    else:
                        stdoutdata, stderrdata = pproc.communicate(
                            input=input, timeout=timeout)
                except SystemExit as e:
                    raise RunCmdException("SystemExit raised (2)") from e
            else:
                if sys.version_info[0] == 2:
                    if timeout is not None:
                        warnings.warn(
                            "[run_cmd_private] timeout is only available with Python 3")
                    stdoutdata, stderrdata = pproc.communicate(input=input)
                else:
                    stdoutdata, stderrdata = pproc.communicate(
                        input=input, timeout=timeout)

            out = decode_outerr(stdoutdata, encoding, encerror, cmd)
            err = decode_outerr(stderrdata, encoding, encerror, cmd)
        else:
            # communicate is False: use of threads
            if sin is not None and len(sin) > 0:
                raise Exception(
                    "communicate should be True to send something on stdin")
            stdout, stderr = pproc.stdout, pproc.stderr

            begin = time.perf_counter()
            last_update = begin
            # with threads
            (stdoutReader, stdoutQueue) = _AsyncLineReader.getForFd(
                stdout, catch_exit=catch_exit)
            (stderrReader, stderrQueue) = _AsyncLineReader.getForFd(
                stderr, catch_exit=catch_exit)
            runloop = True

            while (not stdoutReader.eof() or not stderrReader.eof()) and runloop:
                while not stdoutQueue.empty():
                    line = stdoutQueue.get()
                    decol = decode_outerr(
                        line, encoding, encerror, cmd)
                    if fLOG is not None:
                        fLOG(decol.strip("\n\r"))
                    out.append(decol.strip("\n\r"))
                    last_update = time.perf_counter()
                    if stop_running_if is not None and stop_running_if(decol, None):
                        runloop = False
                        break

                while not stderrQueue.empty():
                    line = stderrQueue.get()
                    decol = decode_outerr(
                        line, encoding, encerror, cmd)
                    if fLOG is not None:
                        fLOG(decol.strip("\n\r"))
                    err.append(decol.strip("\n\r"))
                    last_update = time.perf_counter()
                    if stop_running_if is not None and stop_running_if(None, decol):
                        runloop = False
                        break
                time.sleep(0.05)

                delta = time.perf_counter() - last_update
                if tell_if_no_output is not None and delta >= tell_if_no_output:
                    if fLOG is not None:
                        fLOG("[run_cmd] No update in {0} seconds for cmd: {1}".format(
                            "%5.1f" % (last_update - begin), cmd))
                    last_update = time.perf_counter()
                full_delta = time.perf_counter() - begin
                if timeout is not None and full_delta > timeout:
                    runloop = False
                    if fLOG is not None:
                        fLOG("[run_cmd] Timeout after {0} seconds for cmd: {1}".format(
                            "%5.1f" % full_delta, cmd))
                    break

            if runloop:
                # Waiting for async readers to finish...
                stdoutReader.join()
                stderrReader.join()

                # Waiting for process to exit...
                returnCode = pproc.wait()
                err_read = True

                if returnCode != 0:
                    try:
                        # we try to close the ressources
                        stdout.close()
                        stderr.close()
                    except Exception as e:
                        warnings.warn("Unable to close stdout and sterr.")
                    if catch_exit:
                        raise RunCmdException("SystemExit raised with error code {0}\nOUT:\n{1}\nERR-0:\n{2}".format(
                            returnCode, "\n".join(out), "\n".join(err)))
                    raise subprocess.CalledProcessError(returnCode, cmd)

                if not skip_waiting:
                    pproc.wait()
            else:
                out.append("[run_cmd] killing process.")
                if fLOG is not None:
                    fLOG(
                        "[run_cmd] killing process because stop_running_if returned True.")
                pproc.kill()
                err_read = True
                if fLOG is not None:
                    fLOG("[run_cmd] process killed.")
                skip_out_err = True

            out = "\n".join(out)
            if skip_out_err:
                err = "Process killed."
            else:
                if err_read:
                    err = "\n".join(err)
                else:
                    temp = err = stderr.read()
                    try:
                        err = decode_outerr(temp, encoding, encerror, cmd)
                    except Exception:
                        err = decode_outerr(temp, encoding, "ignore", cmd)
                stdout.close()
                stderr.close()

        # same path for whether communicate is False or True
        err = err.replace("\r\n", "\n")
        if fLOG is not None:
            fLOG("end of execution", cmd)

        if len(err) > 0 and log_error and fLOG is not None:
            fLOG("error (log)\n%s" % err)

        if sys.platform.startswith("win"):
            return out.replace("\r\n", "\n"), err.replace("\r\n", "\n")
        else:
            return out, err
    else:

        return "", ""


class _AsyncLineReader(threading.Thread):

    def __init__(self, fd, outputQueue, catch_exit):
        threading.Thread.__init__(self)

        assert isinstance(outputQueue, queue.Queue)
        assert callable(fd.readline)

        self.fd = fd
        self.catch_exit = catch_exit
        self.outputQueue = outputQueue

    def run(self):
        if self.catch_exit:
            try:
                for _ in map(self.outputQueue.put, iter(self.fd.readline, b'')):
                    pass
            except SystemExit as e:
                self.outputQueue.put(str(e))
                raise RunCmdException("SystemExit raised (3)") from e
        else:
            for _ in map(self.outputQueue.put, iter(self.fd.readline, b'')):
                pass

    def eof(self):
        return not self.is_alive() and self.outputQueue.empty()

    @classmethod
    def getForFd(cls, fd, start=True, catch_exit=False):
        q = queue.Queue()
        reader = cls(fd, q, catch_exit)

        if start:
            reader.start()

        return reader, q


def run_cmd_old(cmd, sin="", shell=False, wait=False, log_error=True,
                secure=None, stop_waiting_if=None, do_not_log=False,
                encerror="ignore", encoding="utf8", cwd=None, fLOG=print):
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
    @param      cwd                 current folder
    @param      fLOG                logging function
    @return                         content of stdout, stderr  (only if wait is True)


    .. faqref::
        :title: Exception when installing a module

        This error can occur when a module is installed on a virtual environment
        created before *pip* was updated on the main distribution.
        The solution consists in removing the virtual environment and create it again.

        ::

            c:\\Python34_x64vir\\install\\Scripts\\python -u setup.py install
            running install
            running bdist_egg
            running egg_info
            Traceback (most recent call last):
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2785, in _dep_map
                return self.__dep_map
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2642, in __getattr__
                raise AttributeError(attr)
            AttributeError: _DistInfoDistribution__dep_map

            During handling of the above exception, another exception occurred:

            Traceback (most recent call last):
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2776, in _parsed_pkg_info
                return self._pkg_info
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2642, in __getattr__
                raise AttributeError(attr)
            AttributeError: _pkg_info

            During handling of the above exception, another exception occurred:

            Traceback (most recent call last):
            File "setup.py", line 169, in <module>
                package_data=package_data,
            File "C:\\Python34_x64\\Lib\\distutils\\core.py", line 148, in setup
                dist.run_commands()
            File "C:\\Python34_x64\\Lib\\distutils\\dist.py", line 955, in run_commands
                self.run_command(cmd)
            File "C:\\Python34_x64\\Lib\\distutils\\dist.py", line 974, in run_command
                cmd_obj.run()
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\setuptools\\command\\install.py", line 67, in run
                self.do_egg_install()
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\setuptools\\command\\install.py", line 109, in do_egg_install
                self.run_command('bdist_egg')
            File "C:\\Python34_x64\\Lib\\distutils\\cmd.py", line 313, in run_command
                self.distribution.run_command(command)
            File "C:\\Python34_x64\\Lib\\distutils\\dist.py", line 974, in run_command
                cmd_obj.run()
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\setuptools\\command\\bdist_egg.py", line 151, in run
                self.run_command("egg_info")
            File "C:\\Python34_x64\\Lib\\distutils\\cmd.py", line 313, in run_command
                self.distribution.run_command(command)
            File "C:\\Python34_x64\\Lib\\distutils\\dist.py", line 974, in run_command
                cmd_obj.run()
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\setuptools\\command\\egg_info.py", line 171, in run
                ep.require(installer=installer)
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2355, in require
                items = working_set.resolve(reqs, env, installer)
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 835, in resolve
                new_requirements = dist.requires(req.extras)[::-1]
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2586, in requires
                dm = self._dep_map
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2787, in _dep_map
                self.__dep_map = self._compute_dependencies()
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2809, in _compute_dependencies
                for req in self._parsed_pkg_info.get_all('Requires-Dist') or []:
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 2778, in _parsed_pkg_info
                metadata = self.get_metadata(self.PKG_INFO)
            File "c:\\Python34_x64vir\\install\\lib\\site-packages\\pkg_resources\\__init__.py", line 1993, in get_metadata
                raise KeyError("No metadata except PKG-INFO is available")
            KeyError: 'No metadata except PKG-INFO is available'
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
    if not do_not_log and fLOG is not None:
        fLOG("execute ", cmd)

    if sys.platform.startswith("win"):

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        try:
            proc = subprocess.Popen(cmd, shell=shell,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    startupinfo=startupinfo, cwd=cwd)
        except FileNotFoundError as e:
            raise RunCmdException("unable to run CMD:\n{0}".format(cmd)) from e
    else:
        try:
            proc = subprocess.Popen(split_cmp_command(cmd), shell=shell,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    cwd=cwd)
        except FileNotFoundError as e:
            raise RunCmdException("unable to run CMD:\n{0}".format(cmd)) from e
    if wait:

        out = []
        skip_waiting = False

        if secure is None:
            for line in proc.stdout:
                if not do_not_log and fLOG is not None:
                    fLOG(line.decode(encoding, errors=encerror).strip("\n"))
                try:
                    out.append(
                        line.decode(
                            encoding,
                            errors=encerror).strip("\n"))
                except UnicodeDecodeError as exu:
                    raise RunCmdException(
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
                            if not do_not_log and fLOG is not None:
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
        if not do_not_log and fLOG is not None:
            fLOG("end of execution ", cmd)
        if len(err) > 0 and log_error and not do_not_log and fLOG is not None:
            fLOG("error (log)\n%s" % err)
        # return bytes.decode (out, errors="ignore"), bytes.decode(err,
        # errors="ignore")
        proc.stdout.close()
        proc.stderr.close()

        return out, err
    else:
        return "", ""
