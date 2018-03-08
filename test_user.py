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



    def test_api_can_create_user(self):
        """ tests if the api can add a user"""

        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)


    def test_cannot_create_account_with_email_already_exist(self):
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post('/api/auth/register', data={"username":"chuck","email":"collinsnjau39@gmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(res.status_code,404)

    def test_api_can_login_user(self):
        """user creates account"""
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        """user logs in"""
        res=self.client().post('/api/v1/auth/login', data=self.login)
        self.assertEqual(res.status_code,200)


    def test_api_cannot_register_without_all_fields(self):
        result=self.client().post('/api/v1/auth/register', data={"username":"collins","password":"123456"})
        self.assertEqual(result.status_code,400)

    def test_api_cannot_login_user_with_fields_missing(self):
        result=self.client().post('/api/v1/auth/login',data={"username":"collins"})
        self.assertEqual(result.status_code,400)

    def test_api_cannot_create_account_with_username_exists(self):
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post('/api/auth/register', data={"username":"collins","email":"collinsnjau40@gmail.com","password":"123456","confirm_password":"123456"})
        self.assertEqual(res.status_code,404)

    def test_api_password_must_be_greater_than_six_characters(self):
        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)

        res=self.client().post('/api/auth/register', data={"username":"njau","email":"collinsnjau40@gmail.com","password":"123","confirm_password":"123"})
        self.assertEqual(res.status_code,404)






        

    def tearDown(self):
        User.user_list=[]    






if __name__ == "__main__":
    unittest.main()