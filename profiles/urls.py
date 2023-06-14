"""
    urls.py - Profile URLs

    This module contains the URL patterns for the profile endpoints.

    URL Patterns:
    - profile: Endpoint to manage user profiles.
    - update-profile: Endpoint to update a specific user profile.

    Views:
    - ProfileAPIView: API view class for managing user profiles.

"""

from django.urls import path
from .views import ProfileAPIView

urlpatterns = [
    path('', ProfileAPIView.as_view(), name='profile'),
    path('/<int:pk>', ProfileAPIView.as_view(), name='update-profile'),
]