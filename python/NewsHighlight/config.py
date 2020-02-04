import os

class Config:

    HIGHLIGHT_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apikey=0412983810954d639953702fca063935'  
    NEWSHIGHLIGHT_API_KEY = os.environ.get('NEWSHIGHLIGHT_API_KEY')
    NEWS_HLIGHT='https://newsapi.org/v2/everything?&apiKey=0412983810954d639953702fca063935' 
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
"development":DevConfig,
"production":ProdConfig
}