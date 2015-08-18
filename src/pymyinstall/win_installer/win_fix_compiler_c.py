"""
@file
@brief Various to set up a C++ compiler
"""
import os


def switch_to_VS_compiler(python_path, version=12):
    """
    applies fix described in `Build a Python 64 bit extension on Windows 8 <http://www.xavierdupre.fr/blog/2013-07-07_nojs.html>`_

    @param  python_path     python path
    @param  version         Visual Studio version, 12 = VS2013
    @return                 impacted files
    """
    name = os.path.join(python_path, "Lib", "distutils", "msvc9compiler.py")
    with open(name, "r") as f:
        content = f.read()
    content = content.replace(
        "'win-amd64' : 'amd64',", "'win-amd64' : 'x86_amd64',")
    content = content.replace(
        "if majorVersion >= 6:", "if majorVersion >= 6 :\n        majorVersion = " + str(version))
    with open(name, "w") as f:
        f.write(content)
    return [name]


def switch_to_mingw_compiler(python_path):
    """
    applies a fix to use MinGW to compile extensions (does not work with Jupyter)

    @param  python_path     python path
    """
    dirname = os.path.join(python_path, "Lib", "distutils")
    cfg = os.path.join(dirname, "distutils.cfg")
    with open(cfg, "w") as f:
        f.write("""[build]
                    compiler = mingw32

                    [build_ext]
                    compiler = mingw32
                    """.replace("                            ", ""))
    return [cfg]
