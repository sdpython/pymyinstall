
.. blogpost::
    :title: Anaconda and MKL
    :keywords: MKL, Anaconda
    :date: 2016-02-18
    :categories: Anaconda

    Sometimes, Anaconda displays the following warning::

        Vendor:  Continuum Analytics, Inc.
        Package: mkl
        Message: trial mode expires in 27 days

    Not sure how to handle this
    (see `conda remove mkl should be the same as conda remove --features mkl <https://github.com/conda/conda/issues/894>`_).
    See also `Anaconda 2.5 Release - now with MKL Optimizations <https://www.reddit.com/comments/44klx4>`_.
    I did::

        conda remove --features mkl

    And::

        conda uninstall mkl

    It seems to work.
