from flask_sqlalchemy import SQLAlchemy
import json

def Config(app):
    local_server = True

    with open('config.json','r') as f:
        params = json.load(f)['params']


    if(local_server):
        app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
    



    