from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import login_user, current_user, logout_user, login_required
from project.models import Post
from project.posts.form import PostForm
from project import db

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def NewPost():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post Created", "success")
        return redirect(url_for('main.HomePage'))
    return render_template("create_post.html", title = "New Post", form=form, legend='New Post')

@posts.route("/post/<int:post_id>")
def PostID(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title = post.title, post = post)

@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def PostUpdate(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post Updated", "success")
        return redirect(url_for('posts.PostID', post_id = post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template("create_post.html", title = "Update Post", form=form, legend='Update Post')

@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def PostDelete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post Deleted", "success")
    return redirect(url_for('main.HomePage'))
