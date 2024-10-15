from flask import Blueprint, render_template, request, session, redirect, url_for, flash
confirmbp = Blueprint('confirm', __name__, url_prefix='/confirm')

@confirmbp.route('/')
def show():
    return render_template('confirm.html')