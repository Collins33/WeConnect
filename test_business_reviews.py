import unittest
import os
import json
from app import create_app
from app.models import Review, Business


class ReviewTestCase(unittest.TestCase):
    """the class to test the reviews"""

    def setUp(self):
        """this test will run before every test"""

        #initilize the app with the configuration settings
        self.app=create_app(config_name="testing")
        #get the test client for the app
        self.client=self.app.test_client

        #data to be used as payload for creating a business and review
        self.business={"name":"tropics","description":"Business that sells tropical drinks","location":"nairobi","contact":"071234445"}
        self.review={"description":"Awesome restaurant with good food and nice servive"}



    def test_api_create_business(self):
        #test if the api can create a business 
        res=self.client().post('/api/v1/businesses', data=self.business)
        self.assertEqual(res.status_code,201)
