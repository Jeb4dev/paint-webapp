from sqlalchemy.sql import func
from . import db


class Artwork(db.Model):
    """
    This object has images href, creator name and date.
    """

    __tablename__ = 'artworks'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    title = db.Column(db.String, nullable=False)
    filename = db.Column(db.String, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Artwork(id={self.id})"
