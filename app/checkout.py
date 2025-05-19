from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Product, db, ShippingOrder, Order
from app import db
from app.models import Order, Product, ShippingOrder
from datetime import datetime

checkoutbp = Blueprint('checkout', __name__, url_prefix='/checkout')

@checkoutbp.route('/')
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

@checkoutbp.route('/save', methods=['POST'])
def save_order():
    
    print(request.form)
    # Get data from the form
    total_price = float(request.form.get('total_price', 0))
    shipping_method = request.form.get('shipping_method', 'Standard')
    user_id = current_user.id if current_user.is_authenticated else None

    # Get all products in the user's cart
    cart = session.get('cart', {})
    order_ids = []
    for product_id, quantity in cart.items():
        # Create a new order for each product
        new_order = Order(
            status="Pending",
            total_price=total_price,
            created_at=datetime.now(),
            user_id=user_id,
            product_id=int(product_id)
        )
        db.session.add(new_order)
        db.session.flush()  # Get new_order.id before commit
        order_ids.append(new_order.id)

    # Save shipping info for the first order (or adapt for multiple orders)
    shipping = ShippingOrder(
        order_id=order_ids[0] if order_ids else None,
        first_name=request.form.get('FirstName'),
        middle_name=request.form.get('MiddleName'),
        surname=request.form.get('SurName'),
        phone_number=request.form.get('PhoneNumber'),
        email=request.form.get('Email'),
        address_line1=request.form.get('Addressline1'),
        address_line2=request.form.get('Addressline2'),
        suburb=request.form.get('Suburb'),
        postal_code=request.form.get('PostalCode'),
        city=request.form.get('City'),
        state=request.form.get('State'),
        country=request.form.get('Country')
    )
    db.session.add(shipping)

    db.session.commit()
    session['cart'] = {}

    order_date = datetime.now().strftime('%d/%m/%Y %H:%M (GMT+10) AEST')
    return render_template('confirmation.html', order_date=order_date)