import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = article('null','Forbes.com','Billy Bambrough, Contributor','Twitter CEO Jack Dorsey Has Made A Bold Prediction About Bitcoin','https://www.forbes.com/sites/billybambrough/2019/02/04/twitter-ceo-jack-dorsey-has-made-a-bold-prediction-about-bitcoin/','2019-02-04T06:10:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()
