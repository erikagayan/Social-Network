from rest_framework import viewsets, mixins

from social_app.permissions import (
    IsAuthenticatedAndHasPermission,
)

from social_app.serializers import (
    PostSerializer,
    LikeSerializer,
    PostListSerializer,
    AnalyticsSerializer,
)

from social_app.models import Post, Like, Analytics


class PostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedAndHasPermission,)

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
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


class AnalyticsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    permission_classes = (IsAuthenticatedAndHasPermission,)

    def get_queryset(self):
        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")

        if date_from and date_to:
            return Analytics.objects.filter(date__range=[date_from, date_to])
        elif date_from:
            return Analytics.objects.filter(date__gte=date_from)
        elif date_to:
            return Analytics.objects.filter(date__lte=date_to)
        else:
            return Analytics.objects.all()
