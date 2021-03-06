from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default='default.jpg', nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_num = db.Column(db.Integer, db.ForeignKey('books.id'))
    rating = db.Column(db.Integer)

    def __repr__(self):
        return f'User {self.title}'


class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String, nullable=False)
    book_num = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref='book', lazy='dynamic')
    review = db.relationship('Review',backref = 'book',lazy="dynamic")

    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.date_posted}')"

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    review = db.Column(db.String)
    date = db.Column(db.DateTime,default = datetime.utcnow)
    books_id = db.Column(db.Integer,db.ForeignKey('books.id'))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.title}'