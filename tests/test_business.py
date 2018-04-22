import unittest
import os
import json
from app import create_app
from app.models import Business

class BusinessTestCase(unittest.TestCase):

    business_url='/api/v1/businesses'
    business_id_url='/api/v1/businesses/{}'

    def setUp(self):
        #initialize our app with the testing configuration
        self.app=create_app(config_name="testing")
        #get the app test client
        self.client=self.app.test_client
        #data to use as test payload
        self.business={"name":"tropics","description":"Business that sells tropical drinks","location":"nairobi","contact":"071234445"}
        self.testBusiness={"name":"wwe","description":"Wrestling business","location":"nairobi","contact":"071234445"}

        #data for testing response when a field is missing
        self.business_name_missing={"name":"","description":"Business that sells tropical drinks","location":"nairobi","contact":"071234445"}
        self.business_description_missing={"name":"tropics","description":"","location":"nairobi","contact":"071234445"}
        self.business_location_missing={"name":"tropics","description":"Business that sells tropical drinks","location":"","contact":"071234445"}
        self.business_contact_missing={"name":"tropics","description":"Business that sells tropical drinks","location":"nairobi","contact":""}

        
    
    
    def addBusiness(self):
        """this method adds a business to the datastructure"""
        return self.client().post(BusinessTestCase.business_url, data=self.business)
       


    def test_business_creation(self):
        #test if the api can create a business 
        add_business=self.client().post(BusinessTestCase.business_url,data=self.business)

        self.assertEqual(add_business.status_code,201)
        self.assertIn("Business that sells tropical drinks",str(add_business.data))

    def test_api_can_get_all_businesses(self):
        #tests if the api can get all the businesses
        self.addBusiness()
        

        result=self.client().get(BusinessTestCase.business_url)

        self.assertEqual(result.status_code,200)
        

        self.assertIn("Business that sells tropical drinks",str(result.data))


    def test_api_return_right_response_if_no_business_found(self):
        result=self.client().get(BusinessTestCase.business_url)
        self.assertEqual(result.status_code,400)
        self.assertIn("business does not exist",str(result.data))


    def test_api_can_get_business_by_id(self):
        self.addBusiness
        res=self.client().post(BusinessTestCase.business_url, data=self.testBusiness)

        self.assertEqual(res.status_code,201)
        #convert response to json
        result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))

        #make get request and add the id
        get_request=self.client().get(BusinessTestCase.business_id_url.format(result_in_json['id']))

        #assert the request status
        self.assertIn("Wrestling business",str(get_request.data))

    def test_api_can_edit_business(self):

        #tests if a the api can get a business and edit it 
        res=self.client().post(BusinessTestCase.business_url, data=self.business)

        self.assertEqual(res.status_code,201)
        #convert response into json so as to get the id
        result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))

        #make a put request
        #this edits the current business
        put_request=self.client().put(BusinessTestCase.business_id_url.format(result_in_json['id']), data={"name":"tropics","description":"Business that sells tropical guns","location":"Thika","contact":"071234445"})

        self.assertIn("Business that sells tropical guns",str(put_request.data))

    def test_api_deletes_business(self):
        #test if api can delete a business
        res=self.client().post(BusinessTestCase.business_url, data=self.business)

        self.assertEqual(res.status_code,201)
        #convert response into json so as to get the id
        result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))
        
        #delete and pass in the id
        result=self.client().delete(BusinessTestCase.business_id_url.format(result_in_json['id']))

        # self.assertEqual(result.status_code,200)
        #try to run get request for deleted business
        deleted_business=self.client().get(BusinessTestCase.business_id_url.format(result_in_json['id']))
        
        #should return 404
        self.assertEqual(deleted_business.status_code,404)


    def test_api_cannot_register_without_all_fields(self):
        res=self.client().post(BusinessTestCase.business_url, data={"name":"tropics","contact":"09385789"})
        self.assertEqual(res.status_code,400)

    def test_api_cannot_get_nonexistent_by_id(self):
        self.addBusiness()
        result=self.client().get('/api/v1/businesses/10')
        self.assertEqual(result.status_code,404)

    def test_api_cannot_delete_nonexistent_business(self):
        self.addBusiness()

        #try to edit first business
        put_request=self.client().put('/api/v1/businesses/1', data={"name":"tropics","description":"Business that sells tropical guns","location":"Thika","contact":"071234445"})

        self.assertEqual(put_request.status_code,200)
        self.assertIn("Business that sells tropical guns",str(put_request.data))
        
        #try to edit non existent business
        put_request=self.client().put('/api/v1/businesses/10', data={"name":"tropics","description":"Business that sells tropical guns","location":"Thika","contact":"071234445"})

        self.assertEqual(put_request.status_code,404)


    def test_api_cannot_create_business_name_exist(self):
        self.addBusiness()
        res=self.client().post(BusinessTestCase.business_url, data={"name":"tropics","description":"Business that sells drinks","location":"nairobi","contact":"071234446"})
        self.assertEqual(res.status_code,400)


    def test_api_cannot_create_business_contact_exist(self):
        result=self.client().post(BusinessTestCase.business_url, data=self.business)
        self.assertEqual(result.status_code,201)

        res=self.client().post(BusinessTestCase.business_url, data={"name":"tropical","description":"Business that sells drinks","location":"nairobi","contact":"071234445"})
        self.assertEqual(res.status_code,400)
    
    def test_api_can_get_business_by_name(self):
        res=self.client().post(BusinessTestCase.business_url, data=self.business)
        res.test=self.client().post(BusinessTestCase.business_url, data=self.testBusiness)

        self.assertEqual(res.status_code,201)
        #convert response to json
        result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))

        #make get request and add the id
        get_request=self.client().get(BusinessTestCase.business_id_url.format(result_in_json['name']))

        #assert the request status
        self.assertEqual(get_request.status_code,200)


    def test_api_gives_error_name_missing(self):
        res=self.client().post(BusinessTestCase.business_url, data=self.business_name_missing)
        self.assertEqual(res.status_code,400)
        self.assertIn('name is missing',str(res.data))

    def test_api_gives_error_description_missing(self):
        res=self.client().post(BusinessTestCase.business_url,data=self.business_description_missing)
        self.assertEqual(res.status_code,400)
        self.assertIn('description missing',str(res.data))

    def test_api_gives_error_location_missing(self):
        res=self.client().post(BusinessTestCase.business_url,data=self.business_location_missing)
        self.assertEqual(res.status_code,400)
        self.assertIn('business location is missing',str(res.data))

    def test_api_gives_error_contact_missing(self):
        res=self.client().post(BusinessTestCase.business_url,data=self.business_contact_missing)
        self.assertEqual(res.status_code,400)
        self.assertIn('business contact is missing',str(res.data))


    def test_api_cannot_register_duplicate_name(self):
        self.addBusiness()
        res=self.client().post(BusinessTestCase.business_url, data={"name":"Tropics","description":"Business that sells drinks","location":"nairobi","contact":"071234446"})
        self.assertEqual(res.status_code,400)


    def tearDown(self):
        #runs after every test
        #makes the business_list empty
        Business.business_list=[]    
            




if __name__ == "__main__":
    unittest.main()          