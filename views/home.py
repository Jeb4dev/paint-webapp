from flask import Blueprint, redirect, url_for, render_template, session
from flask_login import current_user

home = Blueprint('index', __name__)


@home.get('/')
def index():

    redirect(url_for('artworks.guess_name'))
