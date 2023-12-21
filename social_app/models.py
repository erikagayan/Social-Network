from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from users.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return str(self.title)

    def has_object_permission(self, request):
        return request.user.is_authenticated and (request.user == self.author or request.user.is_staff)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def has_object_permission(self, request):
        return request.user == self.user

    class Meta:
        ordering = ["-created_at"]
        unique_together = [("user", "post")]
