from flask import Blueprint, render_template

artworks = Blueprint('images', __name__)


@artworks.get('/')
def index():
    return "users' artworks"


@artworks.route('/draw', methods=['GET', 'POST'])
def draw():
    return render_template('artworks/draw.html')


@artworks.get('/guess')
def guess():
    pass
