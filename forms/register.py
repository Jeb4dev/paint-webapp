from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=3)])
    password = PasswordField('Password', [validators.Length(min=3)])
    submit = SubmitField('Register')
