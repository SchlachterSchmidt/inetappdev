from flask import render_template, redirect, make_response, Blueprint, url_for, flash
from flask_login import login_required, current_user

home_blueprint = Blueprint('home', __name__)

from ..models import db
from ..models.post import Post as PostModel
from ..forms.post import Post as PostForm

@home_blueprint.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    # TODO: remove

    form = PostForm()
    if form.validate_on_submit():
        post = PostModel(body=form.post.data, author=current_user)
        # TODO: save is not working
        # post.save()
        post.save()
        flash('Your post is now live!')
        return redirect(url_for('.home'))
    posts = current_user.followed_posts().all()
    return render_template("home.html", title='Home Page', form=form,
                           posts=posts)
