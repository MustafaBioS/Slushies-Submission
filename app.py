from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.secret_key = 'MySecretKey123'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    bcrypt = Bcrypt(app)

    from routes import register_routes
    register_routes(app, db, bcrypt)

    migrate = Migrate(app, db)

    return app