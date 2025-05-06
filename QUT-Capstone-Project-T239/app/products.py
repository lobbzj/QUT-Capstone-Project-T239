
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
from .forms import CreateProductForm, CommentForm
from .models import db, Product, Comment
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user


productsbp = Blueprint('product', __name__, url_prefix='/products')


@productsbp.route("/<id>", methods=['GET'])
@productsbp.route("/<id>", methods=['GET', 'POST'])
def show(id):
    product = Product.query.filter_by(id=id).first()
    related_products = Product.query.filter_by(category=product.category).filter(
        Product.id != product.id).limit(3).all()
    comments = Comment.query.filter_by(
        product_id=product.id).order_by(Comment.id.asc()).all()

    cmtForm = CommentForm()

    if request.method == 'POST' and cmtForm.validate_on_submit():
        comment_text = cmtForm.text.data
        if current_user.is_authenticated:
            new_comment = Comment(
                content=comment_text, user_id=current_user.id, product_id=product.id)
            db.session.add(new_comment)
            db.session.commit()
            flash('Comment added!', 'success')
            return redirect(url_for('product.show', id=product.id))
        else:
            flash('You need to be logged in to comment.', 'warning')
            return redirect(url_for('auth.login'))
    elif request.method == 'POST':
        flash('Comment cannot be empty.', 'danger')

    return render_template('productPurchase.html', product=product, related_products=related_products, comments=comments, form=cmtForm)

    # except Exception as e:
    #     print(e)
    #     message = "Product was not found"
    #     return render_template("404.html")


@productsbp.route('/create', methods=['GET', 'POST'])
@login_required
def create_product():
    form = CreateProductForm()

    subcategories = {
        "stadiums & venues": ["Audio System", "Video System", "Drone", "Ticketing", "Security&Safety", "Internet of Thing"],
        "equipment": ["Automated Camera", "Pitch Marking", "Race Timing", "Smart Bat", "Smart Helmet", "Shot Clock", "Disability&Inclusion", "Monitor&Testing"],
        "by sport": ["Athletics", "Basketball", "Golf", "Tennis", "Cricket", "Volleyball", "Hockey"],
        "sports technology": ["Athelete Management", "Coaching&Training", "Fitness&Companion App", "Virtual Reality", "Sports Management Tool", "Social&Fans tool", "Sports Analytics"],
        "wearables and fitness devices": ["Smart Watch", "Smart Clothing", "Fitness Tracker", "Jumping Device", "Health Wearable", "Smart Jursey", "Swim Suit"]
    }

    if request.method == 'POST':
        category = request.form.get('product_category')
        if category in subcategories:
            form.sub_category.choices = [(item, item)
                                         for item in subcategories[category]]

    if form.validate_on_submit():
        try:

            db_file_path = check_upload_file(form)

            product = Product(
                name=form.name.data,
                description=form.description.data,
                image=db_file_path,
                price=float(form.price.data),
                stock=int(form.stock.data),
                category=form.product_category.data,
                sub_category=form.sub_category.data
            )

            db.session.add(product)
            db.session.commit()

            flash('Product created successfully!', 'success')
            return redirect(url_for('main.index'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error creating product: {str(e)}', 'danger')

    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {field}: {error}", 'danger')

    return render_template('create.html', form=form)


def check_upload_file(form):
    # get file data from form
    fp = form.image.data
    filename = fp.filename
    # get the current path of the module file… store image file relative to this path
    BASE_PATH = os.path.dirname(__file__)
    # upload file location – directory of this file/static/image
    upload_path = os.path.join(
        BASE_PATH, 'static/img', secure_filename(filename))
    # store relative path in DB as image location in HTML is relative
    db_upload_path = '/static/img/' + secure_filename(filename)
    # save the file and return the db upload path
    fp.save(upload_path)
    return db_upload_path


@productsbp.route('<id>/comment', methods=['GET', 'POST'])
@login_required
def comment(id):
    product_obj = Product.query.filter_by(id=id).first()
    # here the form is created form = CommentForm()
    form = CommentForm()
    if form.validate_on_submit():

        comment = Comment(text=form.text.data,
                          product=product_obj, user=current_user)
        # print(form.text.data)
        db.session.add(comment)
        try:
            db.session.commit()
            flash("Your comment was successful!")
        except (RuntimeError, TypeError, NameError):
            print(Exception)
            print('ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR!!!!!!')
    return redirect(url_for('product.show', id=id))


@productsbp.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return render_template('searchResults.html', results=[], query=query)

    # Example: search in product name or description (case-insensitive)
    results = Product.query.filter(
        Product.name.ilike(
            f"%{query}%") | Product.description.ilike(f"%{query}%")
    ).all()

    return render_template('searchResults.html', results=results, query=query)
