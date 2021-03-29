from app import db, login_manager;
from flask_login import UserMixin;
import datetime
from flask_login import current_user;

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True);
    username = db.Column(db.String(120),  unique=True, nullable=False);
    email = db.Column(db.String(120), unique=True, nullable=False);
    password = db.Column(db.String(120), nullable=False);
    trivigame = db.relationship('TriviaGame', backref='author', lazy=True);

    def __repr__(self):
        return f"User ('{self.username}', '{self.email}')";

class TriviaGame(db.Model):
    id = db.Column(db.Integer, primary_key=True);
    content = db.Column(db.String(200), nullable=False);
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now());
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False);
    file = db.Column(db.String(100));

    def __repr__(self):
        return f"TriviaGame('{self.content}', '{self.date}')";