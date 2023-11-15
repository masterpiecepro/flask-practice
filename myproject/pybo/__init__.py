from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config #요까지 함 11월 15일 수요일 부터 담날 새벽 12시 50분까지 ㅎㅎ

def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    return app