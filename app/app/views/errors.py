from flask import render_template, Blueprint
from flask import current_app as app

from ..models import db

errors_blueprint = Blueprint('errors_blueprint', __name__)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
