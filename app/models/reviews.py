class Review:

    all_reviews = []

    def __init__(self,news_title,author,description,url,urlToImage,publishedAt,content):
        self.news_title = news_title
        self.author = author
        self.descriptionl = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    class Review:


    @classmethod
    def get_reviews(cls,title):

        response = []

        for review in cls.all_reviews:
            if review.news_title == title:
                response.append(review)

        return response