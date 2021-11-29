import os


class Config:
    SECRET_KEY: str = os.environ.get('SECRET_KEY', 'super-secret-key')
    WTF_CSRF_SECRET_KEY: str = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL', 'sqlite:///app.db').replace('postgres', 'postgresql')
    IMG_BB_API_KEY: str = os.environ.get('IMG_BB_API_KEY', '')
