from flask import render_template
from webapp import app

@app.route('/')
def index():
    return render_template('index.html', title='Homepage')

if __name__ == '__main__':
    app.run(debug=True)