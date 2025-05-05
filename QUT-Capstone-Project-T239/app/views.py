from flask import Blueprint, render_template, request, session
from .models import User, Product, Comment, Order, Payment
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)