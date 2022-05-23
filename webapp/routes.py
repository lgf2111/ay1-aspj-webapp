from flask import render_template
from webapp import app
from webapp.forms import LoginForm

@app.route('/')
def index():
    return render_template('index.html', title='Homepage', search=True)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html', title='Login', form=form)