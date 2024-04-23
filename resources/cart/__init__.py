from flask_smorest import Blueprint

bp = Blueprint("cart", __name__, description="Routes for Cart")

from . import routes