from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from datetime import datetime
confirmationbp = Blueprint('confirmation', __name__, url_prefix='/confirmation')

@confirmationbp.route('/')
def show():
    return render_template('confirmation.html')

def orderdate():
    current_date = datetime.now().strftime('%D/%m/%Y')
    return render_template('confirmation.html', order_date = current_date)