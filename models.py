from app import db


class User(db.Model):

    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, nullable = False)
    password = db.Column(db.String(64), unique = False, nullable = True)

    def __repr__(self):
        return f"<User {self.username}>"