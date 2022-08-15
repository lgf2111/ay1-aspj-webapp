from wsgiref.handlers import format_date_time
from flaskblog import create_app, db
from flask import session, g
import datetime
from datetime import timedelta, datetime
from flask_login import current_user, logout_user

# from OpenSSL import SSL
# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')  

app = create_app()

@app.before_request
def before_request():
    if current_user.is_active:
        if current_user.logout_time == None:
            logout_user()
        elif datetime.now() >= current_user.logout_time:
            current_user.logout_time = None
            db.session.commit()
            logout_user()
        

    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=30)
    session.modified = True
    g.user = current_user
    

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, ssl_context='adhoc')
    # USE FLASK RUN WHEN REVIEWING
