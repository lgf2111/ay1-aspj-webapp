from flask import Flask
import flask_monitoringdashboard as dashboard
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flaskblog.logger import setup_logger
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
admin = Admin(name='Flask Blog', template_mode='bootstrap3')
mail = Mail()
limiter = Limiter(key_func=get_remote_address)
root_logger = setup_logger('', 'logs/root.log')
users_logger = setup_logger('users', 'logs/users.log')
posts_logger = setup_logger('posts', 'logs/posts.log')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    dashboard.config.init_from(file='monitor/config.cfg')
    dashboard.bind(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    mail.init_app(app)
    limiter.init_app(app)

    from flaskblog.models import User, Post
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