from flask import Blueprint, render_template, request, redirect, url_for

cartbp = Blueprint('cart', __name__, url_prefix='/cart')

cart_items = [
    {'id': 1, 'name': 'Product 1', 'price': 149.99, 'quantity': 1},
    {'id': 2, 'name': 'Product 2', 'price': 160, 'quantity': 2},
    {'id': 3, 'name': 'Product 3', 'price': 185, 'quantity': 1},
]

# displaying the cart
@cartbp.route('/')
def cart():
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', items=cart_items, total=total_price)

# removing items from cart
@cartbp.route('/remove/<int:item_id>', methods=['POST'])
def remove_item(item_id):
    global cart_items
    cart_items = [item for item in cart_items if item['id'] != item_id]
    return redirect(url_for('cart.cart'))

