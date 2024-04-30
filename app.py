"""Blogly application."""

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "chickens are delicious"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Redirects to user listing"""
    return redirect('/users')

@app.route('/users')
def user_page():
    """Shows user listing"""
    users = User.query.all()
    return render_template('user_list.html', users=users)

@app.route('/users/new')
def create_user():
    """Renders user to list form"""
    
    return render_template('user_create_form.html')

@app.route('/users/new', methods=["POST"])
def add_user():
    """Adds user to list"""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]
    
    new_user = User(first_name=first_name, last_name=last_name, image_url=img_url)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(f'/users/{new_user.id}')

@app.route('/users/<user_id>')
def show_user(user_id):
    """Shows user listing"""
    
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(Post.user_id == user.id).all()
    
    return render_template('user_details.html', user=user, posts=posts)

@app.route('/users/<user_id>/edit')
def show_edit_form(user_id):
    """renders edit form"""
    
    user = User.query.get_or_404(user_id)
    
    return render_template('user_edit_form.html', user=user)

@app.route('/users/<user_id>/edit', methods=["POST"])
def edit_user(user_id):
    """edits a user"""
    edit_user = User.query.get_or_404(user_id)
    
    edit_user.first_name = request.form["first_name"] or edit_user.first_name
    edit_user.last_name = request.form["last_name"] or edit_user.last_name
    edit_user.image_url = request.form["img_url"] or edit_user.image_url
    
    db.session.add(edit_user)
    db.session.commit()
    
    return redirect(f'/users/{edit_user.id}')

@app.route('/users/<user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """deletes a user"""
    
    posts = Post.query.filter(Post.user_id == user_id).all()
    
    for post in posts:
        db.session.delete(post)
    
    User.query.filter_by(id = user_id).delete()

    db.session.commit()
    
    return redirect(f'/')

@app.route('/users/<user_id>/posts/new')
def show_post_form(user_id):
    """Shows form to add post to user"""
    
    user = User.query.get_or_404(user_id)
    
    return render_template('post_form.html', user=user)

@app.route('/users/<user_id>/posts/new', methods=["POST"])
def add_post(user_id):
    """Shows form to add post to user"""
    
    title = request.form["title"]
    content = request.form["content"]
    
    user = User.query.get_or_404(user_id)
    
    new_post = Post(title=title, content=content, user_id=user.id)
    
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(f'/users/{user.id}')

@app.route('/posts/<post_id>')
def show_post(post_id):
    """Shows posts using id"""
    
    post = Post.query.get_or_404(post_id)
    
    return render_template('post.html', post=post)

@app.route('/posts/<post_id>/edit')
def edit_post_form(post_id):
    """Shows form to edit posts"""
    
    post = Post.query.get_or_404(post_id)
    
    user = User.query.get_or_404(post.user.id)
    
    return render_template('post_edit_form.html', post=post, user=user)

@app.route('/posts/<post_id>/edit', methods=["POST"])
def edit_post(post_id):
    """Edit posts by id"""
    
    edit_post = Post.query.get_or_404(post_id)
    
    edit_post.title = request.form["title"] or edit_post.title
    edit_post.content = request.form["content"] or edit_post.content
    
    db.session.add(edit_post)
    db.session.commit()
    
    return redirect(f'/posts/{edit_post.id}')

@app.route('/posts/<post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """deletes a user"""
    
    post = Post.query.get_or_404(post_id)
    user_id = post.user.id
    
    Post.query.filter_by(id = post_id).delete()

    db.session.commit()
    
    return redirect(f'/users/{user_id}')