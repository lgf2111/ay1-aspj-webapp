from flask import Flask, session
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import flask_monitoringdashboard as dashboard
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_mail import Mail
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import stripe
import os
import dotenv

from flaskblog.logger import setup_logger
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"
admin = Admin(name='Flask Blog', template_mode='bootstrap4')
mail = Mail()
limiter = Limiter(key_func=get_remote_address)
dotenv.load_dotenv()
stripe_keys = {
    'secret_key': os.environ['STRIPE_SECRET_KEY'],
    'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}
stripe.api_key = stripe_keys['secret_key']

root_logger = setup_logger('', 'logs/root.log')
users_logger = setup_logger('users', 'logs/users.log')
posts_logger = setup_logger('posts', 'logs/posts.log')




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.update(SESSION_COOKIE_SECURE = True, SESSION_COOKIE_HTTPONLY = True, SESSION_COOKIE_SAMESITE='Lax')
    sentry_sdk.init(
        dsn="https://bc8b621ab5b241bdba1939206c8a35dc@o1276780.ingest.sentry.io/6605916",
        integrations=[
            FlaskIntegration(),
        ],
        traces_sample_rate=1.0
    )
    dashboard.config.init_from(file='monitor/config.cfg')
    dashboard.bind(app)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    limiter.init_app(app)

    class ModelView(sqla.ModelView):
        def is_accessible(self):
            return current_user.is_authenticated
    from flaskblog.models import User, Post
    class ModelView(sqla.ModelView):
        create_template = 'admin/create.html'
        def is_accessible(self):
            if current_user.is_authenticated:
                return current_user.role_id == 2
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))


    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app