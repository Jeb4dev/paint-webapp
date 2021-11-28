from flask import Blueprint, render_template, request
from flask_login import current_user

from forms.upload import UploadForm

artworks = Blueprint('images', __name__)


@artworks.get('/')
def index():
    return "users' artworks"


@artworks.route('/draw', methods=['GET', 'POST'])
def draw():
    form = UploadForm()

    if request.method == 'POST' and current_user and form.validate_on_submit():
        print(current_user)
    return render_template('artworks/draw.html', form=form)


@artworks.get('/guess')
def guess():
    pass
