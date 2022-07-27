# Delete flaskblog/site.db first
from dotenv import load_dotenv
load_dotenv()
from flaskblog import db, create_app
from flaskblog.models import *
app = create_app()
# db.create_all(app=app)
# roles = [Role(name='User'),Role(name='Admin'),]
with app.app_context():
    user = User.query.filter_by(username='lgf2111').first()
    user.role_id = 2
    # for role in roles:
    #     db.session.add(role)
    db.session.commit()
