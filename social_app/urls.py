from django.urls import path
from social_app import views

urlpatterns = [
    path("posts/", views.PostListCreateView.as_view(), name="post-list"),
    path(
        "posts/<int:pk>/",
        views.PostRetrieveUpdateDestroyView.as_view(),
        name="post-detail",
    ),
    path("likes/", views.LikeListCreateView.as_view(), name="like-list"),
    path(
        "likes/<int:pk>/",
        views.LikeRetrieveUpdateDestroyView.as_view(),
        name="like-detail",
    ),
]

app_name = "social_app"
