from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,SubmitField,SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class Amount_add(FlaskForm):
    amount = FloatField('Amount',validators=[DataRequired()])
    expense_message = StringField('Message',validators=[DataRequired()])
    category = SelectField('Category',validators=[DataRequired()],choices=[('Miscellaneous','Miscellaneous'),
    ('Cash','Cash'),('Fixed Payment','Fixed Payment'),('Project Payment','Project Payment'),('Raw Material','Raw Material'),('Profit','Profit')])
    date = DateField('Date',format='%Y-%m-%d',validators=[DataRequired()])
    update = SubmitField('Update')


class Miscellaneous(FlaskForm):
    starting_date = DateField('Starting Date',format='%Y-%m-%d',validators=[DataRequired()])
    ending_date = DateField('Ending Date',format='%Y-%m-%d',validators=[DataRequired()])
    check = SubmitField('Check')