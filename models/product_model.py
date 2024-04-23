from app import db

class ProductModel(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    body = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)

    def from_dict(self, a_dict):
        self.name = a_dict['name']
        setattr(self, 'body', a_dict['body'])
        self.price = a_dict['price']

    def save_product(self):
        db.session.add(self)
        db.session.commit()

    def del_product(self):
        db.session.delete(self)
        db.session.commit()
