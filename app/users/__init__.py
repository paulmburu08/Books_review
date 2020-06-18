from flask import Blueprint

users = Blueprint('main',__name__)

from .routes import *