from app import app
from flask import render_template, redirect, url_for
from app.forms import OpponentForm
from app.models import db, Opponents


@app.route('/', methods=['GET', 'POST'])
def index():
    form = OpponentForm()
    if form.validate_on_submit():
        opponent = Opponents(form.opponent.data, form.date.data)
        db.session.add(opponent)
        db.session.commit()
        return redirect(url_for('playerList'))
    return render_template('landingPage.html', form=form)
