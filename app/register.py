from flask import Blueprint, render_template, request, session

registerbp = Blueprint('register', __name__)

@registerbp.route('/register', methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return 'Registered'
    return render_template('register.html')
