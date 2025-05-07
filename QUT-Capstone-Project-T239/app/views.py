from flask import Blueprint, render_template, request, session
from app.models import User, Product, Comment, Order, Payment
from . import db

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    products = Product.query.order_by(Product.id.desc()).limit(8).all()
<<<<<<< HEAD
    # Fetch unique categories for filtering
    categories = {product.category for product in products if product.category}
    return render_template('index.html', products=products, categories=categories)
=======
    return render_template('index.html', products=products)


>>>>>>> Search-Attempt
