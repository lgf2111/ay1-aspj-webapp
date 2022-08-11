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
    user = User(username='213587x', role_id=2, email='213587x@gmail.com', password=bcrypt.generate_password_hash('Year2Semester1').decode('utf-8'))
    db.session.add(user)
    db.session.commit()
