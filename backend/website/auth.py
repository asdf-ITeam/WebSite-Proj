from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phoneNumber = request.form.get('phone-number')
        password = request.form.get('password')

        user = User.query.filter_by(phone_number=phoneNumber).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash("Logged in successfully", category="success")
            # Redirect to the home page or another appropriate page after login
            return redirect(url_for('views.home'))
        else:
            flash("Login unsuccessful. Check phone number and password.", category="error")

    return render_template("login.html",user=current_user)




@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        firstName = request.form.get('name')
        lastName = request.form.get('last_name')
        phoneNumber = request.form.get('phone-number')
        password = request.form.get('password')
        passwordConfirm = request.form.get('password-confirm')

        existing_user = User.query.filter_by(phone_number=phoneNumber).first()
        if existing_user:
            flash('Phone number already exists.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif password != passwordConfirm or len(password) < 6:
            flash('Passwords must match and be at least 6 characters.', category='error')
        else:
            new_user = User(
                first_name=firstName,
                last_name=lastName,
                phone_number=phoneNumber,
                password=generate_password_hash(password, method="pbkdf2:sha256")
            )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            flash('Account created', category='success')
            return redirect(url_for("views.home"))

    return render_template("signup.html",user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', category='success')
    # Redirect to the home page or another appropriate page after logout
    return redirect(url_for('views.home'))
