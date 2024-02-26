from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator

class InputForm(FlaskForm):
    user_input = StringField('Enter something:', validators=[DataRequired()])
    description = TextAreaField('Enter something 2', validators=[DataRequired()])
    email = EmailField('Enter something 3', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
