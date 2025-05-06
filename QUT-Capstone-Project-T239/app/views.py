from flask import Blueprint, render_template, request, session
from .models import User, Product, Comment, Order, Payment
from . import db

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    products = Product.query.order_by(Product.id.desc()).limit(8).all()
    return render_template('index.html', products=products)


