#endpoints
#flask --app main --debug run
from flask import Blueprint,render_template
from flask_login import  login_required, current_user


views=Blueprint('views',__name__)

@views.route("/")
def home():
    return render_template("home.html",user=current_user)

@views.route("/article")
def article():
    return render_template("article.html")

@views.route("/gallery")
def gallery():
    return render_template("gallery.html")

"""@views.route("/admin")
def admin():
    return render_template("AdminPanel.html")
"""