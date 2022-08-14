from flaskblog import create_app
from flask import session, g
from flask_login import current_user
import datetime
from datetime import timedelta
# from OpenSSL import SSL
# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')  

app = create_app()

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    session.modified = True
    g.user = current_user

    

if __name__ == '__main__':
    # app.run(debug=True, ssl_context='adhoc')
    app.run(debug=True)
    # USE FLASK RUN WHEN REVIEWING
