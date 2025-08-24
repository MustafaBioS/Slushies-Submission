from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, nullable = False)
    password = db.Column(db.String(64), unique = False, nullable = True)

    def __repr__(self):
        return f"<User {self.username}>"
    
class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(64), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('tasks', lazy=True))
