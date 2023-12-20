from django.urls import path, include
from social_app import views
from rest_framework import routers

from social_app.views import PostViewSet


router = routers.DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "social_app"
