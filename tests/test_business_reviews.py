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

    business_review_url='api/v1/businesses/{}/reviews'

    def setUp(self):
        """this test will run before every test"""

        #initilize the app with the configuration settings
        self.app=create_app(config_name="testing")
        #get the test client for the app
        self.client=self.app.test_client

        #data to be used as payload for creating a business and review
        self.business={"name":"tropics","description":"Business that sells tropical drinks","location":"nairobi","contact":"071234445"}
        self.review={"description":"Awesome restaurant with good food and nice servive"}


    def create_business(self):
        return self.client().post('/api/v1/businesses',data=self.business)    

    def test_api_create_business(self):
        #test if the api can create a business 
        res=self.client().post('/api/v1/businesses', data=self.business)
        self.assertEqual(res.status_code,201)


    def test_api_create_review(self):
        #first add the business
        self.create_business()
        
        #make post request to add review
        result=self.client().post(ReviewTestCase.business_review_url.format("1"), data=self.review)
        self.assertEqual(result.status_code,201)
        self.assertIn("Awesome restaurant with good food and nice servive",str(result.data))


    def test_api_display_review(self):
        #first add the business
        self.create_business()
        #make post request to add review
        self.client().post(ReviewTestCase.business_review_url.format("1"), data=self.review)
        #make get request to get all reviews
        result_get=self.client().get(ReviewTestCase.business_review_url.format("1"))
        self.assertEqual(result_get.status_code,201)
        self.assertIn("Awesome restaurant with good food and nice servive",str(result_get.data))


    def test_api_add_review_business_nonexistent(self):
        """this tests if you can add a review for a business that does not exist"""
        self.create_business()
        business_review=self.client().post(ReviewTestCase.business_review_url.format("1"), data=self.review)
        self.assertEqual(business_review.status_code,201)

        second_review=self.client().post(ReviewTestCase.business_review_url.format("3"), data=self.review)
        self.assertEqual(second_review.status_code,404)   


    def tearDown(self):
        #runs after every test
        #makes the business_list  and reviews_list empty
        Business.business_list=[]
        Review.review_list=[]     


if __name__ == "__main__":
    unittest.main()         
