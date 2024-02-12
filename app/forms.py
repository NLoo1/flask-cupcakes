from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, FloatField, TextAreaField, validators
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddCupcakeForm(FlaskForm):
    """Form for adding pets."""

    flavor= StringField("Flavor",
                      validators=[InputRequired()])
    size= SelectField("Size",
                      validators=[InputRequired()], choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])
    rating= IntegerField("Rating",
                      validators=[InputRequired(), NumberRange(min=1, max=5)])
    image= StringField("Image URL",
                      validators=[InputRequired(), URL()])
