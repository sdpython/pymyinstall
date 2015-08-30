# -*- coding: utf-8 -*-
"""
@file
@brief Helpers, inspired from `utils.py <https://github.com/winpython/winpython/blob/master/winpython/utils.py>`_
"""
from __future__ import print_function

import os
import os.path as osp
import subprocess
import tarfile
import zipfile
import fnmatch
# import winreg
import glob
import shutil

from .win_helper import patch_shebang_line


def is_program_installed(basename):
    """
    Return program absolute path if installed in PATH
    Otherwise, return None

    @param      basename        base name
    @return                     boolean
    """
    if os.path.exists(basename):
        return True
    for path in os.environ["PATH"].split(os.pathsep):
        abspath = osp.join(path, basename)
        if osp.isfile(abspath):
            return abspath


def extract_msi(fname, targetdir=None, verbose=False, fLOG=print):
    """
    Extract .msi installer to a temporary directory (if targetdir
    is None). Return the temporary directory path

    @param  fname           local installer (exe)
    @param  targetdir       where to install
    @param  verbose         verbose
    @param  fLOG            logging function
    @return                 targetdir
    """
    extract = 'msiexec.exe'
    bname = osp.basename(fname)
    args = ['/a', '%s' % bname]
    if not verbose:
        args += ['/quiet', '/qn']
    args += ['TARGETDIR=%s' % targetdir]
    cmd = [extract] + args
    fLOG("RUN: ", cmd)
    subprocess.call(cmd, cwd=osp.dirname(fname))
    fLOG('fname=%s' % fname)
    fLOG('TARGETDIR=%s' % targetdir)

    if "python-3" in fname.lower():
        subprocess.call(
            [r'%s\%s' % (targetdir, 'python.exe'), '-m', 'ensurepip'],
            cwd=osp.dirname(r'%s\%s' % (targetdir, 'pythons.exe')))
        # We patch ensurepip live (shame) !!!!
        # rational: https://github.com/pypa/pip/issues/2328
        for fname in glob.glob(r'%s\Scripts\*.exe' % targetdir):
            patch_shebang_line(fname)
    return targetdir


def extract_exe(fname, targetdir=None, verbose=False, fLOG=print, szip="7z.exe"):
    """
    Extract *.exe* archive to a temporary directory (if targetdir
    is None). Return the temporary directory path

    @param  fname           local installer (exe)
    @param  targetdir       where to install
    @param  verbose         verbose
    @param  szip            path to 7z.exe
    @param  fLOG            logging function
    @return                 targetdir
    """
    extract = szip
    if not is_program_installed(extract):
        pp = os.environ["PATH"].split(";")
        raise FileNotFoundError(
            "Required program '%s' was not found in PATH:\n  %s" % (extract, "\n  ".join(pp)))
    bname = osp.basename(fname)
    args = ['x', '-o%s' % targetdir, '-aos', bname]
    if verbose:
        retcode = subprocess.call([extract] + args, cwd=osp.dirname(fname))
    else:
        p = subprocess.Popen([extract] + args, cwd=osp.dirname(fname),
                             stdout=subprocess.PIPE)
        p.communicate()
        p.stdout.close()
        retcode = p.returncode
    if retcode != 0:
        raise RuntimeError("Failed to extract %s (return code: %d)"
                           % (fname, retcode))
    return targetdir


def extract_archive(fname, targetdir=None, verbose=False, fLOG=print):
    """
    Extract .zip, .exe (considered to be a zip archive) or .tar.gz archive
    to a temporary directory (if targetdir is None).
    Return the temporary directory path

    @param  fname           zip file or exe file
    @param  targetdir       where to install
    @param  verbose         verbose
    @param  fLOG            logging function
    @return                 targetdir
    """
    if osp.splitext(fname)[1] in ('.zip', '.exe'):
        obj = zipfile.ZipFile(fname, mode="r")
    elif fname.endswith('.tar.gz'):
        obj = tarfile.open(fname, mode='r:gz')
    else:
        raise RuntimeError("Unsupported archive filename %s" % fname)
    obj.extractall(path=targetdir)
    return targetdir


def clean_msi(folder, pattern, verbose=False, fLOG=print):
    """
    clean all files follwing a specific pattern

    @param      folder      folder
    @param      pattern     files to remove
    @param      verbose     display more information
    @param      fLOG        logging function
    @return                 removed files (as operation)
    """
    def find(loc, pattern):
        exes = []
        for root, dirnames, filenames in os.walk(loc):
            for filename in fnmatch.filter(filenames, pattern):
                exes.append(os.path.join(root, filename))
        return exes
    remove = find(folder, pattern)
    operations = []
    for r in remove:
        if verbose:
            fLOG("remove", r)
            os.remove(r)
            operations.append(("remove", r))
    return operations


def extract_copy(fname, targetdir=None, verbose=False, fLOG=print, szip=None):
    """
    Copy *.exe* to targetdir

    @param  fname           local installer (exe)
    @param  targetdir       where to install
    @param  verbose         verbose
    @param  fLOG            logging function
    @param  szip            unused
    @return                 targetdir
    """
    shutil.copy(fname, targetdir)
