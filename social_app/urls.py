from django.urls import path, include
from rest_framework import routers
from social_app.views import (
    PostViewSet,
    LikeViewSet,
    AnalyticsViewSet,
)

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("likes", LikeViewSet)
router.register("analytics", AnalyticsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "social_app"
