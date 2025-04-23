from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime, timedelta
confirmationbp = Blueprint('confirmation', __name__, url_prefix='/confirmation')

@confirmationbp.route('/')
@login_required
def show():
    # Get the current date and time in GMT+10 (AEST)
    gmt_plus_10 = datetime.utcnow() + timedelta(hours=10)
    order_date = gmt_plus_10.strftime('%d/%m/%Y %H:%M (GMT+10) AEST')

    # Pass the formatted order date to the template
    return render_template('confirmation.html', order_date=order_date)



