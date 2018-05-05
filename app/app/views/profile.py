from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import current_user, login_required

from flask import current_app as app

from ..models.user import User
from ..models.post import Post
from ..models import db
from ..forms.edit_profile import EditProfile

profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('.profile', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('.profile', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None

    return render_template('profile.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


@profile_blueprint.route('/profile/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfile(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.save()
        flash('Your changes have been saved.')
        return redirect(url_for('.profile', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@profile_blueprint.route('/profile/<username>/follow')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None or user == current_user:
        flash('There was a problem following {}.'.format(username))
        return redirect(url_for('.profile', username=current_user.username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('.profile', username=username))


@profile_blueprint.route('/profile/<username>/unfollow')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None or user == current_user:
        flash('There was a problem unfollowing {}.'.format(username))
        return redirect(url_for('.profile', username=current_user.username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are no longer following {}.'.format(username))
    return redirect(url_for('.profile', username=username))
