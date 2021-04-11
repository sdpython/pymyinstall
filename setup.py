# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
import warnings
from setuptools import setup, find_packages
from pyquicksetup import read_version, read_readme, default_cmdclass


#########
# settings
#########


project_var_name = "pymyinstall"
project_owner = 'sdpython'
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = project_var_name + ', installation, Xavier Dupré'
DESCRIPTION = """Easy installation of modules for data scientists"""
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
    project_var_name + ".win_installer": ["*.r", "*.jl", "*.iss"],
    project_var_name + ".win_installer.icons": ["*.ico"],
    project_var_name + ".win_installer.tutorial.french": ["*.xlsx"],
}


entry_points = {
    'console_scripts': [
        'pymy_update3 = pymyinstall.cli.pymy_update:main',
        'pymy_install3 = pymyinstall.cli.pymy_install:main',
        'pymy_deps3 = pymyinstall.cli.pymy_deps:main',
        'pymy_status3 = pymyinstall.cli.pymy_status:main',
    ]}
if sys.platform.startswith("win"):
    entry_points['console_scripts'].extend([
        'pymy_update = pymyinstall.cli.pymy_update:main',
        'pymy_install = pymyinstall.cli.pymy_install:main',
        'pymy_deps = pymyinstall.cli.pymy_deps:main',
        'pymy_status = pymyinstall.cli.pymy_status:main',
    ])

setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name, subfolder='src'),
    author='Xavier Dupré',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html",
    download_url="https://github.com/sdpython/pymyinstall/",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=default_cmdclass(),
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    install_requires=["setuptools", "pip>=10.0", "urllib3",
                      "requests", 'pyquicksetup>=0.2'],
    entry_points=entry_points,
)
