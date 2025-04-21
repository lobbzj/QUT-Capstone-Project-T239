from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash
from .forms import LoginForm, RegisterForm
from .models import User
from . import db

# Blueprint
authbp = Blueprint('auth', __name__)

# Register route
@authbp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        uname = register_form.user_name.data
        pwd = register_form.password.data
        email = register_form.email_id.data
        mobile = register_form.mobile.data
        address = register_form.address.data
        city = register_form.city.data
        state = register_form.state.data
        zip_code = register_form.zip_code.data
        member_type = register_form.member_type.data

        # Combine address fields
        full_address = f"{address}, {city}, {state} {zip_code}"

        # Check if user already exists
        user = db.session.scalar(db.select(User).where(User.name == uname))
        if user:
            login_user(user) # minh added this
            flash('Username already exists, please try another.', 'danger')
            return redirect(url_for('auth.register'))

        # Hash the password
        pwd_hash = generate_password_hash(pwd)

        # Create new user
        # changed email=email --> emailid=email
        new_user = User(name=uname, password_hash=pwd_hash, mobile=mobile, email=email, address=full_address, member_type=member_type)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')

        return redirect(url_for('auth.login'))
        

    return render_template('user.html', form=register_form, heading='Register')



# Login route
@authbp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_name = login_form.user_name.data
        password = login_form.password.data
        member_type = login_form.member_type.data

        # Check if user exists
        user = db.session.scalar(db.select(User).where(User.name == user_name))

        if user is None:
            flash('Incorrect username', 'danger')
        elif not check_password_hash(user.password_hash, password):
            flash('Incorrect password', 'danger')
        else:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))

    return render_template('user.html', form=login_form, heading='Login', action='login')


# Logout route
@authbp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

