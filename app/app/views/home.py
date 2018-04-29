from flask import render_template, redirect, make_response, Blueprint, url_for, flash
from flask_login import login_required

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/home')
@login_required
def home():
    # TODO: remove
    posts = []
    return render_template('home.html', title='Home Page', posts=posts)
