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


@app.route('/player_stat', methods=['GET', 'POST'])
def player_stat():
    selected_id = request.args.get('id', None)
    players = Players.query.all()
    current_opponent = Opponents.query.filter_by(date=date.today()).first()
    selected_player = Players.query.filter_by(player_id=selected_id).first()
    return render_template('player_stat.html', current_opponent=current_opponent, players=players,
                           selected_player=selected_player)


@app.route('/edit_stat', methods={'POST'})
def edit_stat():
    player_id = request.form['player_id']
    selected_id = request.form['selected_id']

    current_player = Players.query.filter_by(player_id=player_id).first()
    current_opponent = Opponents.query.filter_by(date=date.today()).first()

    if selected_id == 'ftm':
        current_player.pm_1 += 1
        current_player.pa_1 += 1
        current_opponent.home_team_points += 1
        db.session.commit()
    elif selected_id == 'pm2':
        current_player.pm_2 += 1
        current_player.pa_2 += 1
        current_opponent.home_team_points += 2
        db.session.commit()
    elif selected_id == 'pm3':
        current_player.pm_3 += 1
        current_player.pa_3 += 1
        current_opponent.home_team_points += 3
        db.session.commit()
    elif selected_id == 'fta':
        current_player.pa_1 += 1
        db.session.commit()
    elif selected_id == 'pa2':
        current_player.pa_2 += 1
        db.session.commit()
    elif selected_id == 'pa3':
        current_player.pa_3 += 1
        db.session.commit()
    elif selected_id == 'oreb':
        current_player.rebounds_o += 1
        db.session.commit()
    elif selected_id == 'dreb':
        current_player.rebounds_d += 1
        db.session.commit()
    elif selected_id == 'opf':
        current_player.fouls_o += 1
        db.session.commit()
    elif selected_id == 'dpf':
        current_player.fouls_d += 1
        db.session.commit()
    elif selected_id == 'ast':
        current_player.assists += 1
        db.session.commit()
    elif selected_id == 'to':
        current_player.turnovers += 1
        db.session.commit()
    elif selected_id == 'blk':
        current_player.blocks += 1
        db.session.commit()
    elif selected_id == 'stl':
        current_player.steals += 1
        db.session.commit()
    return "success"


@app.route('/final_stat', methods=['GET', 'POST'])
def final_stat():
    selected_id = request.args.get('id', None)
    players = Players.query.all()
    current_opponent = Opponents.query.filter_by(date=date.today()).first()
    selected_player = Players.query.filter_by(player_id=selected_id).first()

    if selected_id is None:
        fga = 0
        fgm = 0
        percentage1 = 0
        percentage2 = 0
        percentage3 = 0
        percentage_fg = 0
    else:
        fga = selected_player.pa_2 + selected_player.pa_3
        fgm = selected_player.pm_2 + selected_player.pm_3
        if fga == 0:
            percentage_fg = 0
        else:
            percentage_fg = round((fgm / fga) * 100)

        if selected_player.pa_1 == 0:
            percentage1 = 0
        else:
            percentage1 = round((selected_player.pm_1 / selected_player.pa_1) * 100)

        if selected_player.pa_2 == 0:
            percentage2 = 0
        else:
            percentage2 = round((selected_player.pm_2 / selected_player.pa_2) * 100)

        if selected_player.pa_3 == 0:
            percentage3 = 0
        else:
            percentage3 = round((selected_player.pm_3 / selected_player.pa_3) * 100)
    return render_template('final_stat.html', current_opponent=current_opponent, players=players,
                           selected_player=selected_player, fga=fga, fgm=fgm, percentage1=percentage1,
                           percentage2=percentage2, percentage3=percentage3, percentage_fg=percentage_fg)
