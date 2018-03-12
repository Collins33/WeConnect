import random
import re

class Business(object):

    """class to create instance of business"""
    business_list=[]

    def __init__(self,name,description,location,contact):
        self.id=len(Business.business_list)+1
        self.name=name
        self.description=description
        self.location=location
        self.contact=location
        

    def save_business(self,name,description,location,contact):
        """this method adds a dict to the business list"""
        """the dict contains details of the business"""

        new_business={}

        new_business["name"]=name
        new_business["description"]=description
        new_business["location"]=location
        new_business["contact"]=contact
        new_business["id"]=self.id


        Business.business_list.append(new_business)
        return new_business
        
    
    @classmethod
    def get_all_businesses(cls):
        """it will return the contents of the list
         print(cls.business_list)"""
        return cls.business_list
      
      
    @classmethod
    def find_business_id(cls,id):
        """will return the dicts inside businesslist"""

        business=[business for business in cls.business_list if business['id'] == id]
        print(business)
        return business


    @classmethod
    def check_name_exists(cls,name):
        for business in cls.business_list:
            if business.get("name") == name:
                return True
            return False


    @classmethod
    def check_contact_exists(cls,contact):
        for business in cls.business_list:
            if business.get("contact") == contact:
                return True
            return False        
      
      
      
class User(object):
    """
    class to create a user
    """
    """ the user list will contain a dictionery of created users"""
    user_list=[]


    def __init__(self,username,email,password,confirm_password):
        self.username=username
        self.email=email
        self.password=password
        self.confirm_password=confirm_password


    def save_user(self,username,email,password,confirm_password):
        """
        this method gets user details as parameters,
        uses them to create a dict and append dict
        to the user_list
        """
        new_user={}

        new_user["username"]=username
        new_user["email"]=email
        new_user["password"]=password
        new_user["confirm_password"]=confirm_password

        if new_user["password"] == new_user["confirm_password"]:
            User.user_list.append(new_user)
            
            message="successfully registered user"
            return message

        
        message="password must match the confirm_password"
        return message
     
    @classmethod
    def login(cls,username,password):
        """logs in user by checking if they exist in the list"""
        for user in cls.user_list:
            if user["username"]==username and user["password"]==password:
                message="you have successfully logged in"
                return message
            
            message="username or password is invalid"
            return message    
   

    @classmethod
    def check_email_exists(cls,email):
        """validates email to avoid two accounts with same user email"""
        for user in cls.user_list:
            if user.get("email") == email:
                return True
            
            return False

    @classmethod
    def check_name_exists(cls,username):
        """validate username to avoid two accounts with same username"""
        for user in cls.user_list:
            if user.get("username") == username:
                return True

            return False
    
    @staticmethod
    def validate_password(password):
        if len(password)<6:
            return True

        return False

    @staticmethod
    def check_empty_email(email):
        empty=[""," ","  ","   ","    ","     ","      ","       ","       ","        ","         ","          ","           ","            "]
        if email in empty:
            return True

        return False

    @staticmethod
    def check_empty_password(password):
        empty=["       ","        ","         ","          ","           ","            "]
        if  password in empty:
            return True
        return False
                   
    @staticmethod
    def valid_email(email):
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
           return True
           
        return False

        

        

        