import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123@localhost:5432/Library'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '123'

    
