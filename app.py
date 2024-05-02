"""Blogly application."""

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag
from datetime import datetime

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

    user = User.query.get(user_id)
    
    db.session.delete(user)
    db.session.commit()
    
    return redirect(f'/')

@app.route('/users/<user_id>/posts/new')
def show_post_form(user_id):
    """Shows form to add post to user"""
    
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    
    return render_template('post_form.html', user=user, tags=tags)

@app.route('/users/<user_id>/posts/new', methods=["POST"])
def add_post(user_id):
    """Shows form to add post to user"""
    
    title = request.form["title"]
    content = request.form["content"]
    
    user = User.query.get_or_404(user_id)
    
    new_post = Post(title=title, content=content, user_id=user.id)
    db.session.add(new_post)
    
    tags = request.form.getlist('tags')
    for tag_name in tags:
        tag = Tag.query.filter_by(name = tag_name).one()
        new_post.tags.append(tag)
    
    db.session.commit()
    
    return redirect(f'/users/{user.id}')

@app.route('/posts/<post_id>')
def show_post(post_id):
    """Shows posts using id"""
    
    post = Post.query.get_or_404(post_id)
    time = post.created_at.strftime(f"%a %b %d %Y, %-I:%M %p")
    
    return render_template('post.html', post=post, time=time)

@app.route('/posts/<post_id>/edit')
def edit_post_form(post_id):
    """Shows form to edit posts"""
    
    post = Post.query.get_or_404(post_id)
    
    tags = Tag.query.all()
    
    return render_template('post_edit_form.html', post=post, tags=tags)

@app.route('/posts/<post_id>/edit', methods=["POST"])
def edit_post(post_id):
    """Edit posts by id"""
    
    edit_post = Post.query.get_or_404(post_id)
    
    edit_post.title = request.form["title"] or edit_post.title
    edit_post.content = request.form["content"] or edit_post.content
    edit_post.tags = []
    
    tags = request.form.getlist('tags')
    
    for tag_name in tags:
        tag = Tag.query.filter_by(name = tag_name).one()
        edit_post.tags.append(tag)
    
    db.session.add(edit_post)
    db.session.commit()
    
    return redirect(f'/posts/{edit_post.id}')

@app.route('/posts/<post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """Deletes a post"""
    
    post = Post.query.get_or_404(post_id)
    user_id = post.users.id
    
    Post.query.filter_by(id = post_id).delete()

    db.session.commit()
    
    return redirect(f'/users/{user_id}')

@app.route('/tags')
def show_tags():
    """show tags page"""
    
    tags = Tag.query.all()
    
    return render_template('tags.html', tags=tags)

@app.route('/tags/<tag_id>')
def show_tag_details(tag_id):
    """show tag detail page"""
    
    tag = Tag.query.get(tag_id)
    
    return render_template('tag_details.html', tag=tag)

@app.route('/tags/new')
def add_tag_page():
    """add tag to tags list"""
    
    return render_template('tag_create_form.html')

@app.route('/tags/new', methods=["POST"])
def add_tag_database():
    """adds tag to database"""
    
    name = request.form["name"]
    new_tag = Tag(name=name)
    
    db.session.add(new_tag)
    db.session.commit()
    
    return redirect('/tags')

@app.route('/tags/<tag_id>/edit')
def edit_tag(tag_id):
    """shows edit tag page"""
    
    tag = Tag.query.get(tag_id)
    
    return render_template("tag_edit_form.html", tag=tag)

@app.route('/tags/<tag_id>/edit', methods=["POST"])
def edit_tag_data(tag_id):
    """shows edit tag page"""
    
    new_tag = Tag.query.get(tag_id)
    
    new_tag.name = request.form["name"]
    
    db.session.add(new_tag)
    db.session.commit()
    
    return redirect("/tags")

@app.route('/tags/<tag_id>/delete', methods=["POST"])
def delete_tag(tag_id):
    """shows edit tag page"""
    
    tag = Tag.query.get(tag_id)
    
    db.session.delete(tag)
    db.session.commit()
    
    return redirect("/tags")