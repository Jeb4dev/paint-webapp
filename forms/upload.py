from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, HiddenField, validators


class UploadForm(FlaskForm):
    title = StringField('Title', validators=[validators.InputRequired()])
    image = HiddenField('Image', validators=[validators.InputRequired()])
    submit = SubmitField('Post')
