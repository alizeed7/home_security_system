import unittest

# This enables running the tests from the command line
if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('api', pattern='unit_test.py')
    unittest.TextTestRunner().run(test_suite)
