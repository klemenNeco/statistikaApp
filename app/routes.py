from app import app
from flask import render_template
from app.forms import OpponentForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = OpponentForm()
    return render_template('landingPage.html', form=form)
