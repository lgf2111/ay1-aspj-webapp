from flaskblog import create_app
# from OpenSSL import SSL
# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('server.key')
# context.use_certificate_file('server.crt')  

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
    # USE FLASK RUN WHEN REVIEWING
