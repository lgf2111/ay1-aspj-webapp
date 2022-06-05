from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
# from werkzeug.datastructures import ImmutableDict
from flask_talisman import Talisman

app = Flask(__name__)
# Talisman(app) # Security Misconfiguration (https://flask.palletsprojects.com/en/2.1.x/security/)
app.config['SECRET_KEY'] = 'd4c39371a9cfbee4c7f47cad1979a0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# Security Misconfiguration (https://www.securecoding.com/blog/flask-security-best-practices/)
csrf = CSRFProtect(app)
# jinja_options = ImmutableDict(
#     extensions=[
#     'jinja2.ext.autoescape', 'jinja2.ext.with_' #Turn auto escaping on
#     ])
# # Autoescaping depends on you
# app.jinja_env.autoescape = True | False 




from webapp import routes