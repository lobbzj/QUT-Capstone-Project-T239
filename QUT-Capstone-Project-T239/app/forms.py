from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, EqualTo, DataRequired
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

# Create new destination

# product Form
class ProductForm(FlaskForm):
    title = StringField('Product Title', validators=[InputRequired(), Length(
        min=3, max=30)], render_kw={"placeholder": "Enter Product Title"})
    image = FileField('Product Image',
                      validators=[FileRequired(message='Image cannot be empty'),
                                  FileAllowed(
                                      ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')
                                  ])
    description = TextAreaField('Description',
                                validators=[InputRequired(), Length(min=3)], render_kw={"placeholder": "Enter Description:  "})
    price = IntegerField('Price', validators=[InputRequired()], render_kw={
                         "placeholder": "Enter Price"})
    contactDetails = TextAreaField('Contact Details',
                                   validators=[InputRequired(), Length(min=3, max=100)], render_kw={"placeholder": "Enter Contact Details:  "})
    submit = SubmitField("Create")


class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    member_type = RadioField('Member Type', choices=[('guest', 'Guest'), ('business_partner', 'Business Partner')], validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

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


    # User comment
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()], render_kw={
                         "placeholder": "Leave a comment:  "})
    submit = SubmitField('Create')

