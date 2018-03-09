import unittest
from app.models import Business

class TestBusiness(unittest.TestCase):
    def setUp(self):
        """create new instance of business"""
        self.business=Business("pakjel","local supermarket","landless","0702848032")

    def test_initilize_business(self):
        self.assertEqual(self.business.name,"pakjel")


    def test_save_adds_business_to_list(self):
        self.business.save_business(self.business.name,self.business.description,self.business.location,self.business.contact)
        self.assertTrue(len(Business.business_list)>0)

    def test_find_business_by_id(self):
        self.business.save_business(self.business.name,self.business.description,self.business.location,self.business.contact)
        found_business=Business.find_business_id(self.business.id)

        self.assertEqual(found_business[0]["name"],self.business.name)


    def tearDown(self):
        """clears list after every test"""
        Business.business_list=[]   







if __name__ == "__main__":
    unittest.main()     