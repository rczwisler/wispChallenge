'''
Flask app factory for the wisp RESTful API

Functions
    create_app()
'''
from flask import Flask
from wisp_api import special_math

def create_app():
    '''
    Returns a Flask REST API to do special math

        Returns:
            api (Flask): REST API is Flask App
    '''
    api = Flask(__name__)


    @api.route('/')
    def hello_world():
        return "Hello World!"

    api.register_blueprint(special_math.bp)

    return api

application = create_app()
