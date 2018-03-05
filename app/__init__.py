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
            name=str(request.data.get('name', '')),
            description=str(request.data.get('description', '')),
            location=str(request.data.get('location', '')),
            contact=str(request.data.get('contact',''))

            if name:
                #create business object
                business=Business(name=name,description=description,location=location,contact=contact)
                #save the business
                business.save_business()

                #turn object into json
                response=jsonify({
                    'name':business.name,
                    'description':business.description,
                    'location':business.location,
                    'contact':business.contact
                })

                response.status_code=201
                return response


        else:
            businesses=Business.get_all_businesses()

            results=[]

            for business in businesses:
                obj={
                    'name':business.name,
                    'description':business.description,
                    'location':business.location,
                    'contact':business.contact
                }
                results.append(obj)
            response=jsonify(results)
            response.status_code=200
            return response            

    return app


