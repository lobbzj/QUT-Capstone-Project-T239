from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms.fields import TextAreaField, SubmitField, StringField, TimeField, PasswordField, DateField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()], render_kw={
                         "placeholder": "Leave a comment:  "})
    submit = SubmitField('Create')

class CreateForm(FlaskForm):
    type = TextAreaField(validators=[InputRequired()])
    amount = IntegerField(validators=[InputRequired()])
    submit = SubmitField('Book')