
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# a url prefix will refer to prefix for the url

productsbp = Blueprint('products', __name__, url_prefix='/products')


@productsbp.route('/purchase')
def show():
    return render_template('productPurchase.html')
