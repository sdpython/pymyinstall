# -*- coding: utf-8 -*-
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
       "run27" in sys.argv or \
       "sdist" in sys.argv or \
       "setupdep" in sys.argv or \
       "test_local_pypi" in sys.argv or \
       "upload_docs" in sys.argv or \
       "setup_hook" in sys.argv or \
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
                        "pyquickhelper",
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

if is_local():
    def write_version():
        pyquickhelper = import_pyquickhelper()
        from pyquickhelper import write_version_for_setup
        return write_version_for_setup(__file__)

    if sys.version_info[0] != 2:
        write_version()

    if os.path.exists("version.txt"):
        with open("version.txt", "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
    else:
        raise FileNotFoundError("version.txt")
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

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

if "--verbose" in sys.argv:
    verbose()

if is_local():
    pyquickhelper = import_pyquickhelper()
    r = pyquickhelper.process_standard_options_for_setup(
        sys.argv, __file__, project_var_name,
        additional_notebook_path=["pyquickhelper"],
        unittest_modules=["pyquickhelper"])

    if "build_script" in sys.argv and sys.platform.startswith("win"):
        this = os.path.dirname(__file__)
        with open(os.path.join(this, "auto_setup_build_sphinx.bat"), "r") as f:
            content = f.read()
        code = "%pythonexe% -u -c \"import sys;sys.path.append('src');from pymyinstall.packaged import update_all;update_all(temp_folder='build/update_modules', verbose=True)\""
        content = content.replace("%pythonexe% -u setup.py build_sphinx", code)
        with open(os.path.join(this, "auto_update_modules.bat"), "w") as f:
            f.write(content)

else:
    r = False

if len(sys.argv) == 1 and "--help" in sys.argv:
    pyquickhelper = import_pyquickhelper()
    pyquickhelper.process_standard_options_for_setup_help()

if not r:

    if sys.version_info[0] >= 3:
        entry_points = {
            'console_scripts': [
                'pymy_update3 = pymyinstall.scripts.pymy_update:main',
                'pymy_install3 = pymyinstall.scripts.pymy_install:main',
            ]}
        if sys.platform.startswith("win"):
            entry_points['console_scripts'].extend([
                'pymy_update = pymyinstall.scripts.pymy_update:main',
                'pymy_install = pymyinstall.scripts.pymy_install:main',
            ])
    else:
        entry_points = {
            'console_scripts': [
                'pymy_update = pymyinstall.scripts.pymy_update:main',
                'pymy_install = pymyinstall.scripts.pymy_install:main',
            ]}

    setup(
        name=project_var_name,
        version='%s%s' % (sversion, subversion),
        author='Xavier Dupré',
        author_email='xavier.dupre AT gmail.com',
        url="http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html",
        download_url="https://github.com/sdpython/pymyinstall/",
        description=DESCRIPTION,
        long_description=long_description,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        install_requires=["pip>=7.1", "pipdeptree"],
        entry_points=entry_points
    )
