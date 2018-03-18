import unittest
import os
import json
from app import create_app
from app.models import Business,Review



class ReviewTestCase(unittest.TestCase):
    """the class to test the reviews"""
    """first create business"""
    """get the business id"""
    """use it to create the review"""

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


    def test_api_create_review(self):
        #first add the business
        res=self.client().post('/api/v1/businesses', data=self.business)
        self.assertEqual(res.status_code,201)
        #get the id of the created business
        res_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))
        #make post request to add review
        result=self.client().post('api/v1/businesses/{}/reviews'.format(res_in_json['id']), data=self.review)
        self.assertEqual(result.status_code,201)


    def test_api_display_review(self):
        #first add the business
        res=self.client().post('/api/v1/businesses', data=self.business)
        self.assertEqual(res.status_code,201)
        #get the id of the created business
        res_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))
        #make post request to add review
        result=self.client().post('api/v1/businesses/{}/reviews'.format(res_in_json['id']), data=self.review)
        self.assertEqual(result.status_code,201)

        #make get request to get all reviews
        result_get=self.client().get('api/v1/businesses/{}/reviews'.format(res_in_json['id']))
        self.assertEqual(result_get.status_code,201)





        






    def tearDown(self):
        #runs after every test
        #makes the business_list  and reviews_list empty
        Business.business_list=[]
        Review.review_list=[]     











if __name__ == "__main__":
    unittest.main()         
