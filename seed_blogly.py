"""Seed file to make sample data for db."""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

hanks = User(first_name = "Tom", last_name = "Hanks", image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Tom_Hanks_TIFF_2019.jpg/220px-Tom_Hanks_TIFF_2019.jpg")
washington = User(first_name = "Denzel", last_name = "Washington", image_url = "https://www.the-sun.com/wp-content/uploads/sites/6/2023/11/denzel-washington-attends-opening-night-833267780.jpg")
berry = User(first_name = "Halle", last_name = "Berry", image_url = "https://i.pinimg.com/originals/b0/9a/39/b09a3954c53d03d911be0ec7ff0dd9b7.jpg")
depp = User(first_name = "Johnny", last_name = "Depp", image_url = "https://m.media-amazon.com/images/M/MV5BOTBhMTI1NDQtYmU4Mi00MjYyLTk5MjEtZjllMDkxOWY3ZGRhXkEyXkFqcGdeQXVyNzI1NzMxNzM@._V1_.jpg")
union = User(first_name = "Gabrielle", last_name = "Union", image_url = "https://www.usmagazine.com/wp-content/uploads/2023/03/Gabrielle-Union-Feature.jpg?w=800&h=1421&crop=1&quality=86&strip=all")

db.session.add_all([hanks, washington, berry, depp, union])
db.session.commit()

# Create some sample posts
posts_data = [
    {
        'title': 'Baking Basics & Beyond',
        'content': 'Embark on a delicious journey as we explore the basics of baking. From essential tools to must-try recipes, learn how to create mouthwatering treats in your own kitchen!',
        'user_id': hanks.id
    },
    {
        'title': 'National Park Wonders',
        'content': 'Uncover the beauty of America’s national parks as we venture off the beaten path. From breathtaking landscapes to wildlife encounters, let’s discover nature’s wonders together.',
        'user_id': washington.id
    },
    {
        'title': 'Photography Tips 101',
        'content': 'Capture stunning moments with confidence as we dive into the world of photography. From composition techniques to camera settings, unleash your creativity and elevate your photos!',
        'user_id': berry.id
    },
    {
        'title': 'Quick & Nutritious Eats',
        'content': 'Transform your meals with wholesome ingredients and simple recipes. Discover nutritious dishes that are as delicious as they are easy to make!',
        'user_id': depp.id
    },
    {
        'title': 'Budget Travel Hacks',
        'content': 'Satisfy your wanderlust without breaking the bank! Learn savvy travel hacks and insider tips for planning affordable adventures to bucket-list destinations.',
        'user_id': union.id
    },
    {
        'title': 'Mindfulness Practices',
        'content': 'Embrace mindfulness as a path to greater well-being and happiness. Discover practical techniques for living in the present moment and reducing stress in your daily life.',
        'user_id': hanks.id
    },
    {
        'title': 'DIY Home Decor Ideas',
        'content': 'Personalize your living space with DIY decor projects that reflect your style and personality. Get inspired with easy-to-follow tutorials and budget-friendly design ideas!',
        'user_id': washington.id
    },
    {
        'title': 'Thrifty Fashion Tips',
        'content': 'Elevate your wardrobe without emptying your wallet! Discover smart shopping tips and trendy outfit ideas that prove fashion doesn’t have to come with a hefty price tag.',
        'user_id': berry.id
    },
    {
        'title': 'Gardening for All',
        'content': 'Connect with nature and nurture your green thumb with gardening tips for every season. From beginner basics to advanced techniques, let’s grow together!',
        'user_id': depp.id
    },
    {
        'title': 'Worldly Kitchen Delights',
        'content': 'Embark on a culinary adventure from the comfort of your own home! Explore diverse cuisines, discover new ingredients, and savor the flavors of the world.',
        'user_id': union.id
    }
]

# Insert posts into the database
for post_data in posts_data:
    post = Post(**post_data)
    db.session.add(post)

db.session.commit()

