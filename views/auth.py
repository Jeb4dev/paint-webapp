from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/')
def account():
    return 'account page'


@auth.route('/login')
def login():
    return 'login page'


@auth.route('/register')
def register():
    return 'register page'
