from datetime import datetime
from flask import render_template, redirect, Blueprint, url_for, flash
from flask_login import current_user, login_user, logout_user

from ..models.user import User
from ..forms.login import Login

session_blueprint = Blueprint('session', __name__)

@session_blueprint.route('/', methods=['GET', 'POST'])
@session_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    login_form = Login()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.verify_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('.login'))
        login_user(user, remember=login_form.remember_me.data)
        return redirect(url_for('home.home'))
    return render_template('login.html', title='Sign In', form=login_form)


@session_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.login'))


@session_blueprint.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        current_user.save()
