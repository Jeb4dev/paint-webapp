from . import db


class Likes(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artworks.id'))

