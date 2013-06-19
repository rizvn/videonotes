import unittest
import app.validation as validation

class Validation_Test(unittest.TestCase):
    def test_validate_empty_password(self):
        errors = validation.validate_pwd("")
        self.assertEqual(len(errors), 1, 'blank password not rejected')

    def test_validate_short_pass(self):
        errors = validation.validate_pwd("")
        self.assertEqual(len(errors), 1, 'short password not rejected')

    def test_validate_valid_pwd(self):
        errors = validation.validate_pwd("1234566")
        self.assertEqual(len(errors), 0, 'Invalid number of errors')


if __name__ == '__main__':
    unittest.main()
