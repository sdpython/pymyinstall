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
        "azure_batch",
        "azure_common",
        "azure_graphrbac",
        "azure_mgmt",
        "azure_mgmt_nspkg",
        "azure_mgmt_authorization",
        "azure_mgmt_common",
        "azure_mgmt_batch",
        "azure_mgmt_cdn",
        "azure_mgmt_cognitiveservices",
        "azure_mgmt_commerce",
        "azure_mgmt_compute",
        "azure_mgmt_logic",
        "azure_mgmt_network",
        "azure_mgmt_notificationhubs",
        "azure_mgmt_powerbiembedded",
        "azure_mgmt_redis",
        "azure_mgmt_resource",
        "azure_mgmt_scheduler",
        "azure_mgmt_storage",
        "azure_mgmt_web",
        "azure_nspkg",
        "azure_servicebus",
        "azure_servicemanagement_legacy",
        "azure_storage",
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
        "linkedin",
        "logbook",
        "markdown2",
        "msrest",
        "msrestazure",
        "mbstrdecoder",
        "networkx",
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
        "pyquickhelper",
        "pytablereader",
        "pytablewriter",
        "qgrid",  # magic command
        "requests_file",
        "requests-ftp",
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
