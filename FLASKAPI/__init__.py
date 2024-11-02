import sys
import os

# Proje dizinini sys.path'e ekle
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from flask import Flask
from config import Config
from models import db
from routes import api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

def create_app():
    
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    jwt = JWTManager(app)
    db.init_app(app)
    
    app.register_blueprint(api, url_prefix='/api')
    
    return app