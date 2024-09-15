from flask import Blueprint, render_template, request, session

loginbp = Blueprint('login', __name__)

@loginbp.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return 'Logged in'
    return render_template('login.html')