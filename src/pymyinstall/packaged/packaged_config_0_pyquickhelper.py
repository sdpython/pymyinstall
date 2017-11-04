#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""
import sys


def pyquickhelper_set():
    """
    list of modules needed to run unit test of module *pyquickhelper*
    """
    names = [
        "alabaster",
        "autopep8",
        "babel",
        "backports.shutil-get-terminal-size",
        "bleach",
        "blockdiag",
        "brewer2mpl",
        "certifi",
        "codecov",
        "colorama",
        "coverage",
        "Cython",
        "cycler",
        "decorator",
        "docformatter",
        "docutils",
        "entrypoints",
        "et_xmlfile",
        "filelock",
        "flake8",
        "funcparserlib",
        "git-pandas",
        "gitdb2",
        "gitpython",
        "husl",
        "html5lib",
        "imagesize",
        "ipython",
        "ipykernel",
        "ipympl",
        "ipystata" if sys.version_info[0] == 2 else None,
        "ipython_genutils",
        "ipywidgets",
        "isort",
        "jedi",
        "jinja2",
        "jsonschema",
        "jupyter-console",
        "jupyter",
        "jupyter_core",
        "jupyter_client",
        "jupyter-pip",
        "jupyter_sphinx",
        "jyquickhelper",
        "keyring",
        "lxml",
        "matplotlib",
        "metakernel",
        "micropython-libc" if not sys.platform.startswith("win") else None,
        "micropython-ffilib" if not sys.platform.startswith(
            "win") else None,
        "micropython-fcntl" if not sys.platform.startswith(
            "win") else None,
        'markupsafe',
        "mccabe",
        "mistune",
        "multi_key_dict",
        "nbformat",
        "nbconvert",
        "nbpresent",
        "nbsphinx",
        "nose",
        "backports_abc",
        "notebook",
        "notedown",
        "numpy",
        "jdcal",
        "olefile",
        "openpyxl",
        "path.py",
        "pbr",
        "pandas",
        "pandoc-attributes",
        "pandocfilters",
        "parso",
        "patsy",
        "pep8",
        "pexpect",  # if not sys.platform.startswith("win") else None,
        "pickleshare",
        "Pillow",
        "pipdeptree",
        "prompt_toolkit",
        "psutil",
        "ptyprocess",  # if not sys.platform.startswith("win") else None,
        "pycodestyle",
        "pydocstyle",
        "pycparser",
        "pyflakes",
        "pygments",
        "pyparsing",
        'pypiserver',
        "python-dateutil",
        "python-jenkins",
        "pytz",
        "pywin32" if sys.platform.startswith("win") else None,
        "pywin32-ctypes" if sys.platform.startswith("win") else None,
        "pyzmq",
        "qtconsole",
        "releases",
        "requests",
        "semantic_version",
        "simplegeneric",
        "six",
        "smmap2",
        "sphinx",
        "sphinx_gallery",
        "sphinxcontrib-blockdiag",
        'sphinxcontrib-images',
        'sphinxcontrib-imagesvg',
        'sphinxcontrib-jsdemo',
        'snowballstemmer',
        'sphinx-rtd-theme',
        "sphinxjp.themes.revealjs",
        'tabulate',
        'tqdm',
        "terminado" if not sys.platform.startswith("win") else None,
        "testpath",
        "tornado",
        "traitlets",
        "unify",
        "untokenize",
        "urllib3",
        "virtualenv",
        "xlrd",
        "wcwidth",
        "webcolors",
        "webencodings",
        "wheel",
        "widgetsnbextension",
        "wild_sphinx_theme",
        "win_unicode_console",
        "winrandom" if sys.platform.startswith("win") else None,
        "winshell" if sys.platform.startswith("win") else None,
    ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
