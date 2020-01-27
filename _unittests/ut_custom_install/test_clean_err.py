# coding: utf-8
"""
@brief      test log(time=45s)
"""
import textwrap
import unittest
from pymyinstall.installcustom.install_custom_python import _clean_err1


class TestClearErr(unittest.TestCase):

    def test_clean_err(self):
        err = textwrap.dedent("""
                /var/lib/jenkins/workspace/pymyinstall/tpath/temp_py38_minimal/Python-3.8.1/Modules/_testcapimodule.c: In function ‘PyInit__testcapi’:
                /var/lib/jenkins/workspace/pymyinstall/tpath/temp_py38_minimal/Python-3.8.1/Modules/_testcapimodule.c:6216:5: warning: ‘tp_print’ is deprecated [-Wdeprecated-declarations]
                     MyList_Type.tp_print = 0;
                     ^~~~~~~~~~~
                In file included from ./Include/object.h:746:0,
                                 from ./Include/pytime.h:6,
                                 from ./Include/Python.h:85,
                                 from /var/lib/jenkins/workspace/pymyinstall/tpath/temp_py38_minimal/Python-3.8.1/Modules/_testcapimodule.c:15:
                ./Include/cpython/object.h:260:30: note: declared here
                     Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
                                              ^~~~~~~~
                ERROR: typepy 0.6.4 requires six<2.0.0,>=1.10.0, which is not installed.
                ERROR: tabledata 0.9.1 requires six<2.0.0,>=1.10.0, which is not installed.
                ERROR: mbstrdecoder 0.8.4 requires chardet<4,>=3.0.4, which is not installed.
                ERROR: google-auth 1.11.0 requires cachetools<5.0,>=2.0.0, which is not installed.
                ERROR: google-auth 1.11.0 requires pyasn1-modules>=0.2.1, which is not installed.
                ERROR: google-auth 1.11.0 requires rsa<4.1,>=3.1.4, which is not installed.
                ERROR: google-auth 1.11.0 requires six>=1.9.0, which is not installed.
                ERROR: dataproperty 0.43.3 requires six<2.0.0,>=1.10.0, which is not installed.
                ERROR: chainer 7.1.0 requires filelock, which is not installed.
                ERROR: chainer 7.1.0 requires numpy>=1.9.0, which is not installed.
                ERROR: chainer 7.1.0 requires protobuf>=3.0.0, which is not installed.
                ERROR: chainer 7.1.0 requires six>=1.9.0, which is not installed.
                ERROR: chainer 7.1.0 requires typing-extensions, which is not installed.
                """)
        err2 = _clean_err1(err)
        self.assertEqual(err2, None)
        



if __name__ == "__main__":
    unittest.main()
