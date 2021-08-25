from app import db


class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(50), index=True, nullable=False)
    jersey_no = db.Column(db.String(50), index=True, nullable=False)
    pa_1 = db.Column(db.Integer, index=True)
    pm_1 = db.Column(db.Integer, index=True)
    pa_2 = db.Column(db.Integer, index=True)
    pm_2 = db.Column(db.Integer, index=True)
    pa_3 = db.Column(db.Integer, index=True)
    pm_3 = db.Column(db.Integer, index=True)
    fouls_o = db.Column(db.Integer, index=True)
    fouls_d = db.Column(db.Integer, index=True)
    rebounds_o = db.Column(db.Integer, index=True)
    rebounds_d = db.Column(db.Integer, index=True)
    assists = db.Column(db.Integer, index=True)
    turnovers = db.Column(db.Integer, index=True)
    blocks = db.Column(db.Integer, index=True)
    steals = db.Column(db.Integer, index=True)
    id_positon = db.Column(db.Integer, db.ForeignKey('positions.position_id'), nullable=False)
    id_opponent = db.Column(db.Integer, db.ForeignKey('opponents.opponent_id'))

    def __repr__(self):
        return '<{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}>'\
            .format(self.player_id, self.full_name, self.pa_1, self.pm_1, self.pa_2, self.pm_2, self.pa_3, self.pm_3,
                    self.fouls_o, self.fouls_d, self.rebounds_o, self.rebounds_d, self.assists, self.turnovers,
                    self.blocks, self.steals)

    def __init__(self):
        print("bottom text")


class Positions(db.Model):
    position_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    position = db.Column(db.String(50), index=True, nullable=False)
    id_position = db.relationship('Players', backref='position', lazy=True)

    def __repr__(self):
        return '<{}. {}>'.format(self.position_id, self.position)

    def __init__(self, position_id, position):
        self.position_id = position_id
        self.position = position


class Opponents(db.Model):
    opponent_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    team_name = db.Column(db.String(50), index=True)
    points = db.Column(db.Integer, index=True)
    score = db.Column(db.Boolean, index=True)
    result = db.Column(db.Boolean, index=True)
    date = db.Column(db.Date, index=True, nullable=False)
    home_team_points = db.Column(db.Integer, index=True)
    id_opponent = db.relationship('Players', backref='opponent', lazy=True)

    def __repr__(self):
        return '<{}: {} - {}>'.format(self.opponent_id, self.team_name, self.date)

    def __init__(self, team_name, date):
        self.team_name = team_name
        self.date = date
        self.points = 0
