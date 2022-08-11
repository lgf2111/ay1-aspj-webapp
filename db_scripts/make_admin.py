import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from dotenv import load_dotenv
load_dotenv()
from flaskblog import db, create_app, bcrypt
from flaskblog.models import *
app = create_app()
with app.app_context():
    user = User.query.filter_by(username=input('Username: ')).first()
    user.role_id = 2
    db.session.commit()
