import unittest
import json
import os
from app import create_app
from app.models import User


""" 
This file contains tests for the user end points
"""

class UserTestCase(unittest.TestCase):
    """class for testing the user"""

    user_register='/api/v1/auth/register'
    user_login='/api/v1/auth/login'
    user_reset='/api/v1/auth/reset-password'

    def setUp(self):
        """ this method runs after every test
        The method initilizes our app with the testing configuration
        It gets the test client
        Creates the test data
        """
        self.app=create_app(config_name="testing")
        self.client=self.app.test_client

        self.user={"username":"collins","email":"collinsnjau39@gmail.com","password":"123456","confirm_password":"123456"}

        self.login={"username":"collins","password":"123456"}

        self.reset={"email":"collinsnjau39@gmail.com","password":"987654","confirm_password":"987654"}



    def test_api_can_create_user(self):
        """ tests if the api can add a user"""

        result=self.client().post(UserTestCase.user_register, data=self.user)
        self.assertEqual(result.status_code,200)


    def test_cannot_create_account_with_email_already_exist(self):
        result=self.client().post(UserTestCase.user_register, data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post(UserTestCase.user_register, data={"username":"chuck","email":"collinsnjau39@gmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(res.status_code,400)

    def test_api_can_login_user(self):
        """user creates account"""
        result=self.client().post(UserTestCase.user_register, data=self.user)
        self.assertEqual(result.status_code,200)

        """user logs in"""
        res=self.client().post(UserTestCase.user_login, data=self.login)
        self.assertEqual(res.status_code,200)


    def test_api_cannot_register_without_all_fields(self):
        result=self.client().post(UserTestCase.user_register, data={"username":"collins","password":"123456"})
        self.assertEqual(result.status_code,400)

    def test_api_cannot_login_user_with_fields_missing(self):
        result=self.client().post(UserTestCase.user_login,data={"username":"collins"})
        self.assertEqual(result.status_code,400)

    def test_api_cannot_create_account_with_username_exists(self):
        result=self.client().post(UserTestCase.user_register, data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post(UserTestCase.user_register, data={"username":"collins","email":"collinsnjau40@gmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(res.status_code,400)

    def test_api_password_must_be_greater_than_six_characters(self):
        result=self.client().post(UserTestCase.user_register, data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post(UserTestCase.user_register, data={"username":"njau","email":"collinsnjau40@gmail.com","password":"123","confirm_password":"123"})
        self.assertEqual(res.status_code,400)


    def test_api_reset_password(self):
        """this will test if user can reset password"""
        result=self.client().post(UserTestCase.user_register, data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post(UserTestCase.user_reset, data=self.reset)
        self.assertEqual(res.status_code,200)

    def test_api_cannot_reset_password_confirm_not_match(self):

        """this will test if user can reset password
        if password and confirm are not same"""

        result=self.client().post(UserTestCase.user_register, data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post(UserTestCase.user_reset, data={"email":"collinsnjau39@gmail.com","password":"987654","confirm_password":"9876543"})
        self.assertEqual(res.status_code,409)



    def test_api_cannot_reset_account_that_does_not_exist(self):

        """this will test if user can reset account that 
        does not exist"""

        result=self.client().post(UserTestCase.user_register, data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post(UserTestCase.user_reset, data={"email":"collinsnjau100@gmail.com","password":"987654","confirm_password":"987654"})
        self.assertEqual(res.status_code,404)


    def test_api_can_validate_email(self):
        """this will test if user cannot register with an email
        that is invalid"""
        result=self.client().post(UserTestCase.user_register,data={"username":"collins","email":"collinsnjaugmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(result.status_code,400)

    def test_api_validate_username(self):
        """this will test if user with empty
        username will register"""
        result=self.client().post(UserTestCase.user_register,data={"username":" ","email":"collinsnjau@gmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(result.status_code,400)

    def test_api_validate_password(self):
        """this will test if user with empty password
        can register""" 
        result=self.client().post(UserTestCase.user_register,data={"username":"collins","email":"collinsnjau@gmail.com","password":"       ","confirm_password":"       "})
        self.assertEqual(result.status_code,400)

    def test_api_response_wrong_method_register(self):
        """this will test the response for a wrong http method"""
        result=self.client().get(UserTestCase.user_register)
        self.assertEqual(result.status_code,405)
        self.assertIn("method not allowed when registering user.Use post",str(result.data))

    def test_api_response_wrong_method_login(self):
        """this will test the response for wrong http method when loging in"""
        result=self.client().get(UserTestCase.user_login)
        self.assertEqual(result.status_code,405)
        self.assertIn("method not allowed when loging in user.Use post",str(result.data))

    def test_api_response_wrong_method_logout(self):
        """this will test the response for wrong http method when logging out"""
        result=self.client().get('/api/v1/auth/logout')
        self.assertIn("method not allowed when loging out user.Use post",str(result.data))
        self.assertEqual(result.status_code,405)   



    def tearDown(self):
        User.user_list=[]    

if __name__ == "__main__":
    unittest.main()