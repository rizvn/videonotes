import unittest
import app.validation as validation

class ValidationTest(unittest.TestCase):
    def test_validate_pwd(self):
        errors = validation.validate_pwd("")
        self.assertEqual(len(errors), 1, 'Invalid number of errors')
