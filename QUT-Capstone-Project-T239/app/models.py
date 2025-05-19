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
    sub_category = db.Column(db.String(80))
    # add the foreign key
    comments = db.relationship('Comment', backref='product')
    orders = db.relationship('Order', backref='product')

    # string print method
    def __repr__(self):
        return f"Name: {self.name}"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)

    def getNiceTime(self):
        return self.created_at.strftime("%d/%m/%y/%I:%M %p")

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


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'
    
# added by Minh
# cart table deleted by Jonas
    
    
# added by Jonas
class ShippingOrder(db.Model):
    __tablename__ = 'shippingaddress'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship('Order', backref='shipping_orders')

    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(120))
    address_line1 = db.Column(db.String(200))
    address_line2 = db.Column(db.String(200))
    suburb = db.Column(db.String(100))
    postal_code = db.Column(db.String(20))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))

    def __repr__(self):
        return f"Shipping for Order ID: {self.order_id}"