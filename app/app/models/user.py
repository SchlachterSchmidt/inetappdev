from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy.sql import func
from flask_login import UserMixin
from hashlib import md5


from . import db
from .followers import followers
from .post import Post
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
    about_me = db.Column(db.String(500))
    last_seen = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    posts = db.relationship('Post', backref='author', lazy='dynamic')


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

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def __repr__(self):
        """User representation."""
        return '<user %r>' % (self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
