from app import app

import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(id):
    '''
    Function that gets the json response to our url request
    '''
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None

        if news_details_response:
                id = news_details_response.get('id')
                name = news_details_response.get('name')
                author = news_details_response.get('author')
                title  = news_details_response.get('title ')
                description = news_details_response.get('description')
                url = news_details_response.get('url')
                urlToImage=news_details_response.get('urlToImage')
                publishedAt = news_details_response.get('publishedAt')
                content = news_details_response.get('content')

                 news_object = News(id,name,author,title,description,url,urlToImage,publishedAt,content)
        else:
                print("API didn't succeed")
    return news_object

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
        id = news_item.get('id')
        name=news_item.get('name')
        author=news_item.get('author')
        title = news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt=news_item.get('publishedAt')
        content= news_item.get('content')
        

        if urlToImage:
            news_object = News(id,name,author,title,description,url,urlToImage,publishedAt,content)
            news_articles.append(news_object)

    return news_articles