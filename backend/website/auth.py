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
            flash("ورود با موفقیت انجام شد", category="success")
            # Redirect to the home page or another appropriate page after login
            return redirect(url_for('views.home'))
        else:
            flash("ورود ناموفق. شماره تلفن یا رمز عبور را بررسی کنید.", category="error")

    return render_template("login.html", user=current_user)


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
            flash('شماره تلفن از قبل وجود دارد.', category='error')
        elif len(firstName) < 2:
            flash('نام باید بیشتر از یک حرف باشد.', category='error')
        elif len(lastName) < 2:
            flash('نام خانوادگی باید بیشتر از یک حرف باشد.', category='error')
        elif password != passwordConfirm or len(password) < 6:
            flash('رمز عبور باید حداقل ۶ حرف باشد و با تایید آن مطابقت داشته باشد.', category='error')
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

            flash('حساب کاربری ایجاد شد', category='success')
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('با موفقیت خارج شدید', category='success')
    return redirect(url_for('views.home'))
