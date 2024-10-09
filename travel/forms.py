from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, FileField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}


class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Cover Image', validators=[FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only PNG or JPG files allowed')])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField('Create')

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Create')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('Enter user name')])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email Address', validators=[Email()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Login')