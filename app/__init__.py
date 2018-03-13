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
            value=User.check_email_exists(email)
            value_name=User.check_name_exists(username)
            validate_password=User.validate_password(password)
            validate_password_exists=User.check_empty_password(password)
            validate_email_exists=User.check_empty_email(email)
            validEmail=User.valid_email(email)

            if  value:
                response=jsonify({"message":"email already exists","status_code":400})
                response.status_code=400    
                return response
                return response.status_code

            elif value_name:
                response=jsonify({"message":"username already exists","status_code":400})
                response.status_code=400    
                return response
                return response.status_code

            elif validate_password:
                response=jsonify({"message":"password must be longer than 6 characters","status_code":400})
                response.status_code=400    
                return response
                return response.status_code

            elif validate_password_exists:
                response=jsonify({"message":"password must have characters","status_code":400})
                response.status_code=400    
                return response
                return response.status_code

            elif validate_email_exists:
                response=jsonify({"message":"email must have characters","status_code":400})
                response.status_code=400    
                return response
                return response.status_code

            elif validEmail:
                response=jsonify({"message":"email must have correct format eg collinsnjau39@gmail.com","status_code":400})
                response.status_code=400    
                return response
                return response.status_code


            else:
                user=User(username=username,email=email,password=password,confirm_password=confirm_password)
                message=user.save_user(username,email,password,confirm_password)
                """turn message into json"""
                response=jsonify({"message":message,"status_code":201})
                response.status_code=201

                
                return response
                return response.status_code

        else:
            response=jsonify({"message":"enter all details","status_code":400})
            response.status_code=400
            return response
            return response.status_code



    @app.route('/api/v1/auth/login', methods=['POST'])
    def login():
        """this end point will log in a user based on username and password"""
        username = str(request.data.get('username', ''))
        password=str(request.data.get('password', ''))

        if username and password:
            
            if session.get("username") is None:
                validate_user=User.login(username,password)
                if validate_user:
                    session["username"]=username
                    response=jsonify({"message":"successfully logged in","status_code":200})
                    response.status_code=200
                    return response
                    return response.status_code

                else:
                    response=jsonify({"message":"username or email is invalid","status_code":400})
                    response.status_code=400
                    return response
                    return response.status_code


            else:
                response=jsonify({"message":"You are already logged in","status_code":409})
                response.status_code=409
                return response
                return response.status_code 
                

        else:
            response=jsonify({"message":"enter all details","status_code":400})
            response.status_code=400
            return response
            return response.status_code



    @app.route('/api/v1/auth/logout', methods=["POST"])
    def logout():
        """this endpoint will logout the user
        by removing them from the session"""

        if session.get("username") is not None:
            session.pop("username", None)
            response=jsonify({"message":"Login successful","status_code":200})
            response.status_code=200
            return response
            return response.status_code

        return jsonify({"message": "You are not logged in"})    
                    

    @app.route('/api/v1/businesses', methods=['POST','GET'])
    def business():
        
        if session.get("username") is not None:
            if request.method == 'POST':
                """gets data from request and save business"""

                name = str(request.data.get('name', ''))          
                description=str(request.data.get('description', ''))
                location=str(request.data.get('location', ''))
                contact=str(request.data.get('contact', ''))

                if name and description and location and contact:
                    """validate that it is not duplicate"""
                    validateName=Business.check_name_exists(name)
                    validateContact=Business.check_contact_exists(contact)
                    if validateName:
                        response=jsonify({"message":"Business name already exists","status_code":400})
                        response.status_code=400    
                        return response
                        return response.status_code

                    elif validateContact:
                        response=jsonify({"message":"Business contact already exists","status_code":400})
                        response.status_code=400  
                        return response
                        return response.status_code

                    
                    else:
                        """create business object"""
                        business=Business(name=name,description=description,location=location,contact=contact)
                        
                        new_business=business.save_business(name,description,location,contact)

                        
                        response=jsonify(new_business)
                        response.status_code=201

                        return response

                else:
                    response=jsonify({"message":"enter all details","status_code":400})
                    response.status_code=400
                    return response
                    return response.status

            else:
                Businesses=Business.business_list
                response=jsonify({"businesses":Businesses})
                response.status_code=200
                return response


        elif session.get("username") is None:
            """run this if user is logged out"""
            response=jsonify({"message":"must be logged in to add or view businesses","status_code":403})
            response.status_code=403
            return response
            return response.status_code
                    

                

    @app.route('/api/v1/businesses/<int:id>', methods=['GET','PUT','DELETE'])
    def business_manipulation(id):

        if session.get("username") is not None:
            """gets the id of the business"""
            """uses the id to get a single business"""
            
            business_found= Business.find_business_id(id)

            if not business_found:
                response=jsonify({"message":"business does not exist","status":404})

            
            if request.method == "GET":
                if business_found:     
                    response=jsonify({"business":business_found})
                    response.status_code=200
                    return response

                else:
                    response=jsonify({"message":"business does not exist","status":404})
                    response.status_code=404
                    return response
                    return response.status_code


            elif request.method == "PUT":
                if business_found:

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
                    response=jsonify({"message":"Cannot update business that does not exist","status":404})
                    response.status_code=404
                    return response
                    return response.status_code


            else:
                if business_found:

                    businesses=Business.get_all_businesses()
                    businesses.remove(business_found[0])
                    response=jsonify({"business":"business successfully deleted","status":200})
                    response.status_code=200
                    return response
                else:
                    response=jsonify({"message":"Cannot delete business that does not exist","status":404})
                    response.status_code=404
                    return response
                    return response.status_code


        else:
            response=jsonify({"message":"must be logged in to add or view businesses","status_code":401})
            response.status_code=401
            return response
            return response.status_code




    return app


