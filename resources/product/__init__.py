from flask_smorest import Blueprint

bp = Blueprint("products", __name__, description="Routes for Products")

from . import routes