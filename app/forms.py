from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


class OpponentForm(FlaskForm):
    opponent = StringField('Vpiši ime nasprotnika', validators=[DataRequired()])
    date = DateField('Izberi datum tekme', format='%d-%m-%Y', default=datetime.now())
    submit = SubmitField('NADALJUJ')

