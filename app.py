from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MySecretKey123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'

    db.init_app(app)

    migrate = Migrate(app, db)



    return app