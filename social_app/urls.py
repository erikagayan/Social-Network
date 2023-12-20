from django.urls import path, include
from social_app import views
from rest_framework import routers

from social_app.views import PostViewSet, PostDetailView

router = routers.DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("posts/<int:pk>/", PostDetailView.as_view()),
]

app_name = "social_app"
