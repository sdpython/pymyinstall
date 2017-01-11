"""
@file
@brief Functions to help creating a setup

.. versionadded:: 1.1
"""
import os
import sys

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
    project_var_name : ["*.pyd", "*.dll" ],
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
    * `pypi/__NAME__ <__URL__>`_
    * `GitHub/__NAME__ <__URL__>`_
    * `documentation <__URL__>`_
    * `Travis <https://travis-ci.org/__ALIAS__/__NAME__>`_
    * `Blog <http:/__NAME__/helpsphinx/blog/main_0000.html#ap-main-0>`_


Getting started
---------------

* to be defined


Functionalities
---------------

* to be defined


Versions
--------

* **0.1 - 2016/??/??**
    * **new:** first version
'''

if sys.version_info[0] == 2:
    from codecs import open


def create_empty_folder_setup(fold, name, author=None, description=None, url=None, durl=None, version="0.1",
                              subversion="0"):
    """
    create a quick empty shell for a new project

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
