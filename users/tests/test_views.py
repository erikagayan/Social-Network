from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


def create_user(**params):
    """Helper function to create new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        payload = {
            "username": "testname",
            "email": "test@example.com",
            "password": "testpass123",
        }
        res = self.client.post(reverse("users:create"), payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(**res.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        user_details = {"username": "testuser", "password": "testpass"}
        create_user(**user_details)

        payload = {
            "username": user_details["username"],
            "password": user_details["password"],
        }
        res = self.client.post(reverse("users:token"), payload)

        self.assertIn("refresh", res.data)
        self.assertIn("access", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given"""
        create_user(username="testuser", password="testpass")
        payload = {"username": "testuser", "password": "wrong"}
        res = self.client.post(reverse("users:token"), payload)

        self.assertNotIn("refresh", res.data)
        self.assertNotIn("access", res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        self.user = create_user(
            username="testuser", password="testpass", email="test@example.com"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in user"""
        res = self.client.get(reverse("users:manage"))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["username"], self.user.username)
        self.assertEqual(res.data["email"], self.user.email)
