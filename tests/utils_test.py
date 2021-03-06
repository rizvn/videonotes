__author__ = 'riz'
import app.utils as utils

import unittest

class Utils_test(unittest.TestCase):
    def test_sec_to_time(self):
        result = utils.sec_to_time(90)
        assert result == "01:30"

    def test_generate_random_string(self):
        result = utils.generateRandomString()
        assert result

    def test_encrypt(self):
        result = utils.encrypt('helloworld')
        assert result

    def test_joinWheres(self):
        wheres = ['a = 1234 ' , None, 'b = 456 ']
        result =  utils.joinWheres(wheres)
        self.assertEqual(result , 'WHERE a = 1234 AND b = 456 ')

if __name__ == '__main__':
    unittest.main()