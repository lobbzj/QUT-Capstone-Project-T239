from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from flask_login import login_required, current_user

checkoutbp = Blueprint('checkout', __name__, url_prefix='/checkout')

@checkoutbp.route('/')
@login_required
def show():
    return render_template('checkout.html')