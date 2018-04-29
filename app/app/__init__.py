from flask import Flask
from config import app_config
from flask_bootstrap import Bootstrap

def create_app(config_mode='development'):
    """Wrapping app creation in factory according to specified config."""
    # create app and load config

    app = Flask(__name__, template_folder='templates')
    app.config.from_object(app_config[config_mode])

    from app.views.login import login_blueprint

    app.register_blueprint(login_blueprint)

    from .models import db

    # register app with SQLAlchemy
    db.app = app
    db.init_app(app)

    bootstrap = Bootstrap(app)

    if config_mode == 'development':
        print(app.config)

    return app
