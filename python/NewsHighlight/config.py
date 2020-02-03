import os

class Config:

    NEWSHIGHLIGHT_API_BASE_URL ='https://api.the newshighlight.org/3/news/{}?api_key={}'
    NEWSHIGHLIGHT_API_KEY = os.environ.get('NEWSHIGHLIGHT_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}