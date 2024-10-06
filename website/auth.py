from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(user_email=email).first()
        if user:
            if check_password_hash(user.user_password, password):
                flash('Logged in', category='success')
                login_user(user)
                redirect('/')
            else:
                flash('Username or password is incorrect', category='error')
        else:
            flash('There are no accounts with this email', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password_1 = request.form.get('password_1')
        password_2 = request.form.get('password_2')

        user = User.query.filter_by(user_email=email).first()
        if user:
            flash('An account with this email already exists. You can log in here', category='error')
            return redirect('/login')
        if len(password_1) < 8:
            flash("Password must be at least 7 characters", category='error')
        elif password_1 != password_2:
            flash("Passwords do not match", category='error')
        else:
            new_user = User(user_email=email, firstName=first_name, user_password=generate_password_hash(password_1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully", category='success')
            login_user(new_user)
            return redirect('/')
    return render_template("sign_up.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    return render_template("/logout.html")

@auth.route('/logout_confirm', methods=['POST'])
@login_required
def logout_confirm():
    logout_user()
    flash('You have been logged out.', category='success')
    return redirect(url_for('auth.login'))