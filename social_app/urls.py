from django.urls import path, include
from rest_framework import routers
from social_app.views import (
    PostViewSet,
    PostDetailView,
    LikeViewSet,
)

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("likes", LikeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:pk>/", PostDetailView.as_view()),
]

app_name = "social_app"
