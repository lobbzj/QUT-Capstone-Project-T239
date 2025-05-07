from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user
from .models import Cart, Product, db

cartbp = Blueprint('cart', __name__, url_prefix='/cart')

# displaying the cart
@cartbp.route('/')
def view_cart():
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

    return render_template('cart.html', items=cart_items, total=total_price)

# Adding items to the cart
@cartbp.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Initialize the cart in the session if it doesn't exist
    if 'cart' not in session:
        session['cart'] = {}

    # Get the quantity from the form
    quantity = int(request.form.get('product_qty', 1))

    # Add the product to the cart or update its quantity
    cart = session['cart']
    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity

    session['cart'] = cart  # Save the updated cart back to the session

    # Check the action (add_to_cart or purchase)
    action = request.form.get('action')
    if action == 'purchase':
        flash('Product added to cart! Redirecting to checkout...', 'success')
        return redirect(url_for('checkout.show'))  # Redirect to the checkout page
    else:
        flash('Product added to cart!', 'success')
        return redirect(url_for('product.show', id=product_id))  # Redirect back to the product page

# removing items from cart
@cartbp.route('/remove/<int:product_id>', methods=['POST'])
def remove_item(product_id):
    cart = session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]  # Remove the product from the cart

    session['cart'] = cart  # Save the updated cart back to the session
    return redirect(url_for('cart.view_cart'))

# Updating item quantity in the cart
@cartbp.route('/update/<int:product_id>', methods=['POST'])
def update_quantity(product_id):
    cart = session.get('cart', {}) 
    new_quantity = int(request.form.get('quantity', 1)) 
    if str(product_id) in cart:
        if new_quantity > 0:
            cart[str(product_id)] = new_quantity
        else:
            del cart[str(product_id)] 
    session['cart'] = cart  
    flash('Cart updated successfully!', 'success')
    return redirect(url_for('cart.view_cart'))