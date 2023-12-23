import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_network.settings")
django.setup()

import random
import json
from faker import Faker
from users.models import User
from social_app.models import Post, Like


with open("config.json", "r") as f:
    config = json.load(f)

bot = Faker()

for i in range(config["number_of_users"]):
    username = bot.user_name()

    user = User.objects.create_user(username=username, password="password")

    for j in range(random.randint(1, config["max_posts_per_user"])):
        title = bot.sentence()
        content = bot.text()

        post = Post.objects.create(author=user, title=title, content=content)


for i in range(config["max_likes_per_user"]):
    post = Post.objects.order_by("?").first()

    Like.objects.create(user=random.choice(User.objects.all()), post=post)
