import unittest
import os
import json
from app import create_app
from app.models import Business,User

class BusinessTestCase(unittest.TestCase):

    def setUp(self):
        #initialize our app with the testing configuration
        self.app=create_app(config_name="testing")
        #get the app test client
        self.client=self.app.test_client
        #data to use as test payload
        self.business={"name":"tropics","description":"Business that sells tropical drinks","location":"nairobi","contact":"071234445"}
        self.testBusiness={"name":"wwe","description":"Wrestling business","location":"nairobi","contact":"071234445"}
    


    def register_user(self,username="collins",email="collinsnjau39@gmail.com",password="1234567",confirm_password="1234567"):
        """this method will register a test user"""
        user_data={
            'username':username,
            'email':email,
            'password':password,
            'confirm_password':confirm_password
        }
        return self.client().post('/api/v1/auth/register', data=user_data)


    def login_user(self,username="collins",password="1234567"):
        """this method will log in a user"""
        user_data={
            'username':username,
            'password':password
        }

        return self.client().post('/api/v1/auth/login', data=user_data)

    def test_api_cannot_create_business_user_logged_in(self):
        res=self.client().post('/api/v1/businesses', data=self.business)
        self.assertEqual(res.status_code,403)



    # def test_business_creation(self):
    #     # """first register a user then log them in"""
    #     # register_user=self.register_user()
    #     # self.assertEqual(register_user.status_code,200)
        
        
    #     # login_user=self.login_user() 
    #     # self.assertEqual(login_user.status_code,200)

    #     #test if the api can create a business 
    #     res=self.client().post('/api/v1/businesses', data=self.business)
    #     self.assertEqual(res.status_code,403)
        

    # def test_api_can_get_all_businesses(self):
    #     #tests if the api can get all the businesses
    #     res=self.client().post('/api/v1/businesses', data=self.business)

    #     self.assertEqual(res.status_code,201)

    #     result=self.client().get('/api/v1/businesses')

    #     self.assertEqual(result.status_code,200)

    #     # self.assertIn("Business that sells tropical drinks",str(res.data))

    # def test_api_can_get_business_by_id(self):
    #     res=self.client().post('/api/v1/businesses', data=self.business)
    #     res.test=self.client().post('/api/v1/businesses', data=self.testBusiness)

    #     self.assertEqual(res.status_code,201)
    #     #convert response to json
    #     result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))

    #     #make get request and add the id
    #     get_request=self.client().get('/api/v1/businesses/{}'.format(result_in_json['id']))

    #     #assert the request status
    #     self.assertEqual(get_request.status_code,200)

    # def test_api_can_edit_business(self):
    #     #tests if a the api can get a business and edit it 
    #     res=self.client().post('/api/v1/businesses', data=self.business)

    #     self.assertEqual(res.status_code,201)
    #     #convert response into json so as to get the id
    #     result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))

    #     #make a put request
    #     #this edits the current business
    #     put_request=self.client().put('/api/v1/businesses/{}'.format(result_in_json['id']), data={"name":"tropics","description":"Business that sells tropical guns","location":"Thika","contact":"071234445"})

    #     self.assertEqual(put_request.status_code,200)

        
        


    # def test_api_deletes_business(self):
    #     #test if api can delete a business
    #     res=self.client().post('/api/v1/businesses', data=self.business)

    #     self.assertEqual(res.status_code,201)
    #     #convert response into json so as to get the id
    #     result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))
        
    #     #delete and pass in the id
    #     result=self.client().delete('/api/v1/businesses/{}'.format(result_in_json['id']))

    #     # self.assertEqual(result.status_code,200)
    #     #try to run get request for deleted business
    #     deleted_business=self.client().get('/api/v1/businesses/{}'.format(result_in_json['id']))
        
    #     #should return 404
    #     self.assertEqual(deleted_business.status_code,404)


    # def test_api_cannot_register_without_all_fields(self):

    #     res=self.client().post('/api/v1/businesses', data={"name":"tropics","contact":"09385789"})
    #     self.assertEqual(res.status_code,400)

    # def test_api_cannot_get_nonexistent_by_id(self):

    #     res=self.client().post('/api/v1/businesses', data=self.business)
    #     self.assertEqual(res.status,'201 CREATED' )

    #     result=self.client().get('/api/v1/businesses/10')
    #     self.assertEqual(result.status_code,404)

    # def test_api_cannot_delete_nonexistent_business(self):
    #     res=self.client().post('/api/v1/businesses', data=self.business)
    #     self.assertEqual(res.status_code,201)

    #     #try to edit first business
    #     put_request=self.client().put('/api/v1/businesses/1', data={"name":"tropics","description":"Business that sells tropical guns","location":"Thika","contact":"071234445"})

    #     self.assertEqual(put_request.status_code,200)
        
    #     #try to edit non existent business
    #     put_request=self.client().put('/api/v1/businesses/10', data={"name":"tropics","description":"Business that sells tropical guns","location":"Thika","contact":"071234445"})

    #     self.assertEqual(put_request.status_code,404)


    # def test_api_cannot_create_business_name_exist(self):
    #     result=self.client().post('/api/v1/businesses', data=self.business)
    #     self.assertEqual(result.status_code,201)

    #     res=self.client().post('/api/v1/businesses', data={"name":"tropics","description":"Business that sells drinks","location":"nairobi","contact":"071234446"})
    #     self.assertEqual(res.status_code,400)


    # def test_api_cannot_create_business_contact_exist(self):
    #     result=self.client().post('/api/v1/businesses', data=self.business)
    #     self.assertEqual(result.status_code,201)

    #     res=self.client().post('/api/v1/businesses', data={"name":"tropical","description":"Business that sells drinks","location":"nairobi","contact":"071234445"})
    #     self.assertEqual(res.status_code,400)


    def tearDown(self):
        #runs after every test
        #makes the business_list empty
        Business.business_list=[]    
            




if __name__ == "__main__":
    unittest.main()          