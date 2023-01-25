from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app_template import db, login_manager
from flask_login import UserMixin

#usermixin = isauthenicated, anonymous, isactive, getid


#load user
@login_manager.user_loader
def load_user(userinfo_id):
    return UserInfo.query.get(int(userinfo_id))



#-----------------USERINFO AND CAPABILITES----------------#

class UserInfo(db.Model, UserMixin):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return UserInfo.query.get(user_id)


    def __repr__(self):
        return f"UserInfo('{self.username}', '{self.email}', '{self.image_file}')"
