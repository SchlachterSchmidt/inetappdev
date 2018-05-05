from flask import render_template, Blueprint, request, url_for
from flask_login import login_required

from flask import current_app as app

from ..models.post import Post

joystream_blueprint = Blueprint('joystream', __name__)

@joystream_blueprint.route('/joystream')
@login_required
def joystream():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('.joystream', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('.joystream', page=posts.prev_num) \
        if posts.has_prev else None

    return render_template('joystream.html',
                           title='The Joystream',
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url)
