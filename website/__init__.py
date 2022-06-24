from locale import format_string
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #initialize flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jkasdfjhasjkhf adfsdklasfd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    return app
