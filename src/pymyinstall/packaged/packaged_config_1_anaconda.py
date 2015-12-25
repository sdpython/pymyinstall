#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""
import sys
from ..installhelper.module_install import ModuleInstall
from ..installhelper.module_install_exceptions import MissinReferenceException


def anaconda_ext_set():
    """
    list of modules Anaconda uses and not in the regular list of packages
    """
    mod = [
        ModuleInstall(
            "affine", "pip", purpose="Matrices describing affine transformation of the plane"),
        ModuleInstall("configobj", "pip",
                      purpose="Config file reading, writing and validation."),
    ]

    return [_ for _ in mod if _ is not None]


def anaconda_set():
    """
    list of modules in Anaconda
    """
    names = """
            --abstract-rendering Linux Mac
            affine
            alabaster
            ansi2html
            appscript Mac
            --argcomplete
            --astroid
            --astropy
            azure
            babel
            basemap
            bcolz
            beautifulsoup4
            --binstar
            --binstar-build
            --biopython
            bitarray
            blaze
            --blaze-core
            blist
            --blockspring
            blz
            bokeh
            --boost
            boto
            bottleneck
            --bsdiff4
            btrees
            certifi
            cffi
            --chameleon
            chest
            --chrpath Linux
            --click
            --cligj
            --cloudpickle
            --clyent
            --cmake Linux Mac
            colorama
            --conda
            --conda-api
            --conda-build
            --conda-env
            --configobj
            coverage
            --cryptography
            --cssselect Linux Mac
            --csvkit
            --cubes
            --curl
            cvxopt
            --cymem Linux Mac
            cython
            cytoolz
            dask
            datashape
            datrie
            dbf
            decorator
            dill
            django
            docopt
            docutils
            dynd-python
            ecdsa
            --ephem
            --execnet
            --fastcache
            feedparser
            --fiona
            flake8
            flask
            flask-login
            --flask-wtf
            --fontconfig Linux
            --freeglut Linux
            --freetype Linux Mac
            future
            futures
            gdal
            gensim
            --geos
            greenlet
            guidata
            guiqwt
            --gunicorn Linux Mac
            h5py
            --hdf5
            heapdict
            holoviews
            html5lib
            --icu Linux Mac
            --idna
            --iopro
            ipython
            itsdangerous
            --jdcal
            jedi
            jinja2
            joblib
            --jpeg Linux Mac
            jsonschema
            --lancet-ioam
            --launcher Mac Windows
            --ldap3
            --libconda
            --libdynd Linux Mac
            --libffi Linux
            --libgdal
            --libnetcdf
            --libpng Linux Mac
            --libsodium Linux Mac
            --libtiff Linux Mac
            --libxml2 Linux Mac
            --libxslt Linux Mac
            line_profiler
            llvmlite
            locket
            lockfile
            --logilab-common
            lxml
            markdown
            markdown2
            markupsafe
            --mathjax
            matplotlib
            mccabe
            --mdp
            --meld3
            --menuinst Windows
            --mingw Windows
            mistune
            mock
            mpmath
            msgpack-python
            multimethods
            multipledispatch
            --murmurhash Linux Mac
            --mysql-connector-python
            --nano Linux Mac
            natsort
            --ncurses Linux Mac
            netcdf4
            networkx
            nltk
            --node-webkit Mac Windows
            nose
            numba
            numexpr
            numpy
            --numpydoc
            odo
            openpyxl
            --openssl Linux Mac
            pandas
            param
            paramiko
            partd
            passlib
            --pastedeploy
            --patchelf Linux
            patsy
            pep8
            persistent
            --pexpect Linux Mac
            pillow
            pip
            plac
            ply
            --preshed Linux Mac
            psutil
            psycopg2
            --ptyprocess Linux Mac
            py
            pyasn1
            pycosat
            pycparser
            pycryptodome
            --pycurl Linux Mac
            pyflakes
            pygments
            pylint
            pymc
            pymongo
            pymysql
            pyodbc
            pyopengl
            pyopengl-accelerate
            pyopenssl
            pyparsing
            PyQt4
            --pyramid
            pyreadline Windows
            pyserial
            --pysnmp Linux Mac
            --pystan Linux Mac
            pytables
            pytest
            --pytest-cache
            --pytest-pep8
            --python
            python-dateutil
            pythonqwt
            pytz
            --pywget
            pywin32 Windows
            pyyaml
            pyzmq
            --qt Linux Mac
            quandl
            queuelib
            --rasterio
            --readline Linux Mac  (should be gnureadline)
            --redis Linux Mac
            --redis-py Linux Mac
            --reportlab
            --repoze.lru
            requests
            rope
            --runipy
            sas7bdat
            --scikit-bio Linux Mac
            scikit-image
            scikit-learn
            scipy
            seaborn
            semantic_version
            --setuptools
            --sh Linux Mac
            shapely
            --sip Linux Mac
            six
            snowballstemmer
            --snuggs
            sockjs-tornado
            --spacy
            sphinx
            sphinx_rtd_theme
            spyder
            sqlalchemy
            --sqlite Linux Mac
            sqlparse
            statsmodels
            --stripe
            sympy
            terminado Linux
            theano
            --thinc
            --tk Linux Mac
            toolz
            tornado
            --translationstring
            --twisted
            ujson
            unidecode
            --unixodbc Linux
            --unxutils Windows
            --util-linux Linux
            --venusian
            --virtualenv
            vispy
            w3lib
            --webob
            werkzeug
            whoosh
            --wtforms
            xlrd
            xlsxwriter
            --xlwings
            xlwt
            xray
            --xz Linux Mac
            --yaml Linux Mac
            --zeromq Linux Mac
            --zlib
            --zope.deprecation
            zope.interface
            """
    names = [_.strip("\n\r ") for _ in names.split("\n")]
    names = [_ for _ in names if len(_) > 0]

    def filter(mod):
        if mod.startswith("--"):
            return None
        if " " in mod:
            spl = mod.split()
            mod = spl[0]
            plat = [_.lower() for _ in spl[1:]]
            if sys.platform.startswith("win32"):
                if "windows" in plat:
                    return mod
            elif sys.platform.startswith("mac"):
                if "mac" in plat:
                    return mod
            elif "linux" in plat:
                return mod
            return None
        else:
            return mod

    names = [filter(_) for _ in names]

    from . import find_module_install
    errors = []
    for m in names:
        if m is None:
            continue
        try:
            find_module_install(m, must_exist=True)
        except MissinReferenceException:
            errors.append(m)

    if len(errors) > 0:
        from . import all_set
        sl = "\n".join(errors)
        sl2 = "\n".join(sorted(_.name for _ in all_set()))
        raise MissinReferenceException(
            "no reference for:\n{0}\n-----------\nAVAILABLE\n-----------\n{1}".format(sl, sl2))

    return [find_module_install(_) for _ in names if _ is not None]
