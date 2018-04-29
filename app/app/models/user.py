from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy.sql import func
from flask_login import UserMixin


from . import db
from app import login

class User(UserMixin, db.Model):
    """User model."""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True, nullable=False)
    lastname = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False, unique=True)
    username = db.Column(db.String(64),
                         index=True, nullable=False, unique=True)
    password_hash = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def hash_password(self, password):
        """Hash plain text user password and store."""
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        """Verify plain text user provided password against stored hash."""
        return pwd_context.verify(password, self.password_hash)

    def save(self):
        """Save user to DB. This includes create and update operations."""
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        """User representation."""
        return '<user %r>' % (self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
