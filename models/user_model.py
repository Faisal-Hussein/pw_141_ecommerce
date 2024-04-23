from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False)
    first_name= db.Column(db.String(75))
    last_name= db.Column(db.String(75))


    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def del_user(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, user_dict):
        for k , v in user_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)