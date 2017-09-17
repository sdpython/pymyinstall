# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
import warnings
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########

project_var_name = "pymyinstall"
sversion = "1.1"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = project_var_name + ', installation, Xavier Dupré'
DESCRIPTION = """Easy installation of modules for data scientists"""
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
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

############
# functions
############


def is_local():
    file = os.path.abspath(__file__).replace("\\", "/").lower()
    if "/temp/" in file and "pip-" in file:
        return False
    if \
       "bdist_msi" in sys.argv or \
       "build27" in sys.argv or \
       "build_script" in sys.argv or \
       "build_sphinx" in sys.argv or \
       "build_ext" in sys.argv or \
       "bdist_wheel" in sys.argv or \
       "bdist_wininst" in sys.argv or \
       "clean_pyd" in sys.argv or \
       "clean_space" in sys.argv or \
       "copy27" in sys.argv or \
       "copy_dist" in sys.argv or \
       "local_pypi" in sys.argv or \
       "notebook" in sys.argv or \
       "publish" in sys.argv or \
       "publish_doc" in sys.argv or \
       "register" in sys.argv or \
       "unittests" in sys.argv or \
       "unittests_LONG" in sys.argv or \
       "unittests_SKIP" in sys.argv or \
       "unittests_GUI" in sys.argv or \
       "run27" in sys.argv or \
       "sdist" in sys.argv or \
       "setupdep" in sys.argv or \
       "test_local_pypi" in sys.argv or \
       "upload_docs" in sys.argv or \
       "setup_hook" in sys.argv or \
       "copy_sphinx" in sys.argv or \
       "write_version" in sys.argv:
        try:
            import_pyquickhelper()
        except ImportError as e:
            warnings.warn(str(e))
            raise e
        return True
    else:
        return False


def import_pyquickhelper():
    try:
        import pyquickhelper
    except ImportError:
        sys.path.append(
            os.path.normpath(
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        "..",
                        "pyquickhelper" if sys.version_info[
                            0] >= 3 else "py27_pyquickhelper_27",
                        "src"))))
        try:
            import pyquickhelper
        except ImportError as e:
            message = "module pyquickhelper is needed to build the documentation ({0}), not found in path {1}".format(
                sys.executable,
                sys.path[
                    -1])
            raise ImportError(message) from e
    return pyquickhelper


def verbose():
    print("---------------------------------")
    print("package_dir =", package_dir)
    print("packages    =", packages)
    print("package_data=", package_data)
    print("current     =", os.path.abspath(os.getcwd()))
    print("---------------------------------")

##########
# version
##########


if is_local() and "--help" not in sys.argv and "--help-commands" not in sys.argv:
    def write_version():
        pyquickhelper = import_pyquickhelper()
        from pyquickhelper.pycode import write_version_for_setup
        return write_version_for_setup(__file__)

    if sys.version_info[0] != 2:
        write_version()

    versiontxt = os.path.join(os.path.dirname(__file__), "version.txt")
    if os.path.exists(versiontxt):
        with open(versiontxt, "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
        if subversion == ".0":
            raise Exception("Subversion is wrong: '{0}'.".format(subversion))
    else:
        raise FileNotFoundError(versiontxt)
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

if "upload" in sys.argv and not subversion:
    # avoid uploading with a wrong subversion number
    try:
        import pyquickhelper
        pyq = True
    except ImportError:
        pyq = False
    raise Exception(
        "subversion is empty, cannot upload, is_local()={0}, pyquickhelper={1}".format(is_local(), pyq))

##############
# common part
##############

if os.path.exists(readme):
    if sys.version_info[0] == 2:
        from codecs import open
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""
if os.path.exists(history):
    if sys.version_info[0] == 2:
        from codecs import open
    with open(history, "r", encoding='utf-8-sig') as f:
        long_description += f.read()

if "--verbose" in sys.argv:
    verbose()


def file_filter_pep8(filename):
    filename = filename.replace("\\", "/")
    return "/whl/" not in filename


if is_local():
    pyquickhelper = import_pyquickhelper()
    logging_function = pyquickhelper.get_fLOG()
    from pyquickhelper.pycode import process_standard_options_for_setup
    logging_function(OutputPrint=True)
    r = process_standard_options_for_setup(
        sys.argv, __file__, project_var_name,
        # not need for the regular setup, just for the documentation, unit
        layout=["html"],
        # tests
        requirements=["pyquickhelper"],
        additional_notebook_path=["pyquickhelper", "jyquickhelper"],
        additional_local_path=["pyquickhelper"],
        unittest_modules=["pyquickhelper"], fLOG=logging_function,
        covtoken=("b67b3051-8c5d-460b-b2fa-51d81ab7008c",
                  "'_UT_36_std' in outfile"),
        file_filter_pep8=file_filter_pep8)
    if not r and not ({"bdist_msi", "sdist",
                       "bdist_wheel", "publish", "publish_doc", "register",
                       "upload_docs", "bdist_wininst", "build_ext"} & set(sys.argv)):
        raise Exception("unable to interpret command line: " + str(sys.argv))
else:
    r = False

if not r:
    if len(sys.argv) in (1, 2) and sys.argv[-1] in ("--help-commands",):
        pyquickhelper = import_pyquickhelper()
        from pyquickhelper.pycode import process_standard_options_for_setup_help
        process_standard_options_for_setup_help(sys.argv, fLOG=print)

    if sys.version_info[0] >= 3:
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
    else:
        entry_points = {
            'console_scripts': [
                'pymy_update = pymyinstall.cli.pymy_update:main',
                'pymy_install = pymyinstall.cli.pymy_install:main',
                'pymy_deps = pymyinstall.cli.pymy_deps:main',
                'pymy_status = pymyinstall.cli.pymy_status:main',
            ]}

    setup(
        name=project_var_name,
        version='%s%s' % (sversion, subversion),
        author='Xavier Dupré',
        author_email='xavier.dupre@gmail.com',
        license="MIT",
        url="http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html",
        download_url="https://github.com/sdpython/pymyinstall/",
        description=DESCRIPTION,
        long_description=long_description,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        install_requires=["setuptools", "pip>=7.1"],
        entry_points=entry_points,
    )
