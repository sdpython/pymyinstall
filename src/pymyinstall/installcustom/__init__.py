"""
@file
@brief Shortuts
"""
from .install_custom_exceptions import ManualDownloadException
from .install_custom import download_page, where_in_path
from .install_custom_7z import install_7z
from .install_custom_chromedriver import install_chromedriver
from .install_custom_git import install_git
from .install_custom_graphviz import install_graphviz
from .install_custom_javajdk import install_javajdk
from .install_custom_jenkins import install_jenkins
from .install_custom_julia import install_julia
from .install_custom_inkscape import install_inkscape
from .install_custom_miktex import install_miktex
from .install_custom_mingw import install_mingw
from .install_custom_operadriver import install_operadriver
from .install_custom_pandoc import install_pandoc
from .install_custom_putty import install_putty
from .install_custom_python import install_python, folder_older_than
from .install_custom_R import install_R
from .install_custom_scite import install_scite, modify_scite_properties
from .install_custom_sqlitespy import install_sqlitespy
from .install_custom_sbt import install_scala_sbt
from .install_custom_tdm_gcc import install_tdm_gcc
