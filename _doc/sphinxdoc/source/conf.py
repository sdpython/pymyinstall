# -*- coding: utf-8 -*-
import sys
import os
import sphinx_readable_theme
from pyquickhelper.helpgen.default_conf import set_sphinx_variables

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "pymyinstall", "Xavier Dupré", 2019,
                     "readable", sphinx_readable_theme.get_html_theme_path(),
                     locals(), add_extensions=None,
                     extlinks=dict(issue=('https://github.com/sdpython/pymyinstall/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/"


epkg_dictionary.update({
    'avconv': 'http://debian-facile.org/doc:media:avconv',
    'boost': "http://www.boost.org/",
    'boost_python': "http://www.boost.org/doc/libs/release/libs/python/",
    'clang': 'https://clang.llvm.org/get_started.html',
    'cvxopt': "http://cvxopt.org/",
    'cvxpy': "http://www.cvxpy.org/en/latest/index.html",
    'Debian 9': 'https://www.debian.org/News/2017/20170617',
    'dlib': "http://dlib.net/",
    'dotnet': 'https://www.microsoft.com/net',
    'ffmpeg': 'https://www.ffmpeg.org/',
    'java': 'https://www.java.com/',
    'imageio': 'https://imageio.github.io/',
    'keyring': 'https://github.com/jaraco/keyring',
    'line_profiler': 'https://github.com/rkern/line_profiler',
    'minepy': 'https://github.com/minepy/minepy',
    'MKL': 'https://software.intel.com/en-us/mkl',
    'ML.net': 'https://www.microsoft.com/net/learn/apps/machine-learning-and-ai/ml-dotnet',
    'mono': 'https://www.mono-project.com/',
    'nodejs': 'https://nodejs.org/en/',
    'onnx': 'https://onnx.ai/',
    'pip': 'https://pip.pypa.io/en/stable/',
    'protobuf': 'https://github.com/protocolbuffers/protobuf',
    'pyaudio': 'https://people.csail.mit.edu/hubert/pyaudio/docs/',
    'pypi': 'https://pypi.org/',
    'pycuda': 'https://mathema.tician.de/software/pycuda/',
    'pycurl': 'http://pycurl.io/',
    'pyopencl': 'https://documen.tician.de/pyopencl/',
    'pythonnet': 'https://github.com/pythonnet/pythonnet',
    'spacy': 'https://spacy.io/',
    'SQLiteSpy': "https://www.yunqa.de/delphi/products/sqlitespy/index",
    'statsmodels': "http://www.statsmodels.org/stable/index.html",
    'tables': 'https://www.pytables.org/usersguide/tutorials.html',
    'TensorFlow': 'https://www.tensorflow.org/',
    'ufw': 'https://doc.ubuntu-fr.org/ufw',
    'unrar': 'https://en.wikipedia.org/wiki/Unrar',
    'virtualenv': 'https://virtualenv.pypa.io/en/stable/',
})
