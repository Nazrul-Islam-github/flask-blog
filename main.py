import sys
import asyncio
from flask.helpers import make_response
sys.path.append('/database')
from logging import debug
from flask import Flask, render_template, request,session
from PIL import Image
from datetime import datetime
import os
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'nazrul1234'
# --------------config database------------------
if __name__ == '__main__':
    from database import config_database , contact_models 
    config_database.Config(app)
# --------------config database end------------------

db = SQLAlchemy(app)

# ------------------------------end database setup-------------------------------

with open('config.json','r')as f:
    params= json.load(f)['params']
    



@app.route('/')
def home():
    try:
        posts =  contact_models.Posts.query.filter_by().all()[0:5]
        return render_template('index.html',posts= posts)
        
    except Exception as e:
        return 'server error 500'






@app.route('/post/<string:post_slug>',methods=['GET'])
def post_route(post_slug):
    try:
        post = contact_models.Posts.query.filter_by(slug=post_slug).first()
        if post == None:
            return '404 page not found'

        return render_template('post.html',post=post)
        
    except Exception as e:
        return '500 server error if are you user try again letter'


@app.route('/about')
def about():
    return render_template('about.html')





# ---------------------Login Route---------
@app.route('/login',methods=['GET','POST'])
def login():
    if ('user' in session and session['user'] == params['admin_user']):
        post = contact_models.Posts.query.all()
        return render_template('dashboard.html',posts = post)


    if(request.method == 'POST'):
        username = request.form.get('email')
        password = request.form.get('password')
        if username == params['admin_user'] and password == params['admin_password']:
            # set the session variable
            session['user'] = username
            post = contact_models.Posts.query.all()
            return render_template('dashboard.html', posts = post)

    return render_template('sign.html')

# ----------------------






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



@app.route('/json',methods=['POST'])
def test():
    if(request.method=='POST'):
        data = request.get_json()
        print(type(data))
        print(data['name'])
        res = json.dumps(data)
        print(res)
    return res



if __name__ == '__main__':
    app.run(debug=True)
