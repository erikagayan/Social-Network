from django.test import TestCase
from django.contrib.auth import get_user_model
from social_app.models import Post, Like, Analytics

User = get_user_model()


class PostModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.post = Post.objects.create(
            author=self.user, title="Test Post", content="Test content"
        )

    def test_post_creation(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "Test content")

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_likes_count_default(self):
        self.assertEqual(self.post.likes_count, 0)


class LikeModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.post = Post.objects.create(
            author=self.user, title="Test Post", content="Test content"
        )
        self.like = Like.objects.create(user=self.user, post=self.post)

    def test_like_creation(self):
        self.assertEqual(self.like.user, self.user)
        self.assertEqual(self.like.post, self.post)

    def test_likes_count_increase(self):
        self.post.likes_count += 1
        self.post.save()
        self.assertEqual(self.post.likes_count, 1)


class AnalyticsModelTests(TestCase):
    def setUp(self):
        self.analytics = Analytics.objects.create(date="2023-12-23", likes_count=0)

    def test_analytics_creation(self):
        self.assertEqual(self.analytics.date, "2023-12-23")
        self.assertEqual(self.analytics.likes_count, 0)

    def test_analytics_likes_count_increase(self):
        self.analytics.likes_count += 10
        self.analytics.save()
        self.assertEqual(self.analytics.likes_count, 10)
