from flask import Blueprint, render_template, request, session
from .models import User, Product, Comment, Order, Payment

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')