import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '+\xaeOm\xa7D["\xff\x1b-\x83\xd7\x87\xd4\x8a\x8730\xa0\x00\x1fe\xe9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir ,'apppy.db')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login" #make sure to redirect to login page 
login_manager.init_app(app)

import models
import views 
