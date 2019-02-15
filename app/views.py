from flask import render_template
from app import app
from .request import get_news,get_news


# Views
@app.route('/news/<int:id>')
def news(id):

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular news
    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    current_showing_news = get_news('current_broadcasting')
    regional_news= get_news('newspapers')
    mass_media_news=get_news('television')
    # print(popular_movies)
    title = 'Home - Welcome to The best News Articles Website Online'
    return render_template('index.html', title = title,popular = popular_news,upcoming = upcoming_news, current_broadcasting = current_showing_news,newspapers=regional_news,television=mass_media_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title)


@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    news=get_news(id)
    title = f'You are reading {news.title}'
    return render_template('news.html',title = title,news=news)
