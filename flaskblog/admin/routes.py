from flask import render_template, Blueprint


admin = Blueprint('admin', __name__)


@admin.route("/admin/accounts")
def admin_accounts():
    return render_template('admin/accounts.html')