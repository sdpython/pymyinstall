# -*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""


def pyensae_set():
    """
    list of modules needed to run unit test of module *pyensae*
    """
    from .packaged_config_0_pyquickhelper import pyquickhelper_set
    from .packaged_config_4_ml import ensae_set
    names = pyquickhelper_set()
    names += [
        "adal",
        "ansi2html",  # ssh
        "ansiconv",  # ssh
        "antlr4-python3-runtime",
        "asn1crypto",
        "bcrypt",
        "beautifulsoup4",
        "branca",
        "cffi",
        "colorlog",
        "colormap",
        "cryptography",
        "dbfread",
        "dominate",
        "easydev",
        "ecdsa",  # paramiko
        "elasticsearch",
        "folium",  # maps
        "idna",
        "ijson",
        "inflection",  # quandl
        "ipaddress",
        "ipykernel",
        "isodate",
        "python3-linkedin",
        "markdown2",
        "more-itertools",
        "mpl_finance",
        "msrest",
        "msrestazure",
        "networkx",
        "ndg-httpsclient",  # quandl
        "oauthlib",
        "osmapi",  # maps
        "pandas-datareader",
        "paramiko",  # ssh
        "pyasn1",
        "pycrypto",  # paramiko, cannot be replaced by pycryptodome
        "pycryptodomex",
        "pycurl",  # markdown2
        "PyJWT",
        "pynacl",  # paramiko
        "pyopenssl",  # quandl
        "pyquickhelper",
        "pytablereader",
        "pytablewriter",
        "qgrid",  # magic command
        "quandl",
        "requests_file",
        "requests-ftp",
        "requests_oauthlib",
        "scipy",
        "scikit-learn",
        "simplesqlite",
        "toml",
        "wrapt",
    ]

    for m in ensae_set():
        if m.name.startswith("azure"):
            names.append(m)

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
