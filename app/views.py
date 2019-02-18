from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news, get_news, search_news
from .models import review
from .forms import ReviewForm
Review = review.Review


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular news, upcoming current,regional and television news
    popular_news = get_news('popular')
    business_news = get_news('business')
    techCrunch_news = get_news('techCrunch')
    publishedAt_news= get_news('publishedAt')

    title = 'Home - Welcome to The best News Articles Website Online'

     search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_title=search_news))
    else:
    return render_template('index.html', title = title,popular = popular_news,business=business_news, techCrunch=techCrunch_news, publishedAt=publishedAt_news)
    


@app.route('/news/<category>')
def news(category):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(category)
    # print(news.author)
    title = f'You are reading {news.title}'
    return render_template('news.html',title = title,news=news)

@app.route('/search/<news_title>')
def search(news_title):
    '''
    View function to display the search results
    '''
    news_title_list = news_title.split(" ")
    news_title_format = "+".join(news_title_list)
    searched_news = search_news(news_title_format)
    title = f'search results for {news_title}'
    return render_template('search.html',news = searched_news)

@app.route('/news/review/new/<category>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(title)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.category,title,news.urlToImage,review)
        new_review.save_review()
        return redirect(url_for('news',title = movie.title ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)