from flask import Blueprint, render_template
from flask_login import current_user
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
            "like_count": Likes.query.filter_by(artwork_id=artwork_obj.id).count(),
            "like_status": like_status,
        }
        all_artwork_details.append(artwork_details)
    return render_template('gallery/index.html', user=current_user, artworks=all_artwork_details)


@gallery.get('/<int:id_>')
def single(id_):
    artwork_obj = Artwork.query.filter_by(id=id_).first()
    if Likes.query.filter_by(artwork_id=id_, user_id=artwork_obj.owner_id).first():
        like_status = True
    else:
        like_status = False
    artwork_details = {
        "artwork_id": id_,
        "href": artwork_obj.filename,
        "date": artwork_obj.date,
        "title": artwork_obj.title,
        "owner_id": artwork_obj.owner_id,
        "owner_name": User.query.filter_by(id=artwork_obj.owner_id).first().username,
        "like_count": Likes.query.filter_by(artwork_id=artwork_obj.id).count(),
        "like_status": like_status,
    }
    return render_template('gallery/single.html', user=current_user, artworks=artwork_details)
