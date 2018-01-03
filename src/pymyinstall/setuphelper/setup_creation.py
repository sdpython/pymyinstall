# -*- coding: utf-8 -*-
"""
@file
@brief Functions to help creating a setup

.. versionadded:: 1.1
"""
import os
import sys
from ..installhelper import run_cmd

_setup_py = """
# -*- coding: utf-8 -*-
import sys
import os
import warnings
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########


project_var_name = "__NAME__"
sversion = "__VERSION__"
subversion = "__SUBVERSION__"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'


KEYWORDS = project_var_name
DESCRIPTION = '''__DESCRIPTION___'''
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]


#######
# data
#######

packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {
    project_var_name : ["*.pyd", "*.dll", "*.so" ],
}


def verbose():
    print("---------------------------------")
    print("package_dir =", package_dir)
    print("packages    =", packages)
    print("package_data=", package_data)
    print("current     =", os.path.abspath(os.getcwd()))
    print("---------------------------------")


setup(
    name=project_var_name,
    version='%s%s' % (sversion, subversion),
    author='__AUTHOR__',
    author_email='__EMAIL__',
    url="__URL__",
    download_url="__DURL__",
    description=DESCRIPTION,
    long_description=long_description,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    install_requires=[]
)
"""

_readme_rst = '''
.. _l-README:

README / Changes
================

.. image:: https://travis-ci.org/sdpython/pymyinstall.svg?branch=master
    :target: https://travis-ci.org/sdpython/pymyinstall
    :alt: Build status

.. image:: https://badge.fury.io/py/pymyinstall.svg
    :target: http://badge.fury.io/py/pymyinstall

.. image:: http://img.shields.io/pypi/dm/pymyinstall.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/pymyinstall

.. image:: http://img.shields.io/github/issues/sdpython/pymyinstall.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pymyinstall/issues

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT


**Links:**

* `GitHub/__NAME__ <__URL__>`_
* `documentation <__URL__>`_
* `Blog <http:/__NAME__/helpsphinx/blog/main_0000.html#ap-main-0>`_
'''

if sys.version_info[0] == 2:
    from codecs import open


def create_empty_folder_setup(fold, name, author=None, description=None, url=None, durl=None, version="0.1",
                              subversion="0"):
    """
    Creates a quick empty shell for a new project.

    @param      fold        location
    @param      name        name of the project
    @param      author      author
    @param      description description
    @param      url         url for the documentation
    @param      durl        url to download it
    @param      version     version
    @param      subversion  third part of the version number
    @return                 list of created files
    """
    src = os.path.join(fold, "src")
    mod = os.path.join(src, name)
    create = [fold, src, mod]
    for f in create:
        if not os.path.exists(f):
            os.makedirs(f)

    replace = dict(__AUTHOR__=author,
                   __DESCRIPTION__=description,
                   __URL__=url,
                   __DURL__=durl,
                   __VERSION__=version,
                   __SUBVERSION__=subversion,
                   __NAME__=name)

    def adapt(content):
        for k, v in replace.items():
            if v is not None:
                content = content.replace(k, v)
        return content

    readme = os.path.join(fold, "README.rst")
    with open(readme, "w", encoding="utf-8") as f:
        f.write(adapt(_readme_rst))

    setup = os.path.join(fold, "setup.py")
    with open(setup, "w", encoding="utf-8") as f:
        f.write(adapt(_setup_py))

    writ = [setup, readme]

    if sys.platform.startswith("win"):
        bat = os.path.join(fold, "wheel.bat")
        with open(bat, "w") as f:
            f.write("{0} setup.py bdist_wheel".format(sys.executable))
        writ.append(bat)

    return writ


_setup_py_existing = """
# -*- coding: utf-8 -*-
import sys
import os
import warnings
from distutils.core import setup
from setuptools import find_packages

DESCRIPTION = '''__DESCRIPTION__'''

packages = find_packages('src', exclude='src')
package_dir = {k: 'src/' + k.replace(".", "/") for k in packages}
package_data = {
__PACKDATA__
}

setup(name="__FOLDER__", version="__VERSION__",
    description=DESCRIPTION, long_description=DESCRIPTION,
    packages=packages, package_dir=package_dir,
    package_data=package_data
)
"""


def create_folder_setup(fold, wheel=True, output_path=None, fLOG=None, version=None, description=None):
    """
    Creates a quick setup for an existing or installed projects.

    @param      fold            folder or module (must be imported first)
    @param      wheel           run the setup to build the wheel
    @param      output_path     copies everything here it not None
    @param      version         to overwrite version
    @param      description     to overwrite description
    @return                     list of created files

    .. exref::
        :title: Create a setup from installed packages
        :lid: ex-torch-setup

        This packages :epkg:`pandas` into a wheel from the installed
        sources. Location of the sources can be specified too.

        ::

            from pymyinstall.setuphelper import create_folder_setup
            create_folder_setup('pandas', fLOG=print, output_path='.')
    """
    if fLOG:
        fLOG("[create_folder_setup] process '{0}'".format(fold))
    if not os.path.exists(fold):
        if fold not in sys.modules:
            raise ValueError("Unable to find module '{0}'".format(fold))
        mod = sys.modules[fold]
        info = dict(__VERSION__=mod.__version__,
                    __DESCRIPTION__=mod.__doc__,
                    __FOLDER__=fold)
        fold = os.path.dirname(mod.__file__)
    else:
        info = dict()

    # Module name
    name = os.path.split(fold)[-1]
    if fLOG:
        fLOG("[create_folder_setup] name='{0}'".format(name))
        fLOG("[create_folder_setup] fold='{0}'".format(fold))

    if output_path is not None:
        # Copies everything.
        if fLOG:
            fLOG("[create_folder_setup] copy to '{0}'".format(output_path))
        from pyquickhelper.filehelper import synchronize_folder
        dest = os.path.join(output_path, 'src', name)
        if not os.path.exists(dest):
            os.makedirs(dest)
        # , filter_copy=lambda name: '__pycache__' not in name)
        synchronize_folder(fold, dest)
        fold = dest
        fold_ = output_path
    else:
        raise ValueError("output_path must be specified")

    if len(info) == 0 and version is None:
        # Import the module.
        if name in sys.modules:
            del sys.modules[name]
        f = os.path.normpath(os.path.abspath(fold))
        f_ = os.path.normpath(os.path.join(fold, '..'))
        if fold_ not in sys.path:
            sys.path.insert(0, f_)
            rem = True
        else:
            rem = False

        mod = __import__(name)
        if rem:
            ind = sys.path.index(f_)
            del sys.path[ind]
        del sys.modules[name]

        info = dict(__VERSION__=mod.__version__,
                    __DESCRIPTION__=description or mod.__doc__,
                    __FOLDER__=name)
    else:
        info = dict(__VERSION__=version,
                    __DESCRIPTION__=description,
                    __FOLDER__=name)

    # Package data
    from pyquickhelper.filehelper import explore_folder
    _, files = explore_folder(fold, fullname=False)
    pack = {}
    for f in files:
        ff = os.path.split(f)[0]
        f = os.path.relpath(f, fold)
        if '__pycache__' in f:
            continue
        ext = os.path.splitext(f)[-1]
        if ext in {'.py', '.pyc'}:  # , '.pyd'}:
            continue
        f, n = os.path.split(f)
        f = f .replace("\\", "/").replace("/", ".")
        if f not in pack:
            pack[f] = []
            init = os.path.join(ff, "__init__.py")
            while not os.path.exists(init):
                if fLOG:
                    fLOG("[create_folder_setup] add '{0}'".format(init))
                with open(init, "w") as fi:
                    fi.write('# added for additional files')
                ff = os.path.split(ff)[0]
                init = os.path.join(ff, "__init__.py")
        pack[f].append(n)

        if fLOG:
            fLOG("[create_folder_setup] add '{0}' in '{1}'".format(n, f))

    rows = ["  '{2}{3}{0}': {1},".format(
        k, v, name, '.' if k else '') for k, v in pack.items()]
    info['__PACKDATA__'] = "\n".join(rows)

    # Writes setup.py
    script = _setup_py_existing
    for k, v in info.items():
        if v is not None:
            script = script.replace(k, v)
    setup = os.path.join(fold_, 'setup.py')
    if fLOG:
        fLOG("[create_folder_setup] write='{0}'".format(setup))
    with open(setup, "w") as f:
        f.write(script)

    if wheel:
        cmd = '"{0}" -u setup.py bdist_wheel'.format(
            sys.executable.replace("w.exe", ".exe"))
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG, change_path=fold_)
        if fLOG:
            fLOG('[create_folder_setup] OUT --------------\n' + out)
            fLOG('[create_folder_setup] ERR --------------\n' + err)
        return [setup]
    else:
        return [setup]
