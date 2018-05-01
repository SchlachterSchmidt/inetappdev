"""Final project flask app config file."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Config super class."""
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    """Config class for dev environment."""
    SQLALCHEMY_DATABASE_URI = os.environ['DEV_DATABASE_URL']
    POSTS_PER_PAGE = 3

class PrdConfig(Config):
    """Config class for prod environment."""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['PRD_DATABASE_URL']
    POSTS_PER_PAGE = 50

app_config = {
    'development': DevConfig,
    'production': PrdConfig,
}
