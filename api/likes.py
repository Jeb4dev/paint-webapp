from flask import Blueprint, request
from flask_login import current_user, login_required

from models.likes import Likes
from app import db

api = Blueprint('api', __name__)


@login_required
@api.route('/likes/add', methods=['POST'])
def add_like():
    user_id = current_user.id
    artwork_id = request.args.get('artwork_id', 0, type=int)
    user_likes = Likes.query.filter_by(user_id=user_id, artwork_id=artwork_id).first()
    if user_likes:
        return False
    else:
        new_likes = Likes(artwork_id=artwork_id, user_id=user_id)
        db.session.add(new_likes)
        db.session.commit()
        return True


@login_required
@api.route('/likes/remove', methods=['POST'])
def remove_like():
    user_id = current_user.id
    artwork_id = request.args.get('artwork_id', 0, type=int)
    user_likes = Likes.query.filter_by(user_id=user_id, artwork_id=artwork_id).first()
    if user_likes:
        db.session.remove(user_likes)
        db.session.commit()
        return True
    else:
        return False


@api.route('/likes/get/count', methods=['GET'])
def get_like_count():
    artwork_id = request.args.get('artwork_id', 0, type=int)
    likes_count = Likes.query.filter_by(artwork_id=artwork_id).count()
    if likes_count:
        return likes_count
    else:
        return False
