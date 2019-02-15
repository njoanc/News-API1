from flask import render_template
from app import app
from .request import get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular news
    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    now_showing_news = get_news('now_playing')
    # print(popular_movies)
    title = 'Home - Welcome to The best News Articles Website Online'
    return render_template('index.html', title = title,popular = popular_news,upcoming = upcoming_news, now_showing = now_showing_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title)


@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    title = f'You are reading {news_id}'
    return render_template('news.html',title = title)
