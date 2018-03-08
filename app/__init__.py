from flask_api import FlaskAPI

from instance.config import app_config
from flask import request, jsonify, abort

def create_app(config_name):
    from app.models import Business
    #create instance of flaskapi
    app=FlaskAPI(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')



    #api functionality
    @app.route('/api/v1/businesses', methods=['POST','GET'])
    def business():
        if request.method == 'POST':
            #EXTRACT INFO FROM THE REQUEST
            name = str(request.data.get('name', ''))          
            description=str(request.data.get('description', ''))
            location=str(request.data.get('location', ''))
            contact=str(request.data.get('contact', ''))

            if name:
                #create business object
                business=Business(name=name,description=description,location=location,contact=contact)
                #save the business
                new_business=business.save_business(name,description,location,contact)

                #turn object into json
                response=jsonify(new_business)
                response.status_code=201
                return response


        else:
            businesses=Business.get_all_businesses()
            response=jsonify({"businesses":businesses})
            response.status_code=200
            return response  


    @app.route('/api/v1/businesses/<int:id>', methods=['GET','PUT','DELETE'])
    def business_manipulation(id):
        #get business by id
        business_found= Business.find_business_id(id)

        if not business_found:
            abort(404)

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


