from flask_smorest import Blueprint

bp = Blueprint("users", __name__, description="Routes for Users")

from . import routes