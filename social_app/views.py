from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser

from social_app.permissions import (
    IsAdminOrIfAuthenticatedReadOnly,
    IsAuthenticatedAndHasPermission,
)

from social_app.serializers import (
    PostSerializer,
    LikeSerializer,
    PostListSerializer,
)

from social_app.models import Post, Like


class PostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedAndHasPermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticatedAndHasPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        like = serializer.save()
        post = like.post
        post.likes_count += 1
        post.save()

        return like

    def perform_destroy(self, instance):
        instance.post.likes_count -= 1
        instance.post.save()

        instance.delete()
