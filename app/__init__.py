from flask import Flask

def create_app():
    '''Returns flask object'''
    app = Flask(__name__)
    app.config.from_object("settings")
    print(app.config)
    return app