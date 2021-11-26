from flask import Blueprint

home = Blueprint('index', __name__)


@home.get('/')
def index():
    return 'Index page'
