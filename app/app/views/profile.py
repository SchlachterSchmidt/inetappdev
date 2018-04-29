from flask import render_template, redirect, make_response, Blueprint, url_for, flash

profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route('/profile')
def profile():
    return "profile"
