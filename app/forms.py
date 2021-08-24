from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


class OpponentForm(FlaskForm):
    opponent = StringField('', validators=[DataRequired()], id="opponent_input")
    date = DateField('', format='%d-%m-%Y', default=datetime.now(), id="date_input")
    submit = SubmitField('NADALJUJ', id="continue_button")

