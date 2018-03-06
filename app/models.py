import random

class Business(object):
    #empty list containing created businesses
    business_list=[]

    def __init__(self,name,description,location,contact):
        self.id=random.randint(0,100)
        self.name=name
        self.description=description
        self.location=location
        self.contact=location
        

    def save_business(self,name,description,location,contact):
        new_business={}

        new_business["name"]=name
        new_business["description"]=description
        new_business["location"]=location
        new_business["contact"]=contact


        Business.business_list.append(new_business)
        return new_business
        
        
        
   
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
        print(cls.business_list)
        return cls.business_list

    # @classmethod
    # def find_business_id(cls,id):
    #     #this method finds a business based on the id
    #     #it loops through the business_list and find the business that matches the is
    #     for business in cls.business_list:
    #         if business.id == id:
    #             return business    



