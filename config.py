import os

class Config:
  """
  General config parent class
  """
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?api_key={}'

class ProdConfig(Config):
  """
  Production configuration child class
  Args:
    Config : The parent configuration class with general configuration settings
  """
  pass
class DevConfig(Config):
  """
  Development configuration child class
  Args:
    Config: The parent configuration class with general configuration settings
  """
  DEBUG =  True
config_options = {
  'development': DevConfig,
  'production' : ProdConfig
}
    