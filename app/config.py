import logging
import os


class BaseConfig:
    APP_NAME = os.environ.get('APP_NAME')
    DEBUG = True
    TESTING = True
    LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    LOGGING_LOCATION = 'logs/flask.log'
    LOGGING_LEVEL = logging.DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    PREFERRED_URL_SCHEME = 'https'
    TEMPLATES_AUTO_RELOAD = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_DEV_URI')
    PREFERRED_URL_SCHEME = 'http'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    # etc
