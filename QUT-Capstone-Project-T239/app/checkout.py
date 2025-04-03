from flask import Blueprint, render_template, request, session, redirect, url_for, flash
checkoutbp = Blueprint('checkout', __name__, url_prefix='/checkout')

@checkoutbp.route('/')
def show():
    return render_template('checkout.html')