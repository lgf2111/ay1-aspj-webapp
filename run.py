from flaskblog import create_app, db
from flask import session, g, flash
import datetime
from datetime import timedelta, datetime
from flask_login import current_user, logout_user

app = create_app()

@app.before_request
def before_request():
    if current_user.is_active:
        if current_user.logout_time == None:
            flash('Your session has ended.', 'info')
            logout_user()
        elif datetime.now() >= current_user.logout_time:
            current_user.logout_time = None
            db.session.commit()
            flash('Your session is invalid.', 'info')
            logout_user()
            flash('This session has ended', 'danger')
        

    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)
    session.modified = True
    g.user = current_user
    

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, ssl_context='adhoc')
    # USE FLASK RUN WHEN REVIEWING
