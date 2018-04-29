from flask import render_template, redirect, make_response, Blueprint, url_for
import os

from ...models import User
from ...forms.login import Login

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/hello')
def hello():
    return make_response('hello world', 200)

@home_blueprint.route('/', methods=['GET', 'POST'])
@home_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = Login()
    if login_form.validate_on_submit():
        # debug
        print('Login requested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=login_form)
