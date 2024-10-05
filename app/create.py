from flask import Blueprint, render_template

createbp = Blueprint('create', __name__)

@createbp.route('/create')
def create():
    return render_template('create.html')
