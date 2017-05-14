#-*- coding: utf-8 -*-
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
        "azure",
        "azure-batch",
        "azure-common",
        "azure-graphrbac",
        "azure-mgmt",
        "azure-mgmt-nspkg",
        "azure-mgmt-authorization",
        "azure-mgmt-common",
        "azure-mgmt-batch",
        "azure-mgmt-cdn",
        "azure-mgmt-cognitiveservices",
        "azure-mgmt-commerce",
        "azure-mgmt-compute",
        "azure-mgmt-logic",
        "azure-mgmt-network",
        "azure-mgmt-notificationhubs",
        "azure-mgmt-powerbiembedded",
        "azure-mgmt-redis",
        "azure-mgmt-resource",
        "azure-mgmt-scheduler",
        "azure-mgmt-storage",
        "azure-mgmt-web",
        "azure-nspkg",
        "azure-servicebus",
        "azure-servicemanagement-legacy",
        "azure-storage",
        "azureml",
        "beautifulsoup4",
        "branca",
        "cffi",
        "colormap",
        "chardet",
        "cryptography",
        "dataproperty",
        "dbfread",
        "dominate",
        "easydev",
        "ecdsa",  # paramiko
        "folium",  # maps
        "idna",
        "ipykernel",
        "isodate",
        "keyring",
        "python3-linkedin",
        "logbook",
        "markdown2",
        "msrest",
        "msrestazure",
        "mbstrdecoder",
        "networkx",
        "oauthlib",
        "osmapi",  # maps
        "packaging",
        "pandas_datareader",
        "paramiko",  # ssh
        "pathvalidate",
        "prompt_toolkit",
        "pyasn1",
        "pycodestyle",
        "pycrypto",  # paramiko, cannot be replaced by pycryptodome
        "pycryptodomex",
        "PyJWT",
        "pyquickhelper",
        "simplesqlite",
        "pytablereader",
        "pytablewriter",
        "qgrid",  # magic command
        "requests_file",
        "requests-ftp",
        "requests_oauthlib",
        "scipy",
        "scikit-learn",
        "toml",
        "typepy",
        "urllib3",
        "xlsxwriter",
        "xlwt",
    ]

    for m in ensae_set():
        if m.name.startswith("azure"):
            names.append(m)

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
