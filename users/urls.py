from django.urls import path
from users import views


urlpatterns = [
    path("users/", views.UserListCreateView.as_view(), name="user-list"),
    path(
        "users/<int:pk>/",
        views.UserRetrieveUpdateDestroyView.as_view(),
        name="user-detail",
    ),
]

app_name = "users"
