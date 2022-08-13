from flask import Flask

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import flask_monitoringdashboard as dashboard

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flaskblog.logger import setup_logger
from flaskblog.config import Config

import os


sentry_sdk.init(
    dsn=os.environ.get('SENTRY_SDK_DSN'),
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0
)
dashboard.config.init_from(file='monitor/config.cfg')
db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"

mail = Mail()
limiter = Limiter(key_func=get_remote_address)

root_logger = setup_logger('', 'logs/root.log')
users_logger = setup_logger('users', 'logs/users.log')
posts_logger = setup_logger('posts', 'logs/posts.log')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    dashboard.bind(app)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    mail.init_app(app)
    limiter.init_app(app)


    from flaskblog.admin import admin, AdminView
    from flaskblog.models import User, Post
    admin.init_app(app)
    admin.add_view(AdminView(User, db.session))
    admin.add_view(AdminView(Post, db.session))


    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app