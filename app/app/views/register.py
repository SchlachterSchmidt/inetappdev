from flask import render_template, redirect, Blueprint, url_for, flash
from flask_login import current_user

from ..models.user import User
from ..forms.register import Register

blueprint_register = Blueprint('register', __name__)

@blueprint_register.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    register_form = Register()
    if register_form.validate_on_submit():
        user = User(username=register_form.username.data,
                    email=register_form.email.data,
                    firstname=register_form.firstname.data,
                    lastname=register_form.lastname.data)
        user.hash_password(register_form.password.data)
        user.save()
        flash('Welcome to the Joystream!')
        return redirect(url_for('session.login'))
    return render_template('register.html', title='Register', form=register_form)
