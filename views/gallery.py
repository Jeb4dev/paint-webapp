from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from models.artwork import Artwork
from models.user import User
from models.likes import Likes
gallery = Blueprint('gallery', __name__)


@gallery.get('/')
def index():
    all_artworks = Artwork.query.all()
    all_artwork_details = []
    for artwork_obj in all_artworks:
        if Likes.query.filter_by(artwork_id=artwork_obj.owner_id, user_id=artwork_obj.owner_id).first():
            like_status = True
        else:
            like_status = False
        artwork_details = {
            "artwork_id": artwork_obj.id,
            "href": artwork_obj.filename,
            "date": artwork_obj.date,
            "title": artwork_obj.title,
            "owner_id": artwork_obj.owner_id,
            "owner_name": User.query.filter_by(id=artwork_obj.owner_id).first().username,
            "like_count": Likes.query.filter_by(artwork_id=artwork_obj.owner_id).count(),
            "like_status": like_status,
        }
        all_artwork_details.append(artwork_details)
    return render_template('gallery/index.html', user=current_user, artworks=all_artwork_details)