"""
@brief      test log(time=20s)
"""
import os
import unittest


class TestDownloadSetup (unittest.TestCase):

    def test_setup(self):
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_download_setup")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))


if __name__ == "__main__":
    unittest.main()
