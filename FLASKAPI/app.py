from __init__ import create_app
from flask_migrate import Migrate
from models import db
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta


app = create_app()

migrate = Migrate(app, db)


if __name__ == '__main__':
  
    app.run(debug=True)