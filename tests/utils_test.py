__author__ = 'riz'
import app.utils as utils

import unittest

class UtilsTest(unittest.TestCase):
    def test_sec_to_time(self):
        result = utils.sec_to_time(90)
        assert result == "01:30"