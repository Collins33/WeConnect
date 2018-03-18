# WeConnect

WeConnect provides a platform that brings businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted with using an api

[![Build Status](https://travis-ci.org/Collins33/WeConnect.svg?branch=master)](https://travis-ci.org/Collins33/WeConnect)

[![Coverage Status](https://coveralls.io/repos/github/Collins33/WeConnect/badge.svg?branch=master)](https://coveralls.io/github/Collins33/WeConnect?branch=master)

## Getting Started

-git clone https://github.com/Collins33/WeConnect.git

-cd WeConnect

-virtualenv venv

-source venv/bin/activate

-pip install -r requirements.txt

## Running tests
- pytest

### Prerequisites

-python 3.6

-virtual environment

## Running it on machine
-source .env

-flask run

## ENDPOINTS
| Endpoint                                | FUNCTIONALITY |
| ----------------------------------------|:-------------:|
| POST /api/auth/register                 | This will register  the user       |
| POST /api/auth/login                    | This will login a registered user  |
| POST /api/auth/logout                   | This will log out a logged in user |
| POST /api/auth/reset-password           | This will reset the password       | 
| POST  /api/businesses                   | This will add the business         |
| PUT /api/businesses/businessId          | This will update the business      | 
| DELETE /api//businesses/businessId      | This will delete a business        |
| GET  /api/businesses                    | This will get all businesses       |
| GET  /api/businesses/businessId         | retrieve a single business by id   |
| GET  /api/businesses/businessName       | retrieve a single business by name |
| POST  /api/businesses/businessId/reviews| add a review                  |
| GET  /api/businesses/businessId/reviews | get all reviews               |       
       
       


## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pip](https://pypi.python.org/pypi/pip) - Dependency Management
* [HTML/CSS/BOOTSTRAP](https://getbootstrap.com/)-Front-end 


 

## Authors

* **COLLINS NJAU MURU** 



## License

This project is licensed under the MIT License ]




