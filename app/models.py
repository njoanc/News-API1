class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,url,urlToImage, publishedAt, content):
        self.author =author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content=content



class Review:

    all_reviews = []

    def __init__(self,author,title,description,url,urlToImage, publishedAt, content):
        self.news_author = news_author
        self.news_title = news_title
        self.news_description = news_description
        self.news_url = news_url
        self.news_urlToImage = news_urlToImage
        self.news_publishedAt = news_publishedAt
        self.news_content = news_content


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,title):

        response = []

        for review in cls.all_reviews:
            if review.news_title == title:
                response.append(review)

        return response