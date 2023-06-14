from django.urls import path
from .views import ProfileAPIView

urlpatterns = [
    path('', ProfileAPIView.as_view(), name='profile'),
    path('/<int:pk>', ProfileAPIView.as_view(), name='update-profile'),
]