from flask import Blueprint, jsonify
from flask.views import MethodView
from app import db
from schemas import ProductSchema
from models.product_model import ProductModel
from flask_smorest import abort
from . import bp


@bp.route('/product')
class ProductList(MethodView):

    @bp.response(200, ProductSchema(many=True))
    def get(self):

        products = ProductModel.query.all()
        return products
    
    @bp.arguments(ProductSchema)
    @bp.response(201, ProductSchema)
    def post(self, data):
        try:
            existing_prod = ProductModel.query.filter_by(name=data['name']).first()
            if existing_prod:
                abort(400, message="Product already exists; try a different one.")

            product = ProductModel()
            product.from_dict(data)
            product.save_product()
            
            return product
        
        except Exception:
            abort(500, message="Unexpected error; please try again.")


@bp.route('/product/<int:id>')
class Product(MethodView):
    @bp.response(200, ProductSchema)
    def get(self, id):
    
        product = ProductModel.query.get(id)

        if product:
            return product
        else:
            abort(400, error='Product not found')

    @bp.arguments(ProductSchema)
    @bp.response(200, ProductSchema)
    def put(self, data, id):
        product = ProductModel.query.get(id)
        if product:
            product.from_dict(data)
            product.save_product()
            return product
        else:
            abort(400, message="Not a valid product")

    def delete(self, id):
        product = ProductModel.query.get(id)
        if product:
            product.del_product()
            return { "Message": "Product deleted"}, 200
        abort(400, message="Not a valid product")