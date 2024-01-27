#endpoints
#flask --app main --debug run
from flask import Blueprint,render_template
from flask_login import current_user


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

@views.route("/adminn")
def adminn():
    return render_template("AdminPanel.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")
