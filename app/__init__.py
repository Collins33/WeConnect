from flask_api import FlaskAPI

from instance.config import app_config
from flask import request, jsonify, abort,session


def create_app(config_name):
    from app.models import Business
    from app.models import User
    #create instance of flaskapi
    app=FlaskAPI(__name__,instance_relative_config=True)
    SESSION_TYPE = 'redis'
    app.secret_key='my-key'
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    


    
    @app.route("/")
    def welcome():
        message="Welcome to WeConnect-API"
        response=jsonify({"welcome":message})
        return response


    #api functionality
    @app.route('/api/v1/auth/register', methods=['POST'])
    def register():
        """ 
        This end point will register a user by getting info from the request
        """
        username = str(request.data.get('username', ''))          
        email=str(request.data.get('email', ''))
        password=str(request.data.get('password', ''))
        confirm_password=str(request.data.get('confirm_password', ''))

        if username and email and password and confirm_password:

            value_email_check=User.check_email_exists(email)
            # validateEmail=User.validate_email(email)
            # validPassword=User.validate_password(password)

            if  value_email_check:
                response=({"message":"Email already exists"})

                    
                return response
                
                
            else:
                
                user=User(username=username,email=email,password=password,confirm_password=confirm_password)
                message=user.save_user(username,email,password,confirm_password)
                """turn message into json"""
                response=jsonify({"message":message,"status_code":201})
                """response.status_code=201"""
                
                return response
                return response.status_code
                


    @app.route('/api/v1/auth/login', methods=['POST'])
    def login():
        """this end point will log in a user based on username and password"""
        username = str(request.data.get('username', ''))
        password=str(request.data.get('password', ''))

        if username and password:
            session["username"]=username
            message=User.login(username,password)
            response=jsonify({"message":message,"status_code":201})
            return response
            return response.status_code


    @app.route('/api/v1/auth/logout', methods=["POST"])
    def logout():
        """this endpoint will logout the user
        by removing them from the session"""

        if session.get("username") is not None:
            session.pop("username", None)
            return jsonify({"message": "Logout successful"})
        return jsonify({"message": "You are not logged in"})    
                    




     




     
                    
 
    @app.route('/api/v1/businesses', methods=['POST','GET'])
    def business():
        if request.method == 'POST':
            """gets data from request and save business"""

            name = str(request.data.get('name', ''))          
            description=str(request.data.get('description', ''))
            location=str(request.data.get('location', ''))
            contact=str(request.data.get('contact', ''))

            if name:
                """create business object"""
                
                business=Business(name=name,description=description,location=location,contact=contact)
                
                new_business=business.save_business(name,description,location,contact)

                
                response=jsonify(new_business)
                response.status_code=201

                return response
        else:
            Businesses=Business.business_list
            response=jsonify({"Businesses":Businesses})
            response.status_code=200
            return response

                

    @app.route('/api/v1/businesses/<int:id>', methods=['GET','PUT','DELETE'])
    def business_manipulation(id):
        """gets the id of the business"""
        """uses the id to get a single business"""
        
        business_found= Business.find_business_id(id)

        if not business_found:
            message="No business found"
            response=jsonify({"message":message,"status_code":404})
            return response

        if request.method == "GET":
            response=jsonify({"Business":business_found})
            response.status_code=200
            return response

        elif request.method == "PUT":
            name = str(request.data.get('name', ''))          
            description=str(request.data.get('description', ''))
            location=str(request.data.get('location', ''))
            contact=str(request.data.get('contact', ''))

            business_found[0]["name"] =name
            business_found[0]["description"]=description
            business_found[0]["location"]=location
            business_found[0]["contact"]=contact

            response=jsonify({"business":business_found})
            response.status_code=200
            return response

        else:
            businesses=Business.get_all_businesses()
            businesses.remove(business_found[0])
            response=jsonify({"business":businesses})
            response.status_code=200
            return response


    return app


