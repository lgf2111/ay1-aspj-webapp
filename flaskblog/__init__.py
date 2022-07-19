from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.logger import setup_logger
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
limiter = Limiter(key_func=get_remote_address)
root_logger = setup_logger('', 'logs/records.log')
# logging.basicConfig(
#     level=logging.INFO,
#     format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
#     handlers=[
#         logging.FileHandler("record.log"),
#         logging.StreamHandler()
#     ]
# )


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    limiter.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.admin.routes import admin
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(errors)

    return app