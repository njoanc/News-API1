from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
        
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
    
    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'