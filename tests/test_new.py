import unittest
from app.models import Source

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of news class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = Source('BBC','BBC','This is a media house','bbc.com',"general",'en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':