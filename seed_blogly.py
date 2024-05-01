"""Seed file to make sample data for db."""

from models import User, Post, Tag, PostTag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

london = User(first_name = "Lauren", last_name = "London", image_url = "https://cdn.magzter.com/1452682922/1675938396/articles/iQ6hdev_u1676973823823/LAUREN-LONDON-FINDING-NEW-PURPOSE-AFTER-LOSS.jpg")
washington = User(first_name = "Denzel", last_name = "Washington", image_url = "https://www.the-sun.com/wp-content/uploads/sites/6/2023/11/denzel-washington-attends-opening-night-833267780.jpg")
berry = User(first_name = "Halle", last_name = "Berry", image_url = "https://i.pinimg.com/originals/b0/9a/39/b09a3954c53d03d911be0ec7ff0dd9b7.jpg")
flynn = User(first_name = "Rome", last_name = "Flynn", image_url = "https://m.media-amazon.com/images/M/MV5BN2U5ZTQzMDMtMGMwMC00YTJjLWJiNWEtYjYzYjM2NzNiZjA5XkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_.jpg")
union = User(first_name = "Gabrielle", last_name = "Union", image_url = "https://www.usmagazine.com/wp-content/uploads/2023/03/Gabrielle-Union-Feature.jpg?w=800&h=1421&crop=1&quality=86&strip=all")

db.session.add_all([washington, berry, flynn, london, union])
db.session.commit()

# Create some sample posts
posts_data = [
    {
        'title': 'Baking Basics & Beyond',
        'content': 'Embark on a delicious journey as we explore the basics of baking. From essential tools to must-try recipes, learn how to create mouthwatering treats in your own kitchen!',
        'user_id': london.id
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
        'user_id': flynn.id
    },
    {
        'title': 'Budget Travel Hacks',
        'content': 'Satisfy your wanderlust without breaking the bank! Learn savvy travel hacks and insider tips for planning affordable adventures to bucket-list destinations.',
        'user_id': union.id
    },
    {
        'title': 'Mindfulness Practices',
        'content': 'Embrace mindfulness as a path to greater well-being and happiness. Discover practical techniques for living in the present moment and reducing stress in your daily life.',
        'user_id': flynn.id
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
        'user_id': london.id
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

# Sample data for tags
tags_data = [
    {'name': 'fun'},
    {'name': 'cooking'},
    {'name': 'love'},
    {'name': 'fashion'},
    {'name': 'beauty'}
]

# Insert tags into the database
for tag_data in tags_data:
    tag = Tag(**tag_data)
    db.session.add(tag)

db.session.commit()

# Sample data for post_tags (mapping posts to tags)
post_tags_data = [
    {'post_id': 1, 'tag_id': 2},  # Baking Basics & Beyond tagged with cooking
    {'post_id': 1, 'tag_id': 1},  # Baking Basics & Beyond also tagged with fun
    {'post_id': 2, 'tag_id': 1},  # National Park Wonders tagged with fun
    {'post_id': 2, 'tag_id': 2},  # National Park Wonders also tagged with cooking
    {'post_id': 3, 'tag_id': 4},  # Photography Tips 101 tagged with fashion
    {'post_id': 4, 'tag_id': 2},  # Quick & Nutritious Eats tagged with cooking
    {'post_id': 4, 'tag_id': 1},  # Quick & Nutritious Eats also tagged with fun
    {'post_id': 5, 'tag_id': 1},  # Budget Travel Hacks tagged with fun
    {'post_id': 5, 'tag_id': 5},  # Budget Travel Hacks also tagged with beauty
    {'post_id': 6, 'tag_id': 1},  # Mindfulness Practices tagged with fun
    {'post_id': 6, 'tag_id': 5},  # Mindfulness Practices also tagged with beauty
    {'post_id': 7, 'tag_id': 4},  # DIY Home Decor Ideas tagged with fashion
    {'post_id': 8, 'tag_id': 5},  # Thrifty Fashion Tips tagged with beauty
    {'post_id': 9, 'tag_id': 2},  # Gardening for All tagged with cooking
    {'post_id': 10, 'tag_id': 3}, # Worldly Kitchen Delights tagged with love
    {'post_id': 10, 'tag_id': 1}, # Worldly Kitchen Delights also tagged with fun
]

# Insert post_tags into the database
for post_tag_data in post_tags_data:
    post_tag = PostTag(**post_tag_data)
    db.session.add(post_tag)

db.session.commit()