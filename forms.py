from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species",
                         choices=[('cat', 'Cat'), 
                                 ('dog', 'Dog'), 
                                 ('porcupine', 'Porcupine')],
                         validators=[InputRequired()])
    photo_url = StringField("Photo URL", 
                           validators=[Optional(), URL()])
    age = IntegerField("Age",
                      validators=[Optional(), 
                                NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", 
                         validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", 
                          validators=[Optional(), URL()])
    notes = TextAreaField("Notes", 
                         validators=[Optional()])
    available = SelectField("Available?",
                          choices=[('True', 'Yes'), ('False', 'No')],
                          validators=[InputRequired()])