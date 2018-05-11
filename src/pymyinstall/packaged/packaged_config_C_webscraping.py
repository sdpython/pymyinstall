# -*- coding: utf-8 -*-
"""
@file
@brief Defines a set of modules to try
"""

from ..installhelper.module_install import ModuleInstall


def scraping_set():
    """
    modules which help scraping the web, it requires the modules in set *small*
    """
    mod = [
        ModuleInstall(
            "langdetect", "pip", usage="WEB",
            purpose="Language detection library ported from Google's language-detection."),
        ModuleInstall(
            "justext", "pip", usage="WEB",
            purpose="Program jusText is a tool for removing boilerplate content, such as navigation links, headers, " +
            "and footers from HTML pages. It is designed to preserve mainly text containing full " +
            "sentences and it is therefore well suited for creating linguistic resources such as Web corpora."),
        ModuleInstall(
            "tldextract", "pip", usage="WEB",
            purpose="Accurately separate the TLD from the registered domain and subdomains of a URL, using the Public Suffix List."),
        ModuleInstall(
            "cchardet", "wheel", usage="WEB",
            purpose="Universal encoding detector. This library is faster than chardet."),
        ModuleInstall(
            "multidict", "pip",
            purpose="Multidicts are useful for working with HTTP headers, URL query args etc."),
        ModuleInstall(
            "async_timeout", "pip", usage="WEB",
            purpose="Timeout context manager for asyncio programs"),
        ModuleInstall(
            "yarl", "pip", usage="WEB",
            purpose="Yet another URL library"),
        ModuleInstall(
            "idna_ssl", "pip", usage="WEB",
            purpose="Patch ssl.match_hostname for Unicode(idna) domains support"),
        ModuleInstall(
            "aiohttp", "wheel", usage="WEB",
            purpose="http client/server for asyncio"),
        ModuleInstall(
            "sky", "pip", usage="WEB",
            purpose="sky is a web scraping framework, implemented with the latest python versions in mind (3.4+). " +
            "It uses the asynchronous asyncio framework, " +
            "as well as many popular modules and extensions."),
    ]

    return [_ for _ in mod if _ is not None]
