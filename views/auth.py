from flask import Blueprint, render_template, redirect, url_for, flash
from forms.login import LoginForm
from flask_login import login_user, login_required, logout_user, current_user
from forms.register import RegisterForm
from models.user import User

auth = Blueprint('auth', __name__)


@auth.route('/')
def account():
    if current_user.is_authenticated:
        return f'Hello {current_user.username}'
    return redirect(url_for('auth.login'))


@login_required
@auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash("logged out successfully")
    return redirect(url_for('auth.account'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.account'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            if user.check_password(password):
                login_user(user, remember=True)
                flash("Invalid password")
                return redirect(url_for('auth.account'))
            else:
                flash("Invalid password")
        else:
            flash("Username does not exist")
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("You are already logged in.")
        return redirect(url_for('auth.account'))

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            flash("username already exists")
            return redirect(url_for('auth.register'))
        else:
            new_user = User.create(username, password)
            print(f"{username} registered")
            login_user(new_user, remember=True)
            flash("Registering was successful")
            return redirect(url_for('auth.account'))

    return render_template('auth/register.html', form=form)
