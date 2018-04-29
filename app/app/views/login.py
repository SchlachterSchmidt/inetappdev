from flask import render_template, redirect, make_response, Blueprint, url_for, flash
from flask_login import current_user, login_user
import os

from ..models.user import User
from ..forms.login import Login

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/hello')
def hello():
    return make_response('hello world', 200)

@login_blueprint.route('/', methods=['GET', 'POST'])
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = Login()
    if login_form.validate_on_submit():
        # debug
        print('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))

        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('.login'))
        login_user(user, remember=login_form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=login_form)
