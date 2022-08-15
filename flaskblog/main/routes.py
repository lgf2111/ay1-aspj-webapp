from flask import render_template, request, Blueprint
from flaskblog.models import Post, User



main = Blueprint('main', __name__)



@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('main/home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('main/about.html', title='About')



# Test Sentry
# @main.route('/debug-sentry')
# def trigger_error():
#     division_by_zero = 1 / 0