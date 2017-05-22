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
        "azure-mgmt misses",
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
        "azure_datalake_store",
        "azure_keyvault",
        "azure_mgmt_containerregistry",
        "azure_mgmt_datalake_analytics",
        "azure_mgmt_datalake_store",
        "azure_mgmt_devtestlabs",
        "azure_mgmt_dns",
        "azure_mgmt_documentdb",
        "azure_mgmt_iothub",
        "azure_mgmt_keyvault",
        "azure_mgmt_monitor",
        "azure_mgmt_rdbms",
        "azure_mgmt_sql",
        "azure_mgmt_trafficmanager",
        "azure_servicefabric",
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
        "inflection",  # quandl
        "ipykernel",
        "isodate",
        "keyring",
        "python3-linkedin",
        "logbook",
        "markdown2",
        "more-itertools",
        "msrest",
        "msrestazure",
        "mbstrdecoder",
        "networkx",
        "ndg_httpsclient",  # quandl
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
        "pyopenssl",  # quandl
        "pyquickhelper",
        "simplesqlite",
        "pytablereader",
        "pytablewriter",
        "qgrid",  # magic command
        "quandl",
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
