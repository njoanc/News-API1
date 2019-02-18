from app import app

import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
        '''
        Function that gets the json response to our url request
        '''
        def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_articles = process_articles(news_articles_list)


    return news_articles

   def process_articles(news_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_articles: A list of news objects
    '''
    news_articles = []
    for news_item in news_list:
        author = news_item.get('author')    
        title = news_item.get('title')
        description = movie_item.get('description')
        url = movie_item.get('url')
        urlToImage = movie_item.get('urlToImage')
        publishedAt = movie_item.get('publishedAt')
        content = news_item.get('content')

        if title:
            new_object = News(author,title,description,url,urlToImage,publishedAt,content)
            movie_articles.append(news_object)

    return news_results 