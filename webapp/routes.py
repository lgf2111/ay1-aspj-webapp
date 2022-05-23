from flask import render_template
from webapp import app

@app.route('/')
def index():
    return render_template('index.html', title='Homepage', search=True)

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/gfllf')
def login():
    return render_template('gfllf.html', title='gfllf')
