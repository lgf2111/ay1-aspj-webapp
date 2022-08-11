from crypt import methods
from flask import render_template, request, Blueprint, redirect, url_for, flash
from flask.json import jsonify
from flask_login import current_user
from flaskblog.models import Post
from flaskblog.main.forms import PaymentForm

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


@main.route("/plans")
def plans():
    return render_template('main/plans.html', title='Plans')


@main.route("/plans/get-premium", methods=["GET","POST"])
def get_premium():
    if not current_user.is_authenticated:
        flash("Please login or register first.", "danger")
        return redirect(url_for('users.login'))
    form = PaymentForm()
    if form.validate_on_submit():
        credit_card = {
        'CreditCardNumber': form.CreditCardNumber.data,
        'CardHolder': form.CardHolder.data,
        'ExpirationDateMM': form.ExpirationDateMM.data,
        'ExpirationDateYY': form.ExpirationDateYY.data,
        'SecurityCode': form.SecurityCode.data,
        'Amount': form.Amount.data,
        }
        return jsonify(credit_card)
    return render_template('main/get-premium.html', title='Get Premium', form=form)


# Test Sentry
# @main.route('/debug-sentry')
# def trigger_error():
#     division_by_zero = 1 / 0