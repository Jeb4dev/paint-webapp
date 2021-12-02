from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required

from models.likes import Likes
from models import db

api_likes = Blueprint('likes', __name__)


@login_required
@api_likes.route('/add', methods=['POST'])
def add_like():
    user_id = current_user.id
    artwork_id = request.args.get('artwork_id', 0, type=int)
    user_likes = Likes.query.filter_by(user_id=user_id, artwork_id=artwork_id).first()
    if user_likes:
        return jsonify(False)
    else:
        new_likes = Likes(artwork_id=artwork_id, user_id=user_id)
        db.session.add(new_likes)
        db.session.commit()
        return jsonify(True)


@login_required
@api_likes.route('/remove', methods=['POST'])
def remove_like():
    user_id = current_user.id
    artwork_id = request.args.get('artwork_id', 0, type=int)
    user_likes = Likes.query.filter_by(user_id=user_id, artwork_id=artwork_id).first()
    if user_likes:
        db.session.delete(user_likes)
        db.session.commit()
        return jsonify(True)
    else:
        return jsonify(False)


@api_likes.route('/get/count', methods=['GET'])
def get_like_count():
    artwork_id = request.args.get('artwork_id', 0, type=int)
    likes_count = Likes.query.filter_by(artwork_id=artwork_id).count()
    if likes_count:
        return jsonify(likes_count)
    else:
        return jsonify(False)
