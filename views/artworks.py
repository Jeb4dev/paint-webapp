import requests
import base64
from urllib.parse import urlencode
from uuid import uuid4
from pprint import pprint

from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from flask_login import current_user

from forms.upload import UploadForm
from forms.game import GameNameForm
from models import db
from models.artwork import Artwork
from config import Config

artworks = Blueprint('artworks', __name__)


@artworks.get('/')
def index():
    return "users' artworks"


@artworks.route('/draw', methods=['GET', 'POST'])
def draw():
    form = UploadForm()
    form.idempotency_key.data = str(uuid4())
    if request.method == 'POST' and current_user and form.validate_on_submit():
        # prevent second form submission
        artwork = Artwork.query.filter_by(idempotency_key=form.idempotency_key.data).first()
        if not artwork:
            config = Config()

            image = base64.b64encode(base64.b64decode(form.image.data.replace('data:image/png;base64,', '').strip()))
            resp = requests.post('https://api.imgbb.com/1/upload?' + urlencode({
                'key': config.IMG_BB_API_KEY,
                'name': f'user-upload-{current_user.id}-{str(uuid4())}'
            }), data={
                'image': image
            })

            api_response = resp.json()
            pprint(api_response)

            if 'success' in api_response and api_response['success']:
                artwork = Artwork(
                    title=form.title.data,
                    filename=api_response['data']['image']['url'],
                    delete_url=api_response['data']['delete_url'],
                    owner_id=current_user.id,
                    idempotency_key=form.idempotency_key.data
                )

                db.session.add(artwork)
                db.session.commit()
                return render_template('artworks/draw.html', form=form)

            else:
                flash('Unable to upload image due hosting error')
        else:
            return artwork.filename
    return render_template('artworks/draw.html', form=form)


@artworks.get('/guess')
def guess():
    if current_user.is_authenticated:
        session['name'] = current_user.username
    if 'name' not in session:
        return redirect(url_for('artworks.guess_name'))
    return render_template('artworks/game.html')


@artworks.route('/guess/name', methods=['GET', 'POST'])
def guess_name():
    form = GameNameForm()
    if current_user.is_authenticated:
        return redirect(url_for('artworks.guess'))
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('artworks.guess'))
    return render_template('form_base.html', form=form, title="Draw and Guess", form_name="Your name")
