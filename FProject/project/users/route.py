from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import login_user, current_user, logout_user, login_required
from project import db, bcrypt
from project.models import User, Post
from project.users.form import (RegistrationForm, LoginForm, UpdateAccountForm, 
                                 RequestResetForm, ResetPasswordForm)
from project.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route("/register", methods=["GET", "POST"])
def Register():
    if current_user.is_authenticated:
        return redirect(url_for('main.HomePage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created! You are now able to login", "success")
        return redirect(url_for('users.Login'))
    return render_template("register.html", title = "Register", form = form)

@users.route("/login", methods=["GET", "POST"])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('main.HomePage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.email == "admin@blog.com" and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.userlist'))
        elif user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.HomePage'))
        else:
            flash("Login Denied. Check email and password", "danger")
    return render_template("login.html", title = "Login", form = form)

@users.route('/userlist')
def userlist():
    if current_user.is_authenticated and current_user.email == "admin@blog.com":
        users = models.User.query.all()
        try:
            return render_template('userlist.html', title="User List", users=users)
        except:
            return abort(404)
    try:
        return redirect(url_for('home'))
    except:
        return abort(404)

@users.route("/test")
@login_required
def Admin():
    if current_user.admin:
        users = models.User.query.all()
        return render_template("userlist.html", title = "Admin", users=users)

@users.route("/logout")
def LogOut():
    logout_user()
    return redirect(url_for('main.HomePage'))

@users.route("/account", methods=["GET", "POST"])
@login_required
def Account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Account Updated", "success")
        return redirect(url_for('users.Account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file= url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("account.html", title = "Account", image_file=image_file, form=form)

@users.route("/user/<string:username>")
def UserPosts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username = username).first_or_404()
    posts = Post.query.filter_by(author=user) \
            .order_by(Post.date_posted.desc()) \
            .paginate(page=page, per_page=3)
    return render_template("user_posts.html", posts=posts, user=user)

@users.route("/reset_password", methods=["GET", "POST"])
def ResetRequest():
    if current_user.is_authenticated:
        return redirect(url_for('main.HomePage'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        send_reset_email(user)
        flash("An Instruction Email has been sent to your email to reset password", "info")
        return redirect(url_for('users.Login'))
    return render_template("reset_request.html", title = "Reset Password", form=form)

@users.route("/reset_password/<token>", methods=["GET", "POST"])
def ResetToken(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.HomePage'))
    user = User.verify_reset_token(token)
    if user is None:
        flash("Invalid or Expired Token", "warning")
        return redirect(url_for('users.ResetRequest'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f"Pasword Updated! You are now able to login", "success")
        return redirect(url_for('users.Login'))
    return render_template("reset_token.html", title = "Reset Password", form=form)