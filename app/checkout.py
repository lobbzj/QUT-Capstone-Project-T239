from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Product, db

checkoutbp = Blueprint('checkout', __name__, url_prefix='/checkout')

@checkoutbp.route('/')
@login_required
def show():
    cart = session.get('cart', {})  # Get the cart from the session
    cart_items = []

    # Fetch product details for each product in the cart
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': product.price * quantity
            })

    # Calculate the total price of the cart
    total_price = sum(item['total_price'] for item in cart_items)

    # Pass the cart items and total price to the checkout template
    return render_template('checkout.html', items=cart_items, total=total_price)