from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, FloatField, FileField
from wtforms.validators import DataRequired, NumberRange

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired(), NumberRange(min=1)])
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired(), NumberRange(min=1)])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    type = SelectField('Type', choices=[('Apartment', 'Apartment'), ('House', 'House')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired()])

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
