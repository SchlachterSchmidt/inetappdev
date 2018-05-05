from flask import render_template, redirect, Blueprint, url_for, flash, request
from flask_login import login_required, current_user

from flask import current_app as app

from ..models import db
from ..models.post import Post as PostModel
from ..forms.post import Post as PostForm

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = PostForm()
    if form.validate_on_submit():
        post = PostModel(body=form.post.data, author=current_user)
        post.save()
        flash('Your post is now live!')
        return redirect(url_for('.home'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('.home', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('.home', page=posts.prev_num) \
        if posts.has_prev else None

    return render_template("home.html", title='Home Page', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)
