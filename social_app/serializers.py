from rest_framework import serializers
from social_app.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "created_at", "updated_at"]


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "author", "title"]


class LikeSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ["id", "user", "post", "created_at"]
