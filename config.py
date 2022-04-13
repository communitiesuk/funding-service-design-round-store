"""Flask configuration."""
from os import environ
from os import path

#  Application Config
SECRET_KEY = environ.get("SECRET_KEY") or "dev"
SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME") or "session_cookie"
FLASK_ROOT = path.dirname(path.realpath(__file__))
FLASK_ENV = environ.get("FLASK_ENV") or "development"
