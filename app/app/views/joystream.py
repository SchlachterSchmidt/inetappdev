from flask import render_template, Blueprint
from flask_login import login_required

from ..models.post import Post

joystream_blueprint = Blueprint('joystream', __name__)

@joystream_blueprint.route('/joystream')
@login_required
def joystream():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('joystream.html', title='The Joystream', posts=posts)
