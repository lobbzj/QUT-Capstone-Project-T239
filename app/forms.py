from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, EqualTo, DataRequired
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

# Login Form
class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    member_type = RadioField('Member Type', choices=[('guest', 'Guest'), ('business_partner', 'Business Partner')], validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

# Registration Form
class RegisterForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    email_id = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    mobile = StringField('Mobile Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[
        ('QLD', 'QLD'), ('NSW', 'NSW'), ('VIC', 'VIC'), ('SA', 'SA'),
        ('WA', 'WA'), ('TAS', 'TAS'), ('NT', 'NT'), ('ACT', 'ACT')
    ], validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    member_type = RadioField('Member Type', choices=[('guest', 'Guest'), ('business_partner', 'Business Partner')], validators=[DataRequired()])
    validation_code = StringField('Validation Code')  # needed for business partner
    submit = SubmitField('Register')

# Create Product Form
class CreateProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Product Description', validators=[DataRequired()])
    image = FileField('Product Image', validators=[FileRequired(message='Image cannot be empty'), FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])
    price = StringField('Product Price', validators=[DataRequired()])
    stock = StringField('Product Stock', validators=[DataRequired()])
    product_category = SelectField('Product Category', choices=[
        ('stadiums & venues', 'Stadiums & Venues'),
        ('equipment', 'Equipment'),
        ('by sport', 'By Sport'),
        ('sports technology', 'Sports Technology'),
        ('wearables and fitness devices', 'Wearables and Fitness Devices')
    ], validators=[DataRequired()])
    sub_category = SelectField('Sub Category', choices=[], validators=[DataRequired()]) 
    submit = SubmitField('Create Product')


# Comment Form
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()], render_kw={
                         "placeholder": "Leave a comment:  "})
    submit = SubmitField('Create')

