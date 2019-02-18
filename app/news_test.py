import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("Bitstop","Bitstop dévoile la nouvelle génération de distributeurs automatiques de bitcoin, lors de la conférence EuroCIS","MIAMI, 18 février 2019 /PRNewswire/ -- Bitstop, pionnier en matière de distributeurs automatiques de bitcoin (Bitcoin ATM), s'est associé avec KIOSK Information Systems (KIOSK), le plus important fournisseur de solutions personnalisées en libre-service en Amé…","https://www.prnewswire.com/news-releases/bitstop-devoile-la-nouvelle-generation-de-distributeurs-automatiques-de-bitcoin-lors-de-la-conference-eurocis-844172769.html","https://mma.prnewswire.com/media/628363/Bitstop_Logo.jpg?p=facebook", "2019-02-18T06:03:00Z","La plateforme logicielle des distributeurs automatiques de bitcoin Bitstop, associée au matériel de pointe de KIOSK, établit une nouvelle référence dans le secteur des distributeurs automatiques de bitcoin qui, parti de rien, est passé à plus de 4000 distribu… [+2955 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()