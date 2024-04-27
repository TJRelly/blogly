"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

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
    image_url = db.Column(db.String, server_default='https://cdn-icons-png.flaticon.com/512/3135/3135715.png')
    
    def __repr__(self):
        user = self
        return f"<User id={user.id} first_name= {user.first_name} last_name= {user.last_name} img_url={user.image_url}>"