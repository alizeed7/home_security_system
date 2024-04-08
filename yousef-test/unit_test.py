import route
import unittest



class MyTestCase(unittest.TestCase):

    def setUp(self):
        route.app.testing = True
        self.app = route.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code,200)
        self.assertEqual(b'"Home Page success"\n'  ,result.data)
        print("Testing home page:")
        print ("\tExpected status code: 200\n\tActual status code: 200")
        print("\n\tExpected data: Test home page\n\tActual data: Test home page")


    def test_login_correct(self):
        result = self.app.post('/login/yousefhammad/SYSC3010')
        self.assertEqual(result.status_code,200)
        self.assertEqual(b'{"message":"Login successful"}\n', result.data)

        print("\nTesting login with correct data:")
        print ("\tExpected status code: 200\n\tActual status code: 200")
        print("\n\tExpected data: message: Login successful\n\tActual data: message: Login successful")


    def test_login_incorrect(self):
        result = self.app.post('/login/yousefhammad/WRONG')
        self.assertEqual(result.status_code,401)
        self.assertEqual(b'{"error":"Invalid username or password"}\n', result.data)

        print("\nTesting login with incorrect data:")
        print ("\tExpected status code: 401\n\tActual status code: 401")
        print("\n\tExpected data: error: Invalid username or password\n\tActual data: error: Invalid username or password")


    def test_register(self):
        result = self.app.post('/register_user/TESTUSER/testuser/user@gmail.com/613-000-000/123')
        self.assertEqual(result.status_code,200)
        self.assertEqual(b'{"message":"User added successfully"}\n', result.data)

        print("\nTesting user registration:")
        print ("\tExpected status code: 200\n\tActual status code: 200")
        print("\n\tExpected data: message: User added successfully\n\tActual data: message: User added successfully")


    def test_get_valid_user_attribute(self):
        result = self.app.get('/get_user_attributes/testuser/email')
        self.assertEqual(result.status_code,200)
        self.assertEqual(b'{"email":"user@gmail.com"}\n', result.data)

        print("\nTesting getting valid user attirubtes:")
        print ("\tExpected status code: 200\n\tActual status code: 200")
        print("\n\tExpected data: email: user@gmail.com\n\tActual data: email: user@gmail.com")


    def test_get_invalid_user_attribute(self):
        result = self.app.get('/get_user_attributes/INVALID/email')

        self.assertEqual(result.status_code,404)
        self.assertEqual(b'{"error":"User not found or attribute does not exist"}\n', result.data)

        print("\nTesting getting invalid user attirubtes:")
        print ("\tExpected status code: 404\n\tActual status code: 404")
        print("\n\tExpected data: error: User not found or attribute does not exist\n\tActual data: error: User not found or attribute does not exist")



    def test_get_valid_user_invalidAttribute(self):
        result = self.app.get('/get_user_attributes/testuser/NOTHING')

        self.assertEqual(result.status_code,404)
        self.assertEqual(b'{"error":"User not found or attribute does not exist"}\n', result.data)

        print("\nTesting getting valid user but invalid attirubtes:")
        print ("\tExpected status code: 404\n\tActual status code: 404")
        print("\n\tExpected data: error: User not found or attribute does not exist\n\tActual data: error: User not found or attribute does not exist")





if __name__ == "__main__":
    tester = MyTestCase()

    tester.setUp()

    tester.test_home()

    tester.test_login_correct()

    tester.test_login_incorrect()

    tester.test_register()

    tester.test_get_valid_user_attribute()

    tester.test_get_invalid_user_attribute()

    tester.test_get_valid_user_invalidAttribute()


    print("\nAll tests successfully passed for GUI...")

