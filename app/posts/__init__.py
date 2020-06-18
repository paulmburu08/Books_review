from flask import Blueprint

posts = Blueprint('main',__name__)

from .routes import *