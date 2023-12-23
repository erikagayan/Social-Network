from django.test import TestCase
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

User = get_user_model()


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_attributes = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123",
        }
        self.user = User.objects.create_user(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()), {"id", "username", "email", "last_login", "is_staff"}
        )

    def test_username_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["username"], self.user_attributes["username"])

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["email"], self.user_attributes["email"])

    def test_user_creation(self):
        new_user_data = {
            "username": "newtestuser",
            "email": "newtest@example.com",
            "password": "newtestpassword123",
        }
        serializer = UserSerializer(data=new_user_data)
        self.assertTrue(serializer.is_valid())
        new_user = serializer.save()
        self.assertEqual(User.objects.get(username="newtestuser"), new_user)

    def test_user_update(self):
        update_user_data = {"username": "updatedtestuser", "password": "newpassword123"}
        serializer = UserSerializer(
            instance=self.user, data=update_user_data, partial=True
        )
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertEqual(updated_user.username, "updatedtestuser")
