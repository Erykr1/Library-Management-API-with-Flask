from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Otomatik artan ID
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Otomatik olarak oluşturulma zamanı

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username= db.Column(db.String(100),unique=True,nullable=False)
    password_hash=db.Column(db.String(250),nullable=False)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)