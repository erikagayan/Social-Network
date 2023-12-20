from rest_framework import generics
from social_app.models import Post, Like
from social_app.serializers import PostSerializer, LikeSerializer
from social_app.permissions import (
    IsAdminOrIfAuthenticatedReadOnly,
    IsAuthenticatedAndHasPermission,
)
from rest_framework import viewsets, mixins
from rest_framework.generics import RetrieveAPIView


class PostViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedAndHasPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
