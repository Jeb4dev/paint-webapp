from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

gallery = Blueprint('gallery', __name__)


@gallery.get('/')
def index():
    return render_template('gallery/index.html', user=current_user, images=6)
