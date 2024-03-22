import unittest


if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('api', pattern='unit_test.py')
    test_suite1 = unittest.TestLoader().discover('person_detection', pattern='person_detection_test.py')
    test_suite2 = unittest.TestLoader().discover('person_detection', pattern='lighting_control_test.py')
    
    unittest.TextTestRunner().run(test_suite)
    unittest.TextTestRunner().run(test_suite1)
    unittest.TextTestRunner().run(test_suite2)
