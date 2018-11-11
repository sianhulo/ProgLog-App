import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<username>:<password>@127.0.0.1:5432/<database>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "<csrf_secret_key>"
    SECRET_KEY = "<secret_key>"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://<username>:<password>@<host>:<port>/<database>'

class TestingConfig(Config):
    TESTING = True
