from flask_wtf import FlaskForm
from wtforms import validators, widgets, StringField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=3)])
    password = PasswordField('Password', [validators.Length(min=3)])
    submit = SubmitField('Login')
