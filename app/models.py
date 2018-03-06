class Business(object):
    #empty list containing created businesses
    business_list=[]

    def __init__(self,name,description,location,contact):
        self.name=name
        self.description=description
        self.location=location
        self.contact=contact

    def save_business(self):
        #this method will add an instance of business to the list
        Business.business_list.append(self)

    def delete_business(self):
        #this method will remove a business from the list
        Business.business_list.remove(self)

    @classmethod
    def get_all_businesses(cls):
        #it will return the contents of the list
        return cls.business_list



