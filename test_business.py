import unittest
import os
import json
from app import create_app
from app.models import Business

class BusinessTestCase(unittest.TestCase):

    def setUp(self):
        #initialize our app with the testing configuration
        self.app=create_app(config_name="testing")
        #get the app test client
        self.client=self.app.test_client
        #data to use as test payload
        self.business={"name":"tropics","description":"Business that sells tropical drinks","location":"nairobi","contact":"071234445"}


    def test_business_creation(self):
        #test if the api can create a business 
        res=self.client().post('/api/v1/businesses', data=self.business)
        self.assertEqual(res.status_code,201)
        self.assertIn("Business that sells tropical drinks",str(res.data))

    def test_api_can_get_all_businesses(self):
        #tests if the api can get all the businesses
        res=self.client().post('/api/v1/businesses', data=self.business)
        self.assertEqual(res.status_code,201)
        res=self.client().get('/api/v1/businesses')
        self.assertEqual(res.status_code,200)
        self.assertIn("Business that sells tropical drinks",str(res.data))





    # def tearDown(self):
    #     #runs after every test
    #     #makes the business_list empty
    #     Business.business_list=[]    
            




if __name__ == "__main__":
    unittest.main()          