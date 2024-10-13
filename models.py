from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100))

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'))

    episode = db.relationship('Episode', backref='appearances')
    guest = db.relationship('Guest', backref='appearances')

    def validate(self):
        if self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be between 1 and 5")
