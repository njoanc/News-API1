class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL= 'https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&apiKey=d1586deac05c4d1fbf9742533adf9dea'
    NEWS_API_KEY = 'd1586deac05c4d1fbf9742533adf9dea'
   

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

