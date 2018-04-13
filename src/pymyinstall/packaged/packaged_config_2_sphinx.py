# -*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of sphinx themes.
"""
import sys
from ..installhelper.module_install import ModuleInstall


def sphinx_theme_set():
    """
    list of sphinx themes, it requires the modules in set *small*
    """
    mod = [
        ModuleInstall(
            'sphinxjp.themes.basicstrap', 'pip', purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall('sphinxjp.themecore', 'pip',
                      purpose="A sphinx theme plugin extension.", usage="SPHINX"),
        ModuleInstall('solar_theme', 'pip',
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall('cloud_sptheme', 'pip',
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            'sphinx_readable_theme', 'pip', purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            "hachibee-sphinx-theme", "pip", mname="hachibee_sphinx_theme", purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("wild_sphinx_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinx_bootstrap_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            "sphinxjp.themes.sphinxjp", "pip", purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall(
            "sphinx_py3doc_enhanced_theme", "pip", purpose="sphinx theme", usage="SPHINX") if sys.version_info[0] >= 3 else None,
        ModuleInstall(
            "sphinx-better-theme", "pip", mname="better", purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("guzzle_sphinx_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("flyingsphinx", "pip",
                      purpose="sphinx theme", usage="SPHINX/PY2") if sys.version_info[0] == 2 else None,
        ModuleInstall("itcase_sphinx_theme", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinxtrap", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinxcontrib-lunrsearch", "pip", mname="sphinxcontrib.lunrsearch",
                      purpose="simple autocompletion for the sphinx documentation", usage="SPHINX"),
        ModuleInstall("sphinxcontrib-imagesvg", "pip", mname="sphinxcontrib.imagesvg",
                      purpose="support svg in Sphinx", usage="SPHINX"),
        ModuleInstall("sphinxcontrib-jsdemo", "pip", mname="sphinxcontrib.jsdemo",
                      purpose="to demo HTML or Javascript in Sphinx documentation", usage="SPHINX"),
        ModuleInstall("zerovm-sphinx-theme", "pip", mname="zerovm_sphinx_theme",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinx-corlab-theme", "pip", mname="sphinx_corlab_theme",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinxjp.themes.htmlslide", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinxjp.themes.gopher", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinx-gallery", "pip", mname="sphinx_gallery",
                      purpose="gallery for examples", usage="SPHINX"),
        ModuleInstall("docrepr", "pip",
                      purpose="docrepr renders Python docstrings in HTML", usage="SPHINX"),
        ModuleInstall("foundation-sphinx-theme", "pip", mname="foundation_sphinx_theme",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("sphinx_theme_pd", "pip",
                      purpose="sphinx theme", usage="SPHINX"),
        ModuleInstall("mdn-sphinx-theme", "pip", mname="mdn_theme",
                      purpose="A Sphinx theme for the Mozilla Developer Network", usage="SPHINX"),
        ModuleInstall("releases", "github", "bitprophet", usage="SPHINX",
                      purpose="Releases is a Python 2+3 compatible Sphinx extension designed to help you keep " +
                      "a source control friendly, merge friendly changelog file & turn it into useful, " +
                      "human readable HTML output."),
        ModuleInstall("sphinx-redactor-theme", "pip", mname="sphinx_redactor_theme",
                      purpose="sphinx theme", usage="SPHINX"),
    ]
    return [_ for _ in mod if _ is not None]
