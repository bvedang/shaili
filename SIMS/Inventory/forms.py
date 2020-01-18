from wtforms import StringField,SubmitField,IntegerField
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,InputRequired

class Form(FlaskForm):
    start_date = DateField('To',validators=[DataRequired()])
    ending_date = DateField('Till',validators=[DataRequired()])
    submit = SubmitField("Check")