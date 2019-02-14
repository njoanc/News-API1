import unittest
from models import news
News = news.news

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('cnn','CNN','Former acting FBI Director Andrew McCabe said he ordered an investigation into whether President Donald Trump obstructed justice as a way to preserve ongoing inquiries into Russian election meddling in case there was an effort to terminate them.','"https://cdn.cnn.com/cnnnext/dam/assets/180316111830-05-andrew-mccabe-lead-image-super-tease.jpg',2019-02-14T14:26:00Z)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()