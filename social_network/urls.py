from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/social_app/", include("social_app.urls", namespace="social_app")),
    path('api/users/', include('users.urls')),
]
