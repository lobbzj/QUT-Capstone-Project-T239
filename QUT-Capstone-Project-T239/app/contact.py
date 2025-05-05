from flask import Blueprint, request, redirect, render_template, flash
from .models import db, Contact

contactbp = Blueprint("contactbp", __name__, url_prefix='/')

@contactbp.route("/contact", methods=["POST"])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    new_contact = Contact(name=name, email=email, message=message)

    db.session.add(new_contact)
    db.session.commit()

    flash('Your message has been sent successfully!', 'success')
    return redirect("/")