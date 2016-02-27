

.. blogpost::
    :title: Pycrypto, pycryptodome, paramiko to open a SSH connection
    :keywords: cryptography, SSH, paramiko, pycryptodome, pycrypto
    :date: 2016-02-27
    :categories: module
    
    The module `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_
    relies on `paramiko <http://www.paramiko.org/>`_ which depends
    on `pycrypto <https://www.dlitz.net/software/pycrypto/>`_.
    As it is not maintained anymore, I tried to replace
    by `pycryptodome <http://pycryptodome.readthedocs.org/en/latest/>`_ which 
    populate the same folder ``Crypto`` during the installation.
    It is a way to trick *paramiko* as the instruction 
    ``import Crypto`` uses the installed module whether it is *pycrypto*
    or *pycryptodome*. However, *paramiko* fails to open a SSH connection
    with *pycryptodome*. It enters a function in
    `RSA.py <https://github.com/Legrandin/pycryptodome/blob/master/lib/Crypto/PublicKey/RSA.py>`_
    which tells explicitely that some functionalities will not be supported anymore::
    
        # Methods defined in PyCrypto that we don't support anymore
        def sign(self, M, K):
            raise NotImplementedError("Use module Crypto.Signature.pkcs1_15 instead")    
            
    Recently, *pycryptodome* was removed into 
    `pycryptodomex <https://pypi.python.org/pypi/pycryptodomex/3.4.1>`_
    which does not overwrite folder *Crypto* anymore. The last issue I had was
    to find a wheel for *pycrypto* for Python 3.5 on Windows.
    I did not find it so I made it: 
    `pycrypto-2.7a1-cp35-none-win_amd64.whl <http://www.xavierdupre.fr/enseignement/setup/pycrypto-2.7a1-cp35-none-win_amd64.whl>`_.
    I took it from `avosirenfal/pycrypto <https://github.com/avosirenfal/pycrypto>`_
    which was recently updated and made the following changes
    `fix setup.py and a C header to build pycrypto on Windows for Python 3.5 <https://github.com/sdpython/pycrypto/commit/9dbff17ba6f27ede3c2aad3cfd1b264fbc0eb5d4>`_
    and some others
    `disable a test not present in pycrypto 2.6.1 <https://github.com/sdpython/pycrypto/commit/f2c53a24006ff45e69bf0a00b7c3701df18c9763>`_.
    I did not use `GMP <https://gmplib.org/>`_ or `MPIR <http://mpir.org/>`_. 
    Maybe next time.
    
    
    
    