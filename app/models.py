class Source:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self,id,name,description):
        self.id=id
        self.name=name
        self.description = description

class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author=author
        self.title = title
        self.description=description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content


class Review:

    all_reviews = []

    def __init__(self,news_id,name,category,language,country):
        self.news_id = news_id
        self.name = name
        self.category = category
        self.language = language
        self.country = country

    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response