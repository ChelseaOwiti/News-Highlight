import unittest
from models import Newssource
Newssource = newssource.Newssource

class NewssourceTest(unittest.TestCase):
  """
  Test behaviour of our class
  """
  def setUp(self):
    """
    set up method that runs before test
    """
    self.new_newssource = Newssource("", "", "", "")
if __name__ == '__main__':
  unittest.main()