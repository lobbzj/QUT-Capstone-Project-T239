from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    mobile = db.Column(db.String(100), index=True, nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)
    member_type = db.Column(db.String(100), default=False)
    address = db.Column(db.String(100), nullable=True)
    # add the foreign key
    comments = db.relationship('Comment', backref='user')
    orders = db.relationship('Order', backref='user')
    

    # string print method
    def __repr__(self):
        return f"Name: {self.name}"

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    category = db.Column(db.String(80))
    # add the foreign key
    comments = db.relationship('Comment', backref='product')
    orders = db.relationship('Order', backref='product')
    
    # string print method
    def __repr__(self):
        return f"Name: {self.name}"

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    # string print method
    def __repr__(self):
        return f"Comment: {self.text}" 

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80))
    total_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    
    # string print method
    def __repr__(self):
        return f"Order: {self.id}"


class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80))
    total_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
    # string print method
    def __repr__(self):
        return f"Payment: {self.id}" 
