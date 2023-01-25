from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import smtplib
from app_template.settings import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Database, Enryption, and User Authentication Object Creation
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    #--------import users routes----------#

    from app_template.users.routes import users 


    #--------Assign user routes to blueprint----------#

    app.register_blueprint(users)



    return app