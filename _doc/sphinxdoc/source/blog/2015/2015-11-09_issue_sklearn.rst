
.. blogpost::
    :title: Issue with Scipy on Windows and Python 3.5
    :keywords: scipy, numpy, sklearn, scikit-learn, DLL
    :date: 2015-11-01
    :categories: issue

    After updating a couple of modules, I don't remember the exact list,
    I went through the following issue::

        >>> import sklearn
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "C:\Python34_x64\lib\site-packages\sklearn\__init__.py", line 57, in <module>
            from .base import clone
          File "C:\Python34_x64\lib\site-packages\sklearn\base.py", line 11, in <module>
            from .utils.fixes import signature
          File "C:\Python34_x64\lib\site-packages\sklearn\utils\__init__.py", line 11, in <module>
            from .validation import (as_float_array,
          File "C:\Python34_x64\lib\site-packages\sklearn\utils\validation.py", line 16, in <module>
            from ..utils.fixes import signature
          File "C:\Python34_x64\lib\site-packages\sklearn\utils\fixes.py", line 324, in <module>
            from scipy.sparse.linalg import lsqr as sparse_lsqr
          File "C:\Python34_x64\lib\site-packages\scipy\sparse\linalg\__init__.py", line 109, in <module>
            from .isolve import *
          File "C:\Python34_x64\lib\site-packages\scipy\sparse\linalg\isolve\__init__.py", line 6, in <module>
            from .iterative import *
          File "C:\Python34_x64\lib\site-packages\scipy\sparse\linalg\isolve\iterative.py", line 7, in <module>
            from . import _iterative
        ImportError: DLL load failed: The specified module could not be found.
        >>>

    I still do not know why it is failing. It just
    used pip to uninstall numpy and scipy and to install
    them again from
    `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
    It worked. I also noticed the differences in size between Python 3.4 and Python 3.5. It seems
    numpy got bigger whereas scipy got smaller in the same order of magnitude.
    The same trick (uninstalling, installing numpy scipy) does not seem to work
    on Python 3.5 where I got the following error::

        >>> import sklearn
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "C:\Python35_x64\lib\site-packages\sklearn\__init__.py", line 57, in <module>
            from .base import clone
          File "C:\Python35_x64\lib\site-packages\sklearn\base.py", line 9, in <module>
            from scipy import sparse
          File "C:\Python35_x64\lib\site-packages\scipy\sparse\__init__.py", line 213, in <module>
            from .csr import *
          File "C:\Python35_x64\lib\site-packages\scipy\sparse\csr.py", line 13, in <module>
            from ._sparsetools import csr_tocsc, csr_tobsr, csr_count_blocks, \
        ImportError: DLL load failed: The specified procedure could not be found.

    I tried this trick :ref:`l-blog-cvxopt-2015` but it failed too. It finally
    installed
    `Visual Studio Community 2015 <https://www.visualstudio.com/fr-fr/products/visual-studio-community-vs.aspx>`_
    and it worked.
