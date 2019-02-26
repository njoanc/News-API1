from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

        
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    # reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    # password_hash = db.Column(db.String(255))

    # def save_review(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @classmethod
    # def get_reviews(cls,id):
    #     reviews = Review.query.filter_by(news_id=id).all()
    #     return reviews

    def __repr__(self):
        return f'User {self.username}'
    
    # pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User',backref = 'role',lazy="dynamic")

#     def __repr__(self):
#         return f'User {self.name}'
    
