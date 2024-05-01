"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import PrimaryKeyConstraint

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class User(db.Model):
    """Blogly user model"""
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String, nullable=False, default='https://cdn-icons-png.flaticon.com/512/3135/3135715.png')
    
    posts = db.relationship('Post', backref='users', cascade="all, delete")
    
    def __repr__(self):
        user = self
        return f"<User id={user.id} first_name= {user.first_name} last_name= {user.last_name} img_url={user.image_url}>"
 
class Post(db.Model):
    """Blogly posts model""" 
    
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="cascade"))
    
    tags = db.relationship('Tag', secondary='post_tags', backref='posts')
    
    def __repr__(self):
        post = self
        return f"<Post id={post.id} title= {post.title} content= {post.content} created_at={post.created_at} user= {post.users.first_name} {post.users.last_name}>"
    
class Tag(db.Model):
    """Blogly tag model""" 
    
    __tablename__ = "tags"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True)
    
    def __repr__(self):
        tag = self
        return f"<Tag id={tag.id} name={tag.name}>"
    
class PostTag(db.Model):
    """Blogly post and tag model""" 
    
    __tablename__ = "post_tags"
    
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete="cascade"))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id', ondelete="cascade"))
    
    __table_args__ = (
        PrimaryKeyConstraint('post_id', 'tag_id'),
    )
    
    def __repr__(self):
        post_tag = self
        return f"<PostTag post_id={post_tag.post_id} tag_id={post_tag.tag_id}>"
    
# last name, first name, title of post
def get_name_title():
    posts = db.session.query(User, Post).join(Post).all()
    
    for user, post in posts:
        print(user.first_name, user.last_name, post.title)
    
    