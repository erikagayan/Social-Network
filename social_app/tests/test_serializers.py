from django.test import TestCase
from django.contrib.auth import get_user_model
from social_app.models import Post, Like, Analytics
from social_app.serializers import PostSerializer, LikeSerializer, AnalyticsSerializer

User = get_user_model()


class PostSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.post = Post.objects.create(
            author=self.user, title="Test Post", content="Test content"
        )
        self.serializer = PostSerializer(instance=self.post)

    def test_serialize_model(self):
        data = self.serializer.data
        self.assertEqual(data["title"], "Test Post")
        self.assertEqual(data["content"], "Test content")
        self.assertEqual(data["author"], self.user.username)

    def test_deserialize_model(self):
        data = {"title": "New Post", "content": "New content"}
        serializer = PostSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        new_post = serializer.save(author=self.user)

        self.assertEqual(new_post.title, "New Post")
        self.assertEqual(new_post.content, "New content")
        self.assertEqual(new_post.author, self.user)


class LikeSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.post = Post.objects.create(
            author=self.user, title="Test Post", content="Test content"
        )
        self.like = Like.objects.create(user=self.user, post=self.post)
        self.serializer = LikeSerializer(instance=self.like)

    def test_serialize_model(self):
        data = self.serializer.data
        self.assertEqual(data["user"], self.user.username)
        self.assertEqual(data["post"], self.post.id)


class AnalyticsSerializerTests(TestCase):
    def setUp(self):
        self.analytics = Analytics.objects.create(date="2023-12-23", likes_count=10)
        self.serializer = AnalyticsSerializer(instance=self.analytics)

    def test_serialize_model(self):
        data = self.serializer.data
        self.assertEqual(data["date"], "2023-12-23")
        self.assertEqual(data["likes_count"], 10)
