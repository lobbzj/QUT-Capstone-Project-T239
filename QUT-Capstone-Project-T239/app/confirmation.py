from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from datetime import datetime
confirmationbp = Blueprint('confirmation', __name__, url_prefix='/confirmation')

@confirmationbp.route('/')
def show():
    current_date = datetime.now().strftime('%d/%m/%Y')
    id_date = datetime.now().strftime('%Y%m%d')
    return render_template('confirmation.html', order_date = current_date, ID_date = id_date)



