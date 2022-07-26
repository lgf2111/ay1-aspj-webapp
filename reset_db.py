from dotenv import load_dotenv
load_dotenv()
from flaskblog import create_app, db
from flaskblog.models import *
db.create_all(app=create_app())
