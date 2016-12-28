
.. blogpost::
    :title: Why setup.py bdist_wheel does not work?
    :keywords: setup.py, bdist_wheel
    :date: 2016-02-27
    :categories: setup.py

    I recently tried to build a wheel for a specific module::

        python setup.py bdist_wheel

    And it failed with the following error::

        error: invalid command 'bdist_wheel'

    The module `wheel <https://pypi.python.org/pypi/wheel>`_ was installed,
    `setuptools <https://pypi.python.org/pypi/setuptools/>`_ was updated.
    The issue was explained in
    `Why can I not create a wheel in python? <http://stackoverflow.com/questions/26664102/why-can-i-not-create-a-wheel-in-python>`_.
    There are two functions ``setup``, only the one from *setuptools* can build a wheel.
    The file *setup.py* must be updated::

        # from distutils.core import setup
        from setuptools import setup
