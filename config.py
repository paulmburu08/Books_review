import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://paul:pauldatabase@localhost/bookreview1'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='static/profile_pics'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass
     
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://paul:pauldatabase@localhost/bookreview1'    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://paul:pauldatabase@localhost/bookreview1'
    
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}