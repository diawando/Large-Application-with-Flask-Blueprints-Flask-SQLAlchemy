import os

class Config:
    SECRET_KEY = os.environ.get('7f7af3a82860051b621ade99ae0cafc538193178ceb5fd70')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:lavie@localhost:5432/social_media"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

