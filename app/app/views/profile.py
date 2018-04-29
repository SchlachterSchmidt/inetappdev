from flask import render_template, Blueprint
from flask_login import current_user, login_required

from ..models.user import User

profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('profile.html', user=user, posts=posts)
