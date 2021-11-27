from sqlalchemy.sql import func
from __init__ import db


class Artwork(db.Model):
    """
    This object has images file name, creator name and date.
    """

    __tablename__ = 'artworks'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    title = db.Column(db.String, nullable=False)
    filename = db.Column(db.String, nullable=False)

    owner_id = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Artwork(id={self.id})"
