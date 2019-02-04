class Config:
    '''
    General configuration parent class
    '''
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-04&sortBy=publishedAt&apiKey=fd691520fddc45258320ec9fbfa31d02'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
