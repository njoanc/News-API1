from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_news,get_news,search_news
# from .forms import ReviewForm,UpdateProfile
from .. import db,photos
from ..models import Review, User
from flask_login import login_required, current_user


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    title = 'Home - Welcome to The best News Articles Website Online'

    popular_news = get_news('popular')
    # business_sources = get_sources('business')
    # techCrunch_sources = get_sources('techCrunch')
    # publishedAt_sources= get_sources('publishedAt')

    
    return render_template('index.html', title = title,popular = popular_news)

    # search_news = request.args.get('news_query')

    # if search_news:
    #     return redirect(url_for('search',news_title=search_news))
    # else:
    #     return render_template('index.html', title = title,popular = popular_news,business=business_news, techCrunch=techCrunch_news, publishedAt=publishedAt_news)
    


@main.route('/news/<title>')
def news(title):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(title)

    title = f'{title}'
    # reviews = Review.get_reviews(news.title)

    return render_template('news.html',title = title,news=news)

@main.route('/search/<news_author>')
def search(news_author):
    '''
    View function to display the search articles
    '''
    news_author_list = news_author.split(" ")
    news_author_format = "+".join(news_author_list)
    searched_news = search_news(news_author_format)
    title = f'search articles for {news_author}'
    return render_template('search.html',news = searched_news)

@main.route('/news/review/new/<author>', methods = ['GET','POST'])
@login_required
def new_review(author):
    
    form = ReviewForm()
    news = get_news(author)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

         # Updated review instance
        new_review = Review(news_title=news.title,urlToImage=news.urlToImage,news_review=review,user=current_user)

        # new_review = Review(news.author,title,news.urlToImage,review)
        new_review.save_review()
        return redirect(url_for('news',title = news.title ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)