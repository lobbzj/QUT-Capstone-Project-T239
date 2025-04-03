
from flask import Blueprint, render_template, request, session, redirect, url_for, flash
# a url prefix will refer to prefix for the url

productsbp = Blueprint('products', __name__)


@productsbp.route('/products')
def show():
    return render_template('productPurchase.html')

from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from .models import Comment, Product, Booking
from .forms import ProductForm, CommentForm
import os
from werkzeug.utils import secure_filename
from . import db
from flask_login import login_required, current_user
# import details.html

# handles different destiantion pages

# a url prefix will refer to prefix for the url
productsbp = Blueprint('products', __name__, url_prefix='/products')


# this will productually be used to determine what destination is used
@productsbp.route("/<id>", methods=['GET', 'POST'])
def show(id):  # not done yet
    try:
        product = Product.query.filter_by(id=id).first()
        cmtForm = CommentForm()

        if id == None:
            id = "products/create"

        return render_template("products/details.html", product=product, form=cmtForm)
    except:
        message = "product was not found"
        return render_template("error.html", errorMessage=message)


@productsbp.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    print('Method  type: ', request.method)
    productForm = ProductForm()  # I dont know why this ProductForm is not green
    if productForm.validate_on_submit():
        db_file_path = check_upload_file(productForm)
        product = Product(productTitle=productForm.title.data, address=productForm.address.data, date=productForm.date.data, image=db_file_path, startTime=productForm.startTime.data, endTime=productForm.endTime.data,
                      description=productForm.description.data,
                      price=productForm.price.data, contactDetails=productForm.contactDetails.data, user=current_user)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products.create'))

    flash('Successfully Created Product!')
    return render_template('products/create.html', form=productForm)


def check_upload_file(form):
    fp = form.image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)
    upload_path = os.path.join(
        BASE_PATH, 'static/image', secure_filename(filename))
    db_upload_path = '/static/image/' + secure_filename(filename)
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
    return redirect(url_for('products.show', id=id))


# @productsbp.route('<id>/booking', methods=['GET', 'POST'])
# @login_required
# def booking(id):
#     product_obj = Product.query.filter_by(id=id).first()
#     bookform = BookingForm()

#     if bookform.validate_on_submit():
#         booking = Booking(type=bookform.type.data, amount=bookform.amount.data,
#                           product_id=product_obj, user_id=current_user)
#         db.session.add(booking)
#         db.session.commit()
#         flash("Successful Booking")
#     return redirect(url_for('products.show', id=id))