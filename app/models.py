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


    @classmethod
    def find_business_name(cls,name):
        """will return business that matches the name"""
        business=[business for business in cls.business_list if business['name'] == name]
        print (business)
        return business            
      
      
      
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
            
            message="username or email is invalid"
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
    def reset_password(email,password,confirm_password):
        for user in User.user_list:
            if user["email"] == email:
                if password == confirm_password:
                    user["password"]=password
                    user["confirm_password"]=confirm_password
                    message="Password reset was successful"
                    return message

                else:
                    message="Password and confirm password must be the same"
                    return message
            else:
                message="Account does not exist"
                return message


    @staticmethod
    def validate_email(email):
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            return True
        return False

    @staticmethod
    def validate_username(username):
        if not re.match(r"^[A-Za-z0-9\.\+_-]*$",username):
            return True
        return False

    @staticmethod
    def validate_password_format(password):
        if not re.match(r"^[A-Za-z0-9\.\+_-]*$",password):
            return True
        return False




class Review(object):

    review_list=[]

    def __init__(self,description):
        self.description =description
        

    @staticmethod    
    def save_review(desctiption,business_id):
        """this method saves a new review"""
        """it creates a dict and appends it to the 
        review_list"""
        new_review={}
        new_review["review"]=desctiption
        new_review["business"]=business_id

        Review.review_list.append(new_review)
        return new_review 

    @staticmethod
    def all_reviews():
        return Review.review_list

    @classmethod
    def business_reviews(cls,id):
        """this method will return a list of reviews that belong to a specific business"""
        reviews=[review for review in cls.review_list if review["business"] == id]
        return reviews          





                        




        

        

        