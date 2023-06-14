"""
    urls.py - Project URLs

    This module contains the URL configurations for the project.

    URLs:
    - admin/ : URL for the Django admin site.
    - api/profile : URL for the profile API endpoints.
    - api/login : URL for obtaining JWT tokens for authentication.
    - api/login/refresh : URL for refreshing JWT tokens.

"""

from django.contrib import admin
from django.urls import path

from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profile', include('profiles.urls')),
    path('api/login', TokenObtainPairView.as_view()),
    path('api/login/refresh', TokenRefreshView.as_view())
]
