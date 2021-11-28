from flask import Blueprint, render_template, redirect, url_for
from werkzeug.security import check_password_hash
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
            if check_password_hash(password, user.password_hash):
                login_user(user, remember=True)
                return redirect(url_for('auth.account'))
            else: print("wrong pswd")
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.account'))

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            return "username already exists"
            # TODO: flash notification
        else:
            new_user = User.create(username, password)
            print(f"{username} registered")
            login_user(new_user, remember=True)
            return redirect(url_for('auth.account'))

    return render_template('auth/register.html', form=form)
