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



    def test_api_can_create_business(self):
        """ tests if the api can add a user"""

        result=self.client().post('/api/v1/auth/register', data=self.user)
        self.assertEqual(result.status_code,200)


    # def test_cannot_create_account_with_email_already_exist(self):
    #     result=self.client().post('/api/auth/register', data=self.user)
    #     self.assertEqual(result.status_code,200)

    #     res=self.client().post('/api/auth/register', data={"username":"chuck","email":"collinsnjau39@gmail.com","password":"123456","confirm_password":"123456"})
    #     self.assertEqual(result.status_code,409)





if __name__ == "__main__":
    unittest.main()              
    