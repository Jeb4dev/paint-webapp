from flask import Blueprint, redirect, url_for

home = Blueprint('index', __name__)


@home.get('/')
def index():
    return redirect(url_for('artworks.draw'))
