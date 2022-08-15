from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog.models import Post, Comment
from flaskblog import db, posts_logger
from flaskblog.posts.forms import PostForm
from datetime import datetime
from flask_csp.csp import csp_header
import re



posts = Blueprint('posts', __name__)

# @posts.after_request
# def add_security_headers(resp):
#     resp.headers['Content-Security-Policy']="script-src 'self'"
#     return resp


@posts.route("/post/create", methods=['GET', 'POST'])
@login_required
def new_post():
    if not current_user.is_premium:
        if current_user.posts:
            if current_user.posts[-1].date_posted.date() == datetime.today().date():
                flash("You had already posted for today, upgrade premium to have no posting limit!", "warning")
                return redirect(url_for("main.home"))
    form = PostForm()
    if form.validate_on_submit():
        CLEANR = re.compile('<.*?>') 
        cleantext = re.sub(CLEANR, '', form.content.data)
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        link = url_for('posts.post', post_id=post.id, _external=True)
        posts_logger.info(f"Post Created ({current_user.username}): {link}")
        return redirect(url_for('main.home'))
    return render_template('posts/create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        link = url_for('posts.post', post_id=post.id, _external=True)
        posts_logger.warning(f"Post Edit Attempt ({current_user.username}): {link}")
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        link = url_for('posts.post', post_id=post.id, _external=True)
        posts_logger.info(f"Post Edited ({current_user.username}): {link}")
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('posts/create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    if post.author != current_user:
        abort(403)
    [db.session.delete(comment) for comment in comments]
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    posts_logger.info(f"Post Deleted ({current_user.username}): {post}")
    return redirect(url_for('main.home'))


@posts.route('/post/<int:post_id>/comment/new', methods=['GET', 'POST'])
@login_required
# @csp_header({'script-src':"'self'"})
def new_comment(post_id):
    text = request.form.get('text')
    if not text:
        flash('Comment cannot be empty', 'error')
    else:
        # post = Post.query.filter_by(id=post.id)
        if post:
            CLEANR = re.compile('<.*?>') 
            clean_text = re.sub(CLEANR, '', text)
            comment = Comment(text=clean_text, user_id=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else: 
            flash('Post do not exist.', 'error')
    return redirect(url_for('main.home'))


@posts.route("/post/<int:post_id>/edit",)
def edit_post(post_id):
    abort(403)