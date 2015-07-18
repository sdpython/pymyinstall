"""
@file
@brief Various function to install various python module from various location.
"""
from __future__ import print_function

import sys
import platform
import os
import zipfile
import time
import subprocess
import datetime
import re


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
            cwd=None,
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
    @param      cwd                 current folder
    @param      fLOG                logging function
    @return                         content of stdout, stderr  (only if wait is True)


    @FAQ(Exception when installing a module)

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

    @endFAQ
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
                                startupinfo=startupinfo,
                                cwd=cwd)
    else:
        proc = subprocess.Popen(split_cmp_command(cmd),
                                shell=shell,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                cwd=cwd)
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
        proc.stdout.close()
        proc.stderr.close()

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
    files = []
    with zipfile.ZipFile(zipf, "r") as file:
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
        from .module_install import ModuleInstall
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


def get_pip_program(exe=None):
    """
    get ipython executable + fix an issue with PANDOC

    @param      exe             path to python executable
    @param      pandoc_path     if None, call @see fn find_pandoc_path
    @return                     ipython executable

    @FAQ(How can I check the dependencies?)

    The module `pipdeptree <https://github.com/naiquevin/pipdeptree>`_ gives
    you something like::

        Warning!!! Possible confusing dependencies found:
        * bokeh==0.8.2 -> pytz [required: ==2013b, installed: 2015.4]
          Babel==1.3 -> pytz [required: >=0a, installed: 2015.4]
          cubes==1.0.1 -> pytz [installed: 2015.4]
          pandas==0.16.0 -> pytz [required: >=2011k, installed: 2015.4]
          dateutils==0.6.6 -> pytz [installed: 2015.4]
          matplotlib==1.4.3 -> pytz [installed: 2015.4]
        * d3py==0.2.3 -> ipython [installed: 3.1.0]
          rodeo==0.2.4 -> ipython [required: >=3.0.0, installed: 3.1.0]
        * bokeh==0.8.2 -> Werkzeug [required: >=0.9.1, installed: 0.10.4]
          Flask==0.10.1 -> Werkzeug [required: >=0.7, installed: 0.10.4]
        * gensim==0.11.1.post1 -> scipy [required: >=0.7.0, installed: 0.15.1]
          bayespy==0.3.2 -> scipy [required: >=0.13.0, installed: 0.15.1]
          ecos==1.1.1 -> scipy [required: >=0.9, installed: 0.15.1]
          ggplot==0.6.5 -> scipy [installed: 0.15.1]
          Theano==0.7.0 -> scipy [required: >=0.11, installed: 0.15.1]
          cvxpy==0.2.17 -> scipy [required: >=0.13, installed: 0.15.1]
        * cloud-sptheme==1.6 -> Sphinx [required: >=1.1, installed: 1.3.1]
          sphinxjp.themes.revealjs==0.3.0 -> Sphinx [installed: 1.3.1]
          epfl-sphinx-theme==1.1.1 -> Sphinx [required: >=1.1, installed: 1.3.1]
          sphinxcontrib-images==0.5.0 -> Sphinx [required: >=1.1.3, installed: 1.3.1]
          sphinx-rtd-theme==0.1.8 -> Sphinx [required: >=1.3, installed: 1.3.1]
          sphinxjp.themes.basicstrap==0.4.2 -> Sphinx [installed: 1.3.1]
          sphinxjp.themes.sphinxjp==0.3.1 -> Sphinx [installed: 1.3.1]
        * bokeh==0.8.2 -> Pygments [required: >=1.6, installed: 2.0.2]
          Sphinx==1.3.1 -> Pygments [required: >=2.0, installed: 2.0.2]
        * bokeh==0.8.2 -> tornado [required: >=4.0.1, installed: 4.1]
          luigi==1.1.2 -> tornado [installed: 4.1]
        * Sphinx==1.3.1 -> docutils [required: >=0.11, installed: 0.12]
          python-daemon==2.0.5 -> docutils [installed: 0.12]
        * bayespy==0.3.2 -> matplotlib [required: >=1.2.0, installed: 1.4.3]
          scikit-image==0.11.3 -> matplotlib [required: >=1.1.0, installed: 1.4.3]
          ggplot==0.6.5 -> matplotlib [installed: 1.4.3]
        * blaze==0.7.3 -> multipledispatch [required: >=0.4.7, installed: 0.4.7]
          DataShape==0.4.4 -> multipledispatch [installed: 0.4.7]
          odo==0.3.1 -> multipledispatch [installed: 0.4.7]
        * bokeh==0.8.2 -> colorama [required: >=0.2.7, installed: 0.3.3]
          Sphinx==1.3.1 -> colorama [installed: 0.3.3]
        * bokeh==0.8.2 -> python-dateutil [required: >=2.1, installed: 2.4.2]
          azure==0.10.0 -> python-dateutil [installed: 2.4.2]
          cubes==1.0.1 -> python-dateutil [installed: 2.4.2]
          pandas==0.16.0 -> python-dateutil [required: >=2, installed: 2.4.2]
          dateutils==0.6.6 -> python-dateutil [installed: 2.4.2]
          matplotlib==1.4.3 -> python-dateutil [installed: 2.4.2]
          DataShape==0.4.4 -> python-dateutil [installed: 2.4.2]
        * bokeh==0.8.2 -> numpy [required: >=1.7.1, installed: 1.9.2]
          patsy==0.3.0 -> numpy [installed: 1.9.2]
          blaze==0.7.3 -> numpy [required: >=1.7, installed: 1.9.2]
          gensim==0.11.1.post1 -> numpy [required: >=1.3, installed: 1.9.2]
          bayespy==0.3.2 -> numpy [required: >=1.8.0, installed: 1.9.2]
          d3py==0.2.3 -> numpy [installed: 1.9.2]
          pandas==0.16.0 -> numpy [required: >=1.7.0, installed: 1.9.2]
          ecos==1.1.1 -> numpy [required: >=1.6, installed: 1.9.2]
          ggplot==0.6.5 -> numpy [installed: 1.9.2]
          matplotlib==1.4.3 -> numpy [required: >=1.6, installed: 1.9.2]
          numexpr==2.4 -> numpy [required: >=1.6, installed: 1.9.2]
          DataShape==0.4.4 -> numpy [installed: 1.9.2]
          pyqtgraph==0.9.10 -> numpy [installed: 1.9.2]
          Theano==0.7.0 -> numpy [required: >=1.6.2, installed: 1.9.2]
          odo==0.3.1 -> numpy [installed: 1.9.2]
          vispy==0.3.0 -> numpy [installed: 1.9.2]
          h5py==2.5.0 -> numpy [required: >=1.6.1, installed: 1.9.2]
          cvxpy==0.2.17 -> numpy [required: >=1.8, installed: 1.9.2]
          tables==3.1.1 -> numpy [required: >=1.4.1, installed: 1.9.2]
        * networkx==1.9.1 -> decorator [required: >=3.4.0, installed: 3.4.2]
          PyContracts==1.7.1 -> decorator [installed: 3.4.2]
        * bokeh==0.8.2 -> requests [required: >=1.2.3, installed: 2.6.0]
          python-linkedin==4.1 -> requests [required: >=1.1.0, installed: 2.6.0]
          conda==3.7.4 -> requests [installed: 2.6.0]
          sphinxcontrib-images==0.5.0 -> requests [required: >2.2, installed: 2.6.0]
          Kivy-Garden==0.1.1 -> requests [installed: 2.6.0]
          requests-oauthlib==0.4.2 -> requests [required: >=2.0.0, installed: 2.6.0]
        * cryptography==0.8.2 -> cffi [required: >=0.8, installed: 0.9.2]
          pygit2==0.21.3 -> cffi [installed: 0.9.2]
        * bokeh==0.8.2 -> six [required: >=1.5.2, installed: 1.9.0]
          Sphinx==1.3.1 -> six [required: >=1.4, installed: 1.9.0]
          gensim==0.11.1.post1 -> six [required: >=1.2.0, installed: 1.9.0]
          scikit-image==0.11.3 -> six [required: >=1.3, installed: 1.9.0]
          ggplot==0.6.5 -> six [installed: 1.9.0]
          pyOpenSSL==0.15.1 -> six [required: >=1.5.2, installed: 1.9.0]
          matplotlib==1.4.3 -> six [required: >=1.4, installed: 1.9.0]
          cryptography==0.8.2 -> six [required: >=1.4.1, installed: 1.9.0]
          ansi2html==1.1.0 -> six [installed: 1.9.0]
          python-jenkins==0.4.5 -> six [installed: 1.9.0]
          h5py==2.5.0 -> six [installed: 1.9.0]
          html5lib==0.999 -> six [installed: 1.9.0]
          python-dateutil==2.4.2 -> six [required: >=1.5, installed: 1.9.0]
        * bokeh==0.8.2 -> Jinja2 [required: >=2.7, installed: 2.7.3]
          Sphinx==1.3.1 -> Jinja2 [required: >=2.3, installed: 2.7.3]
          Flask==0.10.1 -> Jinja2 [required: >=2.4, installed: 2.7.3]
        * bokeh==0.8.2 -> pandas [required: >=0.11.0, installed: 0.16.0]
          blaze==0.7.3 -> pandas [installed: 0.16.0]
          d3py==0.2.3 -> pandas [installed: 0.16.0]
          ggplot==0.6.5 -> pandas [installed: 0.16.0]
          odo==0.3.1 -> pandas [required: >=0.15, installed: 0.16.0]
        * bokeh==0.8.2 -> pyzmq [required: >=14.3.1, installed: 14.5.0]
          rodeo==0.2.4 -> pyzmq [required: >=13, installed: 14.5.0]
        * d3py==0.2.3 -> networkx [installed: 1.9.1]
          scikit-image==0.11.3 -> networkx [required: >=1.8, installed: 1.9.1]
          odo==0.3.1 -> networkx [installed: 1.9.1]
        * bokeh==0.8.2 -> Flask [required: >=0.10.1, installed: 0.10.1]
          Flask-SQLAlchemy==2.0 -> Flask [required: >=0.10, installed: 0.10.1]
          rodeo==0.2.4 -> Flask [required: >=0.10.1, installed: 0.10.1]
        * bokeh==0.8.2 -> MarkupSafe [required: >=0.18, installed: 0.23]
          Jinja2==2.7.3 -> MarkupSafe [installed: 0.23]
        * matplotlib==1.4.3 -> pyparsing [required: >=1.5.6, installed: 2.0.3]
          PyContracts==1.7.1 -> pyparsing [installed: 2.0.3]
          luigi==1.1.2 -> pyparsing [installed: 2.0.3]
        * bokeh==0.8.2 -> PyYAML [required: >=3.10, installed: 3.11]
          conda==3.7.4 -> PyYAML [installed: 3.11]
        * scikit-image==0.11.3 -> pillow [required: >=1.7.8, installed: 2.8.1]
          python-pptx==0.3.2 -> pillow [required: >=2.0, installed: 2.8.1]
        ------------------------------------------------------------------------
        Warning!!! Cyclic dependencies found:
        - sphinx => sphinx-rtd-theme => sphinx>=1.3
        - sphinx => sphinx-rtd-theme => sphinx>=1.3
        - sphinx-rtd-theme => sphinx => sphinx-rtd-theme<0.2,>=0.1
        - sphinx => sphinx-rtd-theme => sphinx>=1.3
        - Sphinx => sphinx-rtd-theme => sphinx => sphinx-rtd-theme<0.2,>=0.1
        - Sphinx => sphinx-rtd-theme => sphinx => sphinx-rtd-theme<0.2,>=0.1
        - sphinx => sphinx-rtd-theme => sphinx>=1.3
        - sphinx => sphinx-rtd-theme => sphinx>=1.3
        ------------------------------------------------------------------------
        python-pptx==0.3.2
          - lxml [required: >=2.3.2, installed: 3.4.2]
          - pillow [required: >=2.0, installed: 2.8.1]
        d3py==0.2.3
          - ipython [installed: 3.1.0]
          - networkx [installed: 1.9.1]
            - decorator [required: >=3.4.0, installed: 3.4.2]
          - numpy [installed: 1.9.2]
          - pandas [installed: 0.16.0]
            - pytz [required: >=2011k, installed: 2015.4]
            - python-dateutil [required: >=2, installed: 2.4.2]
              - six [required: >=1.5, installed: 1.9.0]
            - numpy [required: >=1.7.0, installed: 1.9.2]
        autopep8==1.1.1
          - pep8 [required: >=1.5.7, installed: 1.5.7]
        dateutils==0.6.6
          - argparse
          - python-dateutil [installed: 2.4.2]
            - six [required: >=1.5, installed: 1.9.0]
          - pytz [installed: 2015.4]
        folium==0.1.2
        python-linkedin==4.1
          - requests [required: >=1.1.0, installed: 2.6.0]
          - requests-oauthlib [required: >=0.3, installed: 0.4.2]
            - oauthlib [required: >=0.6.2, installed: 0.7.2]
            - requests [required: >=2.0.0, installed: 2.6.0]
        sulci==0.3a0
          - genericcache [required: ==1.0.2, installed: 1.0.2]
            - setuptools
        ansi2html==1.1.0
          - six [installed: 1.9.0]
        ansiconv==1.0.0
        antlr4-python3-runtime==4.5
        autopy3==0.51
        azure==0.10.0
          - python-dateutil [installed: 2.4.2]
            - six [required: >=1.5, installed: 1.9.0]
          - pyOpenSSL [installed: 0.15.1]
            - six [required: >=1.5.2, installed: 1.9.0]
            - cryptography [required: >=0.7, installed: 0.8.2]
              - pyasn1 [installed: 0.1.7]
              - setuptools
              - cffi [required: >=0.8, installed: 0.9.2]
                - pycparser [installed: 2.10]
              - six [required: >=1.4.1, installed: 1.9.0]
          - futures [installed: 2.2.0]
        basemap==1.0.8
        bayespy==0.3.2
          - numpy [required: >=1.8.0, installed: 1.9.2]
          - scipy [required: >=0.13.0, installed: 0.15.1]
          - matplotlib [required: >=1.2.0, installed: 1.4.3]
            - python-dateutil [installed: 2.4.2]
              - six [required: >=1.5, installed: 1.9.0]
            - six [required: >=1.4, installed: 1.9.0]
            - pytz [installed: 2015.4]
            - numpy [required: >=1.6, installed: 1.9.2]
            - pyparsing [required: >=1.5.6, installed: 2.0.3]
          - h5py [installed: 2.5.0]
            - six [installed: 1.9.0]
            - numpy [required: >=1.6.1, installed: 1.9.2]
        beautifulsoup4==4.3.2
        bigfloat==0.3.0
        blaze==0.7.3
          - odo [installed: 0.3.1]
            - DataShape [installed: 0.4.4]
              - numpy [installed: 1.9.2]
              - multipledispatch [installed: 0.4.7]
              - python-dateutil [installed: 2.4.2]
                - six [required: >=1.5, installed: 1.9.0]
            - numpy [installed: 1.9.2]
            - pandas [required: >=0.15, installed: 0.16.0]
              - pytz [required: >=2011k, installed: 2015.4]
              - python-dateutil [required: >=2, installed: 2.4.2]
                - six [required: >=1.5, installed: 1.9.0]
              - numpy [required: >=1.7.0, installed: 1.9.2]
            - toolz [installed: 0.7.1]
            - multipledispatch [installed: 0.4.7]
            - networkx [installed: 1.9.1]
              - decorator [required: >=3.4.0, installed: 3.4.2]
          - psutil [installed: 2.2.1]
          - multipledispatch [required: >=0.4.7, installed: 0.4.7]
          - DataShape [installed: 0.4.4]
            - numpy [installed: 1.9.2]
            - multipledispatch [installed: 0.4.7]
            - python-dateutil [installed: 2.4.2]
              - six [required: >=1.5, installed: 1.9.0]
          - SQLAlchemy [installed: 0.9.9]
          - pandas [installed: 0.16.0]
            - pytz [required: >=2011k, installed: 2015.4]
            - python-dateutil [required: >=2, installed: 2.4.2]
              - six [required: >=1.5, installed: 1.9.0]
            - numpy [required: >=1.7.0, installed: 1.9.2]
          - numpy [required: >=1.7, installed: 1.9.2]
          - toolz [installed: 0.7.1]
        blist==1.3.6
        blosc==1.2.4
        bokeh==0.8.2
          - Flask [required: >=0.10.1, installed: 0.10.1]
            - Werkzeug [required: >=0.7, installed: 0.10.4]
            - Jinja2 [required: >=2.4, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
            - itsdangerous [required: >=0.21, installed: 0.24]
          - Jinja2 [required: >=2.7, installed: 2.7.3]
            - MarkupSafe [installed: 0.23]
          - MarkupSafe [required: >=0.18, installed: 0.23]
          - Werkzeug [required: >=0.9.1, installed: 0.10.4]
          - greenlet [required: >=0.4.1, installed: 0.4.5]
          - itsdangerous [required: >=0.21, installed: 0.24]
          - python-dateutil [required: >=2.1, installed: 2.4.2]
            - six [required: >=1.5, installed: 1.9.0]
          - pytz [required: ==2013b, installed: 2015.4]
          - requests [required: >=1.2.3, installed: 2.6.0]
          - six [required: >=1.5.2, installed: 1.9.0]
          - Pygments [required: >=1.6, installed: 2.0.2]
          - pystache [required: >=0.5.3, installed: 0.5.4]
          - Markdown [required: >=2.3.1, installed: 2.6.1]
          - PyYAML [required: >=3.10, installed: 3.11]
          - pyzmq [required: >=14.3.1, installed: 14.5.0]
          - tornado [required: >=4.0.1, installed: 4.1]
            - certifi [installed: 14.5.14]
          - colorama [required: >=0.2.7, installed: 0.3.3]
          - numpy [required: >=1.7.1, installed: 1.9.2]
          - pandas [required: >=0.11.0, installed: 0.16.0]
            - pytz [required: >=2011k, installed: 2015.4]
            - python-dateutil [required: >=2, installed: 2.4.2]
              - six [required: >=1.5, installed: 1.9.0]
            - numpy [required: >=1.7.0, installed: 1.9.2]
        cloud-sptheme==1.6
          - Sphinx [required: >=1.1, installed: 1.3.1]
            - alabaster [required: >=0.7, installed: 0.7.4]
            - six [required: >=1.4, installed: 1.9.0]
            - colorama [installed: 0.3.3]
            - Pygments [required: >=2.0, installed: 2.0.2]
            - Babel [required: >=1.3, installed: 1.3]
              - pytz [required: >=0a, installed: 2015.4]
            - snowballstemmer [required: >=1.1, installed: 1.2.0]
            - docutils [required: >=0.11, installed: 0.12]
            - sphinx-rtd-theme [required: >=0.1, installed: 0.1.8]
            - Jinja2 [required: >=2.3, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
        conda==3.7.4
          - requests [installed: 2.6.0]
          - pycosat [installed: 0.6.1]
          - PyYAML [installed: 3.11]
        coverage==3.7.1
        cubes==1.0.1
          - pytz [installed: 2015.4]
          - python-dateutil [installed: 2.4.2]
            - six [required: >=1.5, installed: 1.9.0]
          - jsonschema [installed: 2.4.0]
        cvxpy==0.2.17
          - scipy [required: >=0.13, installed: 0.15.1]
          - numpy [required: >=1.8, installed: 1.9.2]
          - scs [required: >=1.0.6, installed: 1.0.7]
          - cvxopt [required: >=1.1.6, installed: 1.1.7]
          - ecos [required: >=1.1, installed: 1.1.1]
            - numpy [required: >=1.6, installed: 1.9.2]
            - scipy [required: >=0.9, installed: 0.15.1]
          - toolz [installed: 0.7.1]
        Cython==0.22
        dbfread==2.0.4
        deap==1.0.1
        dynd==0.6.6
        epfl-sphinx-theme==1.1.1
          - Sphinx [required: >=1.1, installed: 1.3.1]
            - alabaster [required: >=0.7, installed: 0.7.4]
            - six [required: >=1.4, installed: 1.9.0]
            - colorama [installed: 0.3.3]
            - Pygments [required: >=2.0, installed: 2.0.2]
            - Babel [required: >=1.3, installed: 1.3]
              - pytz [required: >=0a, installed: 2015.4]
            - snowballstemmer [required: >=1.1, installed: 1.2.0]
            - docutils [required: >=0.11, installed: 0.12]
            - sphinx-rtd-theme [required: >=0.1, installed: 0.1.8]
            - Jinja2 [required: >=2.3, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
        fastcluster==1.1.16
        feedparser==5.1.3
        flake8==2.4.0
          - mccabe [required: >=0.2.1, installed: 0.3]
          - pep8 [required: >=1.5.7, installed: 1.5.7]
          - pyflakes [required: >=0.8.1, installed: 0.8.1]
        Flask-SQLAlchemy==2.0
          - Flask [required: >=0.10, installed: 0.10.1]
            - Werkzeug [required: >=0.7, installed: 0.10.4]
            - Jinja2 [required: >=2.4, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
            - itsdangerous [required: >=0.21, installed: 0.24]
          - SQLAlchemy [installed: 0.9.9]
        gensim==0.11.1.post1
          - numpy [required: >=1.3, installed: 1.9.2]
          - scipy [required: >=0.7.0, installed: 0.15.1]
          - smart-open [required: >=1.2.1, installed: 1.2.1]
            - boto [required: >=2.32, installed: 2.38.0]
            - bz2file [installed: 0.98]
          - six [required: >=1.2.0, installed: 1.9.0]
        ggplot==0.6.5
          - six [installed: 1.9.0]
          - statsmodels [installed: 0.6.1]
          - brewer2mpl [installed: 1.4.1]
          - matplotlib [installed: 1.4.3]
            - python-dateutil [installed: 2.4.2]
              - six [required: >=1.5, installed: 1.9.0]
            - six [required: >=1.4, installed: 1.9.0]
            - pytz [installed: 2015.4]
            - numpy [required: >=1.6, installed: 1.9.2]
            - pyparsing [required: >=1.5.6, installed: 2.0.3]
          - scipy [installed: 0.15.1]
          - patsy [installed: 0.3.0]
            - numpy [installed: 1.9.2]
          - pandas [installed: 0.16.0]
            - pytz [required: >=2011k, installed: 2015.4]
            - python-dateutil [required: >=2, installed: 2.4.2]
              - six [required: >=1.5, installed: 1.9.0]
            - numpy [required: >=1.7.0, installed: 1.9.2]
          - numpy [installed: 1.9.2]
        glueviz==0.4.0
        gmpy2==2.0.5
        graphviz==0.4.3
        hachibee-sphinx-theme==0.2.5
        html5lib==0.999
          - six [installed: 1.9.0]
        husl==4.0.2
        JSAnimation==0.1
        Kivy==1.9.0
          - Kivy-Garden [required: ==0.1.1, installed: 0.1.1]
            - requests [installed: 2.6.0]
        libLAS==1.8.0
        liblinear==1.96
        libsvm==3.20
        llvmpy==0.12.7
        luigi==1.1.2
          - pyparsing [installed: 2.0.3]
          - tornado [installed: 4.1]
            - certifi [installed: 14.5.14]
          - python-daemon [installed: 2.0.5]
            - docutils [installed: 0.12]
            - setuptools
            - lockfile [required: >=0.10, installed: 0.10.2]
        marisa-trie==0.7
        mistune==0.5.1
        mlpy==3.5.0
        mpld3==0.2
        nodeenv==0.13.1
        numba==0.18.2
        openpyxl==1.8.6
        paramiko==1.15.2
          - ecdsa [required: >=0.11, installed: 0.13]
          - pycrypto [required: >=2.1, installed: 2.6.1]
        py4j==0.8.2.1
        PyBrain==0.3
        PyContracts==1.7.1
          - pyparsing [installed: 2.0.3]
          - decorator [installed: 3.4.2]
        pygame==1.9.2a0
        pygit2==0.21.3
          - cffi [installed: 0.9.2]
            - pycparser [installed: 2.10]
        pymc==2.3.4
        pymongo==3.0
        PyOpenGL==3.1.1a1
        pypiserver==1.1.7
        pyqtgraph==0.9.10
          - numpy [installed: 1.9.2]
        pyreadline==2.0
        pyshp==1.2.1
        PySide==1.2.2
        python-igraph==0.7.1.post4
        python-jenkins==0.4.5
          - six [installed: 1.9.0]
          - pbr [required: >=0.8.2, installed: 0.10.8]
            - pip
        PyWavelets==0.3.0.dev0
        pywin32==219
        rodeo==0.2.4
          - ipython [required: >=3.0.0, installed: 3.1.0]
          - Flask [required: >=0.10.1, installed: 0.10.1]
            - Werkzeug [required: >=0.7, installed: 0.10.4]
            - Jinja2 [required: >=2.4, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
            - itsdangerous [required: >=0.21, installed: 0.24]
          - jedi [installed: 0.8.1]
          - docopt [installed: 0.6.2]
          - pyzmq [required: >=13, installed: 14.5.0]
          - markdown2 [installed: 2.3.0]
        rpy2==2.5.6
        scikit-image==0.11.3
          - matplotlib [required: >=1.1.0, installed: 1.4.3]
            - python-dateutil [installed: 2.4.2]
              - six [required: >=1.5, installed: 1.9.0]
            - six [required: >=1.4, installed: 1.9.0]
            - pytz [installed: 2015.4]
            - numpy [required: >=1.6, installed: 1.9.2]
            - pyparsing [required: >=1.5.6, installed: 2.0.3]
          - networkx [required: >=1.8, installed: 1.9.1]
            - decorator [required: >=3.4.0, installed: 3.4.2]
          - pillow [required: >=1.7.8, installed: 2.8.1]
          - six [required: >=1.3, installed: 1.9.0]
        scikit-learn==0.16.0
        seaborn==0.5.1
        selenium==2.45.0
        Shapely==1.5.7
        simplejson==3.6.5
        smopy==0.0.3
        solar-theme==1.3.2
        sphinxcontrib-images==0.5.0
          - Sphinx [required: >=1.1.3, installed: 1.3.1]
            - alabaster [required: >=0.7, installed: 0.7.4]
            - six [required: >=1.4, installed: 1.9.0]
            - colorama [installed: 0.3.3]
            - Pygments [required: >=2.0, installed: 2.0.2]
            - Babel [required: >=1.3, installed: 1.3]
              - pytz [required: >=0a, installed: 2015.4]
            - snowballstemmer [required: >=1.1, installed: 1.2.0]
            - docutils [required: >=0.11, installed: 0.12]
            - sphinx-rtd-theme [required: >=0.1, installed: 0.1.8]
            - Jinja2 [required: >=2.3, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
          - requests [required: >2.2, installed: 2.6.0]
        sphinxjp.themes.basicstrap==0.4.2
          - setuptools
          - Sphinx [installed: 1.3.1]
            - alabaster [required: >=0.7, installed: 0.7.4]
            - six [required: >=1.4, installed: 1.9.0]
            - colorama [installed: 0.3.3]
            - Pygments [required: >=2.0, installed: 2.0.2]
            - Babel [required: >=1.3, installed: 1.3]
              - pytz [required: >=0a, installed: 2015.4]
            - snowballstemmer [required: >=1.1, installed: 1.2.0]
            - docutils [required: >=0.11, installed: 0.12]
            - sphinx-rtd-theme [required: >=0.1, installed: 0.1.8]
              - Sphinx [required: >=1.3, installed: 1.3.1]
                - alabaster [required: >=0.7, installed: 0.7.4]
                - six [required: >=1.4, installed: 1.9.0]
                - colorama [installed: 0.3.3]
                - Pygments [required: >=2.0, installed: 2.0.2]
                - Babel [required: >=1.3, installed: 1.3]
                  - pytz [required: >=0a, installed: 2015.4]
                - snowballstemmer [required: >=1.1, installed: 1.2.0]
                - docutils [required: >=0.11, installed: 0.12]
                - Jinja2 [required: >=2.3, installed: 2.7.3]
                  - MarkupSafe [installed: 0.23]
            - Jinja2 [required: >=2.3, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
        sphinxjp.themes.revealjs==0.3.0
          - setuptools
          - Sphinx [installed: 1.3.1]
            - alabaster [required: >=0.7, installed: 0.7.4]
            - six [required: >=1.4, installed: 1.9.0]
            - colorama [installed: 0.3.3]
            - Pygments [required: >=2.0, installed: 2.0.2]
            - Babel [required: >=1.3, installed: 1.3]
              - pytz [required: >=0a, installed: 2015.4]
            - snowballstemmer [required: >=1.1, installed: 1.2.0]
            - docutils [required: >=0.11, installed: 0.12]
            - sphinx-rtd-theme [required: >=0.1, installed: 0.1.8]
              - Sphinx [required: >=1.3, installed: 1.3.1]
                - alabaster [required: >=0.7, installed: 0.7.4]
                - six [required: >=1.4, installed: 1.9.0]
                - colorama [installed: 0.3.3]
                - Pygments [required: >=2.0, installed: 2.0.2]
                - Babel [required: >=1.3, installed: 1.3]
                  - pytz [required: >=0a, installed: 2015.4]
                - snowballstemmer [required: >=1.1, installed: 1.2.0]
                - docutils [required: >=0.11, installed: 0.12]
                - Jinja2 [required: >=2.3, installed: 2.7.3]
                  - MarkupSafe [installed: 0.23]
            - Jinja2 [required: >=2.3, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
        sphinxjp.themes.sphinxjp==0.3.1
          - setuptools
          - Sphinx [installed: 1.3.1]
            - alabaster [required: >=0.7, installed: 0.7.4]
            - six [required: >=1.4, installed: 1.9.0]
            - colorama [installed: 0.3.3]
            - Pygments [required: >=2.0, installed: 2.0.2]
            - Babel [required: >=1.3, installed: 1.3]
              - pytz [required: >=0a, installed: 2015.4]
            - snowballstemmer [required: >=1.1, installed: 1.2.0]
            - docutils [required: >=0.11, installed: 0.12]
            - sphinx-rtd-theme [required: >=0.1, installed: 0.1.8]
            - Jinja2 [required: >=2.3, installed: 2.7.3]
              - MarkupSafe [installed: 0.23]
        sphinx-bootstrap-theme==0.4.5
          - setuptools
        sphinx-py3doc-enhanced-theme==2.0.1
        sphinx-readable-theme==1.3.0
        spyder==2.3.4
        sympy==0.7.6
        tables==3.1.1
          - numpy [required: >=1.4.1, installed: 1.9.2]
          - numexpr [required: >=2.0.0, installed: 2.4]
            - numpy [required: >=1.6, installed: 1.9.2]
        Theano==0.7.0
          - numpy [required: >=1.6.2, installed: 1.9.2]
          - scipy [required: >=0.11, installed: 0.15.1]
        typecheck-decorator==1.0
        virtualenv==12.1.1
        vispy==0.3.0
          - numpy [installed: 1.9.2]
        wheel==0.24.0
        wild-sphinx-theme==1.0.0
        winshell==0.6
        xlrd==0.9.3
        XlsxWriter==0.7.2
        xmltodict==0.9.2

    @endFAQ
    """
    if exe is None:
        exe = os.path.dirname(sys.executable)
    if sys.platform.startswith("win"):
        if not exe.endswith("Scripts"):
            pi = os.path.join(exe, "Scripts", "pip.exe")
            if not os.path.exists(pi):
                pi = os.path.join(exe, "Scripts", "pip3.exe")
                if not os.path.exists(pi):
                    # Anaconda is different
                    pi = os.path.join(exe, "Scripts", "pip.exe")
                    if not os.path.exists(pi):
                        pi = os.path.join(exe, "Scripts", "pip3.exe")
                        if not os.path.exists(pi):
                            raise FileNotFoundError(pi)
        else:
            pi = os.path.join(exe, "pip.exe")
            if not os.path.exists(pi):
                # Anaconda is different
                pi = os.path.join(exe, "pip.exe")
                if not os.path.exists(pi):
                    pi = os.path.join(exe, "pip3.exe")
                    if not os.path.exists(pi):
                        raise FileNotFoundError(pi)
    else:
        if exe is None:
            return "pip"
        else:
            pi = os.path.join(exe, "pip")

    return pi


def get_file_modification_date(filename):
    """
    get the date modification for a time

    @param      filename        filename
    @return                     datetime
    """
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)


def update_pip(python_path=None, fLOG=print):
    """
    update pip for a specific distribution

    @param      python_path     python path (or sys.executable if None)
    @param      fLOG            logging function
    @return                     output
    """
    if python_path is None:
        python_path = sys.executable
    else:
        python_path = os.path.join(python_path, "python")
    cmd = python_path + " -m pip install -U pip"
    out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
    if err and len(err) > 0:
        raise Exception(
            "unable to update pip.\nCMD:\n{0}\nOUT:\n{1}\nERR:\n{2}".format(cmd, out, err))
    return out


def has_pip():
    """
    tells if pip is installed

    @return     boolean
    """
    try:
        import pip
        f = pip.__file__
        return f is not None
    except ImportError:
        return False


def get_wheel_version(whlname):
    """
    extract the version from a wheel file,
    return ``2.6.0`` for ``rpy2-2.6.0-cp34-none-win_amd64.whl``

    @param      whlname     file name
    @return                 string
    """
    exp = re.compile("[-]([0-9]+[.][0-9]+([.][0-9abdevcr]+))?[-]")
    find = exp.findall(whlname)
    if len(find) == 0:
        raise Exception(
            "unable to extract version of {0} (pattern: {1})".format(whlname, exp.pattern))
    if len(find) > 1:
        raise Exception(
            "unable to extract version of {0} (multiple version) (pattern: {1})".format(whlname, exp.pattern))
    return find[0]
