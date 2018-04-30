from flask import Flask
from config import app_config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


login = LoginManager()

def create_app(config_mode='development'):
    """Wrapping app creation in factory according to specified config."""

    # create app and load config
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(app_config[config_mode])

    # register blueprints
    from app.views.session import session_blueprint
    from app.views.home import home_blueprint
    from app.views.register import blueprint_register
    from app.views.profile import profile_blueprint
    # TODO: not working
    from app.views.errors import errors_blueprint

    app.register_blueprint(session_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(blueprint_register)
    app.register_blueprint(profile_blueprint)
    # TODO: not working
    app.register_blueprint(errors_blueprint)

    # register app with SQLAlchemy
    from .models import db
    db.app = app
    db.init_app(app)

    # register bootstrap extension
    bootstrap = Bootstrap(app)
    # register login manager extension
    login.init_app(app)
    login.login_view = 'session.login'

    if config_mode == 'development':
        print(app.config)

    return app
