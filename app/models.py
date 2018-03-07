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

        else:
            message="password must match the confirm_password"
            return message
     
    @classmethod
    def login(cls,username,password):
        """logs in user by checking if they exist in the list"""
        for user in cls.user_list:
            if user["username"]==username and user["password"]==password:
                message="you have successfully logged in"
                return message
            else:
                message="username or email is invalid"
                return message    
   

    @classmethod
    def check_email_exists(cls,email):
        for user in cls.user_list:
            if user["email"] == email:
                return False
            else:
                return True        


        

        

        