# -*- coding: utf-8 -*-
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
        "asn1crypto",
        "astroid",
        "attrs",
        "autopep8",
        "babel",
        'backcall',
        "backports_abc",
        "backports.shutil-get-terminal-size",
        "bleach",
        "blockdiag",
        "brewer2mpl",
        "cairocffi",
        "cairosvg",
        "certifi",
        "cffi",
        "chardet",
        "codecov",
        "colorama",
        "coverage",
        "cryptography",
        "cssselect2",
        "Cython",
        "cycler",
        "DataProperty",
        "decorator",
        "defusedxml",  # cairosvg
        "docformatter",
        "docutils",
        "entrypoints",
        "et_xmlfile",
        "filelock",
        "funcparserlib",
        "git-pandas",
        "gitdb2",
        "gitpython",
        "html5lib",
        "idna",
        "imagesize",
        "importlib_metadata",
        "ipython",
        "ipykernel",
        "ipympl",
        "ipystata" if sys.version_info[0] == 2 else None,
        "ipython_genutils",
        "ipywidgets",
        "isort",
        "jdcal",
        "jedi",
        "jeepney",
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
        "kiwisolver",
        "lazy_object_proxy",
        "logbook",
        "lxml",
        "matplotlib",
        "mbstrdecoder",
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
        "nose",
        "notebook",
        "notedown",
        "numpy",
        "olefile",
        "openpyxl",
        "path.py",
        "pbr",
        "packaging",
        "pandas",
        "pandoc-attributes",
        "pandocfilters",
        "parso",
        "pathvalidate",
        "patsy",
        "pep8",
        "pexpect",
        "pickleshare",
        "Pillow",
        "pipdeptree",
        "prometheus_client",
        "prompt_toolkit",
        "psutil",
        "ptyprocess",
        "pycodestyle",
        "pycparser",
        "pygments",
        "pylint",
        "pyparsing",
        'pypiserver',
        'pyrsistent',
        "python-dateutil",
        "python-jenkins",
        "pytz",
        "pywin32" if sys.platform.startswith("win") else None,
        "pywin32-ctypes" if sys.platform.startswith("win") else None,
        'pywinpty',
        "pyzmq",
        "qtconsole",
        "requests",
        "secretstorage",
        "semantic_version",
        "simplegeneric",
        "Send2Trash",
        "six",
        "smmap2",
        'snowballstemmer',
        "sphinx",
        "sphinxcontrib-websupport",
        "sphinx_gallery",
        'sphinxcontrib-applehelp',
        'sphinxcontrib-devhelp',
        "sphinxcontrib-blockdiag",
        'sphinxcontrib-htmlhelp',
        'sphinxcontrib-imagesvg',
        'sphinxcontrib-jsdemo',
        'sphinxcontrib-jsmath',
        'sphinxcontrib-qthelp',
        'sphinxcontrib-serializinghtml',
        'sphinxcontrib-websupport',
        'sphinx-rtd-theme',
        "tabledata",
        'tabulate',
        "terminado",
        "testpath",
        "tinycss2",
        "tornado",
        'tqdm',
        "traitlets",
        "typepy",
        "unify",
        "untokenize",
        "urllib3",
        "virtualenv",
        "xlrd",
        "xlsxwriter",
        "xlwt",
        "wcwidth",
        "webcolors",
        "webencodings",
        "wheel",
        "widgetsnbextension",
        "wild_sphinx_theme",
        "win_unicode_console",
        "winrandom" if sys.platform.startswith("win") else None,
        "winshell" if sys.platform.startswith("win") else None,
        "wrapt",  # astroid
        "zipp",
    ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
