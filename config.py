class Config:
  """
  General config parent class
  """
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
    