from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config

app = Flask(__name__)

app.config.from_object(Config)
api = Api(app)
jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_model import UserModel
from models.product_model import ProductModel
from models.cart_model import CartModel

from resources.product import bp as product_bp
app.register_blueprint(product_bp)
from resources.user import bp as user_bp
app.register_blueprint(user_bp)
from resources.cart import bp as cart_bp
app.register_blueprint(cart_bp)