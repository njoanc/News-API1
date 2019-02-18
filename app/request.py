from app import app

import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(title):
        
        '''
        Function that gets the json response to our url request
        '''
        get_news_details_url = base_url.format(title,api_key)
        print(get_news_details_url)

        with urllib.request.urlopen(get_news_details_url) as url:
                news_details_data = url.read()
                news_details_response = json.loads(news_details_data)
                print(news_details_response)

        news_object = None

        if news_details_response:
                author = news_details_response.get('author')
                title = news_details_response.get('title')
                description = news_details_response.get('description')
                url = news_details_response.get('url')
                urlToImage = news_details_response.get('urlToImage')
                publishedAt = news_details_response.get('publishedAt')
                content = news_details_response.get('content')

                news_object = News(author,title,description,url,urlToImage,publishedAt,content)

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
                author = news_item.get('author')    
                title = news_item.get('title')
                description = news_item.get('description')
                url = news_item.get('url')
                urlToImage = news_item.get('urlToImage')
                publishedAt = news_item.get('publishedAt')
                content = news_item.get('content')

        if title:
                news_object = News(author,title,description,url,urlToImage,publishedAt,content)
                news_articles.append(news_object)

        return news_articles 

def search_news(news_title):
    search_news_url = 'https://newsapi.org/v2/search/news?api_key={}&query={}'.format(api_key,news_title)

    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_articles = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_articles = process_articles(search_news_list)


    return search_news_articles