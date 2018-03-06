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
            name=str(request.data.get('name','')),
            description=str(request.data.get('description','')),
            location=str(request.data.get('location', '')),
            contact=str(request.data.get('contact',''))

            if name:
                #create business object
                business=Business(business_name=name,business_description=description,business_location=location,business_contact=contact)
                #save the business
                business.save_business()

                #turn object into json
                response=jsonify({
                    'id':business.id,
                    'name':business.business_name,
                    'description':business.business_description,
                    'location':business.business_location,
                    'contact':business.business_contact
                })

                response.status_code=201
                return response


        else:
            #if request is a get request
            businesses=Business.get_all_businesses()#get all contents in business_list

            results=[]

            for business in businesses:
                #loop through the list
                #convert object into json
                obj={
                    'id':business.id,
                    'name':business.business_name,
                    'description':business.business_description,
                    'location':business.business_location,
                    'contact':business.business_contact
                }
                #append json into results list
                results.append(obj)
            response=jsonify(results)
            response.status_code=200
            return response  


    @app.route('/api/v1/businesses/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def business_manipulation(id):
        #get business by id
        business=Business.find_business_id(id)

        if not business:
            #if the business does no exist

            # get a 404 error
            abort(404)

        # if request.method == 'DELETE':
        #     Business.delete_business(business.id)

        elif request.method == 'PUT':
            #GET VALUES FROM THE REQUEST
            name=str(request.data.get('name','')),
            description=str(request.data.get('description','')),
            location=str(request.data.get('location', '')),
            contact=str(request.data.get('contact',''))

            #replace the values with the values in the request
            business.name=name
            business.description=description
            business.location=location
            business.contact=contact

            #create business object
            business=Business(business_name=name,business_description=description,business_location=location,business_contact=contact)
            #save business
            business.save_business()
            #turn object into json
            response=jsonify({
                'id':business.id,
                'name':business.business_name,
                'description':business.business_description,
                'location':business.business_location,
                'contact':business.business_contact
            })
            #set response status
            response.status_code=200
            return response

        else:
            response=jsonify({
                'id':business.id,
                'name':business.business_name,
                'description':business.business_description,
                'location':business.business_location,
                'contact':business.business_contact
            })
            response.status_code = 200

            return response



                  

    return app


