from flask import render_template, request, Blueprint 
from project.models import Post
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def HomePage():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template("home.html", posts=posts)
#Post.query.all() use this for all user shown in admin

@main.route("/about")
def About():
    return render_template("about.html", title = "About")
