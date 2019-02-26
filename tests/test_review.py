from app.models import User
from app import db


def setUp(self):
        self.user_Wecode = User(username = 'Wecode',password = 'kazuba1', email = 'wecode@wecode')
        self.new_review = Review(news_title='Review for news',urlToImage="http://s.marketwatch.com/public/resources/MWimages/MW-FU197_bitcoi_ZG_20170913101947.jpg",news_review='This news is the best thing since sliced bread',user = self.user_Wecode )

def tearDown(self):
        Review.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_review.news_title,'Review for news')
        self.assertEquals(self.new_review.imurlToImage,"http://s.marketwatch.com/public/resources/MWimages/MW-FU197_bitcoi_ZG_20170913101947.jpg",news_review='This news is the best thing since sliced bread')
        self.assertEquals(self.new_review.news_review,'This news is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_Wecode)

def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)

def test_get_review_by_id(self):

        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)