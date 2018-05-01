from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from . import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

    def save(self):
        db.session.add(self)
        db.session.commit()
