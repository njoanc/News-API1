import os

class Config:
    """
    General configurations parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:kazuba1@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'   

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    """
    Production configuration child class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")   

class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:kazuba1@localhost/pitch'
    

class DevConfig(Config):
    """
    Development config child class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:kazuba1@localhost/pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}