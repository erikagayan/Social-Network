# social_app/tests/test_views.py
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from social_app.models import Post, Like, Analytics


class PostViewSetTests(APIClient):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(
            author=self.user, title="First Post", content="First Content"
        )

    def test_create_post(self):
        """Test creating a new post"""
        url = reverse("post-list")
        data = {"title": "Test Post", "content": "Test content"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.latest("id").title, "Test Post")

    def test_retrieve_post(self):
        """Test retrieving a post"""
        url = reverse("post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "First Post")

    def test_update_post(self):
        """Test updating a post"""
        url = reverse("post-detail", kwargs={"pk": self.post.id})
        data = {"title": "Updated Post", "content": "Updated Content"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_post = Post.objects.get(id=self.post.id)
        self.assertEqual(updated_post.title, "Updated Post")

    def test_delete_post(self):
        """Test deleting a post"""
        url = reverse("post-detail", kwargs={"pk": self.post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())


class LikeViewSetTests(APIClient):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(
            author=self.user, title="Like Post", content="Like Content"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_like_post(self):
        """Test liking a post"""
        url = reverse("like-list")
        data = {"post": self.post.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)

    def test_unlike_post(self):
        """Test unliking a post"""
        like = Like.objects.create(user=self.user, post=self.post)
        url = reverse("like-detail", kwargs={"pk": like.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Like.objects.filter(id=like.id).exists())


class AnalyticsViewSetTests(APIClient):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        Analytics.objects.create(date="2023-12-23", likes_count=10)

    def test_retrieve_analytics(self):
        """Test retrieving analytics"""
        url = reverse("analytics-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["date"], "2023-12-23")
        self.assertEqual(response.data[0]["likes_count"], 10)
