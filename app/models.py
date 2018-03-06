import random

class Business(object):
    #empty list containing created businesses
    business_list=[]

    def __init__(self,business_name,business_description,business_location,business_contact):
        self.id=random.randint(0,100)
        self.business_name=business_name
        self.business_description=business_description
        self.business_location=business_location
        self.business_contact=business_contact

    def save_business(self):
        #this method will add an instance of business to the list
        Business.business_list.append(self)
   
    # @staticmethod  
    # def delete_business(id):
    #     #this method will remove a business from the list
    #     print(Business.business_list)
    #     # for business in cls.business_list:
    #     #     if business.id == id:
    #     #         print(business.name[0])
    #     #         Business.business_list.remove(business.name[0])
                
        
        
        

    @classmethod
    def get_all_businesses(cls):
        #it will return the contents of the list
        return cls.business_list

    @classmethod
    def find_business_id(cls,id):
        #this method finds a business based on the id
        #it loops through the business_list and find the business that matches the is
        for business in cls.business_list:
            if business.id == id:
                return business    



