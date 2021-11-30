from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class GameNameForm(FlaskForm):
    name = StringField('Name', validators=[validators.InputRequired()], render_kw={
        'placeholder': 'Enter your name'
    })
    submit = SubmitField('Enter')
