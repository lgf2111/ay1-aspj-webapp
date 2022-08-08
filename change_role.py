from dotenv import load_dotenv
load_dotenv()
from flaskblog import db, create_app
from flaskblog.models import *
app = create_app()
with app.app_context():
    user = User.query.filter_by(username='test').first()
    user.role_id = 1
    db.session.commit()
