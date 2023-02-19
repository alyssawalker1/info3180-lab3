from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired()])
    TextArea = TextAreaField('Message', validators=[InputRequired()])