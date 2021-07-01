import sys
sys.path.append('D:\\python\\flask\\flask blog')

from main import db


class Contacts(db.Model):
    '''
    sno,name,email,phone_num,msg,date
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(12), unique=True, nullable=False)
    phone_num = db.Column(db.String(120), unique=False, nullable=False)
    msg = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(120), unique=True,)


