import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey=d1586deac05c4d1fbf9742533adf9dea'
    NEWS_API_BASE_URL= 'https://newsapi.org/v2/everything?sources={}&apiKey=d1586deac05c4d1fbf9742533adf9dea'
    NEWS_API_KEY = os.environ.get('d1586deac05c4d1fbf9742533adf9dea') 
    SECRET_KEY= os.environ.get('kazuba')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:kazuba1@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
  

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

