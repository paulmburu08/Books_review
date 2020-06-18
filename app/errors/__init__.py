from flask import Blueprint

errors = Blueprint('main',__name__)

from .handlers import *