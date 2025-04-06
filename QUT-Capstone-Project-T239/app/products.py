
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# a url prefix will refer to prefix for the url

productsbp = Blueprint('products', __name__)


@productsbp.route('/products')
def show():
    return render_template('productPurchase.html')
