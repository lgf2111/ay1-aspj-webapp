import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import logging


sentry_sdk.init(
    dsn="https://85c20ebc1ef34c4eabc117ecaaee1a9f@o1276780.ingest.sentry.io/6473867",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
logging.basicConfig(filename='./record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s') # Insufficient Logging & Monitoring
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'd4c39371a9cfbee4c7f47cad1979a0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# Security Misconfiguration (https://www.securecoding.com/blog/flask-security-best-practices/)
csrf = CSRFProtect(app)


from webapp import routes