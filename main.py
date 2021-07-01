import sys
sys.path.append('/database')
from logging import debug
from flask import Flask, render_template, request
from PIL import Image
from datetime import datetime
import os
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# --------------config database------------------
if __name__ == '__main__':
    from database import config_database , contact_models 
    config_database.Config(app)
# --------------config database end------------------

db = SQLAlchemy(app)

# ------------------------------end database setup-------------------------------


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/post/<string:post_slug>',methods=['GET'])
def post_route(post_slug):
    return render_template('post.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if(request.method == 'POST'):

        '''
        add entry to database
        '''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone_num')
        message = request.form.get('msg')

        entry = contact_models.Contacts(name=name, email=email, phone_num=phone, msg=message , date=datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
