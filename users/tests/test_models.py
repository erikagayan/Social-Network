from django.test import TestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username="testuser", password="12345")
        self.assertEqual(user.username, "testuser")

    def test_user_last_login_default(self):
        user = User.objects.create_user(username="testuser", password="12345")
        self.assertIsNone(user.last_login)

    def test_user_string_representation(self):
        user = User(username="testuser")
        self.assertEqual(str(user), "testuser")
