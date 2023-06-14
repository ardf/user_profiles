"""
    tests.py - Profile API Tests

    This module contains test cases for the profile API endpoints.

    Test Cases:
    - ProfileAPITestCase: Test case class for the profile API.

    Models:
    - Profile: Model representing user profiles.

    Serializers:
    - ProfileSerializer: Serializer class for the Profile model.

"""

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class ProfileAPITestCase(APITestCase):
    """
    ProfileAPITestCase

    Test case class for the profile API.

    """
    def setUp(self):
        """
        Test case setup method.

        - Creates a user.
        - Defines profile data.
        - Creates a profile.
        - Defines the URL for the profile endpoint.

        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'bio': 'Test bio'
        }
        self.profile = Profile.objects.create(**self.profile_data)
        self.url = reverse('profile')

    def test_get_all_profiles(self):
        """
        Test case for retrieving all profiles.

        - Authenticates the user.
        - Sends a GET request to the profile endpoint.
        - Compares the response data with the serialized profiles.

        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_profile(self):
        """
        Test case for creating a profile.

        - Authenticates the user.
        - Reads an image file for the profile picture.
        - Defines new profile data.
        - Sends a POST request to the profile endpoint with the new data.
        - Verifies the response status code.

        """
        self.client.force_authenticate(user=self.user)
        with open('img/profile_pictures/profile_img.jpg', 'rb') as file:
            image_content = file.read()
        image = SimpleUploadedFile(name='profile_img.jpg',content=image_content, content_type='image/jpeg')

        new_data = {
            'name': 'Groot',
            'bio': "I'm groot",
            "email": "groot@groot.com",
            "profile_picture": image
        }
        response = self.client.post(self.url, new_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

    def test_update_profile(self):
        """
        Test case for updating a profile.

        - Authenticates the user.
        - Defines updated profile data.
        - Defines the URL for the specific profile.
        - Sends a PATCH request to the profile endpoint with the updated data.
        - Verifies the response status code and the updated profile data.

        """
        self.client.force_authenticate(user=self.user)
        updated_data = {
            'name': 'Updated Name',
            'bio': 'Updated bio'
        }
        url = reverse('update-profile', args=[self.profile.id])
        response = self.client.patch(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        profile = Profile.objects.get(id=self.profile.id)
        serializer = ProfileSerializer(profile)
        self.assertEqual(response.data, serializer.data)

