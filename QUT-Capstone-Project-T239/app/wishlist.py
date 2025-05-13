from flask import Blueprint, session, redirect, url_for, flash, render_template
from app.models import Product  # Import your Product model

wishlist_bp = Blueprint('wishlist', __name__)

@wishlist_bp.route('/wishlist/add/<int:id>', methods=['POST'])
def add_to_wishlist(id):
    product = Product.query.get_or_404(id)
    if 'wishlist' not in session:
        session['wishlist'] = []
    if product.id not in session['wishlist']:
        session['wishlist'].append(product.id)
        session.modified = True
        flash(f"{product.name} has been added to your wishlist.", "success")
    else:
        flash(f"{product.name} is already in your wishlist.", "info")
    return redirect(url_for('product.show', id=id))

@wishlist_bp.route('/wishlist')
def show_wishlist():
    if 'wishlist' not in session or not session['wishlist']:
        wishlist_items = []
    else:
        wishlist_items = Product.query.filter(Product.id.in_(session['wishlist'])).all()
    return render_template('wishlist.html', wishlist_items=wishlist_items)

@wishlist_bp.route('/wishlist/remove/<int:id>', methods=['POST'])
def remove_from_wishlist(id):
    if 'wishlist' in session and id in session['wishlist']:
        session['wishlist'].remove(id)
        session.modified = True
        flash("Item removed from your wishlist.", "info")
    return redirect(url_for('wishlist.show_wishlist'))