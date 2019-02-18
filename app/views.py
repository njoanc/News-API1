from flask import render_template
from app import app
from .request import get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular news, upcoming current,regional and television news
    popular_news = get_news()
    business_news = get_news()
    techCrunch_news = get_news()
    publishedAt_news= get_news()
    title = 'Home - Welcome to The best News Articles Website Online'
    return render_template('index.html', title = title,popular = popular_news, business=business_news, techCrunch= techCrunch_news, publishedAt=publishedAt_news)
    


@app.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news=get_news(id)
    # print(news.author)
    title = f'You are reading {news.title}'
    return render_template('news.html',title = title,news=news)
