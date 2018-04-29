from flask import render_template, make_response, Blueprint
import os

from ...models import User

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def hello():
    return make_response('hello world', 200)

@home_blueprint.route('/login')
def login():
    return render_template('home.html')

@home_blueprint.route('/test')
def test():
    user = User.query.all()
    return 'user found'
