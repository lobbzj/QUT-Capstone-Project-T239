from flask import Blueprint, render_template, request, session
from app.models import User, Product, Comment, Order, Payment
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    # Fetch all products
    products = Product.query.all()

    # Fetch unique categories for filtering
    categories = {product.category for product in products if product.category}
    return render_template('index.html', products=products, categories=categories)