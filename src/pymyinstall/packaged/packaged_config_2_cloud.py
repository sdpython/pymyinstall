#-*- coding: utf-8 -*-
"""
@file
@brief Defines a set of modules for more machine learning or student projects.
"""
from ..installhelper.module_install import ModuleInstall


def cloud_set():
    """
    modules introduced by students or needed for student projects, it requires the modules in set *extended*
    """
    mod = [
        ModuleInstall("botocore", "pip", usage="AWS",
                      purpose="A low-level interface to a growing number of Amazon Web Services. " +
                      "The botocore package is the foundation for the AWS CLI as well as boto3."),
        ModuleInstall("s3transfer", "pip", usage="AWS",
                      purpose="An Amazon S3 Transfer Manager"),
        ModuleInstall("boto3", "pip", usage="AWS",
                      purpose="A Python interface to Amazon Web Services"),
        ModuleInstall("s3fs", "pip", usage="AWS",
                      purpose="Convenient Filesystem interface over S3"),
        ModuleInstall("boto", "pip",
                      purpose="Amazon Web Services Library"),
        ModuleInstall("google-api-python-client", "pip", mname="googleapiclient",
                      purpose="The Google API Client for Python is a client library for accessing the Plus, Moderator, and many other Google APIs."),
        ModuleInstall("googlemaps", "pip",
                      purpose="Python client library for Google Maps API Web Services"),
        ModuleInstall("python-gmaps", "pip", mname="gmaps",
                      purpose="Google Maps API client http://python-gmaps.readthedocs.org"),
        ModuleInstall("gdata", "pip", usage="GOOGLE",
                      purpose="Python client library for Google data APIs"),
    ]

    mod.append(ModuleInstall("adal", "pip",
                             purpose="The ADAL for Python library makes it easy for python application to authenticate " +
                             "to Azure Active Directory (AAD) in order to access AAD protected web resources."))
    mod.append(ModuleInstall("msrest", "pip",
                             purpose="AutoRest swagger generator Python client runtime."))
    mod.append(ModuleInstall("msrestazure", "pip",
                             purpose="AutoRest swagger generator Python client runtime. Azure-specific module."))
    for name in ['azure-nspkg',
                 'azure-common',
                 'azure-mgmt-nspkg',
                 'azure-mgmt-authorization',
                 'azure-mgmt-common',
                 'azure-storage',
                 'azure-mgmt-batch',
                 'azure-mgmt-cdn',
                 'azure-mgmt-cognitiveservices',
                 'azure-mgmt-commerce',
                 'azure-mgmt-compute',
                 'azure-mgmt-logic',
                 'azure-graphrbac',
                 'azure-mgmt-network',
                 'azure-mgmt-notificationhubs',
                 'azure-mgmt-powerbiembedded',
                 'azure-mgmt-redis',
                 'azure-mgmt-resource',
                 'azure-mgmt-scheduler',
                 'azure-mgmt-storage',
                 'azure-mgmt-web',
                 'azure-batch',
                 'azure-servicebus',
                 'azure-servicemanagement-legacy',
                 'azure-mgmt',
                 # addition 2017-05
                 "azure-keyvault",
                 "azure-datalake-store",
                 "azure-servicefabric",
                 "azure-mgmt-devtestlabs",
                 "azure-mgmt-documentdb",
                 "azure-mgmt-containerregistry",
                 "azure-mgmt-keyvault",
                 "azure-mgmt-dns",
                 "azure-mgmt-datalake-analytics",
                 "azure-mgmt-datalake-nspkg",
                 "azure-mgmt-trafficmanager",
                 "azure-mgmt-rdbms",
                 "azure-mgmt-datalake-store",
                 "azure-mgmt-iothub",
                 "azure-mgmt-sql",
                 "azure-mgmt-monitor",
                 # main package
                 'azure']:

        # azure part
        mname = name.replace("-", ".")
        if mname in ("azure.nspkg", "azure.mgmt.nspkg",
                     "azure.servicemanagement.legacy"):
            skip_import = True
        else:
            skip_import = False
        if mname == name:
            mname = None
        m = ModuleInstall(
            name, "pip", mname=mname, pip_options=["--pre"],
            purpose="Python wrapper for Azure API (HDInsight, Blog Storage)", usage="AZURE",
            skip_import=skip_import)
        mod.append(m)

    mod.append(ModuleInstall("azureml", "pip",
                             purpose="Microsoft Azure Machine Learning Python client library"))

    return [_ for _ in mod if _ is not None]
