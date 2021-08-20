from app import app
from flask import render_template, redirect, url_for, jsonify, request
from app.forms import OpponentForm
from app.models import db, Opponents, Players
from datetime import date


@app.route('/', methods=['GET', 'POST'])
@app.route('/landingPage', methods=['GET', 'POST'])
def index():
    form = OpponentForm()
    if form.validate_on_submit():
        opponent = Opponents(form.opponent.data, form.date.data)
        db.session.add(opponent)
        db.session.commit()
        return redirect(url_for('game'))
    return render_template('landingPage.html', form=form)


@app.route('/game', methods=['GET', 'POST'])
def game():
    players = Players.query.all()
    current_opponent = Opponents.query.filter_by(date=date.today()).first()
    return render_template('game.html', current_opponent=current_opponent, players=players)


@app.route('/add_points', methods=['POST'])
def add_points():
    current_opponent = Opponents.query.filter_by(date=date.today()).first()
    current_points = current_opponent.points
    current_opponent.points = int(current_points) + int(request.form['increment'])
    db.session.commit()
    return jsonify({'result': 'success', 'points': current_opponent.points})
