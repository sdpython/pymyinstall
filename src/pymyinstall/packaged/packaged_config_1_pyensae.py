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
        "azure-mgmt-authorization",
        "azure-mgmt-batch",
        "azure-mgmt-cdn",
        "azure-mgmt-cognitiveservices",
        "azure-mgmt-commerce",
        "azure-mgmt-common",
        "azure-mgmt-compute",
        "azure-mgmt-logic",
        "azure-mgmt-network",
        "azure-mgmt-notificationhubs",
        "azure-mgmt-nspkg",
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
        "azure-datalake-store",
        "azure-keyvault",
        "azure-mgmt-containerregistry",
        "azure-mgmt-datalake-analytics",
        "azure-mgmt-datalake-nspkg",
        "azure-mgmt-datalake-store",
        "azure-mgmt-devtestlabs",
        "azure-mgmt-dns",
        "azure-mgmt-documentdb",
        "azure-mgmt-iothub",
        "azure-mgmt-keyvault",
        "azure-mgmt-monitor",
        "azure-mgmt-rdbms",
        "azure-mgmt-sql",
        "azure-mgmt-trafficmanager",
        "azure-servicefabric",
        "azureml",
        "bcrypt",
        "beautifulsoup4",
        "branca",
        "cffi",
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
        "msrest",
        "msrestazure",
        "networkx",
        "ndg-httpsclient",  # quandl
        "oauthlib",
        "osmapi",  # maps
        "packaging",
        "pandas_datareader",
        "paramiko",  # ssh
        "pyasn1",
        "pycrypto",  # paramiko, cannot be replaced by pycryptodome
        "pycryptodomex",
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
    ]

    for m in ensae_set():
        if m.name.startswith("azure"):
            names.append(m)

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
