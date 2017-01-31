# -*- coding: utf-8 -*-
"""
@file
@brief Helpers, inspired from `utils.py <https://github.com/winpython/winpython/blob/master/winpython/utils.py>`_
"""
from __future__ import print_function

import os
import os.path as osp
import subprocess
import re
import sys
import locale


# =============================================================================
# Patch chebang line (courtesy of Christoph Gohlke)
# =============================================================================
def patch_shebang_line(fname, pad=b' ', fLOG=print):
    """
    Remove absolute path to python.exe in shebang lines.

    @param      python      python extractor
    @param      pad         pad
    @param      fLOG        logging function
    @return                 boolean, True if patched, False otherwise
    """
    if sys.version_info[0] == 2:
        shebang_line = re.compile(r"(#!.+pythonw?\.exe)")  # Python2.7
    else:
        shebang_line = re.compile(b"(#!.+pythonw?\.exe)")  # Python3+

    with open(fname, 'rb') as fh:
        content = fh.read()

    content = shebang_line.split(content, maxsplit=1)
    if len(content) != 3:
        return
    exe = os.path.basename(content[1][2:])
    content[1] = b'#!' + exe + (pad * (len(content[1]) - len(exe) - 2))
    content = b''.join(content)

    try:
        with open(fname, 'wb') as fh:
            fh.write(content)
            fLOG("patched", fname)
        return True
    except Exception:
        fLOG("failed to patch", fname)
        return False


def get_env(name, current=True):
    """
    Return HKCU/HKLM environment variable name and value

    @param      name        name to look for
    @param      current     switch between *HKEY_CURRENT_USER* (True) and *HKEY_LOCAL_MACHINE* (False)
    @return                 tuple (see below)

    For example, get_user_env('PATH') may returns::

        ('Path', u'C:\\Program Files\\Intel\\WiFi\\bin\\')
    """
    import winreg
    root = winreg.HKEY_CURRENT_USER if current else winreg.HKEY_LOCAL_MACHINE
    key = winreg.OpenKey(root, "Environment")
    for index in range(0, winreg.QueryInfoKey(key)[1]):
        try:
            value = winreg.EnumValue(key, index)
            if value[0].lower() == name.lower():
                # Return both value[0] and value[1] because value[0] could be
                # different from name (lowercase/uppercase)
                return value[0], value[1]
        except Exception:
            break


def set_env(name, value, current=True):
    """
    Set HKCU/HKLM environment variables


    @param      name        name to look for
    @param      current     switch between *HKEY_CURRENT_USER* (True) and *HKEY_LOCAL_MACHINE* (False)
    """
    import winreg
    root = winreg.HKEY_CURRENT_USER if current else winreg.HKEY_LOCAL_MACHINE
    key = winreg.OpenKey(root, "Environment")
    try:
        _x, key_type = winreg.QueryValueEx(key, name)
    except WindowsError:
        key_type = winreg.REG_EXPAND_SZ
    key = winreg.OpenKey(root, "Environment", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, name, 0, key_type, value)
    from win32gui import SendMessageTimeout
    from win32con import (HWND_BROADCAST, WM_SETTINGCHANGE,
                          SMTO_ABORTIFHUNG)
    SendMessageTimeout(HWND_BROADCAST, WM_SETTINGCHANGE, 0,
                       "Environment", SMTO_ABORTIFHUNG, 5000)


def create_shortcut(path, description, filename,
                    arguments="", workdir="", iconpath="", iconindex=0):
    """
    Create Windows shortcut (.lnk file)

    @param      path            where to store the link
    @param      description     description
    @param      filename        link name
    @param      arguments       arguments to store
    @param      workdir         working directory
    @para       iconpath        icon
    @param      iconindex       icon index
    @return                     filename
    """
    import pythoncom
    from win32com.shell import shell
    ilink = pythoncom.CoCreateInstance(shell.CLSID_ShellLink, None,
                                       pythoncom.CLSCTX_INPROC_SERVER,
                                       shell.IID_IShellLink)
    ilink.SetPath(path)
    ilink.SetDescription(description)
    if arguments:
        ilink.SetArguments(arguments)
    if workdir:
        ilink.SetWorkingDirectory(workdir)
    if iconpath or iconindex:
        ilink.SetIconLocation(iconpath, iconindex)
    # now save it.
    ipf = ilink.QueryInterface(pythoncom.IID_IPersistFile)
    if not filename.endswith('.lnk'):
        filename += '.lnk'
    filename = os.path.join(path, filename)
    ipf.Save(filename, 0)
    return filename


def decode_fs_string(string):
    """Convert string from file system charset to unicode"""
    charset = sys.getfilesystemencoding()
    if charset is None:
        charset = locale.getpreferredencoding()
    return string.decode(charset)


def exec_shell_cmd(args, path):
    """Execute shell command (*args* is a list of arguments) in *path*"""
    # print " ".join(args)
    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, cwd=path, shell=True)
    return decode_fs_string(process.stdout.read())


def get_gcc_version(path):
    """Return version of the GCC compiler installed in *path*"""
    return exec_shell_cmd('gcc --version', path).splitlines()[0].split()[-1]


def get_r_version(path):
    """Return version of the R installed in *path*"""
    return exec_shell_cmd('dir ..\README.R*', path).splitlines()[-3].split("-")[-1]


def get_julia_version(path):
    """Return version of the Julia installed in *path*"""
    return exec_shell_cmd('julia.exe -v', path).splitlines()[0].split(" ")[-1]


def python_query(cmd, path):
    """Execute Python command using the Python interpreter located in *path*"""
    res = exec_shell_cmd('python -c "%s"' % cmd, path).splitlines()
    if not res:
        raise Exception(
            "CMD:\n{0}\nRES:\n{1}\nPATH:\n{2}".format(cmd, res, path))
    return res[0]


def get_python_infos(path):
    """Return (version, architecture) for the Python distribution located in
    *path*. The version number is limited to MAJOR.MINOR, the architecture is
    an integer: 32 or 64"""
    is_64 = python_query('import sys; print(sys.maxsize > 2**32)', path)
    arch = {'True': 64, 'False': 32}.get(is_64, None)
    ver = python_query("import sys; print('%d.%d' % (sys.version_info.major, "
                       "sys.version_info.minor))", path)
    if re.match(r'([0-9]*)\.([0-9]*)', ver) is None:
        ver = None
    return ver, arch


def get_python_long_version(path):
    """Return long version (X.Y.Z) for the Python distribution located in
    *path*"""
    ver = python_query("import sys; print('%d.%d.%d' % "
                       "(sys.version_info.major, sys.version_info.minor,"
                       "sys.version_info.micro))", path)
    if re.match(r'([0-9]*)\.([0-9]*)\.([0-9]*)', ver) is None:
        ver = None
    return ver


# =============================================================================
# Patch sourcefile (instead of forking packages)
# =============================================================================
def patch_sourcefile(fname, in_text, out_text, silent_mode=False):
    """Replace a string in a source file"""
    import io
    if osp.isfile(fname) and not in_text == out_text:
        with io.open(fname, 'r') as fh:
            content = fh.read()
        new_content = content.replace(in_text, out_text)
        if not new_content == content:
            if not silent_mode:
                print("patching ", fname, "from", in_text, "to", out_text)
            with io.open(fname, 'wt') as fh:
                fh.write(new_content)

# =============================================================================
# Patch sourcelines (instead of forking packages)
# =============================================================================


def patch_sourcelines(fname, in_line_start, out_line, endline='\n', silent_mode=False):
    """Replace the middle of lines between in_line_start and endline """
    import io
    import os.path as osp
    if osp.isfile(fname):
        with io.open(fname, 'r') as fh:
            contents = fh.readlines()
            content = "".join(contents)
            for l in range(len(contents)):
                if contents[l].startswith(in_line_start):
                    begining, middle = in_line_start, contents[
                        l][len(in_line_start):]
                    ending = ""
                    if middle.find(endline) > 0:
                        ending = endline + \
                            endline.join(middle.split(endline)[1:])
                        middle = middle.split(endline)[0]
                    middle = out_line
                    new_line = begining + middle + ending
                    if not new_line == contents[l]:
                        if not silent_mode:
                            print(
                                "patching ", fname, " from\n", contents[l], "\nto\n", new_line)
                    contents[l] = new_line
            new_content = "".join(contents)
        if not new_content == content:
            # if not silent_mode:
            #    print("patching ", fname, "from", content, "to", new_content)
            with io.open(fname, 'wt') as fh:
                try:
                    fh.write(new_content)
                except Exception as e:
                    print("impossible to patch", fname, "from", content,
                          "to", new_content, " --- ", str(e).replace("\n", "--"))


WININST_PATTERN = r'([a-zA-Z0-9\-\_]*|[a-zA-Z\-\_\.]*)-([0-9\.\-]*[a-z]*[0-9]?)(-Qt-([0-9\.]+))?.(win32|win\-amd64)(-py([0-9\.]+))?(-setup)?\.exe'

# SOURCE_PATTERN defines what an acceptable source package name is
# As of 2014-09-08 :
#    - the wheel package format is accepte in source directory
#    - the tricky regexp is tuned also to support the odd jolib naming :
#         . joblib-0.8.3_r1-py2.py3-none-any.whl,
#         . joblib-0.8.3-r1.tar.gz

SOURCE_PATTERN = r'([a-zA-Z0-9\-\_\.]*)-([0-9\.\_]*[a-z]*[0-9]?)(\.zip|\.tar\.gz|\-(py[2-7]*|py[2-7]*\.py[2-7]*)\-none\-any\.whl)'

# WHEELBIN_PATTERN defines what an acceptable binary wheel package is
# "cp([0-9]*)" to replace per cp(34) for python3.4
# "win32|win\_amd64" to replace per "win\_amd64" for 64bit
WHEELBIN_PATTERN = r'([a-zA-Z0-9\-\_\.]*)-([0-9\.\_]*[a-z0-9\+]*[0-9]?)-cp([0-9]*)\-none\-(win32|win\_amd64)\.whl'


def get_source_package_infos(fname):
    """Return a tuple (name, version) of the Python source package"""
    match = re.match(SOURCE_PATTERN, osp.basename(fname))
    if match is not None:
        return match.groups()[:2]


def do_script(this_script, python_exe=None,
              verbose=False, install_options=None):
    """Execute a script (get-pip typically)"""
    if python_exe is None:
        python_exe = sys.executable
    assert osp.isfile(python_exe)
    myroot = os.path.dirname(python_exe)

    # cmd = [python_exe, myroot + r'\Scripts\pip-script.py', 'install']
    cmd = [python_exe]
    if install_options:
        cmd += install_options  # typically ['--no-deps']
        print('script install_options', install_options)
    cmd += [this_script]
    # print('build_wheel', myroot, cmd)
    print("Executing ", cmd)

    if verbose:
        subprocess.call(cmd, cwd=myroot)
    else:
        p = subprocess.Popen(cmd, cwd=myroot, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        p.communicate()
        p.stdout.close()
        p.stderr.close()
    if verbose:
        print("Executed " % cmd)
    return 'ok'


KEY_C = r"Software\Classes\%s"
KEY_C0 = KEY_C % r"Python.%sFile\shell"
KEY_C1 = KEY_C % r"Python.%sFile\shell\%s"
KEY_C2 = KEY_C1 + r"\command"
KEY_DROP0 = KEY_C % r"Python.%sFile\shellex"
KEY_DROP1 = KEY_C % r"Python.%sFile\shellex\DropHandler"
KEY_I = KEY_C % r"Python.%sFile\DefaultIcon"
KEY_D = KEY_C % r"Python.%sFile"
EWI = "Edit with IDLE"
EWS = "Edit with Spyder"

KEY_S = r"Software\Python"
KEY_S0 = KEY_S + r"\PythonCore"
KEY_S1 = KEY_S0 + r"\%s"


def register(target, current=True):
    """Register a Python distribution in Windows registry"""
    import winreg
    root = winreg.HKEY_CURRENT_USER if current else winreg.HKEY_LOCAL_MACHINE

    # Extensions
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C % ".py"),
                      "", 0, winreg.REG_SZ, "Python.File")
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C % ".pyw"),
                      "", 0, winreg.REG_SZ, "Python.NoConFile")
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C % ".pyc"),
                      "", 0, winreg.REG_SZ, "Python.CompiledFile")
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C % ".pyo"),
                      "", 0, winreg.REG_SZ, "Python.CompiledFile")

    # MIME types
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C % ".py"),
                      "Content Type", 0, winreg.REG_SZ, "text/plain")
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C % ".pyw"),
                      "Content Type", 0, winreg.REG_SZ, "text/plain")

    # Verbs
    python = osp.abspath(osp.join(target, 'python.exe'))
    pythonw = osp.abspath(osp.join(target, 'pythonw.exe'))
    spyder = osp.abspath(osp.join(target, os.pardir, 'Spyder.exe'))
    if not osp.isfile(spyder):
        spyder = '%s" "%s\Scripts\spyder' % (pythonw, target)
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C2 % ("", "open")),
                      "", 0, winreg.REG_SZ, '"%s" "%%1" %%*' % python)
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C2 % ("NoCon", "open")),
                      "", 0, winreg.REG_SZ, '"%s" "%%1" %%*' % pythonw)
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C2 % ("Compiled", "open")),
                      "", 0, winreg.REG_SZ, '"%s" "%%1" %%*' % python)
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C2 % ("", EWI)),
                      "", 0, winreg.REG_SZ,
                      '"%s" "%s\Lib\idlelib\idle.pyw" -n -e "%%1"'
                      % (pythonw, target))
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C2 % ("NoCon", EWI)),
                      "", 0, winreg.REG_SZ,
                      '"%s" "%s\Lib\idlelib\idle.pyw" -n -e "%%1"'
                      % (pythonw, target))
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C2 % ("", EWS)),
                      "", 0, winreg.REG_SZ, '"%s" "%%1"' % spyder)
    winreg.SetValueEx(winreg.CreateKey(root, KEY_C2 % ("NoCon", EWS)),
                      "", 0, winreg.REG_SZ, '"%s" "%%1"' % spyder)

    # Drop support
    handler = "{60254CA5-953B-11CF-8C96-00AA00B8708C}"
    for ftype in ("", "NoCon", "Compiled"):
        winreg.SetValueEx(winreg.CreateKey(root, KEY_DROP1 % ftype),
                          "", 0, winreg.REG_SZ, handler)

    # Icons
    dlls = osp.join(target, 'DLLs')
    winreg.SetValueEx(winreg.CreateKey(root, KEY_I % ""),
                      "", 0, winreg.REG_SZ, r'%s\py.ico' % dlls)
    winreg.SetValueEx(winreg.CreateKey(root, KEY_I % "NoCon"),
                      "", 0, winreg.REG_SZ, r'%s\py.ico' % dlls)
    winreg.SetValueEx(winreg.CreateKey(root, KEY_I % "Compiled"),
                      "", 0, winreg.REG_SZ, r'%s\pyc.ico' % dlls)

    # Descriptions
    winreg.SetValueEx(winreg.CreateKey(root, KEY_D % ""),
                      "", 0, winreg.REG_SZ, "Python File")
    winreg.SetValueEx(winreg.CreateKey(root, KEY_D % "NoCon"),
                      "", 0, winreg.REG_SZ, "Python File (no console)")
    winreg.SetValueEx(winreg.CreateKey(root, KEY_D % "Compiled"),
                      "", 0, winreg.REG_SZ, "Compiled Python File")

    # PythonCore entries
    '''
    short_version = utils.get_python_infos(target)[0]
    long_version = utils.get_python_long_version(target)
    key_core = (KEY_S1 % short_version) + r'\%s'
    winreg.SetValueEx(winreg.CreateKey(root, key_core % 'InstallPath'),
                      "", 0, winreg.REG_SZ, target)
    winreg.SetValueEx(winreg.CreateKey(root,
                                       key_core % r'InstallPath\InstallGroup'),
                      "", 0, winreg.REG_SZ, "Python %s" % short_version)
    winreg.SetValueEx(winreg.CreateKey(root, key_core % 'Modules'),
                      "", 0, winreg.REG_SZ, "")
    winreg.SetValueEx(winreg.CreateKey(root, key_core % 'PythonPath'),
                      "", 0, winreg.REG_SZ,
                      r"%s\Lib;%s\DLLs" % (target, target))
    winreg.SetValueEx(winreg.CreateKey(root,
                                       key_core % r'Help\Main Python Documentation'),
                      "", 0, winreg.REG_SZ,
                      r"%s\Doc\python%s.chm" % (target, long_version))
    '''

    # Create start menu entries for all WinPython launchers
    '''
    for path, desc, fname in _get_shortcut_data(target, current=current):
        utils.create_shortcut(path, desc, fname)
    '''

    # Register the Python ActiveX Scripting client (requires pywin32)
    axscript = osp.join(target, 'Lib', 'site-packages', 'win32comext',
                        'axscript', 'client', 'pyscript.py')
    if osp.isfile(axscript):
        subprocess.call('"%s" "%s"' % (python, axscript), cwd=target)
    else:
        print('Unable to register ActiveX: please install pywin32',
              file=sys.stderr)


'''
def unregister(target, current=True):
    """Unregister a Python distribution in Windows registry"""
    # Registry entries
    root = winreg.HKEY_CURRENT_USER if current else winreg.HKEY_LOCAL_MACHINE
    short_version = utils.get_python_infos(target)[0]
    key_core = (KEY_S1 % short_version) + r'\%s'
    for key in (
        # Drop support
        KEY_DROP1 % "", KEY_DROP1 % "NoCon", KEY_DROP1 % "Compiled",
        KEY_DROP0 % "", KEY_DROP0 % "NoCon", KEY_DROP0 % "Compiled",
        # Icons
        KEY_I % "NoCon", KEY_I % "Compiled", KEY_I % "",
        # Edit with IDLE
                KEY_C2 % ("", EWI), KEY_C2 % ("NoCon", EWI),
                KEY_C1 % ("", EWI), KEY_C1 % ("NoCon", EWI),
                # Edit with Spyder
                KEY_C2 % ("", EWS), KEY_C2 % ("NoCon", EWS),
                KEY_C1 % ("", EWS), KEY_C1 % ("NoCon", EWS),
                # Verbs
                KEY_C2 % ("", "open"),
                KEY_C2 % ("NoCon", "open"),
                KEY_C2 % ("Compiled", "open"),
                KEY_C1 % ("", "open"),
                KEY_C1 % ("NoCon", "open"),
                KEY_C1 % ("Compiled", "open"),
                KEY_C0 % "", KEY_C0 % "NoCon", KEY_C0 % "Compiled",
                # Descriptions
                KEY_D % "NoCon", KEY_D % "Compiled", KEY_D % "",
                # PythonCore
                key_core % r'InstallPath\InstallGroup',
                key_core % 'InstallPath',
                key_core % 'Modules',
                key_core % 'PythonPath',
                key_core % r'Help\Main Python Documentation',
                key_core % 'Help',
                KEY_S1 % short_version, KEY_S0, KEY_S,
    ):
        try:
            print(key)
            winreg.DeleteKey(root, key)
        except WindowsError:
            rootkey = 'HKEY_CURRENT_USER' if current else 'HKEY_LOCAL_MACHINE'
            print(r'Unable to remove %s\%s' % (rootkey, key), file=sys.stderr)

    # Start menu shortcuts
    for path, desc, fname in _get_shortcut_data(target, current=current):
        if osp.exists(fname):
            os.remove(fname)
'''
