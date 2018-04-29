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
    from app.views.login import login_blueprint
    app.register_blueprint(login_blueprint)

    # register app with SQLAlchemy
    from .models import db
    db.app = app
    db.init_app(app)

    # register bootstrap extension
    bootstrap = Bootstrap(app)
    # register login manager extension
    login.init_app(app)

    if config_mode == 'development':
        print(app.config)

    return app
