from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    first_name = fields.Str()
    last_name = fields.Str()

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    body = fields.Str(required=True)
    price = fields.Int(required=True)

class CartSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    product_id = fields.Int()