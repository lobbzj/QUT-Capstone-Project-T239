from flask import Blueprint, render_template

mainbp = Blueprint('mainbp', __name__)

@mainbp.route('/')
def index():
    return render_template('base.html')