from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user
from webapp import app, bcrypt
from webapp.forms import LoginForm
from webapp.models import User


@app.route('/')
def index():
    return render_template('index.html', title='Homepage', search=True)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_pass_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.next('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)