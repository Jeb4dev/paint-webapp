from flask import Blueprint, request
from flask_login import current_user, login_required

from models.artwork import Artwork
from models import db
#  TODO: Check if this is used
api_images = Blueprint('images', __name__)


@login_required
@api_images.route('/add', methods=['GET', 'POST'])
def add_img():
    user_id = current_user.id
    url = request.args.get('url', "", type=str)
    title = request.args.get('title', "Unknown artwork", type=str)
    artwork = Artwork.query.filter_by(filename=url).first()
    if artwork:
        return False
    else:
        new_artwork = Artwork(owner_id=user_id, filename=url, title=title)
        db.session.add(new_artwork)
        db.session.commit()
        return True


@api_images.route('/get', methods=['GET'])
def get_img():
    return "success"
    # return Artwork.query.all()
