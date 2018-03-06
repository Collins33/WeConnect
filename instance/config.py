import os
#flask needs configurations before the app starts
#the configurations are for different environments
#the environments are Development, Testing, Production and staging
#all environments inherit from the Config class which contains settings common in all environment
class Config(object):
    #debug tells flask either to run with debugger on or off
    DEBUG=False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    



class DevConfig(Config):
    #configuration for development
    DEBUG=True
    

class TestConfig(Config):
    #configuration for testing
    DEBUG=False
    TESTING=True



class ProdConfig(Config):
    #CONFIGURATION FOR PRODUCTION
    DEBUG=False
    TESTING=False


class StagingConfig(Config): 
    #CONFIGURATION FOR STAGING
    DEBUG=True       


app_config={
    #a dictionery with the configuration classes
    #it is used to export the configuration we specified
    'development':DevConfig,
    'testing':TestConfig,
    'production':ProdConfig,
    'staging':StagingConfig

