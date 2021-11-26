from flask import Blueprint, render_template

from forms.login import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/')
def account():
    return 'account page'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print("login", form.username.data, form.password.data)
        return "Login redirect"
    return render_template('auth/login.html', form=form)


@auth.route('/register')
def register():
    return 'register page'
